from flask import Flask, request
import time
from datetime import datetime
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    
    
    if 'thoughts' in incoming_msg:
        record = time.ctime()
        response = 'Recieved and noted\nKeep it coming!\n\nMoment Recorded: {} '.format(record)
        msg.body(response)
        responded = True

    elif 'achievements' in incoming_msg:
        record = time.ctime()
        response = 'I want more of this coming \nYou are doing awesome,go on and achieve more Champ!\nRemember,there are no limits to what you can achieve\n\nMoment Recorded: {}'.format(record)
        msg.body(response)
        responded = True
        
    elif 'views' in incoming_msg:
        response = 'Your life is not just about you, always do more so you can help more\nYou can not be normal and expect abnormal returns\nTho you might be down now, but keep progressing Man no shortcuts!'
        msg.body(response)
        responded = True
    
    
        
        
    elif 'quote' in incoming_msg:
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieves a quote at this time, Sorry'
        msg.body(quote)   
        responded = True
    elif not responded:
        msg.body('No Chitchat here Man,\nFocus on your craft and consistently do what you do Man\nOnly keep me informed of your actions and thoughts\nKeep improving Champ')
    return str(resp)