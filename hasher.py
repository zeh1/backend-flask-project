import bcrypt





# This class is responsible for 

class PasswordHasherService:
    def __init__(self, raw_password = "empty"):
        self.encoded_password = raw_password.encode('utf-8')
        self.generated_salt = bcrypt.gensalt()

    def get_hash(self):
        return bcrypt.hashpw(self.encoded_password, self.generated_salt)

    def check_pw(self, other_raw_password, string_hash):
        return bcrypt.checkpw(other_raw_password.encode('utf-8'), string_hash.encode('utf-8'))

    def hash_to_string(self, byte_hash):
        return byte_hash.decode('utf-8')
#





# This class is responsible for 

class PasswordCheckerService:
    def