
from pickle import TRUE
from flask import Flask, request
from db import getData, setData
import bcrypt
from Categories import Categories
from Deals import Deals
from CardsLayouts import Cards
from HeaderImage import Image
from password import salt
from flask.helpers import send_from_directory
from BackgroundImages import BackImages
from Footer import Footer
from Searching import Searching
from flask_cors import CORS, cross_origin
app = Flask(__name__, static_folder='Amazon-Clone/build', static_url_path='')
CORS(app)
#!Categories


@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')


@app.route("/Categories", methods=["POST", "GET"])
@cross_origin()
def fetchCategories():
    if request.method == "POST":
        Categories()
    return getData("Categories")

#!Deals


@app.route("/Deals", methods=["POST", "GET"])
@cross_origin()
def fetchDeals():
    if request.method == "POST":
        Deals()
    return getData("Deals")

#!Cards


@app.route("/Cards", methods=["POST", "GET"])
@cross_origin()
def fetchCards():
    if request.method == "POST":
        Cards()
    return getData("Cards")

#!Footer


@app.route("/Footer", methods=["POST", "GET"])
@cross_origin()
def fetchFooter():
    if request.method == "POST":
        Footer()
    return getData("Footer")

#!nav-images


@app.route("/nav-image", methods=["POST", "GET"])
@cross_origin()
def fetchNavImage():
    if request.method == "POST":
        Image()
    return getData("nav-image")

#!BackgroundImages


@app.route("/BackgroundImages", methods=["POST", "GET"])
@cross_origin()
def fetchBGImage():
    if request.method == "POST":
        BackImages()
    return getData("BackgroundImages")


#!Credentials
@app.route("/Credentials")
@cross_origin()
def fetchCredentials():
    return getData("Credentials")


#!HMenu
@app.route("/HMenu")
@cross_origin()
def fetchHMenu():
    return getData("HMenu")


#!Credentials
@app.route("/Cred", methods=["POST"])
@cross_origin()
def checkCred():

    flag = False
    password = bytes(request.json['pass'], 'utf-8')
    userName = request.json['user']
    data = getData("Credentials")

    oPassworwd = data['password']
    oUserName = data['username']

    if(userName == oUserName):
        hashed = bcrypt.hashpw(password, salt)
        if(oPassworwd == str(hashed)):
            flag = True

    return {"authentication": flag}

#!Searching


@app.route("/Search", methods=["POST", "GET"])
@cross_origin()
def getSearch():
    data = Searching(request.json['tag'])
    return data


if __name__ == "__main__":
    app.run(debug=True)
