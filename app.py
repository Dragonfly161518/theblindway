import os
from flask import Flask
from flask import request
import datetime
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from pyzbar import pyzbar

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
    print("TESTTTTTTTTTTTTTTTTTTTTTTTT")
    return 'Hello {}!\n'.format(target)


@app.route('/test', methods=['POST'])
def test():
    data = request.json
    frame = np.array(data['frame'])
    ref.child('np').set({"code": "frame.tolist()"})
    barcodes = pyzbar.decode(frame)
    Distancepx = 103  # px unit
    Distancecm = 60  # cm unit
    DefaultSize = 15  # cm unit
    FocalLength = Distancepx * Distancecm / DefaultSize
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        barcodeData = barcode.data.decode("utf-8")
        # barcodeType = barcode.type

        ref.set({
            "Line": barcodeData,
            "Distance": DefaultSize * FocalLength / h,
            "X": (x + w) / 2,
            "Y": (y + h) / 2,
            "TimeStamp": datetime.datetime.now(),
        })

    return "Success"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
