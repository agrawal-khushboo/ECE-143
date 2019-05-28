import numpy as np
def solvefrob(coefs,b):
    """
    solve frobenius
    """
    assert type(coefs)==list
    assert type(b)==int
    assert b>0
    for c in coefs:
        assert c>0
        assert type(c)==int
    coefs=np.array(coefs)
    dic=dict()
    loc=[]
    bd=np.arange(b+1)
    for i in range(len(coefs)):
        dic[i]=bd
        bd=bd[:,None]
    for i in range(len(coefs)):
        loc.append(coefs[i]*dic[i])
    loc = np.where(sum(loc) == b)
    
    pos = []
    idx = []
    for j in range(len(loc[0])-1, -1, -1):
        pos = []
        for i in range(len(loc)-1, -1, -1):
            pos.append(loc[i][j])
        idx.append(tuple(pos))
    return idx
    

    
