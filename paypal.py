from requests import post


PAYPAL_CLIENT_ID = (
    "AVnMO0zI8b12L_9lD8DCVkTh1PzwFIuOt6u807f_jdzKNNeubJc7ys6o82a0aHYx1ILaaYCdrKXGGYAA"
)
PAYPAL_CLIENT_SECRET = (
    "EKNA3Vs3AnaTdvAiVFNGyrx1fQ2kSzQXekL5SY0cByWZfgExcTTMOmIIQuHtURswMuCOzcXkzJLg9HWi"
)


class Paypal:
    def __init__(self):
        self.client_id = PAYPAL_CLIENT_ID
        self.client_secret = PAYPAL_CLIENT_SECRET

    def authenticate(self):
        url = "https://api.sandbox.paypal.com"
        self.access_token = self.get_access_token()
