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

def f():
    if False:
        return 1
    else:
        pass
    return None

print( f() )