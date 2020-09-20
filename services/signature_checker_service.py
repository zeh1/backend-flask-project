import hmac
from encode_decode_service import EncodeDecodeService
from __secrets import SECRET





TEST_JWT = 'a.b.c'





# This class is responsible for validating a jwt, given a jwt

class SignatureCheckerService:
    def check(jwt = TEST_JWT, secret = SECRET):
        array = jwt.split('.')
        hmac_msg = EncodeDecodeService.encode( array[0] + '.' + array[1] )
        supplied_sig = array[2]
        proper_sig = EncodeDecodeService.to_b64_string( hmac.new(secret, hmac_msg).hexdigest() )
        return supplied_sig == proper_sig
#