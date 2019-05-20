import pandas as pd
import numpy as np
import math
from collections import defaultdict
def multinomial_cond_exp(n, p, cond = "x2"):
    """
    multimomial
    """
    assert type(n)==int
    assert n>0
    assert type(p)==list or np.array
    assert len(p)>0
    for pr in p:
        assert pr>=0.0 and pr<=1.0
    assert math.fsum(p)==1.0
    assert type(cond)==str
    prob=defaultdict(float)
    data=defaultdict(list)
    columns=[]
    p_cond=defaultdict(list)
    p_noncond=defaultdict(list)
    for i in range(len(p)):
        col='x'+str(i)
        prob[col]=p[i]
        columns.append(col)
    cond=cond.strip()
    cond=cond.split('+')
    cond=[c.strip() for c in cond]
    noncond=[]
    for c in columns:
        if c in cond:
            p_cond[c]=prob[c]
        else:
            noncond.append(c)
            p_noncond[c]=prob[c]
    s1=sum(p_cond.values())
    for key in p_cond:
        p_cond[key]/=s1
    s2=sum(p_noncond.values())
    for key in p_noncond:
        p_noncond[key]/=s2
    for k in range(n+1):
        for key in p_cond:
            data[key].append(p_cond[key]*k)
        for key in p_noncond:
            data[key].append(p_noncond[key]*(n-k))
    df=pd.DataFrame(data, index=list(range(n+1)),columns=columns)
    df.index.name='cond'
    return df


