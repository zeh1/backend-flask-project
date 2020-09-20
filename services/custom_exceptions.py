class UserNotFoundException(Exception):
    def __init__(self):
        super().__init__("User not found")

class PasswordIncorrectException(Exception):
    def __init__(self):
        super().__init__("Wrong password")

class UserNotAuthorizedException(Exception):
    def __init__(self):
        super().__init__("Not authorized")

class NoJwtSuppliedException(Exception):
    def __init__(self):
        super().__init__("No jwt supplied")

