from signature_checker_service import SignatureCheckerService
import custom_exceptions
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
            raise custom_exceptions.UserNotAuthorizedException()
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
            raise custom_exceptions.UserNotAuthorizedException()
        else:
            user_id = JwtDeconstructorService(self.jwt)['user_id']
            
            query = '''
                insert into replies(reply_body, post_id, user_id)
                values({reply_body}, {post_id}, {user_id});
            '''.format(reply_body = reply_body, post_id = post_id, user_id = user_id)

        return [query]



    def signin(self, username, password):
        query = '''
            select user_id, username, email, join_date, post_count from users
            where username = {username} and email = {email};
        '''.format(username = username, email = email)
        # leads to: UserNotFoundException and IncorrectCredentialsException
        return [query]



    def signup(self, email, username, password):
        hashed_pw = PasswordHasherService(password).get()
        query1 = '''
            insert into users(username, email, password)
            values({username}, {email}, {password});
        '''.format(username = username, email = email, password = hashed_pw)
        # leads to: UserAlreadyExistsException

        query2 = '''
            select user_id from users where email = {email};
        '''.format(email = email)

        session_id = uuid.uuid4().hex
        query3 = '''
            insert into verifications(session_id, user_id)
            values({session_id}, {user_id});
        '''.format(session_id = session_id, user_id = user_id)



    def fetch_recover_attempt(self, email):
        pass

    def fetch_password_change_attempt(self, password):
        pass

    def fetch_search_query(self, search):
        pass

    def fetch_password_reset_attempt(self, uuid):
        pass

    def fetch_email_validate_attempt(self, uuid):
        pass
#