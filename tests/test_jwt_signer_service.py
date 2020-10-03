import lib.services.jwt_signer_service as j

HEADER = {"alg": "hs256", "typ": "jwt"}

TEST_PAYLOAD = {"payload": 0}



def test_header_is_correct():
    assert HEADER == {"alg": "hs256", "typ": "jwt"}

def test_payload_is_correct():
    assert TEST_PAYLOAD == {"payload": 0}

def test_jwt_signer_service_works():
    
    assert 