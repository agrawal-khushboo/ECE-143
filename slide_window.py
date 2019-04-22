def slide_window(x,width,increment):
    """
    Implement a sliding window for an arbitrary input list. 
    The function should take the window width and the window increment as inputs and should 
    produce a sequence of overlapping lists from the input list. For example, given x=list(range(15)), 
    the following is the output given a window width of 5 and window increment of 2.
    """
    assert increment>0
    assert (isinstance(x, list) or isinstance(x, range))
    if type(x)==range:
        x=list(x)
    assert type(width)==int
    assert type(increment)==int
    assert 0<width<=len(x)
    y=[]
    try:
        for i in range(0,len(x)-width+1,increment):
            z=x[i:(i+width)]
            y.append(z)
        return y
    except:
        return []
    
    
