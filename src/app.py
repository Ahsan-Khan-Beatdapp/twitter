#!/usr/bin/env python3
import sqlite3
import pandas as pd
from flask import Flask, request, redirect, url_for
from data_analysis_and_machine_learning import calculate_average_sentiment

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        team_db = request.form.get("team") + ".db"
        return redirect(url_for('echo_input', team_db=team_db))
    else:
        return '''
        <style>
            body { background-color: #fafafa; font-family: Arial, sans-serif; }
            form { margin: 100px auto; width: 300px; }
            select, input[type="submit"] { width: 100%; padding: 10px; margin: 10px 0; box-sizing: border-box; }
            input[type="submit"] { background-color: #4CAF50; color: white; border: none; cursor: pointer; }
            input[type="submit"]:hover { background-color: #45a049; }
        </style>
        <form method="POST">
            <select name="team">
                <option value="lakers">Lakers</option>
                <option value="raptors">Raptors</option>
                <option value="celtics">Celtics</option>
            </select>
            <input type="submit" value="Calculate Fan Happiness Level">
        </form>
        '''

@app.route("/echo_user_input")
def echo_input():
    team_db = request.args.get('team_db', "")
    
    # Connect to the database
    conn = sqlite3.connect(team_db)

    # Fetch the post_text data
    df = pd.read_sql_query("SELECT post_text FROM posts", conn)

    # Close the database connection
    conn.close()

    # Calculate the average sentiment score
    score = calculate_average_sentiment(df)
    # Rest of your code...
    return f'''
    <style>
        body {{ background-color: #fafafa; font-family: Arial, sans-serif; }}
        div {{ margin: 100px auto; width: 300px; text-align: center; }}
        .score {{ font-size: 2em; color: #4CAF50; }}
    </style>
    <div>
        <p>Fan Happiness Level:</p>
        <p class="score">{score}</p>
    </div>
    '''






