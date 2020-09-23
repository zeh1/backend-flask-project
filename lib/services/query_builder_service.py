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
            values('{reply_body}', {post_id}, {user_id});
        '''.format(reply_body = reply_body, post_id = post_id, user_id = user_id)
        return [query]



    @staticmethod
    def login_attempt(username):
        try_to_retrieve_user_info = '''
            select
            password, user_id, username, email, join_date, post_count
            from users where username = '{username}';
        '''.format(username = username)
        return [try_to_retrieve_user_info]



    # takes in a raw (unhashed) password
    @staticmethod
    def signup_attempt(email, username, password):
        try_to_insert_user = '''
            insert into users(username, email, password)
            values('{username}', '{email}', '{password}');
        '''.format(username = username, email = email, password = PasswordHasherService(password).get())
        return [try_to_insert_user]



    @staticmethod
    def simple_search(search):
        query = '''
            select post_id, post_title, post_body from posts
            where post_title like '%{search}%'
            or post_body like '%{search}%';
        '''.format(search = search)
        return [query]
#