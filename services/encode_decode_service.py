import base64

class EncodeDecodeService:
    def to_b64(_string):
        return base64.urlsafe_b64encode(_string.encode('utf-8'))
        # returns a byte array

    def to_b64_string(_string):
        return base64.urlsafe_b64encode(_string.encode('utf-8')).decode('utf-8')
        # returns a string

    def b64_to_string(_bytes):
        return base64.urlsafe_b64decode(_bytes).decode('utf-8')
        # returns a string

    def encode(_string):
        return _string.encode('utf-8')
        # returns a byte array

    def decode(_bytes):
        return _bytes.decode('utf-8')
        # returns a string
#