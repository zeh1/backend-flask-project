from flask import Flask
from flask import request

from services.query_builder_service import QueryBuilderService as q
from services.query_executor_service import QueryExecutorService as e

app = Flask(__name__)

# intercept jwt, request body json, url params
# perform jwt checking here

@app.route('/api/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'GET':
        offset = request.args.get('offset')
        queries = q.get_posts(offset) if offset else q.get_posts()
        
        res = None
        for query in queries:
            res = e().execute(query)
        # res is a list of tuples/rows
        
        def transform(row):
            return {
                "post_id": row[0],
                "post_title": row[1],
                "post_body": row[2],
                "post_date": row[3],
                "upvote_count": row[4],
                "downvote_count": row[5],
                "user_id": row[6],
                "username": row[7]
            }
        
        # map each tuple/row to a dict
        res = map(transform, res)
        
        # res is a list of dicts
        res = list(res)
        
        # res is now json
        res = {
            "posts": res
        }

        return res

    elif request.method == 'POST':
        pass
#



@app.route('/')
def test():
    return "test"