import numpy as np
def gen_rand_slash(m=6,n=6,direction='back'):
    '''
    generate a random slash
    '''
    assert isinstance(m,int) and m>=2
    assert isinstance(n,int) and n>=2
    assert direction in {'forward','back'}
    img=np.zeros((m,n))
    row=np.random.randint(0,m-1)
    col=np.random.randint(0,n-1)
    lenmax=min((m-row),(n-col))
    slashlen=np.random.randint(2,(lenmax+1))
    for i in range(0,slashlen):
        img[row+i][col+i]=1
    if direction=='back':
        return img
    else:
        return img[::][::-1]
