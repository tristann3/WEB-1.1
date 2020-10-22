# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    return "Hello, World!"

@app.route('/profile/<users_name>')
def profile(users_name):
    return f"<h1>Hey! My name is {users_name}</h1>"

if __name__ == '__main__':
    app.run(debug=True)