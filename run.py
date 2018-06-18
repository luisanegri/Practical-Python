import os
import json 
from flask import Flask, redirect, render_template, request
#import pandas as pd

app = Flask(__name__)

data = []
score = 0
riddle_index = 0



def add_to_file (filename, data):
    with open (filename, "a") as file:
        file.writelines(data)

#store users in users.txt 
def add_users (username):
    add_to_file("data/users.txt", "{0}")


def store_user_score(username, score):
    #user input to record the log
   
    user_data =  {}
    user_data['username'] = username
    user_data['score'] = score
    
    return(username, score)

out = {}

with open('data/usersdata.json','w') as f:
    json.dump(out, f, indent=2)      

    #print(pd.read_json('data/usersdata.json'))   
    
#GET the username, store it in the users file
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        add_to_file("data/users.txt", request.form["username"] + "\n")
        return redirect(request.form["username"])
    return render_template("index.html")


@app.route('/<username>', methods=["GET", "POST"])
def user_game(username):
    global riddle_index
    global data
    global score

    with open("data/riddle.json", "r") as json_data:
        data = json.load(json_data)
        total_questions = len(data)
        
   
    if request.method == "POST":
             
        riddle_index = int(request.form["riddle_index"])
        user_answer = request.form["response"].lower()
        
        
        if data[riddle_index]["answer"] == user_answer:
        # Print correct answer
        # Show score
        # Add score to file
        # Go to next question
            score += 1
            store_user_score(username, score)
            print(score)
            riddle_index += 1
        else:
            print("That's incorrect!")
    
    if request.method == "POST":
        if user_answer == "mount everest" and riddle_index > 9:
            return render_template("end.html")
 
    return render_template("game.html",
                            username=username, data=data, riddle_index=riddle_index, score=score, total_questions=total_questions)

    







app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)