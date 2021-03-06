import hmac
from .encode_decode_service import EncodeDecodeService
from ..config.secrets import SECRET

'''
This class is responsible for checking if a JWT was tampered with
'''

class JwtCheckerService:
    @staticmethod
    def check(jwt, secret = SECRET):
        array = jwt.split('.')
        hmac_msg = EncodeDecodeService.encode( array[0] + '.' + array[1] )
        supplied_sig = array[2]
        proper_sig = EncodeDecodeService.to_b64_string( hmac.new(secret, hmac_msg).hexdigest() )
        return supplied_sig == proper_sig
#