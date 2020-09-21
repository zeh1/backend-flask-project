import uuid





class QueryBuilderService:



    def get_posts(offset = None):
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



    def insert_post(user_id, title, body):
        insert_post_query = '''
            insert into posts(post_title, post_body, user_id)
            values({post_title}, {post_body}, {user_id});
        '''.format(post_title = title, post_body = body, user_id = user_id)
        
        update_post_count_query = '''
            update users set post_count = post_count + 1
            where user_id = {user_id};
        '''.format(user_id = user_id)

        return [insert_post_query, update_post_count_query]
        # need to handle exceptions: no jwt (None), invalid jwt



    def get_replies(post_id):
        query = '''
            select replies.reply_body, users.username, replies.reply_date, replies.upvote_count, replies.downvote_count
            from replies
            inner join users
            on (replies.user_id = users.user_id) and (replies.post_id = {post_id})
            order by replies.reply_date asc;
        '''.format(post_id = post_id)
        return [query]



    def insert_reply(post_id, reply_body, user_id):
        query = '''
            insert into replies(reply_body, post_id, user_id)
            values({reply_body}, {post_id}, {user_id});
        '''.format(reply_body = reply_body, post_id = post_id, user_id = user_id)
        return [query]
        # need to handle exceptions: no jwt, invalid jwt



    # requires a processed (hashed) password
    def login_attempt(username, password):
        query = '''
            select user_id, username, email, join_date, post_count from users
            where username = {username} and email = {email};
        '''.format(username = username, email = email)

        return [query]
        # need to handle exceptions: UserNotFoundException, IncorrectCredentialsException



    # requires a processed (hashed) password
    def signup_attempt(email, username, password):
        try_to_insert_user = '''
            insert into users(username, email, password)
            values({username}, {email}, {password});
        '''.format(username = username, email = email, password = password)
        # need to handle exception: UserAlreadyExistsException

        session_id = uuid.uuid4().hex
        create_verification_session = '''
            insert into verifications(session_id, user_id)
            values({session_id}, (select user_id from users where username = {username}));
        '''.format(session_id = session_id, username = username)

        # retrieve session id in order to send email verification
        retrieve_session_id = '''
            select session_id from verifications
            where user_id = (select user_id from users where username = {username});
        '''.format(username = username)

        return [try_to_insert_user, create_verification_session, retrieve_session_id]



    def password_reset_attempt(email):
        check_if_user_exists = '''
            select email from users where email = {email};
        '''.format(email = email)
        # need to handle exception: user not found

        session_id = uuid.uuid4().hex
        create_reset_session = '''
            insert into resets(session_id, user_id)
            values({session_id}, (select user_id from users where email = {email}));
        '''.format(session_id = session_id, email = email)

        retrieve_session_id = '''
            select session_id from resets
            where user_id = (select user_id from users where email = {email});
        '''.format(email = email)

        return [check_if_user_exists, create_reset_session, retrieve_session_id]



    def password_change_attempt(password, new_password):
        