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
