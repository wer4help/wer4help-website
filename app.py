from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/leadership")
def leadership():
    return render_template("leadership.html")


@app.route("/team")
def team():
    return render_template("team.html")


@app.route("/events")
def events():
    return render_template("events.html")


@app.route("/impact")
def impact():
    return render_template("impact.html")  
# change later if you create impact.html


@app.route("/acknowledgment")
def acknowledgment():
    return render_template("acknowledgment.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/donate")
def donate():
    return render_template("donate.html")


if __name__ == "__main__":
    app.run(debug=True)
