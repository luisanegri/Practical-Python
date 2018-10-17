# Riddle Game
Demo: http://py-game.herokuapp.com/

## Overview

> This logic-driven web application created in Python is a riddle game that will generate 10 riddles to be unraveled.

## UX

This game was created for people who enjoy to exercise their minds through challenges but also enjoy having some fun!

* Users are identified by a unique username (without authentication)
* To each correct answer 1 point is added, the next question is displayed and the score is printed on the screen 
* To each incorrect answer no point is added and the user can try it again
* The players have the choice to skip a question
* The result is displayed during the game and in the end
* Multiple users can play at the same time

## Technologies Used

* HTML
* CSS
* Bootstrap
        - to give a responsive design 
* Python
        - to build the game's logic
* Flask
        - as a webframework for Python

## Testing

The game's logic was tested manually by comparing the logic applied and the effect achieved

1. Choosing an username
-If the form is not filled out the game does not start. :heavy_check_mark:

2. Riddles
-Each time the user gives the correct answer the next riddle is loaded. :heavy_check_mark:

4. Skip riddle
-Every time the user skips the riddle, the next riddle is loaded. :heavy_check_mark:

3. Scoring
-Each time the user answers correctly, 1 point is added to the user's score. :heavy_check_mark:
-Each time the user answers incorrectly, the user does not get any point. :heavy_check_mark:
-The points are accumulated throughout the game. :heavy_check_mark:


The capability of having multiple players using the app at the same time in different browsers was also tested.
A user is able to use the back/forward button without breaking the site.


## Deployment

* This project was deployed at Heroku
Procedure:
1. Create requirements.txt 

        pip3 freeze --local requirements.txt
        
2. Create Procfile

        echo web: python run.py > Procfile
        
3. Create [Heroku](https://www.heroku.com/) App 
4. Set Config Vars adding IP and PORT on Heroku app settings

        IP 0.0.0.0
        PORT 5000
        
5. Login to Heroku on the terminal

        Heroku login
        
6. Deploy to Heroku

        Scale the app's web process to 1 dyno: heroku ps:scale web=1
        git remote add https://git.heroku.com/py-game.git
        git push heroku master








