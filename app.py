from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    title = "Chris Ladd's Portfolio"
    return render_template("index.html", title=title)


@app.route('/about')
def about():
    title = "About Chris Ladd!"
    names = ["John", "Mary", "Wes", "Sally"]
    return render_template('about.html', names=names, title=title)


@app.route('/subscribe')
def subscribe():
    title = "Subscribe to My Email Newsletter"
    return render_template("subscribe.html", title=title)
