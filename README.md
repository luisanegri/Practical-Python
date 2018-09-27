# Riddle Game
Demo: http://py-game.herokuapp.com/

## Overview

> Riddle game created in Python. 


## Features

* Users are identified by a unique username (without authentication)
* Multiple users can play at the same time
* To each correct answer 1 point is added, the next question is displayed and the score is printed on the screen 
* To each incorrect answer no point is added and the user can try it again
* The players have the choice to skip a question
* The result is displayed during the game and in the end


## Technologies Used

* HTML
* CSS
* Bootstrap
* Python
* Flask

## Testing

The game's logic was tested manually by comparing the logic applied and the effect achieved.
The capability of having multiple players using the app at the same time in different browsers was also tested.


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








