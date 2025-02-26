from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from datetime import datetime


class Mailing:

    def __init__(self):
        self.sender = settings.EMAIL_HOST_USER

    def emailResetPassword(self, recipient, name, password):
        html = render_to_string(
            template_name="reset_password.html",
            context={
                "name": name,
                "password": password,
                "now": datetime.now(),
            },
        )
        return self.__sendEmail(
            f"Reseteo de contrasena - {name}",
            [recipient],
            html,
        )

    def __sendEmail(self, subject, recipients, body):
        return send_mail(
            message=None,
            subject=subject,
            recipient_list=recipients,
            html_message=body,
            from_email=self.sender,
        )
