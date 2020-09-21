



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
        # need to handle exceptions: no jwt, invalid jwt



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
        