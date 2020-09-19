from flask import Flask
from flask import request
from query_builder import QueryBuilder

app = Flask(__name__)

@app.route('/api/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'GET':
        pass
    else:
        pass
#

