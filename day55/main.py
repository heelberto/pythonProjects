from flask import Flask

app = Flask(__name__)

def make_underlined(func):
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper


def make_italic(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper


def make_bold(func):
    def wrapper():
        return f"<bold>{func()}</bold>"
    return wrapper


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
@make_italic
@make_bold
def bye():
    return "<h1>Goodbye!</h1>"


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
