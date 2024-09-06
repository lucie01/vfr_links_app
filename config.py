import os
from firebase_admin import credentials, firestore, initialize_app

# Firebase Initialization
def init_firebase():
    firebase_certificate = os.getenv('FIREBASE_CERTIFICATE')
    cred = credentials.Certificate(firebase_certificate)  # Replace with your Firebase Admin SDK key file path
    initialize_app(cred)
    return firestore.client()

db = init_firebase()
