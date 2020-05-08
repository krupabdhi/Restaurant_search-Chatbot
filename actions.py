from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(
    DEBUG=True,
    #EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'test@gmail.com',
    MAIL_PASSWORD = 'password'
    )
mail = Mail(app)

class ActionSearchRestaurants(Action):
    def name(self):
         return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        config={ "user_key":"8ae998e82fb31fb71cfb8c1ce7ed37c3"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        cmin = tracker.get_slot('price1')
        cmax = tracker.get_slot('price2')
        location_detail=zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        results_1 = len(d1["location_suggestions"])
        cuisines_dict={'american':1,'chinese':25,'mexican':73,'italian':55,'north indian':50,'south indian':85}
        results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 50)        
        d = json.loads(results)
        
        # Filter the results based on budget
        d_budget = [d1 for d1 in d['restaurants'] if ((d1['restaurant']['average_cost_for_two'] > int(cmin)) & (d1['restaurant']['average_cost_for_two'] < int(cmax)))]
        # Sort the results according to the restaurant's rating
        d_budget_rating_sorted = sorted(d_budget, key=lambda k: k['restaurant']['user_rating']['aggregate_rating'], reverse=True)
        
        response=""
        if len(d_budget_rating_sorted) == 0:
            response= "no results"
        else:
            d_budget_rating_top5 = d_budget_rating_sorted[:5]
            global email_list
            email_list = d_budget_rating_sorted[:10]
            for restaurant in d_budget_rating_top5:
              response=response+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address'] + " has been rated "  + restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n"
            dispatcher.utter_message("-------------\n"+response+"\n-------------")
            return [SlotSet('location',loc)]

class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'
    
    def run(self, dispatcher, tracker, domain):
        to_email_id = tracker.get_slot('emailid')
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
      
        msg = Message("Top 10 Restaurants!!", sender="test@gmail.com", recipients=[to_email_id])
        msg.body = "Hello! Here are the top 10 restaurants requested: \n\n"
        global email_list
        for restaurant in email_list:
            msg.body += restaurant['restaurant']['name']+ " in " + restaurant['restaurant']['location']['address']+ " with average budget Rs." + str(restaurant['restaurant']['average_cost_for_two'])+ " rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] +"\n"
        with app.app_context():
            mail.send(msg)
        dispatcher.utter_message("EMAIL SENT ..... ENJOY YOUR MEAL :)")
        return []

class VerifyLocation(Action):

    tier1 = []
    tier2 = []

    def __init__(self):
        self.tier1 = ['ahmedabad', 'bangalore', 'chennai',
                       'delhi', 'hyderabad', 'kolkata', 'mumbai', 'pune']
        self.tier2 = ['agra', 'ajmer', 'aligarh', 'allahabad', 'amravati', 'amritsar', 'asansol', 'aurangabad', 'bareilly', 'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bokaro steel city', 'chandigarh', 'coimbatore', 'cuttack', 'dehradun', 'dhanbad', 'durg-bhilai nagar', 'durgapur', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gurgaon', 'guwahati', 'gwalior', 'hubli-dharwad', 'indore', 'jabalpur', 'jaipur', 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kannur', 'kanpur', 'kakinada', 'kochi',
                       'kottayam', 'kolhapur', 'kollam', 'kota', 'kozhikode', 'kurnool', 'lucknow', 'ludhiana', 'madurai', 'malappuram', 'mathura', 'goa', 'mangalore', 'meerut', 'moradabad', 'mysore', 'nagpur', 'nanded', 'nashik', 'nellore', 'noida', 'palakkad', 'patna', 'pondicherry', 'raipur', 'rajkot', 'rajahmundry', 'ranchi', 'rourkela', 'salem', 'sangli', 'shimla', 'siliguri', 'solapur', 'srinagar', 'sultanpur', 'surat', 'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tirunelveli', 'tiruppur', 'ujjain', 'vijayapura', 'vadodara', 'varanasi', 'vasai-virar city', 'vijayawada', 'visakhapatnam', 'vellore', 'warangal']
    def name(self):
        return "action_verify_location"
    
    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        error_msg = "Sorry!! The location is not supported. Please re-enter."
        try:
           loc = loc.lower()
        except(RuntimeError,TypeError,NameError,AttributeError):
            dispatcher.utter_message(error_msg)
            return[SlotSet('location',None),SlotSet('location_check',False)]
        if (loc in self.tier1 or loc in self.tier2): 
            return [SlotSet('location', loc), SlotSet("location_check", True)]
        else:
            dispatcher.utter_message("We do not operate in " + loc + " yet!")
            return [SlotSet('location', None), SlotSet("location_check", False)]