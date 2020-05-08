An Indian startup named 'Foodie' wants to build a conversational bot (chatbot) which can help users discover restaurants across several Indian cities. 

The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience.

steps: 
1) Installed rasa
2) Created a rasa environment.
3) Using the sample file provided, added the required intents , entities , slots  and actions in domain file
4) Added the custom actions according to our requirements.
5) Updated nlu and stories files accordingly

We have created 3 custom actions: 
1--> action_search_restaurants 
2--> verify_location(to validate if city entered is a tier-1 to tier-2 city)
3--> action_send_email 

Here we are considering only 6 cuisine types:
chinese
mexican 
italian
american
north indian and
south indian 


Note:
------

1.) For the email functionality to work correctly, the following statements in actions.py file need to be updated with a valid gmail username/password.
	
	MAIL_USERNAME = 'test_user@gmail.com',
    	MAIL_PASSWORD = 'testpassword'

Similarly, 'sender' parameter in the following line of actions.py (under class ActionSendEMail()) file could be updated with the right 'from' mail id, as mentioned above.

	msg = Message("Top 10 Restaurants!!", sender="test_user@gmail.com", recipients=[to_email_id])


2.) In case the send email functionality times out while chatting with the bot, the "DEFAULT_STREAM_READING_TIMEOUT_IN_SECONDS" parameter in the console.py file under "python3.7⁩/site-packages/⁨rasa⁩/⁨core⁩/⁨channels⁩" could be updated with a value of >=30. The default value is 10.


3.) Intermittently, after the chatbot responds back with the list of 5 restaurants, it would expect an 'affirmation' statement from the end user such as 'Thank you', etc. The bot would then respond back with the question asking whether an email of the top 10 restaurants needs to be sent out, and the regular workflow continues.


4.) Occasionally, when there were issues with the bot not interpreting any intent (though rasa training with nlu/core was completed successfully), the following command helped resolve the issue.

rasa train -vv -dump-stories --force 