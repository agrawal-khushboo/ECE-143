import math
import random
def multinomial_sample(n,p,k=1):
    '''
    multinomial sample
    '''
    assert type(n)==int
    assert type(k)==int
    assert type(p)==list
    assert len(p)>0
    z=0
    for pr in p:
        assert pr>=0 and pr<=1
        if pr!=0:
            z+=1
    assert math.fsum(p)==1
    assert n>0
    assert k>=0
    if k==0:
        return []
    lst=[]
    for s in range(k):
        sample=[]
        dummy=[]
        d=0
        for r in range(z-1):
            if d<n-z:
                rand=random.randint(0,n-z-d)
                dummy.append(rand)
                d+=rand
            else:
                dummy.append(0)
        dummy.append(n-z-d)
        for i in range(len(p)):
            if p[i]==0:
                sample.append(0)
            else:
                sample.append((dummy[-1])+1)
                dummy.pop()
        lst.append(sample)
    return lst
                
