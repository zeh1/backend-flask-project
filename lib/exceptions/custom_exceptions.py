class UserNotFoundException(Exception):
    def __init__(self):
        super().__init__("User not found")
#

class UserNotAuthorizedException(Exception):
    def __init__(self):
        super().__init__("Not authorized")
#

class UserAlreadyExistsException(Exception):
    def __init__(self):
        super().__init__("User already exists")
#





class IncorrectPasswordException(Exception):
    def __init__(self):
        super().__init__("Password is incorrect")
#






class NoJwtSuppliedException(Exception):
    def __init__(self):
        super().__init__("No jwt supplied")
#

class InvalidJwtException(Exception):
    def __init__(self):
        super().__init__("Invalid jwt")
#





class InvalidSearchException(Exception):
    def __init__(self):
        super().__init__("Invalid search terms")
#