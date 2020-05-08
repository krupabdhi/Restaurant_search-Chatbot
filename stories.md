## complete path1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_verify_location
    - slot{"location": "delhi"}
    - slot{"location_check": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"price1": "300","price2": "700"}
    - slot{"price1":"300"}
    - slot{"price2":"700"}
    - action_search_restaurants
    - slot{"cuisine": "Chinese"}
    - slot{"location": "delhi"}
    - utter_ask_emailtop10
* affirm
    - utter_ask_emailid
* send_email{"emailid":"rahul.abc@gmail.com"}
    - slot{"emailid":"rahul.abc@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## complete path2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_verify_location
    - slot{"location": "Chennai"}
    - slot{"location_check": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "Chennai"}
    - utter_ask_price
* restaurant_search{"price1": "0","price2": "300"}
    - slot{"price1":"0"}
    - slot{"price2":"300"}
    - action_search_restaurants
    - slot{"cuisine": "South Indian"}
    - slot{"location": "Chennai"}
    - utter_ask_emailtop10
* dont_send_email
    - utter_goodbye
    - action_restart

## location specified
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - slot{"location_check": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "bangalore"}
    - utter_ask_price
* restaurant_search{"price1": "700","price2": "5000"}
    - slot{"price1":"700"}
    - slot{"price2":"5000"}
    - action_search_restaurants
    - slot{"cuisine": "Mexican"}
    - slot{"location": "bangalore"}
    - utter_ask_emailtop10
* affirm
    - utter_ask_emailid
* send_email{"emailid":"ram.varma@gmail.com"}
    - slot{"emailid":"ram.varma@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## location specified
* greet
    - utter_greet
* restaurant_search{"location": "hassan"}
    - slot{"location": "hassan"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_check": false}
    - utter_ask_location
* restaurant_search{"location": "coimbatore"}
    - slot{"location": "coimbatore"}
    - action_verify_location
    - slot{"location": "coimbatore"}
    - slot{"location_check": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "coimbatore"}
    - utter_ask_price
* restaurant_search{"price1": "300","price2": "600"}
    - slot{"price1":"300"}
    - slot{"price2":"600"}
    - action_search_restaurants
    - slot{"cuisine": "Chinese"}
    - slot{"location": "coimbatore"}
    - utter_ask_emailtop10
* affirm
    - utter_ask_emailid
* send_email{"emailid":"ram.varma@gmail.com"}
    - slot{"emailid":"ram.varma@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## cuisine specified
* greet
    - utter_greet
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_location
* restaurant_search{"location": "Kota"}
    - slot{"location": "Kota"}    
    - action_verify_location
    - slot{"location": "Kota"}
    - slot{"location_check": true}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* restaurant_search{"price1": "0","price2": "300"}
    - slot{"price1":"0"}
    - slot{"price2":"300"}
    - action_search_restaurants
    - slot{"location": "Kota"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_emailtop10
* affirm
    - utter_ask_emailid
* send_email{"emailid":"Alex@hotmail.com"}
    - slot{"emailid":"Alex@hotmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Patiala"}
    - slot{"location": "Patiala"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_check": false}
    - utter_ask_location
* restaurant_search{"location": "lucknow"}
    - slot{"location": "lucknow"}
    - action_verify_location
    - slot{"location": "lucknow"}
    - slot{"location_check": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "lucknow"}
    - utter_ask_price
* restaurant_search{"price1": "0","price2": "300"}
    - slot{"price1":"0"}
    - slot{"price2":"300"}
    - action_search_restaurants
    - slot{"cuisine": "North Indian"}
    - slot{"location": "lucknow"}
    - utter_ask_emailtop10
* affirm
    - utter_ask_emailid
* send_email{"emailid":"adil.abc@live.com"}
    - slot{"emailid":"adil.abc@live.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## location specified
* greet
    - utter_greet
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_verify_location
    - slot{"location": "Pune"}
    - slot{"location_check": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Pune"}
    - utter_ask_price
* restaurant_search{"price1": "400","price2": "800"}
    - slot{"price1":"400"}
    - slot{"price2":"800"}
    - action_search_restaurants
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Pune"}
    - utter_ask_emailtop10
* dont_send_email
    - utter_goodbye
    - action_restart

## cuisine specified
* greet
    - utter_greet
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_location
* restaurant_search{"location": "haridwar"}
    - slot{"location": "haridwar"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_check": false}
    - utter_ask_location
* restaurant_search{"location": "kochi"}
    - slot{"location": "kochi"}
    - action_verify_location
    - slot{"location": "kochi"}
    - slot{"location_check": true}
    - slot{"cuisine": "Chinese"}
    - utter_ask_price
* restaurant_search{"price1": "300","price2": "700"}
    - slot{"price1":"300"}
    - slot{"price2":"700"}
    - action_search_restaurants
    - slot{"location": "kochi"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_emailtop10
* dont_send_email
    - utter_goodbye
    - action_restart

## location & cuisine specified
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "belgaum"}
    - slot{"cuisine": "italian"}
    - slot{"location": "belgaum"}
    - action_verify_location
    - slot{"location": "belgaum"}
    - slot{"location_check": true}
    - utter_ask_price
* restaurant_search{"price1": "300","price2": "700"}
    - slot{"price1":"300"}
    - slot{"price2":"700"}
    - action_search_restaurants
    - slot{"cuisine": "italian"}
    - slot{"location": "belgaum"}
    - utter_ask_emailtop10
* affirm
    - utter_ask_emailid
* send_email{"emailid":"itsme@yahoo.com"}
    - slot{"emailid":"itsme@yahoo.com"}
    - action_send_email
    - utter_goodbye
    - action_restart
    
## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "american","location": "hyderabad","price1": "500","price2": "1000"}
    - slot{"cuisine": "american"}
    - slot{"location": "hyderabad"}
    - action_verify_location
    - slot{"location": "hyderabad"}
    - slot{"location_check": true}
    - slot{"price1":"500"}
    - slot{"price2":"1000"}
    - action_search_restaurants
    - slot{"cuisine": "american"}
    - slot{"location": "hyderabad"}
    - utter_ask_emailtop10
* dont_send_email
    - utter_goodbye
    - action_restart

## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican","location": "Kolkata","price1": "700","price2": "1000"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Kolkata"}
    - action_verify_location
    - slot{"location": "Kolkata"}
    - slot{"location_check": true}
    - slot{"price1":"700"}
    - slot{"price2":"1000"}
    - action_search_restaurants
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Kolkata"}
    - utter_ask_emailtop10
* send_email{"emailid":"Shyam.ab@yahoo.com"}
    - slot{"emailid":"Shyam.ab@yahoo.com"}
    - action_send_email
    - utter_goodbye
    - action_restart


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "pondicherry"}
    - slot{"location": "pondicherry"}
    - action_verify_location
    - slot{"location": "pondicherry"}
    - slot{"location_check": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price1": "300", "price2": "700"}
    - slot{"price1": "300"}
    - slot{"price2": "700"}
    - action_search_restaurants
    - slot{"location": "pondicherry"}
    - utter_ask_emailtop10
* affirm
    - utter_ask_emailid
* send_email{"emailid": "mayur.patilg@gmail.com"}
    - slot{"emailid": "mayur.patilg@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_location
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_verify_location
    - slot{"location": "Hyderabad"}
    - slot{"location_check": true}
    - utter_ask_price
* restaurant_search{"price1": "300", "price2": "700"}
    - slot{"price1": "300"}
    - slot{"price2": "700"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - utter_ask_emailtop10
* send_email{"emailid": "mayur_19@hotmail.com"}
    - slot{"emailid": "mayur_19@hotmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "hosur"}
    - slot{"location": "hosur"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_check": false}
    - utter_ask_location
* restaurant_search{"location": "salem"}
    - slot{"location": "salem"}
    - action_verify_location
    - slot{"location": "salem"}
    - slot{"location_check": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* restaurant_search{"price1": "300", "price2": "700"}
    - slot{"price1": "300"}
    - slot{"price2": "700"}
    - action_search_restaurants
    - slot{"location": "salem"}
    - utter_ask_emailtop10
* affirm
    - utter_ask_emailid
* send_email{"emailid": "mayur.patilg@gmail.com"}
    - slot{"emailid": "mayur.patilg@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "patiala"}
    - slot{"location": "patiala"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_check": false}
    - utter_ask_location
* restaurant_search{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - action_verify_location
    - slot{"location": "chandigarh"}
    - slot{"location_check": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price1": "700", "price2": "5000"}
    - slot{"price1": "700"}
    - slot{"price2": "5000"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_ask_emailtop10
* dont_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Ludhiana", "price1": "500", "price2": "1000"}
    - slot{"location": "Ludhiana"}
    - slot{"price1": "500"}
    - slot{"price2": "1000"}
    - action_verify_location
    - slot{"location": "Ludhiana"}
    - slot{"location_check": true}
    - action_search_restaurants
    - slot{"location": "Ludhiana"}

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "ludhiana", "price1": "400", "price2": "800"}
    - slot{"location": "ludhiana"}
    - slot{"price1": "400"}
    - slot{"price2": "800"}
    - action_verify_location
    - slot{"location": "ludhiana"}
    - slot{"location_check": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "ludhiana"}
    - utter_ask_emailtop10
* affirm
    - utter_ask_emailid
* send_email{"emailid": "mayur_19@hotmail.com"}
    - slot{"emailid": "mayur_19@hotmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "price1": "500", "price2": "1000"}
    - slot{"cuisine": "Mexican"}
    - slot{"price1": "500"}
    - slot{"price2": "1000"}
    - utter_ask_location
* restaurant_search{"location": "gurgaon"}
    - slot{"location": "gurgaon"}
    - action_verify_location
    - slot{"location": "gurgaon"}
    - slot{"location_check": true}
    - action_search_restaurants
    - slot{"location": "gurgaon"}
* affirm
    - utter_ask_emailtop10
* affirm
    - utter_ask_emailid
* send_email{"emailid": "testid@yahoo.com"}
    - slot{"emailid": "testid@yahoo.com"}
    - action_send_email
* affirm
    - utter_goodbye



## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "patna"}
    - slot{"location": "patna"}
    - action_verify_location
    - slot{"location": "patna"}
    - slot{"location_check": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price1": "300", "price2": "700"}
    - slot{"price1": "300"}
    - slot{"price2": "700"}
    - action_search_restaurants
    - slot{"location": "patna"}
* affirm
    - utter_ask_emailtop10
* affirm
    - utter_ask_emailid
* send_email{"emailid": "theone_rox@yahoo.com"}
    - slot{"emailid": "theone_rox@yahoo.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_location
* restaurant_search{"location": "Ambur"}
    - slot{"location": "Ambur"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_check": false}
    - utter_ask_location
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_verify_location
    - slot{"location": "Jaipur"}
    - slot{"location_check": true}
    - utter_ask_price
* restaurant_search{"price1": "500", "price2": "1500"}
    - slot{"price1": "500"}
    - slot{"price2": "1500"}
    - action_search_restaurants
    - slot{"location": "Jaipur"}
* affirm
    - utter_ask_emailtop10
* dont_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_check": false}
    - utter_ask_location
* restaurant_search{"location": "rajkot"}
    - slot{"location": "rajkot"}
    - action_verify_location
    - slot{"location": "rajkot"}
    - slot{"location_check": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price1": "400", "price2": "1100"}
    - slot{"price1": "400"}
    - slot{"price2": "1100"}
    - action_search_restaurants
    - slot{"location": "rajkot"}
* affirm
    - utter_ask_emailtop10
* affirm
    - utter_ask_emailid
* send_email{"emailid": "mayur.patilg@gmail.com"}
    - slot{"emailid": "mayur.patilg@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "American", "location": "patiala"}
    - slot{"cuisine": "American"}
    - slot{"location": "patiala"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_check": false}
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_verify_location
    - slot{"location": "pune"}
    - slot{"location_check": true}
    - utter_ask_price
* restaurant_search{"price1": "500", "price2": "1200"}
    - slot{"price1": "500"}
    - slot{"price2": "1200"}
    - action_search_restaurants
    - slot{"location": "pune"}
    - utter_ask_emailtop10
* affirm
    - utter_ask_emailid
* send_email{"emailid": "mayur.patilg@gmail.com"}
    - slot{"emailid": "mayur.patilg@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "Mysore", "price1": "300", "price2": "600"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Mysore"}
    - slot{"price1": "300"}
    - slot{"price2": "600"}
    - action_verify_location
    - slot{"location": "mysore"}
    - slot{"location_check": true}
    - action_search_restaurants
    - slot{"location": "mysore"}
    - utter_ask_emailtop10
* dont_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "price2": "500"}
    - slot{"cuisine": "north indian"}
    - slot{"price2": "500"}
    - utter_ask_location
* restaurant_search{"location": "dindigul"}
    - slot{"location": "dindigul"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_check": false}
    - utter_ask_location
* restaurant_search{"location": "kolhapur"}
    - slot{"location": "kolhapur"}
    - action_verify_location
    - slot{"location": "kolhapur"}
    - slot{"location_check": true}
    - action_search_restaurants
    - slot{"location": "kolhapur"}
    - utter_ask_emailtop10
* dont_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata", "price1": "400"}
    - slot{"location": "Kolkata"}
    - slot{"price1": "400"}
    - action_verify_location
    - slot{"location": "kolkata"}
    - slot{"location_check": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_emailtop10
* send_email{"emailid": "mayur_19@hotmail.com"}
    - slot{"emailid": "mayur_19@hotmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "haridwar", "price1": "300"}
    - slot{"location": "haridwar"}
    - slot{"price1": "300"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_check": false}
    - utter_ask_location
* restaurant_search{"location": "thrissur"}
    - slot{"location": "thrissur"}
    - action_verify_location
    - slot{"location": "thrissur"}
    - slot{"location_check": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - slot{"location": "thrissur"}
    - utter_ask_emailtop10
* dont_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian", "location": "gangtok"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "gangtok"}
    - action_verify_location
    - slot{"location": null}
    - slot{"location_check": false}
    - utter_ask_location
* restaurant_search{"location": "Cuttack"}
    - slot{"location": "Cuttack"}
    - action_verify_location
    - slot{"location": "cuttack"}
    - slot{"location_check": true}
    - utter_ask_price
* restaurant_search{"price2": "1000"}
    - slot{"price2": "1000"}
    - action_search_restaurants
    - slot{"location": "cuttack"}
    - utter_ask_emailtop10
* dont_send_email
    - utter_goodbye
