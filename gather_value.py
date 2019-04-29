import random
import math
def get_sample(nbits=1, prob={'0':0.5, '1': 0.5}, n=2):
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
    b=[]
    for i in range(2**nbits):
        bi=int(bin(i)[2:])
        b.append(bi)   
    for p in prob:
        pi=int(p)
        assert pi in b
        assert 0.0<=prob[p]<=1.0
    values=list(prob.values())
    assert math.fsum(values)==1
    assert len(prob)==2**nbits
    if n==0:
        return []
    else:
        l=random.choices(list(prob),list(prob.values()),k=n)
        return l
def map_bitstring(x):
    """
    Write a function map_bitstring that takes a list of bitstrings (i.e., 0101) and maps each bitstring to 0
    if the number of 0s in the bitstring strictly exceeds the number of 1s. Otherwise, map that bitstring to 1. 
    The output of your function is a dictionary of the so-described key-value pairs.
    """
    assert type(x)==list
    assert len(x)>0
    l=len(x[0])
    d={}
    for i in x:
        assert type(i)==str
        assert len(i)==l
        z=0
        o=0
        for j in i:
            assert j=='0' or j=='1'
            if j=='0':
                z+=1
            else:
                o+=1
        if z>o:
            d[i]=0
        else:
            d[i]=1
    return d

def gather_values(x):
    """
    Now that you have get_sample working, generate n samples and tally the number of times an existing key is repeated. 
    Generate a new dictionary with bitstrings as keys and with values as lists that contain the corresponding mapped 
    values from map_bitstring.
    Here is an example for n=20,
    """
    assert type(x)==list
    assert len(x)>0
    d={}
    for i in x:
        d[i]=list()
    for i in x:
        v=map_bitstring([i])
        d[i].append(v[i])
    return d

        
    
    
        
    
    
    
