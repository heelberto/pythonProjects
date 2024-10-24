from flask import Flask
import random

app = Flask(__name__)
num = random.randint(0, 10)

@app.route("/")
def hello_world():
    return '<h1 style="display: flex; justify-content:center;">Guess a number between 0 and 9</h1>' \
            '<img src="https://i.giphy.com/3o7aCSPqXE5C6T8tBC.webp">'


@app.route("/<int:guess>")
def check_num(guess):
    if guess < num:
        return '<h2 style="color:purple;">Too low, try again!</h2>'\
                '<img src="https://i.giphy.com/jD4DwBtqPXRXa.webp">'
    elif guess > num:
        return '<h2 style="color:red;">Too high, try again!</h2>' \
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return '<h2 style="color:green;">Correct!</h2>'\
                '<img src="https://i.giphy.com/4T7e4DmcrP9du.webp">'



if __name__ == "__main__":
    app.run(debug=True)
