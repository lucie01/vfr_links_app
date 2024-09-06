from firebase_admin import credentials, firestore, initialize_app

# Firebase Initialization
def init_firebase():
    cred = credentials.Certificate('./vfrota.json')  # Replace with your Firebase Admin SDK key file path
    initialize_app(cred)
    return firestore.client()

db = init_firebase()
