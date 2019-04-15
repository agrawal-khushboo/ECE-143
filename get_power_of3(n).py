import itertools as it
def get_power_of3(n):
    """
    Given a set of weights {1,3,9,27}, write a function to construct any number between 1 and 40. 
    In other words, using the set above and the addition and subtraction operations, construct 
    any integer between 1 and 40 without re-using elements. For example, 4 = 1+1+1+1 is not acceptable.

For example,

8 = 9 - 1

10 = 1 + 9

Hint: see the itertools module. Your function should return a 4-element list of the decomposition. 
For example, your return value given input 10 should be [1,0,1,0] because 1*1 + 0*3 + 9*1 + 27*0=10. 
Name your function get_power_of3.
    """
    assert type(n)==int
    assert n>0
    assert n<41
    try:
        weight = [-1,1,0]
        comb = [x for x in it.combinations_with_replacement(weight,4)]
        permute=[]
        for c in comb:
            p=[p for p in it.permutations(c)]
            p=set(p)
            for p in p:
                permute.append(p)
        for d in permute: 
            s=0
            for i in range(4):
                s+=d[i]*(3**i)
            if s==n:
                return list(d)
    except:
        return 
  
