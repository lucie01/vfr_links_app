import os
from firebase_admin import credentials, firestore, initialize_app
import firebase_admin

# Firebase Initialization
def init_firebase():
    # Get the Firebase certificate path from the environment variable
    firebase_certificate = os.getenv('FIREBASE_CERTIFICATE')
    
    # Print the value to check if it is being fetched correctly (for debugging)
    print('FIREBASE_CERTIFICATE:', firebase_certificate)

    # Check if the environment variable is set
    if not firebase_certificate:
        raise ValueError("Environment variable 'FIREBASE_CERTIFICATE' is not set or is empty.")

    # Check if Firebase is already initialized to avoid duplicate initialization
    if not firebase_admin._apps:
        try:
            # Load credentials from the provided certificate path
            cred = credentials.Certificate(firebase_certificate)
            # Initialize the Firebase app
            initialize_app(cred)
            print("Firebase initialized successfully.")
        except Exception as e:
            raise ValueError(f"Error initializing Firebase: {e}")
    else:
        print("Firebase is already initialized.")
    
    # Return the Firestore client
    return firestore.client()

# Initialize the Firestore client
db = init_firebase()