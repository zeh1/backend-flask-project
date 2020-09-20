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
    update test2 set id = 7 where id = 5;
'''

print( conn.execute(query) )