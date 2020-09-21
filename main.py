from flask import Flask
from flask import request

from services.query_builder_service import QueryBuilderService
from services.query_executor_service import QueryExecutorService

app = Flask(__name__)

# intercept jwt, request body json, url params
# perform jwt checking here

@app.route('/api/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'GET':
        offset = request.args.get('offset')
        if offset == None:
            
        else:
            return offset
#



@app.route('/')
def test():
    return "test"