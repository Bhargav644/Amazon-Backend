
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
app = Flask(__name__)
#!Categories


@app.route("/Categories", methods=["POST", "GET"])
def fetchCategories():
    if request.method == "POST":
        Categories()
    return getData("Categories")

#!Deals


@app.route("/Deals", methods=["POST", "GET"])
def fetchDeals():
    if request.method == "POST":
        Deals()
    return getData("Deals")

#!Cards


@app.route("/Cards", methods=["POST", "GET"])
def fetchCards():
    if request.method == "POST":
        Cards()
    return getData("Cards")

#!Footer


@app.route("/Footer", methods=["POST", "GET"])
def fetchFooter():
    if request.method == "POST":
        Footer()
    return getData("Footer")

#!nav-images


@app.route("/nav-image", methods=["POST", "GET"])
def fetchNavImage():
    if request.method == "POST":
        Image()
    return getData("nav-image")

#!BackgroundImages


@app.route("/BackgroundImages", methods=["POST", "GET"])
def fetchBGImage():
    if request.method == "POST":
        BackImages()
    return getData("BackgroundImages")


#!Credentials
@app.route("/Credentials")
def fetchCredentials():
    return getData("Credentials")


#!HMenu
@app.route("/HMenu")
def fetchHMenu():
    return getData("HMenu")


#!Credentials
@app.route("/Cred", methods=["POST"])
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
def getSearch():
    data = Searching(request.json['tag'])
    return data


if __name__ == "__main__":
    app.run()
