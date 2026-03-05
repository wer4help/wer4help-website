from flask import Flask, render_template
import socket

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/events")
def events():
    return render_template("events.html")


@app.route("/team")
def team():
    return render_template("team.html")


@app.route("/activity-reports")
def activity_reports():
    return render_template("activity_reports.html")


@app.route("/orientation")
def orientation():
    return render_template("orientation.html")


@app.route("/vighna-vinuta")
def vighna_vinuta():
    return render_template("vighna_vinuta.html")


@app.route("/donate")
def donate():
    return render_template("donate.html")


if __name__ == "__main__":

    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    print("\nAccess the website using:")
    print("http://127.0.0.1:5000")
    print(f"http://{local_ip}:5000\n")

    app.run(host="0.0.0.0", port=5000, debug=True)