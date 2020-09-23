from flask import Flask
from flask import request
from flask import make_response

from lib.services.query_builder_service import QueryBuilderService
from lib.services.query_executor_service import QueryExecutorService
from lib.services.jwt_checker_service import JwtCheckerService
from lib.services.jwt_deconstructor_service import JwtDeconstructorService
from lib.services.jwt_fetcher_service import JwtFetcherService
from lib.exceptions.custom_exceptions import UserNotFoundException, IncorrectPasswordException

app = Flask(__name__)

'''
SAMPLE VALID TOKEN:
eyJhbGciOiAiaHMyNTYiLCAidHlwIjogImp3dCJ9.eyJwYXlsb2FkIjogMH0=.NjQ3YjAwZTBhNDU3NDM3NGU4NTUxNjYyMTk4ZjEwMjA=

no jwt, invalid jwt, user not found, incorrect password/username, user already exists

url params: request.args.get('key')
token = request.headers.get('Authorization').split(' ')[1]
request.get_json()["user_id"]
if request.method == 'GET'

400 bad request due to invalid syntax
401 unauthorized
403 forbidden
404 not found
'''

@app.route('/api/posts', methods=['GET', 'POST'])
def posts():

    if request.method == 'GET':

        offset = request.args.get('offset')
        queries = QueryBuilderService().get_posts(offset) if offset else QueryBuilderService().get_posts()
        
        query_result = None
        for query in queries:
            query_result = QueryExecutorService().execute(query)
        # res is a list of tuples (database rows)
        
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
        
        # map each tuple to a dict
        dictionaries = map(transform, query_result)
        
        list_of_dicts = list(dictionaries)
        
        # make json response
        return {
            "posts": list_of_dicts
        }

    elif request.method == 'POST':

        if request.headers.get('Authorization') == None:
            return "No JWT supplied", 401
        #

        token = request.headers.get('Authorization').split(' ')[1]
        jwt_is_valid = True if JwtCheckerService().check(token) else False
        if jwt_is_valid == False:
            return "Invalid JWT", 401
        #

        try:
            req_body = request.get_json()
            user_id = JwtDeconstructorService(token).get()["user_id"]
            post_title = req_body["post_title"]
            post_body = req_body["post_body"]

            if not isinstance(user_id, int) or not isinstance(post_title, str) or not isinstance(post_body, str):
                return 'Invalid key values', 400

            queries = QueryBuilderService().insert_post(user_id, post_title, post_body)
            for query in queries:
                QueryExecutorService().execute(query)
            return 'Success', 200

        except KeyError:
            return 'Insufficient keys provided', 400

        # maybe wrap whole request in this exception?
        except Exception:
            return 'Unknown error, maybe check http request formatting', 400
#





@app.route('/api/replies', methods=['GET', 'POST'])
def replies():

    if request.method == 'GET':

        post_id = request.args.get('post_id')
        has_post_id = True if post_id else False

        if not has_post_id:

            return 'No id supplied', 400

        else:

            queries = QueryBuilderService().get_replies(post_id)

            query_result = None
            for query in queries:
                query_result = QueryExecutorService().execute(query)

            def transform(row):
                return {
                    "reply_body": row[0],
                    "username": row[1],
                    "reply_date": row[2],
                    "upvote_count": row[3],
                    "downvote_count": row[4]
                }

            dictionaries = map(transform, query_result)
            list_of_dicts = list(dictionaries)
            return {
                "replies": list_of_dicts
            }

    elif request.method == 'POST':

        if request.headers.get('Authorization') == None:
            return "No JWT supplied", 401
        #

        token = request.headers.get('Authorization').split(' ')[1]
        jwt_is_valid = True if JwtCheckerService().check(token) else False
        if jwt_is_valid == False:
            return "Invalid JWT", 401
        #


        try:
            req_body = request.get_json()
            post_id = req_body["post_id"]
            reply_body = req_body["reply_body"]
            user_id = JwtDeconstructorService(token).get()["user_id"]

            if not isinstance(post_id, int) or not isinstance(reply_body, str) or not isinstance(user_id, int):
                return 'Invalid key values', 400
            #

            query = f"select post_id from posts where post_id = {post_id}"
            query_result = QueryExecutorService().execute(query)
            if len(query_result) == 0:
                return 'Invalid post id', 400
            #

            queries = QueryBuilderService().insert_reply(post_id, reply_body, user_id)
            for query in queries:
                QueryExecutorService().execute(query)
            #
            return 'Success', 200

        except KeyError:
            return 'Insufficient keys provided', 400

        # maybe wrap whole request in this exception?
        except Exception:
            return 'Unknown error, maybe check http request formatting', 400





@app.route('/auth/login', methods=['POST'])
def login():

    try:
        req_body = request.get_json()
        username = req_body["username"]
        supplied_password = req_body["password"]
        
        if not isinstance(username, str) or not isinstance(supplied_password, str):
            return 'Invalid key values', 400

        try:
            jwt = JwtFetcherService(username, supplied_password).get()
            header = 'Bearer ' + jwt
            resp = make_response()
            resp.headers['Authorization'] = header
            return resp

        except UserNotFoundException as e:
            return str(e), 404
        except IncorrectPasswordException as e:
            return str(e), 401

    except KeyError:
        return 'Insufficient keys provided', 400
    
    # maybe wrap whole request in this exception?
    except Exception:
        return 'Unknown error, maybe check http request formatting', 400
#





@app.route('/auth/signup', methods=['POST'])
def signup():
    username = request.get_json()["username"]
    email = request.get_json()["email"]
    password = request.get_json()["password"]

    queries = QueryBuilderService().signup_attempt(email, username, password)

    for query in queries:
        print(query)

    return "hi"
#