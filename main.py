from flask import Flask
from flask import request

from services.query_builder_service import QueryBuilderService as q
from services.query_executor_service import QueryExecutorService as e
from services.signature_checker_service import SignatureCheckerService as s
from services.jwt_deconstructor_service import JwtDeconstructorService as j
from services.password_checker_service import PasswordCheckerService as c
from services.jwt_fetcher_service import JwtFetcherService as f

# from services.__custom_exceptions import UserNotFoundException, PasswordIncorrectException

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

        if request.headers.get('Authorization') == None:
            return "no jwt supplied"

        token = request.headers.get('Authorization').split(' ')[1]
        flag = True if s.check(token) else False
        if flag == False:
            return "invalid jwt"

        d = request.get_json()
        queries = q.insert_post(d["user_id"], d["post_title"], d["post_body"])
        for query in queries:
            e().execute(query)

        return 'success'
#

'''
eyJhbGciOiAiaHMyNTYiLCAidHlwIjogImp3dCJ9.eyJwYXlsb2FkIjogMH0=.NjQ3YjAwZTBhNDU3NDM3NGU4NTUxNjYyMTk4ZjEwMjA=
'''





@app.route('/api/replies', methods=['GET', 'POST'])
def replies():



    if request.method == 'GET':
        post_id = request.args.get('post_id')
        flag = True if post_id else False

        if flag:
            queries = q.get_replies(post_id)
            res = None
            for query in queries:
                res = e().execute(query)

            def transform(row):
                return {
                    "reply_body": row[0],
                    "username": row[1],
                    "reply_date": row[2],
                    "upvote_count": row[3],
                    "downvote_count": row[4]
                }

            res = map(transform, res)
            res = list(res)
            res = {
                "replies": res
            }
            return res

        else:
            return 'no id supplied'



    elif request.method == 'POST':

        if request.headers.get('Authorization') == None:
            return "no jwt supplied"

        token = request.headers.get('Authorization').split(' ')[1]
        flag = True if s.check(token) else False
        if flag == False:
            return "invalid jwt"

        # user_id = j(token).get()["user_id"]
        user_id = request.get_json()["user_id"]

        d = request.get_json()
        queries = q.insert_post(d["post_id"], d["reply_body"], d["user_id"])
        for query in queries:
            # e().execute(query)
            print(query)

        return 'success'





@app.route('/auth/login', methods=['POST'])
def login():
    username = request.get_json()["username"]
    supplied_password = request.get_json()["password"]

    try:
        return f(username, supplied_password).get()
    except Exception as e:
        return str(e)
#





@app.route('/auth/signup', methods=['POST'])
def signup():
    username = request.get_json()["username"]
    email = request.get_json()["email"]
    password = request.get_json()["password"]

    queries = q.signup_attempt(email, username, password)

    for query in queries:
        print(query)

    return "hi"
# TODO: refactor, and add error handling





@app.route('/auth/reset_pw', methods=['POST'])
def reset():
    email = request.get_json()["email"]
    queries = q.password_reset_attempt(email)
    for query in queries:
        print(query)
    
    return "hi"
#





@app.route('/auth/change_pw', methods=['POST'])
def change():
    pass