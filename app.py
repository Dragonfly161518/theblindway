import os

from flask import Flask
from flask import request
from firebase import firebase
import datetime


app = Flask(__name__)


@app.route('/')
def hello_world():
    target = os.environ.get('TARGET', 'World')
    return 'Hello {}!\n'.format(target)


@app.route('/login', methods=['POST'])
def login():

    firebase = firebase.FirebaseApplication(
        "https://theblindway-b62dc.firebaseio.com/", None
    )

    firebase.post(
        "/g01",
        {
            "Debug": datetime.datetime.now()
        },
    )
    return "OK"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
