from lib.services.query_executor_service import QueryExecutorService
import sqlite3

create_users_table = '''
create table users (
    user_id integer primary key autoincrement,
    username varchar(16) not null unique,
    email varchar(320) not null unique,
    password varchar(16) not null,
    join_date date default current_date,
    post_count integer default 0
);
'''

create_posts_table = '''
create table posts (
    post_id integer primary key autoincrement,
    post_title text not null,
    post_body text not null,
    post_date date default current_date,
    user_id integer,
    upvote_count integer default 0,
    downvote_count integer default 0,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);
'''

create_replies_table = '''
create table replies (
    reply_id integer primary key autoincrement,
    reply_body text not null,
    user_id integer,
    post_id integer,
    reply_date date default current_date,
    upvote_count integer default 0,
    downvote_count integer default 0,
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(post_id) REFERENCES posts(post_id)
);
'''

queries = [
    create_users_table, 
    create_posts_table,
    create_replies_table
]

for query in queries:
    try:
        i = QueryExecutorService()
        res = i.execute(query)
    except sqlite3.OperationalError as e:
        print(f'ERROR: {e}')
#