import os
import json
from flask import Flask, redirect, render_template, request


app = Flask(__name__)


# Dictionary with user and score
user_data = {}

with open("data/riddle.json", "r") as json_data:
    data = json.load(json_data)
    total_questions = len(data)


# Function to append to file
def add_to_file(filename, data):
    with open(filename, "a") as file:
        file.writelines(data)


def store_user_score(username, score):
    # Dictionary to store username and score
    # Key/value
    user_data[username] = score
    print(user_data)
    # Creates file and open it in write mode
    with open('data/usersdata.json', 'w') as f:
        print(json.dump(user_data, f, indent=2))


# GET the username, store it in the users file
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        add_to_file("data/usersdata.json", request.form["username"] + "\n")
        return redirect(request.form["username"])
    return render_template("index.html")


@app.route('/<username>', methods=["GET", "POST"])
def user_game(username):
    global user_data
    riddle_index = 0
    # Score starting at 0
    score = user_data.get(username, 0)
    points = ''
    result = ''

    if request.method == "POST":
        riddle_index = int(request.form["riddle_index"])
        user_answer = request.form.get("response", "").lower()

        if riddle_index >= total_questions:
            result = "You got {0} correct out of {1}".format
            (score, total_questions)
            return render_template("end.html", result=result)

        if data[riddle_index]["answer"] == user_answer:
            # Increment score
            score += 1
            # Add username/score to function
            store_user_score(username, score)
            # Go to next question
            riddle_index += 1
            # Display message
            points = "Points: {0}".format(score)

        else:
            points = "Points: {0}".format(score)

    return render_template(
                            "game.html",
                            username=username, data=data,
                            riddle_index=riddle_index, score=score,
                            total_questions=total_questions, points=points)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=False)
