import os
from flask import Flask
from flask import request
import datetime
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate(os.getcwd() + '/serviceAccountKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://theblindway-b62dc.firebaseio.com"
})

ref = db.reference('fuck')

config = {
    "apiKey": "AIzaSyCoLhhc45GCqQZWFGtUCf5G_1QAmUTI_QI",
    "authDomain": "theblindway-b62dc.firebaseapp.com",
    "databaseURL": "https://theblindway-b62dc.firebaseio.com",
    "projectId": "theblindway-b62dc",
    "storageBucket": "theblindway-b62dc.appspot.com",
    "messagingSenderId": "277283139846",
    "appId": "1:277283139846:web:f6929cbd3dec5775d3ae87",
    "measurementId": "G-CMESXDR2Q5"
}

# firebase = pyrebase.initialize_app(config)
# db = firebase.database()


app = Flask(__name__)


@app.route('/')
def hello_world():
    target = os.environ.get('TARGET', 'World')
    return 'Hello {}!\n'.format(target)


@app.route('/test', methods=['POST'])
def test():
    users_ref = ref.child('test')
    users_ref.set({
        'alanisawesome': {
            'date_of_birth': 'June 23, 1912',
            'full_name': 'Alan Turing'
        },
        'gracehop': {
            'date_of_birth': 'December 9, 1906',
            'full_name': 'Grace Hopper'
        }
    })
    data = request.json
    params = data['params']
    arr = np.array(data['arr'])
    print(params, arr.shape)
    return "Success"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
