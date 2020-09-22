from .encode_decode_service import EncodeDecodeService
import json

# TODO: write documentation

class JwtDeconstructorService:

    def __init__(self, jwt):
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