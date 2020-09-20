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

import services.__custom_exceptions

try:
    raise services.__custom_exceptions.UserNotFoundException()
except Exception as e:
    print(e)