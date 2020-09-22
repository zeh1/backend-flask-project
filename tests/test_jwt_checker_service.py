import lib.services.jwt_checker_service as j

VALID_JWT = 'eyJhbGciOiAiaHMyNTYiLCAidHlwIjogImp3dCJ9.eyJwYXlsb2FkIjogMH0=.NjQ3YjAwZTBhNDU3NDM3NGU4NTUxNjYyMTk4ZjEwMjA='
INVALID_JWT = 'a.b.c'

def test_valid_jwt_is_correct():
    assert VALID_JWT == 'eyJhbGciOiAiaHMyNTYiLCAidHlwIjogImp3dCJ9.eyJwYXlsb2FkIjogMH0=.NjQ3YjAwZTBhNDU3NDM3NGU4NTUxNjYyMTk4ZjEwMjA='

def test_invalid_jwt_is_correct():
    assert INVALID_JWT == 'a.b.c'

def test_valid_jwt_should_return_true():
    assert j.JwtCheckerService().check(VALID_JWT) == True

def test_invalid_jwt_should_return_false():
    assert j.JwtCheckerService().check(INVALID_JWT) == False
#