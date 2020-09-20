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

class UserAlreadyExistsException(Exception):
    def __init__(self):
        super().__init__("User already exists")

class IncorrectPasswordException(Exception):
    def __init__(self):
        super().__init__("Password is incorrect")

class InvalidSearchException(Exception):
    def __init__(self):
        super().__init__("Invalid search terms")

class InvalidSessionException(Exception):
    def __init__(self):
        super().__init__("Invalid session")

