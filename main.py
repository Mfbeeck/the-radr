from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request
from models import db
from flask_bootstrap import Bootstrap
import data_functions as data_funcs


app = Flask(__name__)

POSTGRES = {
    'user': 'matiasbeeck',
    'pw': '',
    'db': 'nnm-db-dev',
    'host': 'localhost',
    'port': '5432',
}
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
SQLALCHEMY_TRACK_MODIFICATIONS = True

db.init_app(app)

# Instantiate bootstrap
Bootstrap(app)

RANGE_DICT = dict(short_term='Last Month', medium_term='Last 6 Months', long_term='All Time')
FILTER_DICT = dict(popularity='Current Popularity', followers='Follower Count', name='Alphabetical')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/top_artists")
def top_artists(time_range=None):
    if request.args.get('time_range') is not None:
        time_range = request.args.get('time_range')
    else:
        time_range = 'short_term'
    df = data_funcs.get_top_artists()
    return render_template("top_artists.html", df=df[df.time_range==time_range], range_dict=RANGE_DICT, time_range=time_range)

@app.route("/top_tracks")
def top_tracks(time_range=None):
    if request.args.get('time_range') is not None:
        time_range = request.args.get('time_range')
    else:
        time_range = 'short_term'
    df = data_funcs.get_top_tracks()
    return render_template("top_tracks.html", df=df[df.time_range==time_range], range_dict=RANGE_DICT, time_range=time_range)

@app.route("/followed_artists")
def followed_artists(sort=None):
    if request.args.get('sort') is not None:
        sort = request.args.get('sort')
    else:
        sort = 'popularity'
    df = data_funcs.get_followed_artists().sort_values(by=sort, ascending=False).head(30)
    return render_template("followed_artists.html", df=df, filter_dict=FILTER_DICT)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
