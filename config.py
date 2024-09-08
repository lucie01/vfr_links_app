import os
import json
import logging
import firebase_admin
from firebase_admin import credentials, firestore

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Firebase Initialization
def init_firebase():

    # Get the Firebase certificate path from the environment variable
    firebase_certificate = os.getenv('FIREBASE_CERTIFICATE')
    firebase_certificate_dict = json.loads(firebase_certificate)
    
    # Print the value to check if it is being fetched correctly (for debugging)
    print('FIREBASE_CERTIFICATE:', firebase_certificate)
    logger.info("FIREBASE_CERTIFICATE", firebase_certificate)

    # Check if the environment variable is set
    if not firebase_certificate:
        raise ValueError("Environment variable 'FIREBASE_CERTIFICATE' is not set or is empty.")
    
    try:
        # Check if Firebase is already initialized to avoid duplicate initialization
        if not firebase_admin._apps:
            # Load credentials from the JSON dictionary
            cred = credentials.Certificate(firebase_certificate_dict)
            # Initialize the Firebase app
            firebase_admin.initialize_app(cred)
            logger.info("Firebase initialized successfully.")
        else:
            logger.info("Firebase is already initialized.")

        # Return the Firestore client
        mydb = firestore.client()

        data = {
            'task': 'Run firestore',
            'status': 'ON_GOING'
        }

        doc_ref = mydb.collection('tasks').document()
        doc_ref.set(data)

        print('Document ID', doc_ref.id)


    except Exception as e:
        logger.error(f"Error initializing Firebase: {e}")
        raise

# Initialize the Firestore client only once
db = init_firebase()
