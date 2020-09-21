'''
def a():
    x = 1
    def b():
        y = 2
        print('x: ' + f'{x}')
        def c():
            z = 3
            print('y: ' + f'{y}')
        return c
    return b

a()()()
'''





from services.query_builder_service import QueryBuilderService as q
from services.query_executor_service import QueryExecutorService as e

'''
queries = q.get_posts(1)
res = e().execute(queries[0])
print( res )
'''

'''
queries = q.insert_post(1, "inserted post title", "inserted post body")
for entry in queries:
    e().execute(entry)
'''

'''
queries = q.get_replies(1)
print( e().execute(queries[0]) )
'''

'''
queries = q.insert_reply(4, 'inserted reply body', 2)
print( e().execute(queries[0]) )
'''

'''
queries = q.login_attempt('user1')
print( e().execute(queries[0]) )
'''

'''
queries = q.signup_attempt('email2', 'inserted user5', 'my pass')
for entry in queries:
    e().execute(entry)
'''

'''
queries = q.password_reset_attempt('email1')
for entry in queries:
    e().execute(entry)
'''

'''
queries = q.password_change_attempt_part_1(3)
for entry in queries:
    # print(entry)
    print ( e().execute(entry) )
'''

'''
queries = q.password_change_attempt_part_2(4, 'my new pass')
for entry in queries:
    # print(entry)
    print ( e().execute(entry) )
'''

'''
queries = q.simple_search('inserted post')
for entry in queries:
    print( e().execute(entry) )
'''

'''
session = '888813a845f4475a9f0cfdd7ecfbe55f'
new_pass = 'hi'
queries = q.consume_password_reset_attempt(session, new_pass)
for entry in queries:
    # print(entry)
    print( e().execute(entry) )
'''

'''
session = '7508a72038764630aa1c238b4b732f25'
queries = q.consume_verify_email_attempt(session)
for entry in queries:
    # print(entry)
    print(e().execute(entry))
'''