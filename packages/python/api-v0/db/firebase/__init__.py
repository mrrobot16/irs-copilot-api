import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

# Initialize Firebase Admin SDK
credentials = credentials.Certificate("./credentials/firebase/irscopilot-dev-firebase-adminsdk-72ar9-0b73aebc83.json")
firebase_admin.initialize_app(credentials)

client = firestore.client()

# Firestore database instance
firestore_db  = client