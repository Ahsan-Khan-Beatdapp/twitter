#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
    <html>
        <head>
            <title>Input Echo</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    text-align: center;
                    padding: 50px;
                }
                form {
                    background-color: white;
                    padding: 20px;
                    border-radius: 8px;
                    display: inline-block;
                }
                input[type="text"] {
                    padding: 10px;
                    margin: 10px;
                    border-radius: 4px;
                    border: 1px solid #ddd;
                    width: 200px;
                }
                input[type="submit"] {
                    padding: 10px 20px;
                    border-radius: 4px;
                    border: none;
                    background-color: #007bff;
                    color: white;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>
        <body>
            <form action="/echo_user_input" method="POST">
                <input type="text" name="user_input">
                <input type="submit" value="Echo To Screen">
            </form>
        </body>
    </html>
    '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return f'''
    <html>
        <head>
            <title>Input Echo</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    text-align: center;
                    padding: 50px;
                }
                .echo-text {
                    background-color: white;
                    padding: 20px;
                    border-radius: 8px;
                    display: inline-block;
                }
            </style>
        </head>
        <body>
            <div class="echo-text">You entered: {input_text}</div>
        </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)
