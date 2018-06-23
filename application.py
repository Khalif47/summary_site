from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from Summarising.word_processor import summarize, input_file

# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/summary")
def summary():
    return render_template('summary.html')


@app.route("/feedback")
def feedback():
    return render_template('feedback.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == "POST":
        text = request.form['text_a']
        # word barrier
        words = input_file(text)
        words = words.word_barrier()
        sentences = summarize(text, words)
        return render_template('result.html', sentences=sentences)

app.run("0.0.0.0", "8080")
