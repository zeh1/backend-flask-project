import bcrypt
from encode_decode_service import EncodeDecodeService





# This class is responsible for generating a hash, given a password

class PasswordHasherService:
    # accepts a string
    def __init__(self, password = "TEST PASSWORD"):
        self.encoded_password = EncodeDecodeService.encode(password)
        self.generated_salt = bcrypt.gensalt()

    def get(self):
        h = bcrypt.hashpw(self.encoded_password, self.generated_salt)
        h = EncodeDecodeService.decode(h)
        return h
        # returns a string
#