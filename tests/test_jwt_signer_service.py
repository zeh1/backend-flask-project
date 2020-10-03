import lib.services.jwt_signer_service as j

HEADER = {"alg": "hs256", "typ": "jwt"}

TEST_PAYLOAD = {"payload": 0}

RESULT = 'eyJhbGciOiAiaHMyNTYiLCAidHlwIjogImp3dCJ9.eyJwYXlsb2FkIjogMH0=.NjQ3YjAwZTBhNDU3NDM3NGU4NTUxNjYyMTk4ZjEwMjA='


def test_header_is_correct():
    assert HEADER == {"alg": "hs256", "typ": "jwt"}

def test_payload_is_correct():
    assert TEST_PAYLOAD == {"payload": 0}

def test_jwt_signer_service_works():
    res = j.JwtSignerService(TEST_PAYLOAD, HEADER).get()
    print(res)
    assert res == RESULT

