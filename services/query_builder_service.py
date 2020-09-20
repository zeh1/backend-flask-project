from signature_checker_service import SignatureCheckerService
import custom_exceptions
from jwt_deconstructor_service import JwtDeconstructorService





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
        return query



    def insert_post(self, title, body):

        query = None

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

        return query



    def fetch_get_request_to_replies(self):
        pass

    def fetch_post_request_to_replies(self, post_id, reply_body):
        pass

    def fetch_signin_attempt(self, password):
        pass

    def fetch_signup_attempt(self, email, username, password):
        pass

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