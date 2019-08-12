from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/top_artists")
def top_artists():
    return render_template("top_artists.html")

@app.route("/top_tracks")
def top_tracks():
    return render_template("top_tracks.html")

@app.route("/followed_artists")
def followed_artists():
    return render_template("followed_artists.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
