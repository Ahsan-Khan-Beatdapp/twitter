#!/usr/bin/env python3

# Importing
from flask import Flask, request

# keys
api_key = '1MVFftXceUfhExRkSqSpXhy6C'
api_secret_key = "IZb1jbpENLiRqjOVt2vgEhR3jen2CO2RIobZh7E2cACsU95vA5"
bearer_tokem = 'AAAAAAAAAAAAAAAAAAAAAKwkbwEAAAAAI%2BLe3sh6dNEIGF9JCIL5U%2BpCCeY%3DmJgV6Opqm8Km8XNcf04llAVRvKD98SPvtWaZNwvweo09dmM834'
access_token = "1517584070154272768-EvlYEM0uP8LUaup9GTxQqWbTulegc9"
access_token_secret = 'BsMD78683Qb2IY5XJRv1ijRx8pxzNtenCJV83pEKvn8KO'


# Initilizations

app = Flask(__name__)

# Website
@app.route("/")
def main():
    return '''
    <style>
        body { background-color: #fafafa; font-family: Arial, sans-serif; }
        form { margin: 100px auto; width: 300px; }
        input[type="text"] { width: 100%; padding: 10px; margin: 10px 0; box-sizing: border-box; }
        input[type="submit"] { width: 100%; padding: 10px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }
        input[type="submit"]:hover { background-color: #45a049; }
    </style>
    <form action="/echo_user_input" method="POST">
        <input type="text" name="user_input" placeholder="Enter something">
        <input type="submit" value="Echo To Screen">
    </form>
    '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return '''
    <style>
        body { background-color: #fafafa; font-family: Arial, sans-serif; }
        .echo-container { margin: 50px auto; width: 300px; padding: 20px; background-color: #4CAF50; color: white; text-align: center; }
        .output-container { margin: 50px auto; width: 300px; padding: 20px; background-color: #f0f0f0; color: #333; text-align: center; }
        .echo-text { font-size: 20px; color: white; }
        .user-output { font-size: 24px; color: #333; font-weight: bold; }
    </style>
    <div class="echo-container">
        <p class="echo-text">You entered:</p>
    </div>
    <div class="output-container">
        <p class="user-output">''' + input_text + '''</p>
    </div>
    '''


# Tweepy data extraction

import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)