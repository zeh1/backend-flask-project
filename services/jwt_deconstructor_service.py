from .encode_decode_service import EncodeDecodeService
import json





TEST_JWT = 'eyJhbGciOiAiaHMyNTYiLCAidHlwIjogImp3dCJ9.eyJwYXlsb2FkIjogMH0=.NjQ3YjAwZTBhNDU3NDM3NGU4NTUxNjYyMTk4ZjEwMjA='





class JwtDeconstructorService:


    def __init__(self, jwt = TEST_JWT):
        self.jwt = jwt



    def get(self):
        return json.loads( self.__parse() )



    def __parse(self):
        array = self.jwt.split('.')
        
        def transform(jwt_section):
            d = EncodeDecodeService.encode(jwt_section)
            d = EncodeDecodeService.b64_to_string(d)
            return d
        
        res = map(transform, array)

        return list(res)[1]
#