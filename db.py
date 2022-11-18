import pyrebase
import requests

config = {
    "apiKey": "AIzaSyBZXFtpOJNECOVudqc43_Xc-l2QPj9RYrg",
    "authDomain": "db-4c15a.firebaseapp.com",
    "projectId": "db-4c15a",
    "databaseURL": "https://db-4c15a-default-rtdb.firebaseio.com/",
    "storageBucket": "db-4c15a.appspot.com",
    "messagingSenderId": "958653543270",
    "appId": "1:958653543270:web:5c7645bc82dfa7bb544ea7",
    "measurementId": "G-PR7MC32Z9H"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
db_name = "AmazonDB"


def setData(parentName, data):
    '''Set the required data at child named as name'''
    try:
        db.child(db_name).child(data).remove()
        db.child(db_name).child(parentName).set(data)
    except requests.exceptions.HTTPError:
        db.child(db_name).child(parentName).set(data)


def getData(childName):
    '''Get the required data at child named as childName'''
    try:
        res = db.child(db_name).child(childName).get()
        return res.val()
    except requests.exceptions.HTTPError:
        return None
