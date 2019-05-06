import numpy as np
from matplotlib.pylab import subplots, cm
def gen_rand_slash(m=6,n=6,direction='back'):
    """
    The assignment is to write a function that can produce a uniformly random forward 
    or backslashed image (i.e., Numpy array) 
    of at least two non-zero pixels.
    """
    assert type(m)==int
    assert type(n)==int
    assert m>1
    assert n>1
    assert direction=='back' or direction=='forward'
    row=np.random.randint(0,m-1)
    column=np.random.randint(0,n-1)
    slash=min((m-row),(n-column))
    slashlen=np.random.randint(2,slash+1)
    image=np.zeros((m,n))
    for i in range(slashlen):
        image[row+i][column+i]=1
    if direction=='back':
        return image
    else:
        image=np.flip(image,1)
        return image
        
        
