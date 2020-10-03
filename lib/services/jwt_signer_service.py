import hmac, json, base64
from .encode_decode_service import EncodeDecodeService
from ..config.secrets import SECRET





HEADER = {"alg": "hs256", "typ": "jwt"}

TEST_PAYLOAD = {"payload": 0}


'''
This class is responsible for returning a jwt, given a payload.
The jwt returned is a string.
'''

class JwtSignerService:
    # input: payload is a dict
    def __init__(self, payload = TEST_PAYLOAD, header = HEADER, secret = SECRET):
        self.secret = secret
        self.b64_encoded_payload_as_string = EncodeDecodeService.to_b64_string( json.dumps(payload) )
        self.b64_encoded_header_as_string = EncodeDecodeService.to_b64_string( json.dumps(header) )
        self.hmac_msg = EncodeDecodeService.encode( self.b64_encoded_header_as_string + '.' + self.b64_encoded_payload_as_string )

    def __signature(self):        
        sig = hmac.new(self.secret, self.hmac_msg).hexdigest()
        sig = EncodeDecodeService.to_b64_string( sig )
        return sig

    def get(self):
        return self.b64_encoded_header_as_string + '.' + self.b64_encoded_payload_as_string + '.' + self.__signature()
#