import os
import json
import logging
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TYPE = "service_account" #os.getenv("TYPE")
PROJECT_ID = "vfrota" #os.getenv("PROJECT_ID")
PRIVATE_KEY_ID = "a8f2344669ca096215729f794e5511602439ab8e" #os.getenv("PRIVATE_KEY_ID")
PRIVATE_KEY = "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDjvvprHk9H0cUf\nDtvSJgDQx2C+zssFAxyTfN0sa8k2J99H00VlsMvq9Iu9/htD3GrUIEvUl/Vylhpr\n6P1xUkx2ewSvAc/+ohNMLJ3Cr8wkJ217n8X2Gx3TacC+h3X6mCpHir0QNNUkwz7T\nlS229GIg7pvtwyGCO2rkaD3CU890ihV0w5HIrnYJ8JCeSaHR/jPQkvsy0sJBTYut\nGjYS2BzrpDNUHttbeelRV/sEUgwFCOR9HvXCha1EXlLXZ1OqGVSTC15A3ZXcQ1cf\n1dHrbhrL3Ts4PcsW+VGK5izSX/maUmXtJq00lczWCm8MYjWnI52iEsveTWpCWasl\nmu+GNTOpAgMBAAECggEABkY1JO1VVs+vJA9nO+9jF11ey3LsAevXhjKq7zXa+bx4\neMSXxVjtDUCGdwoAm0p/wO9Q138GOo1rFez5ynzvcVYrR1z/625wpKkYAYyRTa+u\nYvkAXarak//2WOlndStrAsSON9uUwaoFWZPjCgbKi0i3kAHPswRLChbbGLbxYK79\n4O28Qq193JpdNz1MACR5rBE/8k6Um4zghx6QSy/FiKp+KSlDti1YiuORysIv6GKE\nrAYnNG+lUGID+4P8ommaKY/dde0IHn0Jon2cfIWB8gonuhvmocv41/U7d3IQluO5\nsADbu1rpZZ/+66FTpL806KIQ4UpDaDl03l4TjNvBgQKBgQD1nckgbbrUj4OKP489\ng+TpFWS5RLW/l6wqG7sn9Ky/Hx/wGnEQwANoGxLAE56DQ1fWy4AehD1OesfzEZtD\nqc4bdECKcIOg4UzNKTaGxNWFOpsH+7D22pP4vSbvkwK1xQC32bwtlGkfUz7kYcew\nh+uzHFENGp9lZNE59qIrO4oBIQKBgQDtX8nabuh+p9ZUMo8ctdIj3/xqr7jrZAOh\nO0rcz4nEQBIlo/XWmMLBjQeGwDZhwSKMKeHf4TgrvUajDA7S54SjFZJ2i95Pgn23\nnYs70Zgp3zpvUU3XL3p0G6Y5ZNzw5KiV8HViCExU9WAzcsZLQvhxhz/LMPqOnXa0\njuZYipJ5iQKBgGS1pdpeI9U0Y0M0fI9EnX/U/c/ZlIxSrI03ga4IbSyQno/cx6+O\ni9cMAswvPzejTUkNeCMLJfgf8AyCk59S6Ofo6u3Y5J/6wXr+AxWPb92JAjhrw0v0\no+fB500kgl/1vy2jYb1utQvbHlaWoUKI+OQgIDu3RtRUWlXiAuynJRcBAoGBANEn\nv+JaKz2+gVm7GuK/SqQVroIKx7ORcqlUZ0hdDhUAJ31HFUy7WY/VxjXzk3dbCCfc\nl4v/FNFle6Ia88zd9r8EOQN/hqkkX8W0aYSRz7PFX+XKC/55dTptSm/z8cHImMtV\nDvkMOsX5V4S9sv+JyQOvmoRdacjT8k5yQ4DsyNeRAoGBAJZKnAzUFRRELKsYvwf4\nZpcbDGP179HpcL8NPJlRIMYcQJ+WJAJKn0hQbQtgXcn3O1iH3Dqs8FEpV2C7uRWs\nA2u2zb4pooycvRcUtd5YiTtHIyHTfoQfa8NDMRfdp+Pync9g5EGmkssJ+GQIpk9z\nk6qzAreCX0tUMbTAGYT8qDON\n-----END PRIVATE KEY-----\n" #os.getenv("PRIVATE_KEY")
CLIENT_EMAIL = "firebase-adminsdk-9wl0p@vfrota.iam.gserviceaccount.com" #os.getenv("CLIENT_EMAIL")
CLIENT_ID = "100293696991674992450" #os.getenv("CLIENT_ID")
AUTH_URI = "https://accounts.google.com/o/oauth2/auth" #os.getenv("AUTH_URI")
TOKEN_URI = "https://oauth2.googleapis.com/token" #os.getenv("TOKEN_URI")
AUTH_PROVIDER_X509_CERT_URL = "https://www.googleapis.com/oauth2/v1/certs" #os.getenv("AUTH_PROVIDER_X509_CERT_URL")
CLIENT_X509_CERT_URL = "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-9wl0p%40vfrota.iam.gserviceaccount.com" #os.getenv("CLIENT_X509_CERT_URL")
UNIVERSE_DOMAIN = "googleapis.com" #os.getenv("UNIVERSE_DOMAIN")


# Create a dictionary with the environment variables
env_vars = {
    "type": TYPE,
    "project_id": PROJECT_ID,
    "private_key_id": PRIVATE_KEY_ID,
    "private_key": PRIVATE_KEY,
    "client_email": CLIENT_EMAIL,
    "client_id": CLIENT_ID,
    "auth_uri": AUTH_URI,
    "token_uri": TOKEN_URI,
    "auth_provider_x509_cert_url": AUTH_PROVIDER_X509_CERT_URL,
    "client_x509_cert_url": CLIENT_X509_CERT_URL,
    "universe_domain": UNIVERSE_DOMAIN,
}
# Load environment variables from .env file
load_dotenv()

# Firebase Initialization
def init_firebase():
    try:
        # Check if Firebase is already initialized to avoid duplicate initialization
        if not firebase_admin._apps:
            # Load credentials from the JSON dictionary
            cred = credentials.Certificate(env_vars)
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
