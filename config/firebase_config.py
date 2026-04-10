import firebase_admin
from firebase_admin import credentials
import os
import json

def init_firebase():
    firebase_creds_json = {
      "type": "service_account",
      "project_id": "ferreteria-unic-delivery",
      "private_key_id": "f651c8c117badccafeaa10c85bfce810ad7bdd43",
      "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCe9sYcKr/ewOGe\nMZ6QCdYPB+aWYYUyCERAeh2NPpQl2KEG5bGKc34+lDQgj0c+o2GETurOhiGEVAug\nOah9z+kofsE8y/yjewNyZEv5cgAypjry33OH3J8x3ngpaHxUqezrfexZTQT8d3ds\ndpoAu2SWl8zZiYy+eh5S80+co9Co4CSdRNnE8vRxjh1pS66tiRSOqRARevjUlfBP\nv/vwyd6y5l1XZFep2OVCEGuq7fwqZYmNA0FMluR/WUiyiZCYjz5ytxUHNvBcSl2m\nOavZUmq1Xs6+mcoxjpkN9Ey6+Ci4GqyOn9SnhkJD4kjcq8xFpMrw0D9bZB4ADBL5\n+PovnpT9AgMBAAECggEAGOWsrK+zYneSPr0lyQiJWsxRfL8kZewuiGy34S3qdS0D\nN3nVP0qMfM+ohGr8bR6YwOi9VQBkEn45Xex5686bBYkoydVnKdGz/gAgeB63Ujd/\n5xdBWIeg9WYTKuUfCAGfRljwIiJyg/pQHZBL2Y6AGCgJYQ7umMy2oCZUk0ODBFfr\nnCmhj3sJQi9yiNdDao7Ehd0vFggHNAP74bGyyNsHBiH7a2XwYp5oJBWscEFLp8JE\nsCel4hgtxYxSHOZbicly1Yy6X0oMt+e14TYWw0tADeZDp7P4WTrP87x48cHxIQtd\n477kO+0E5mISfn/SOhfXIBi0kUF8RMzvgmljsWMl4QKBgQDPw1brqrDr1M8K9kPY\nJQaxtztiyN3mXC0X8k8V8Mg+54tSWAFr2z9UtqJON3VkUX4L0tvGPLxHsdLCwBOT\nob+5YP25m5BA7URrlh2Mow6AVnAOMQFx961Tmoi4by8Zebeojkn7g7AJLSWog5n6\nf8jBfespv6wIOI0ClnGvHuDsbQKBgQDD3v+umgmM4LdSlrNIrVdzBkYPd+XHosQa\nug4PeXU886vpIbIDJlUox9cZzJCGj/F39JS+S4WrSZnvbT4sWN0ljD3quipLkuBw\nz8btKN88NXLsDMNA0IpcuA7SWrPZwm72tI9C52zN+Piixx+X43ZGYS3RnARdTQ8m\nJyzoKFnQ0QKBgQCBg43tvywm9zRR6w6D8SDpLAYTIJBjh9Z8dQqj7MOHoyOQo1fP\neo9SKb+n7p55eOuQR1PFkhr0vn9Z9A7AGza/Qx0n1TfpoX7jamLlRshFbJzR2+7A\nstsToOPVxUmhIeVBZ+Hqrj7QmZo+IDuekoX9SJeOIPQG8+nDUTFxL1ibSQKBgFJD\npXUqoto1Qyl/u7rJetIHj4NNowcuuFhVTjR3maLI4KngighCoD+pdxER1p19dTgh\nVBt8Up63IdzqL9OmWvM7LIIaQEtPW85lpbHTmbaK6EJ1tcfSDlqUvzzf9Wt++uXI\nveamlg8IAz0yjnVXhkRW6kx/z2F0TOmESJsU32wRAoGAdmaYvMDvmF/BMVD8BBGM\nwUTc45RkIt/pGRdU3Mhlo6HEqma3cDHpxLYC9hWpc8X2H1xzHI4KnoRTtI2SLx4E\nlynZckzI76QFUiU//f6km5LqLBKWfpnSaIzjoUmGRvLAFDC41ixog5eatMsmSvkE\neFnJ7cv3ObLEgV1Dcq7z+KM=\n-----END PRIVATE KEY-----\n",
      "client_email": "firebase-adminsdk-fbsvc@ferreteria-unic-delivery.iam.gserviceaccount.com",
      "client_id": "117511321344221989615",
      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      "token_uri": "https://oauth2.googleapis.com/token",
      "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
      "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40ferreteria-unic-delivery.iam.gserviceaccount.com",
      "universe_domain": "googleapis.com"
    }

    
    if not firebase_admin._apps:
        try:
            cred = credentials.Certificate(firebase_creds_json)
            firebase_admin.initialize_app(cred)
            print(">>> Firebase inicializado correctamente")
        except Exception as e:
            print(f">>> Error al inicializar Firebase: {e}")
    else:
        print(">>> Firebase ya estaba inicializado")
