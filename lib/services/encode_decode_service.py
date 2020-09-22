import base64

# TODO: write unit tests, and documentation

class EncodeDecodeService:
    
    @staticmethod
    def to_b64(_string):
        return base64.urlsafe_b64encode(_string.encode('utf-8'))
        # returns a byte array

    @staticmethod
    def to_b64_string(_string):
        return base64.urlsafe_b64encode(_string.encode('utf-8')).decode('utf-8')
        # returns a string

    @staticmethod
    def b64_to_string(_bytes):
        return base64.urlsafe_b64decode(_bytes).decode('utf-8')
        # returns a string

    @staticmethod
    def encode(_string):
        return _string.encode('utf-8')
        # returns a byte array

    @staticmethod
    def decode(_bytes):
        return _bytes.decode('utf-8')
        # returns a string
#