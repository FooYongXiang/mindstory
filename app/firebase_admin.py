# firebase_admin.py
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("path/to/your/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
