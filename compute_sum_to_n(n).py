def compute_sum_to_n(n):
    """
    Write a function that computes the sum of 
    all non-negative integers (i.e. >=0) up to and including a specified value, n. 
    Here is the function signature compute_sum_to_n(n).
    """
    assert type(n)==int
    assert n>=0
    try:
        return int(n*(n+1)/2)
    except:
        return 0
