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

from services.query_executor_service import QueryExecutorService as q

conn = q()

query = '''
    delete from test2 where id = 6;
'''

print( conn.execute(query) )