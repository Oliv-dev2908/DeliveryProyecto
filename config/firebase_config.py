import firebase_admin
from firebase_admin import credentials
import os
import json

def init_firebase():
    firebase_creds_json = {
  "type": "service_account",
  "project_id": "ferreteria-unic-delivery",
  "private_key_id": "6bb03a9ff34bab411aec8bfad6f343751dd50522",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCxAf7fZLvbzZRT\nGBr0Fnfe9j3JO/FpQQl/i9ZM1ZE9yq67W2tydFzmpXATUY+846FUWN7X6QLqVOrU\nqyUzt5tZVZlP2soOJy6t4yyzi3z3KpfvkrHym0TxDIuJFC4kCqKx9lgKQQHIleqo\nOsWr4vlOVmbDXKyaXjAcYTcsBZHMHmEL1RsuDmPgjOnzxE5WtsNzrJ1i/Zs9trEw\nYI/H1Fx+S9AiimygL1fue4DywMDdBjLit3oppDysyStKqAbphKJIkinDt7up3Hen\nDHmW8zfvWPIds9ZXODpRTYz2ww5OK/thUPuXn5h0PzZU0GfQlvnsPoUP57iOCBc4\nzvqyf3q7AgMBAAECggEABItTEkQhSIbSGIIFax/KiwhSVMC7tWKMjmA2K7nN5UK3\nUqsJqqIPIoK7ylstMAG+Cg7QBcX/I6nzb2tHZLkBfX0jlve8eTmLSr6Kzr81gZjv\n1qAy/lH7Jp8WU/oXJyi4vY3f+79oftBOemwr1/pXQSoZsElISxxA6vGZ+4DXGeDg\n1ORDM84YhWPcc79TP6kEBFGkeQ/4moHVzdqqKcBCWPksIkKqcoZzaP13ll+lLI6D\npNo8WezkEdZLP73vieL+Vq5I4AuDSSd4As+LsfE+x9tcwOBuw4s9qh8iD1Pz1KU6\nM8hh4rS+0HV6QVmBsicwLPL/6vXlIx3HcMYqvd5rQQKBgQDh7GeMfUE8MIQm1oub\n4XU2iTtnGakW3SOh28Y5Pgky+v+1maV22/Bhhlg/0TcUpp7Rt/zpRhdxarByFaCt\ndy2oJVl0LiWdPm4BRUoJleoVZpH0UCCv+g/sQODwa7//LG4cwWX9uoOzWm3YJ/+H\nI1pB3toiioCgnKtk7WraEQcO+wKBgQDIkoS/JD3GnX1CreDUFh6HKLmrVpN73CId\nJdHyqWCjlN47VZKc4Rg/wRc48FtCIU1BKJ3uDxr7r0nHu4FVq3gJU5aBCnFHedjy\nCn2CuIsKenP5biVF3QroSy/MU1JOt65ff38DLPhdHqRzH2LwZoDCEtfQdXR33+CH\nm2h2Itp3QQKBgE+30C31gJBRekAOEkMVwftVXx2ZI14K9+jEGOTX6/0OLi6RIZ6Y\nKvDuq7MRCsOBq6bKqjZR4jHF+K64zPKIjBa53x+srN8YSU6veVl6iZe1kqjHoVEX\nBolRt01+Z8gNkGkbIPbv2kruDLZqHrM7mTyG+yeXAZ4qyhuZ3stFmN0DAoGAHNEw\nUWYbmhW2kYX5737eE/097+gYeItAO3/bkknToK0a4NuCnReaLE7Jz1x5QB8Ywmvb\nhQCWl+Kvbwr5oh1oua5QyWl+rQ5MpTnsnoN1NqQxVX0FzevcTVPAIlM2WCj73Kys\nywADDx3/8qpnxLJ1fWzHpSO7AB4iXFlvwMlxKgECgYEAmU0rJ48ViGU0hcgVnsrR\n5aQf9eLNI5NvJ9YqrD0uqymjFyQgXzieUaKvbCb1SWkFHgT+vsRysjbGaSZZLtdX\nDF2KOExjIPHDPPeKswLQ4+ElP0SnMxHcH/imIlkXAzH++tNDrpj8sWSJtri11F8s\nqhKggmUTrnxHfFXd0WBk/w0=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-fbsvc@ferreteria-unic-delivery.iam.gserviceaccount.com",
  "client_id": "117511321344221989615",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40ferreteria-unic-delivery.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
    
    if firebase_creds_json:
        creds_dict = json.loads(firebase_creds_json)
        cred = credentials.Certificate(creds_dict)
        firebase_admin.initialize_app(cred)
        print("Firebase inicializado correctamente")
    else:
        print("Advertencia: FIREBASE_SERVICE_ACCOUNT no encontrada en el entorno")