from query_executor_service import QueryExecutorService
import sqlite3



passwords = [
    "pass1",
    "pass2",
    "pass3"
]

hashed_passwords = [
    "$2b$12$1pxAbfgWRMnmS7UqzTWbYOjJfcUOj7gpS82HKpGc2X70ZVskGIJt.",
    "$2b$12$wwqTtaFjBPZXaSOuH.ccA.i9eQ5STNPmjMPTZUfRVTDWOGxon7bPW",
    "$2b$12$Vr1Kca/SGH2XdZIrLWH18ez5/xj1M94GxPAkFaV9NLujUrFCfOQ/O"
]

usernames = [
    "user1",
    "user2",
    "user3"
]

emails = [
    "emailA@x.com",
    "emailB@x.com",
    "emailC@x.com"
]



populate_users = '''
insert into users(username, email, password, is_verified)
values
( "user1", "emailA@x.com", "$2b$12$1pxAbfgWRMnmS7UqzTWbYOjJfcUOj7gpS82HKpGc2X70ZVskGIJt.", 1 ),
( "user2", "emailB@x.com", "$2b$12$wwqTtaFjBPZXaSOuH.ccA.i9eQ5STNPmjMPTZUfRVTDWOGxon7bPW", 1 ),
( "user3", "emailC@x.com", "$2b$12$Vr1Kca/SGH2XdZIrLWH18ez5/xj1M94GxPAkFaV9NLujUrFCfOQ/O", 1 )
'''

populate_posts = '''
insert into posts(post_title, post_body, user_id)
values
("post title 1", "post body 1", 1),
("post title 2", "post body 2", 2),
("post title 3", "post body 3", 3)
'''

populate_replies = '''
insert into replies(reply_body, user_id, post_id)
values
("reply1", 1, 1),
("reply2", 1, 1),
("reply3", 2, 1)
'''

populate_resets = '''
insert into resets values
("e0a010d5aebd4441a520b35b08cb2c17", 1),
("2241af0947474b8aa062a24563542a46", 2),
("7e9365c6c9ce46f98e92441094362222", 3)
'''

populate_verifications = '''
insert into verifications values
("e0a010d5aebd4441a520b35b08cb2c17", 1),
("2241af0947474b8aa062a24563542a46", 2),
("7e9365c6c9ce46f98e92441094362222", 3)
'''



queries = [
    populate_users, populate_posts, populate_replies, populate_resets, populate_verifications
]



for query in queries:
    try:
        i = QueryExecutorService()
        res = i.execute(query)
    except sqlite3.OperationalError as e:
        print(f'ERROR: {e}')
#