from flask import Flask, request, jsonify
from scraper import get_all_persons

app = Flask(__name__)

# GET request
@app.route('/')
def getAll():
    return jsonify(get_all_persons()), 200

# GET request
@app.route("/get_artist/<index>")
def getArtist(index, artist_firstname, artist_lastname, field):
    artistsData = {
        "index": index,
        "firstname" : artist_firstname,
        "lastname": artist_lastname,
        "field" : field
    }

    extra = request.args.get("extra")
    if extra:
        artistsData["extra"] = extra
        
    return jsonify(artistsData), 200

# # POST request
# @app.route("/create_artist", methods=["POST"])
# def create_artist(): 
#     data = request.get_json()

#     return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug = True)