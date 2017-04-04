"""Yelp Fusion Flask Gateway 

A Yelp Fusion API Gateway (25,000 calls per day) that supports default parameters

Developed by Kevin Chen

"""

from flask import Flask, render_template, request
from pprint import pprint
import requests
from flask.ext.cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Yelp API Key
client_id = 'Q9ohRULV-e8-tDsyJV55pg'
client_secret = 'c41gYgUtO0fOwIkbNp4haWfTWs9OVN3uIdSeEfG051N2KwrJ6jttYgGc0n1qYFm9'

# Get Yelp OAUTH2 token
auth = {'grant_type' : 'client_credentials',
        'client_id' : client_id,
        'client_secret' : client_secret}
token_resp = requests.post('https://api.yelp.com/oauth2/token', data=auth)
token = token_resp.json()['access_token']

@app.route("/")
@cross_origin()
def hello_world():
    return "Hello!"

# GET Business Request (Coordinates Only)
@app.route("/business", methods=['GET'])
@cross_origin()
def get_business():

    # Default Parameters (DC)
    params = {
        'term': 'food',
        'location': 'DC',
    }

    # Overwrite default parameters with arguments
    for key, val in request.args.items():
        print(key)
        if key in params:
            params[key] = val

    pprint(params) #DEBUG

   # set GET request to Yelp API
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'bearer %s' % token}

    resp = requests.get(url=url, params=params, headers=headers)
    
    # respond with Yelp resonse
    return resp.text

if __name__ == '__main__':
    app.run()
