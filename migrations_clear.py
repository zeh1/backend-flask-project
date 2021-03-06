from lib.services.query_executor_service import QueryExecutorService
import sqlite3

delete_users_table = '''
    drop table users;
'''

delete_posts_table = '''
    drop table posts;
'''

delete_replies_table = '''
    drop table replies;
'''

queries = [
    delete_users_table, 
    delete_posts_table,
    delete_replies_table
]

for query in queries:
    try:
        i = QueryExecutorService()
        res = i.execute(query)
    except sqlite3.OperationalError as e:
        print(f'ERROR: {e}')
#