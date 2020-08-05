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


@app.route('/contact')
def subscribe():
    title = "Contact Me"
    return render_template("contact.html", title=title)
