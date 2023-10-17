import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
from config import FIREBASE_CREDENTIALS

# Initialize Firebase Admin SDK

# Mock credentials
do_what_ever_credentials = credentials.Certificate('./credentials_example/firebase/do-what-ever-firebase-adminsdk-64t1o-b5724b437b.json')
firebase_admin.initialize_app(do_what_ever_credentials)
# credentials = credentials.Certificate("./credentials/firebase/irscopilot_dev-72ar9-0b73aebc83.json")
# credentials = credentials.Certificate(FIREBASE_CREDENTIALS)
# firebase_admin.initialize_app(credentials)

client = firestore.client()

# Firestore database instance
firestore_db  = client