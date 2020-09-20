



class Authorizer:
    def __init__(self):
        pass

    def get_jwt(self, username, raw_password):
        payload = {
            "user_id": res[0][0],
            "username": res[0][1],
            "email": res[0][2],
            "join_date": res[0][3],
            "post_count": res[0][4],
            "iat": date.today().strftime("%d/%m/%Y"),
            "expires_on": "TODO"
        }
        signer = Signer(payload)
        sig = signer.get_signature()

    def authorize_jwt(self, jwt):
        pass
#