#!/usr/bin/env python3
import sqlite3
import pandas as pd
from flask import Flask, request, redirect, url_for
from data_analysis_and_machine_learning import calculate_average_sentiment
from fetch_reddit_data_and_create_db import fetch_data_and_create_db
from datetime import datetime
#from transformers import pipeline

# Load the model once when your application starts
#nlp = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

app = Flask(__name__)

@app.route("/update", methods=["POST"])
def update_data():
    fetch_data_and_create_db()
    return redirect(url_for('main'))

@@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        team_db = request.form.get("team") + ".db"
        return redirect(url_for('display_mood', team_db=team_db))
    else:
        return '''
        <html>
        <head>
            <title>Ahsan's NBA Fan Mood Level</title>
        </head>
        <body>
            <style>
                body { background-color: #fafafa; font-family: Arial, sans-serif; }
                form { margin: 100px auto; width: 300px; }
                select, input[type="submit"] { width: 100%; padding: 10px; margin: 10px 0; box-sizing: border-box; }
            </style>
            <form action="/" method="post">
                <select name="team">
                    <option value="lakers">Lakers</option>
                    <option value="celtics">Celtics</option>
                    <option value="raptors">Raptors</option>
                </select>
                <input type="submit" value="Submit">
            </form>
            <form action="/update" method="post">
                <p>Click the button below to update data to most recent</p>
                <input type="submit" value="Update Data">
            </form>
            '''

@app.route("/fan-happiness-level")
def display_mood():
    team_db = request.args.get('team_db', "")
    team_name = team_db.split('.')[0]  # Extract team name from the database name

    # Calculate the average sentiment score
    score = calculate_average_sentiment(team_db)

    # Convert the score to an integer
    score = int(score)

    # Get the current date
    today = datetime.now().strftime('%Y-%m-%d')

    return f'''
    <style>
        body {{ background-color: #fafafa; font-family: Arial, sans-serif; }}
        div {{ margin: 100px auto; width: 300px; text-align: center; }}
        .score {{ font-size: 2em; color: #4CAF50; }}
        .team-name {{ font-size: 1.5em; color: #3F51B5; font-weight: bold; }}
        .date {{ font-size: 1em; color: #9E9E9E; }}
    </style>
    <div>
        <p class="team-name">{team_name.capitalize()} Fan Happiness Level Calculated Based on Data:</p>
        <p class="score">{score}%</p>
        <p class="date">Analysis Date: {today}</p>
    </div>
    '''






