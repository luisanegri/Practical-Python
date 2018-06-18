import os
import json 
from flask import Flask, redirect, render_template, request

app = Flask(__name__)



def add_to_file (filename, data):
    with open (filename, "a") as file:
        file.writelines(data)


#store users in users.txt 
def add_users (username):
    add_to_file("data/users.txt", "{0}")

"""score_file_name = "data/userscore.txt"
   
def write_score(score_file_name, username, score):
    scores = read_scores(score_file_name)
    # add score
    scores[username] = score
    with open(score_file_name, 'w') as f:
        serializer.dump(scores, f)


def read_scores(score_file_name):
    try:
        with open(score_file_name, 'r') as f:
            scores = serializer.load(f)
        return scores
    except IOError:
        # if file does not exist - we have no scores
        return {}

"""
    
    
#GET the username, store it in the users file
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        add_to_file("data/users.txt", request.form["username"] + "\n")
        return redirect(request.form["username"])
    return render_template("index.html")


@app.route('/<username>', methods=["GET", "POST"])
def user_game(username):
    data = []
    with open("data/riddle.json", "r") as json_data:
        data = json.load(json_data)
        
    index = 0
    score = 0
   
    
    def add_score_to_file(username, score):
        add_to_file("data/userscore.txt", "({0}) - {1}\n".format(
            username.title(),
            score))
        
    if request.method == "POST":
             
        index = int(request.form["index"])
        user_answer = request.form["message"].lower()
        
        
        if data[index]["answer"] == user_answer:
        # Print correct answer
        # Show score
        # Add score to file
        # Go to next question
            index += 1
            score += 1
            add_score_to_file(username, score)
            print(score)
        else:
            print("That's incorrect!")
    
    if request.method == "POST":
        if user_answer == "mount everest" and index > 9:
            return render_template("end.html")
 
    return render_template("game.html",
                            username=username, data=data, i=index, score=score)

    







app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)