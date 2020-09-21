import bcrypt
from .encode_decode_service import EncodeDecodeService





# This class is responsible for checking if passwords match

class PasswordCheckerService:
    def check(password, stored_password):
        password = EncodeDecodeService.encode(password)
        stored_password = EncodeDecodeService.encode(stored_password)
        return bcrypt.checkpw(password, stored_password)
#