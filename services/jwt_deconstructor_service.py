


class JwtDeconstructorService:
    def __init__(self, jwt):
        self.jwt = jwt

    def get(self):
        pass

    def __parse(self):
        array = self.jwt.split('.')
        def 
#



class SignatureCheckerService:
    def check(jwt = TEST_JWT, secret = SECRET):
        array = jwt.split('.')
        hmac_msg = EncodeDecodeService.encode( array[0] + '.' + array[1] )
        supplied_sig = array[2]
        proper_sig = EncodeDecodeService.to_b64_string( hmac.new(secret, hmac_msg).hexdigest() )
        return supplied_sig == proper_sig
#