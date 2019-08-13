from flask import Flask, render_template
from flask_bootstrap import Bootstrap

import data_functions as data_funcs

app = Flask(__name__)
# Instantiate bootstrap
Bootstrap(app)

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
    df_followed_artist = data_funcs.get_followed_artists()
    return render_template("followed_artists.html", df=df_followed_artist.head(30))

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
