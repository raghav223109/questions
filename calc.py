def add(x,y):
    """ add function"""
    return x + y

def sub(x,y):
    """ sub function"""
    return x - y


def mul(x,y):
    """ mul function"""
    return x * y

def div(x,y):
    """ div function"""
    if y == 0 :
        raise ValueError('can not be divided by zero')
    return x / y

