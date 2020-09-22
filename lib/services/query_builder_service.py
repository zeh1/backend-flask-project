import uuid
from .password_hasher_service import PasswordHasherService

# TODO: write unit tests, and documentation

class QueryBuilderService:



    @staticmethod
    def get_posts(offset = 0):
        query = '''
            select distinct
            posts.post_id, posts.post_title, posts.post_body, posts.post_date,
            posts.upvote_count, posts.downvote_count, users.user_id, users.username
            from users
            inner join posts on posts.user_id = users.user_id
            order by posts.post_date asc
            limit 15
            offset {offset}
        '''.format(offset = offset)
        return [query]



    @staticmethod
    def insert_post(user_id, title, body):
        insert_post_query = '''
            insert into posts(post_title, post_body, user_id)
            values('{post_title}', '{post_body}', {user_id});
        '''.format(post_title = title, post_body = body, user_id = user_id)
        
        update_post_count_query = '''
            update users set post_count = post_count + 1
            where user_id = {user_id};
        '''.format(user_id = user_id)

        return [insert_post_query, update_post_count_query]
        # need to handle exceptions: no jwt (None), invalid jwt



    @staticmethod
    def get_replies(post_id):
        query = '''
            select replies.reply_body, users.username, replies.reply_date, replies.upvote_count, replies.downvote_count
            from replies
            inner join users
            on (replies.user_id = users.user_id) and (replies.post_id = {post_id})
            order by replies.reply_date asc;
        '''.format(post_id = post_id)
        return [query]



    @staticmethod
    def insert_reply(post_id, reply_body, user_id):
        query = '''
            insert into replies(reply_body, post_id, user_id)
            values('{reply_body}', '{post_id}', {user_id});
        '''.format(reply_body = reply_body, post_id = post_id, user_id = user_id)
        return [query]
        # need to handle exceptions: no jwt, invalid jwt



    # requires a processed (hashed) password
    @staticmethod
    def login_attempt(username):

        try_to_retrieve_user_info = '''
            select
            password, user_id, username, email, join_date, post_count, is_verified
            from users where username = '{username}';
        '''.format(username = username)

        return [try_to_retrieve_user_info]
        # need to handle exceptions:
        # UserNotFoundException
        # IncorrectCredentialsException
        # UserNotVerifiedException



    # takes in a raw (unhashed) password
    @staticmethod
    def signup_attempt(email, username, password):
        try_to_insert_user = '''
            insert into users(username, email, password)
            values('{username}', '{email}', '{password}');
        '''.format(username = username, email = email, password = PasswordHasherService(password).get())
        # need to handle exception: UserAlreadyExistsException

        session_id = uuid.uuid4().hex
        create_verification_session = '''
            insert into verifications(session_id, user_id)
            values('{session_id}', (select user_id from users where username = '{username}'));
        '''.format(session_id = session_id, username = username)

        # retrieve session id in order to send email verification
        retrieve_session_id = '''
            select session_id from verifications
            where user_id = (select user_id from users where username = '{username}');
        '''.format(username = username)

        return [try_to_insert_user, create_verification_session, retrieve_session_id]



    @staticmethod
    def password_reset_attempt(email):
        check_if_user_exists = '''
            select email from users where email = '{email}';
        '''.format(email = email)
        # need to handle exception: user not found

        session_id = uuid.uuid4().hex
        create_reset_session = '''
            insert into resets(session_id, user_id)
            values('{session_id}', (select user_id from users where email = '{email}'));
        '''.format(session_id = session_id, email = email)

        retrieve_session_id = '''
            select session_id from resets
            where user_id = (select user_id from users where email = '{email}');
        '''.format(email = email)

        return [check_if_user_exists, create_reset_session, retrieve_session_id]



    @staticmethod
    def password_change_attempt_part_1(user_id):
        # need to handle exceptions: no jwt, invalid jwt

        retrieve_password = '''
            select password from users where user_id = {user_id};
        '''.format(user_id = user_id)

        return [retrieve_password]



    # check for old_password match outside this class
    # if match then call part 2 to update db with new pass
    # need to handle: IncorrectPasswordException
    # new_password is not yet hashed for input
    @staticmethod
    def password_change_attempt_part_2(user_id, new_password):

        update_password = '''
            update users set password = '{new_password}'
            where user_id = {user_id};
        '''.format(new_password = PasswordHasherService(new_password).get(), user_id = user_id)

        return [update_password]
        


    @staticmethod
    def simple_search(search):
        # need to check for empty/invalid search

        query = '''
            select post_id, post_title, post_body from posts
            where post_title like '%{search}%'
            or post_body like '%{search}%';
        '''.format(search = search)

        return [query]



    # new password is not hashed yet
    @staticmethod
    def consume_password_reset_attempt(_uuid, new_password):
        check_if_session_exists = '''
            select * from resets where session_id = '{session_id}';
        '''.format(session_id = _uuid)
        # need to handle exception: session does not exist

        update_password = '''
            update users set password = '{password}'
            where user_id = (select user_id from resets where session_id = '{session_id}');
        '''.format(password = PasswordHasherService(new_password).get(), session_id = _uuid)

        consume_session = '''
            delete from resets where session_id = '{session_id}';
        '''.format(session_id = _uuid)

        return [check_if_session_exists, update_password, consume_session]



    @staticmethod
    def consume_verify_email_attempt(_uuid):
        update_verification_status = '''
            update users set is_verified = 1
            where user_id = 
            (select user_id from verifications where session_id = '{session_id}');
        '''.format(session_id = _uuid)
        consume_session = '''
            delete from verifications where session_id = '{session_id}';
        '''.format(session_id = _uuid)

        return [update_verification_status, consume_session]