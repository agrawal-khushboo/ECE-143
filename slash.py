import numpy as np
import random
from matplotlib.pylab import subplots, cm
def gen_rand_slash(m=6,n=6,direction='back'):
    """
    The assignment is to write a function that can produce a uniformly random forward 
    or backslashed image (i.e., Numpy array) 
    of at least two non-zero pixels.
    """
    arr=[]
    assert type(m)==int
    assert type(n)==int
    assert m>1
    assert n>1
    assert direction=='back' or direction=='forward'
    if direction=='back':
        for i in range(m-1):
            for j in range(n-1):
                x=np.zeros((m,n))
                x[i,j]=1
                x[i+1,j+1]=1
                arr.append(x)
                k=min((m-i-1),(n-j-1))
                for s in range(k-1):
                    y=np.copy(x)
                    y[i+2+s,j+2+s]=1
                    arr.append(y)
                    x=np.copy(y)
    else:
        for i in range(m-1,0,-1):
            for j in range(n-1):
                x=np.zeros((m,n))
                x[i,j]=1
                x[i-1,j+1]=1
                arr.append(x)
                k=min((i),(n-j-1))
                for s in range(k-1):
                    y=np.copy(x)
                    y[i-2-s,j+2+s]=1
                    arr.append(y)
                    x=np.copy(y)
    a=random.choice(arr)         
    return a

