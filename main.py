import json

from flask import Flask, redirect, url_for, request, Response, jsonify, render_template
import csv

from recommendation import genre_choosing
from songInfo import uzyskajInformacje

app = Flask(
  __name__,
  template_folder='htmlTemplates'
)

@app.route("/")
def hello():
    return render_template('welcomePage.html')

@app.errorhandler(404)
def notFound(error=None):
    message = {
        'status': 404,
        'message': 'Not found ' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

@app.route("/makePlaylist")
def playlista():
    return render_template('makePlaylist.html')

@app.route("/recommendation")
def rekomendacja():
    return render_template('recommendation.html')

@app.route("/searchSongs")
def poszukajPiosenki():
    return render_template('searchSongs.html')

@app.route("/genreRecommendation", methods=['GET','POST'])
def rekomendacjaPoGatunku():
    if request.method == 'GET':
       genre = request.args.get('genre')
       songs = genre_choosing(genre)
       return render_template('genreRecommendation.html', songs=songs)
    else:
        return render_template('genreRecommendation.html')

@app.route("/artistRecommendation", methods=['POST'])
def rekomendacjaPoArtyscie():
    return render_template('artistRecommendation.html')

@app.route("/songRecommendation", methods=['POST'])
def rekomendacjaPoPiosence():
    return render_template('songRecommendation.html')

@app.route("/songInfo", methods=['GET','POST'])
def informacjeOPiosence():
    if request.method == 'POST':
       zasob = request.form.get('zasob')
       title, text = uzyskajInformacje(zasob)
       return render_template('songInfo.html', title=title,text=text)
    else:
        return render_template('songInfo.html')
