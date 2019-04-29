import random
def get_sample(nbits,prob,n):
    """
    Given a number of bits, write the get_sample function to return a list n of random samples from 
    a finite probability mass function defined by a dictionary with keys defined by a specified number of bits. 
    For example, given 3 bits, we have the following dictionary that defines the probability of each of the keys. 
    The values of the dictionary correspond of the probability of drawing any one of these. 
    For example, if all of these were equally likely, then here is the corresponding dictionary p,
    """
    assert type(nbits)==int
    assert type(n)==int
    assert nbits>0
    assert n>=0
    assert type(prob)==dict
    s=0.0
    for p in prob:
        assert type(prob[p])==float or type(prob[p])==int
        s+=prob[p]       
    assert s==1.0
    assert len(prob)==2**nbits
    if n==0:
        return []
    else:
        l=random.choices(list(prob),list(prob.values()),k=n)
        return l
