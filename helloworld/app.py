# app.py
from random import randint
from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'


@app.route('/penguins')
def favoriteAnimal():
    return "Penguins are cute!"

@app.route('/dogs')
def myFavoriteAnimal():
    return "Dogs are awesome!"

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f'Wow, {users_dessert} is my favorite dessert too!'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    return f'One day I {adjective} and bought a {noun}'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    try:
        answer = int(number1) * int(number2)
    except:
        return "Invalid inputs. Please try again by entering 2 numbers!"
    return f'{number1} times {number2} is {answer}.'

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    string = ""
    try:
        for x in range(int(n)):
            string = string + " " + word
    except:
        return "Invalid input. Please try again by entering a word and a number!"
    return string

@app.route('/reverse/<word>')
def reverse(word):
    newStr = ""
    for x in range(len(word)):
        newStr = newStr + word[-1]
        word = word[:-1]
    return newStr

@app.route('/strangecaps/<word>')
def strangecaps(word):
    newStr = ""
    for x in range(len(word)):
        if (x%2 == 0):
            newStr = newStr + word[x].lower()
            print(word[x])
        else:
            newStr = newStr + word[x].upper()
    return newStr

@app.route('/dicegame')
def dicegame():
    randomNum = randint(1,16)
    if (randomNum == 6):
        return f"You rolled a {randomNum}. You Win!"
    else:
        return f"You rolled a {randomNum}. You Lose!"






if __name__ == '__main__':
    app.run(debug=True)