#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)


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


