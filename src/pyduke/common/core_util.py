import numpy as np
from datetime import datetime
from functional import seq

HR_WIDTH = 50

DATE_TIME_FORMAT = '%a, %d-%b-%Y  %H:%M:%S %p'

def hr (size=HR_WIDTH):
    '''Draw a horizontal line of given ``size``'''
    print("-" * size)    

def heading (mesg, size=HR_WIDTH):
    ''' A heading has ``mesg`` with horzintal rule above and below.'''
    print("")
    print("-" * size)
    print(mesg)
    print("-" * size)
    
def join (*mesg, delimiter=" "):
    ''' Join any number of messages ``mesg`` with ``delimiter`` '''
    return delimiter.join (seq(mesg).filter(lambda x: x != None).to_list())

def now():
    ''' Current time '''
    return datetime.now().strftime(DATE_TIME_FORMAT)

def to_2d (X):
    ''' Convert an array or numpy array that is 1d to a row vector that is 2d '''
    return X if (type(X) == np.ndarray and len(X.shape) == 2) else np.array(X).reshape(1, -1)
    
def to_list (x):
    ''' Convert ``x`` to a list. Raise expection if not possible. '''
    if type(x) is tuple or type(x) is list:
        return list(x)
    raise 'InvalidArgumentError: Argument "x" has to be of a type convertable to list using list(<item>), Valid types are "list", "tuple" or "set" Found={}'.format(type(x))

