import firebase_admin
from firebase_admin import credentials
from dotenv import load_dotenv
import os
import json

load_dotenv() 

def init_firebase():
    firebase_creds = os.getenv("FIREBASE_CREDENTIALS")

    if not firebase_creds:
        raise ValueError("❌ FIREBASE_CREDENTIALS no está en el .env")

    firebase_creds_json = json.loads(firebase_creds)

    if not firebase_admin._apps:
        try:
            cred = credentials.Certificate(firebase_creds_json)
            firebase_admin.initialize_app(cred)
            print(">>> Firebase inicializado correctamente")
        except Exception as e:
            print(f">>> Error al inicializar Firebase: {e}")
    else:
        print(">>> Firebase ya estaba inicializado")
