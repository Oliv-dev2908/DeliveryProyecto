import firebase_admin
from firebase_admin import credentials
import os
import json

def init_firebase():
    firebase_creds_json = json.loads(os.getenv("FIREBASE_CREDENTIALS"))

    if not firebase_admin._apps:
        try:
            cred = credentials.Certificate(firebase_creds_json)
            firebase_admin.initialize_app(cred)
            print(">>> Firebase inicializado correctamente")
        except Exception as e:
            print(f">>> Error al inicializar Firebase: {e}")
    else:
        print(">>> Firebase ya estaba inicializado")
