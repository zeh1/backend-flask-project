import bcrypt
from .encode_decode_service import EncodeDecodeService


'''
This class is responsible for checking if two passwords match.
The first password is a raw string password and the other is fetched from the DB
'''

class PasswordCheckerService:
    @staticmethod
    def check(password, stored_password):
        password = EncodeDecodeService.encode(password)
        stored_password = EncodeDecodeService.encode(stored_password)
        return bcrypt.checkpw(password, stored_password)
#