from datetime import date
from .query_executor_service import QueryExecutorService
from ..exceptions.custom_exceptions import UserNotFoundException, IncorrectPasswordException
from .password_checker_service import PasswordCheckerService
from .jwt_signer_service import JwtSignerService





# TODO: refactor class to seperate concerns more

'''
This class is responsible for fetching a JWT given a username and password.
It checks the credentials against the DB and returns a JWT.
If the password is incorrect, or the user is not found, it may throw an exception.
'''

class JwtFetcherService:
    def __init__(self, username, password):
        self.query = '''
            SELECT password, user_id, username, email, join_date, post_count
            FROM users
            WHERE username = '{username}';
        '''.format(username = username)
        self.password = password
        self.username = username
        self.connection = QueryExecutorService()

    def get(self):
        return self.__gen_jwt( self.__gen_payload( self.__check_pw( self.__attempt_fetch() ) ) )

    def __attempt_fetch(self):
        res = self.connection.execute(self.query)
        if len(res) == 0:
            raise UserNotFoundException()
        else:
            return res

    def __check_pw(self, res):
        flag = PasswordCheckerService.check(self.password, res[0][0])
        if flag == False:
            raise IncorrectPasswordException()
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
        return JwtSignerService(payload).get()
#