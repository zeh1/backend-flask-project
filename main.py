from flask import Flask
from flask import request
from encode_decode import EncodeDecodeService
# from query_builder import QueryBuilder

app = Flask(__name__)

@app.route('/api/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'GET':
        pass
    else:
        pass
#

@app.route('/')
def test():
    data = EncodeDecodeService.to_b64_string('asd').encode('utf-8')
    res = EncodeDecodeService.b64_to_string(data)
    return res