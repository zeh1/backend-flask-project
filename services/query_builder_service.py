from signature_checker_service import SignatureCheckerService
import __custom_exceptions
from jwt_deconstructor_service import JwtDeconstructorService
from password_hasher_service import PasswordHasherService
import uuid





class QueryBuilderService:



    def __init__(self, jwt = None):
        self.jwt = jwt
        


    def get_posts(self, offset = None):
        query = None
        if offset != None:
            query = '''
                select * from posts
                order by post_date asc
                limit 15
                offset {offset}
            '''.format(offset = offset)
        else:
            query = '''
                select * from posts
                order by post_date asc
                limit 15
            '''
        return [query]



    def insert_post(self, title, body):

        queries = None

        if self.jwt == None or not SignatureCheckerService.check(self.jwt):
            raise __custom_exceptions.UserNotAuthorizedException()
        else:
            user_id = JwtDeconstructorService(self.jwt)['user_id']
            
            query1 = '''
                insert into posts(post_title, post_body, user_id)
                values({post_title}, {post_body}, {user_id});
            '''.format(post_title = title, post_body = body, user_id = user_id)
            
            query2 = '''
                update users set post_count = post_count + 1
                where user_id = {user_id};
            '''.format(user_id = user_id)

        queries = [query1, query2]

        return queries



    def get_replies(self):
        return ['''
            select * from replies
            order by reply_date asc
            limit 15;
        ''']



    def insert_reply(self, post_id, reply_body):
        query = None

        if self.jwt == None or not SignatureCheckerService.check(self.jwt):
            raise __custom_exceptions.UserNotAuthorizedException()
        else:
            user_id = JwtDeconstructorService(self.jwt)['user_id']
            
            query = '''
                insert into replies(reply_body, post_id, user_id)
                values({reply_body}, {post_id}, {user_id});
            '''.format(reply_body = reply_body, post_id = post_id, user_id = user_id)

        return [query]



    def signin_attempt(self, username, password):
        query = '''
            select user_id, username, email, join_date, post_count from users
            where username = {username} and email = {email};
        '''.format(username = username, email = email)
        # leads to: UserNotFoundException and IncorrectCredentialsException
        return [query]



    def signup_attempt(self, email, username, password):
        queries = None

        hashed_pw = PasswordHasherService(password).get()
        query1 = '''
            insert into users(username, email, password)
            values({username}, {email}, {password});
        '''.format(username = username, email = email, password = hashed_pw)
        # leads to: UserAlreadyExistsException

        session_id = uuid.uuid4().hex
        query2 = '''
            insert into verifications(session_id, email)
            values({session_id}, {email});
        '''.format(session_id = session_id, email = email)
        # create verification session

        query3 = '''
            select session_id from verifications
            where email = {email};
        '''.format(email = email)
        # get session id from here, in order to send email

        # originally i wanted this class to just return a single query
        # for each request but it turned into spaghetti code when
        # it turned out to be more complicated because of sql
        # using multiple queries, and needing to pass data in between queries
        # also there were inefficiencies in the sql data model
        # for the future: prefer natural primary keys over generated ones
        
        # learning points:
        # do not try to implement a query builder, think of another way
        # prefer natural keys
        # try using table joins?
        # understand python upper directory imports...
        # use 3rd party sql libs
        # consider document db for easier implementation

        queries = [query1, query2, query3]

        return queries



    def start_password_reset(self, email):
        queries = None
        
        query1 = '''
            select email from users
            where email = {email};
        '''.format(email = email)
        # check if user exists
        # may return UserNotFoundException

        session_id = uuid.uuid4().hex
        query2 = '''
            insert into resets(session_id, email)
            values({session_id}, {email});
        '''.format(session_id = session_id, email = email)
        # create reset session

        query3 = '''
            select session_id from resets
            where email = {email};
        '''.format(email = email)
        # retrieve session id in order to send email

        queries = [query1, query2, query3]

        return queries



    def password_change_attempt(self, password, new_pass):
        
        queries = None

        if self.jwt == None or not SignatureCheckerService.check(self.jwt):
            raise __custom_exceptions.UserNotAuthorizedException()
        else:
            username = JwtDeconstructorService(self.jwt)['username']

            query1 = '''
                select password from users
                where password = {password} and username = {username}
            '''.format(password = password, username = username)
            # may result in IncorrectPasswordException

            query2 = '''
                update users set password = {new_pass}
                where username = {username}
            '''.format(new_pass = new_pass, username = username)

            queries = [query1, query2]

        return queries



    def search(self, search):
        query = None
        if search == None or search == "":
            raise __custom_exceptions.InvalidSearchException()
        query = '''
            select post_id, post_title, post_body from posts
            where post_title like '%{search}%'
            or post_body like '%{search}%';
        '''.format(search = search)
        return [query]



    def consume_reset_password_attempt(self, uuid, new_pass):
        # check if session exists, retrieve email from sessions db
        # proceed to change pw

        '''
        query1 = '''
            select email from resets
            where session_id = {uuid};
        '''.format(uuid = uuid)
        # may throw invalid session exception
        # get email

        # case/if, subqueries/results, joins
        query2 = '''
            update users set password = {password}
            where email = {email};
        '''.format(password = password, email = email)
        '''



    def consume_verify_email_attempt(self, uuid):
        pass
#