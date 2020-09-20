from datetime import date
from query_executor_service import QueryExecutorService
import custom_exceptions
from password_checker_service import PasswordCheckerService
from signer_service import SignerService





class JwtFetcherService:
    def __init__(self, username, password):
        self.query = '''
            SELECT password, user_id, username, email, join_date, post_count
            FROM users
            WHERE username = {username};
        '''.format(username = username)
        self.password = password
        self.username = username
        self.connection = QueryExecutorService()

    def get(self):
        return self.__gen_jwt( self.__gen_payload( self.__check_pw( self.__attempt_fetch() ) ) )

    def __attempt_fetch(self):
        res = self.connection.execute(self.query)
        if len(res) == 0:
            raise custom_exceptions.UserNotFoundException()
        else:
            return res

    def __check_pw(self, res):
        flag = PasswordCheckerService.check(self.password, res[0][0])
        if flag == false:
            raise custom_exceptions.PasswordIncorrectException()
        else:
            return res

    def __gen_payload(self, res):
        payload = {
            "user_id": res[0][1],
            "username": res[0][2],
            "email": res[0][3],
            "join_date": res[0][4],
            "post_count": res[0][5],
            "iat": date.today().strftime("%d/%m/%Y"),
            "expires_on": "TODO"
        }
        return payload

    def __gen_jwt(self, payload):
        return SignerService(payload).get()
#