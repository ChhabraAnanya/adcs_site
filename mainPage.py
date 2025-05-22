from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/past-events")
def past_events():
    return render_template("past_events.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/upcoming-events")
def upcoming_events():
    return render_template("upcoming_events.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/mission")
def mission():
    return render_template("mission.html")

if __name__ == "__main__":
    app.run()