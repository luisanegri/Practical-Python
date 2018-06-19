import os
import json 
from flask import Flask, redirect, render_template, request


app = Flask(__name__)


# variable with the Riddles - json file
data = []
# Score starting at 0
score = 0
# Riddle index starting at 0
riddle_index = 0



def add_to_file (filename, data):
    with open (filename, "a") as file:
        file.writelines(data)


#store users in users.txt 
def add_users (username):
    add_to_file("data/users.txt", "{0}")


def store_user_score(username, score):
    #dictionary to store username and score
    user_data =  {}
    #key/value
    user_data['username'] = username
    user_data['score'] = score
    return(username, score)


# create file and open it in write mode
with open('data/usersdata.json','w') as f:
    print json.dump(out, f, indent=2)      
    
    
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
            # Increment score
            score += 1
            # Add username/score to function
            store_user_score(username, score)
            # Go to next question
            riddle_index += 1
        else:
            print("That's incorrect!")
    
    
    if request.method == "POST":
        if user_answer == "mount everest" and riddle_index > 9:
            return render_template("end.html")
 
 
    return render_template("game.html",
                            username=username, data=data, riddle_index=riddle_index, 
                            score=score, total_questions=total_questions)

    







app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)