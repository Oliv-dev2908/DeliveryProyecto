from firebase_admin import messaging

class NotificationService:
    @staticmethod
    def send_push_notification(token: str, title: str, body: str, data: dict = None):
        """
        Envía una notificación a un dispositivo específico usando su token.
        """
        if not token:
            print("⚠️ No hay token registrado para este usuario.")
            return

        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            data=data or {}, 
            token=token,
        )

        try:
            response = messaging.send(message)
            print(f"✅ Notificación enviada: {response}")
        except Exception as e:
            print(f"❌ Error enviando push: {e}")