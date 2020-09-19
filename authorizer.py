from connection import Connection
from signer import Signer
from hasher import Hasher
from datetime import date

class Authorizer:
    def __init__(self):
        pass

    def get_jwt(self, username, raw_password):
        conn = Connection()
        hasher = Hasher(raw_password)

        query = '''
            select password from users where username = {username};
        '''.format(username = username)
        res = Connection().execute(query)
        if len(res) == 0:
            raise "none found"
        else:
            res = res[0][0]
        if !(hasher.check_pw(raw_password, res)):
            raise "wrong pass"

        query = '''
            select user_id, username, email, join_date, post_count from users
            where username = {username};
        '''.format(username = username)
        res = Connection().execute(query)
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