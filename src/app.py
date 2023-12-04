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
    return "You entered: " + input_text