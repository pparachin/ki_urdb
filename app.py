import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
 'mysql://root@localhost:3306/ki_urdb_parachin'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config.from_mapping(SECRET_KEY="dev")

db = SQLAlchemy(app)

import songs, albums, authors, genres, nationalities

app.register_blueprint(songs.bp)
app.register_blueprint(albums.bp)
app.register_blueprint(authors.bp)
app.register_blueprint(genres.bp)
app.register_blueprint(nationalities.bp)


@app.route('/')
def index_view():  # put application's code here
    return render_template('index.html')



if __name__ == '__main__':
    app.run()
