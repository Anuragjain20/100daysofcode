from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        function()
        return "<b>" + function() + "</b>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        function()
        return "<em>" + function() + "</em>"

    return wrapper


def make_underlined(function):
    def wrapper():
        function()
        return "<u>" + function() + "</u>"

    return wrapper


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media.giphy.com/media/UIpzEC5QTvuOQ/giphy.gif" width=200>'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye!'


@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello there {name}, you are {number - 1}"


if __name__ == "__main__":
    # Run in debug mode
    app.run(debug=True)
