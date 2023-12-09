#!/usr/bin/env python3
import sqlite3
import pandas as pd
from flask import Flask, request, redirect, url_for
from data_analysis_and_machine_learning import calculate_average_sentiment
from transformers import pipeline

# Load the model 
#nlp = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

# Load MobileBERT tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("google/mobilebert-uncased")
model = AutoModelForSequenceClassification.from_pretrained("google/mobilebert-uncased")

# Create a pipeline for sentiment analysis
nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

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
            h1 { text-align: center; }
        </style>
        <h1>Ahsan's NBA Fans Mood Calculator</h1>
        <form method="POST">
            <select name="team">
                <option value="lakers">Lakers</option>
                <option value="raptors">Raptors</option>
                <option value="celtics">Celtics</option>
            </select>
            <input type="submit" value="Calculate Fan Happiness Level">
        </form>
        '''

from datetime import datetime

@app.route("/echo_user_input")
def echo_input():
    team_db = request.args.get('team_db', "")
    team_name = team_db.split('.')[0]  # Extract team name from the database name

    # Calculate the average sentiment score
    score = calculate_average_sentiment(team_db, nlp)

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






