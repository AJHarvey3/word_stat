from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/length")
def length():
    words = request.args.get("word")
    word_count = len(words.split())
    character = len(words)
    avg_length = character/word_count
    return render_template("length.html", character=character, word_count=word_count, avg_length=avg_length)


if __name__ == '__main__':
    app.run()