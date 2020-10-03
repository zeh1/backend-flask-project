import lib.services.jwt_deconstructor_service as j

TEST_JWT = 'eyJhbGciOiAiaHMyNTYiLCAidHlwIjogImp3dCJ9.eyJwYXlsb2FkIjogMH0=.NjQ3YjAwZTBhNDU3NDM3NGU4NTUxNjYyMTk4ZjEwMjA='
TEST_PAYLOAD = {'payload': 0}

def test_jwt_is_correct():
    assert TEST_JWT == 'eyJhbGciOiAiaHMyNTYiLCAidHlwIjogImp3dCJ9.eyJwYXlsb2FkIjogMH0=.NjQ3YjAwZTBhNDU3NDM3NGU4NTUxNjYyMTk4ZjEwMjA='

def test_payload_is_correct():
    assert TEST_PAYLOAD == {'payload': 0}

def test_jwt_deconstructor_service_works():
    res1 = j.JwtDeconstructorService(TEST_JWT).get()
    res2 = TEST_PAYLOAD
    assert res1 == res2

