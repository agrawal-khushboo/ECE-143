def slide_window(x,width,increment):
    assert increment>0
    assert (isinstance(x, list) or isinstance(x, range))
    if type(x)==range:
        x=list(x)
    assert 0<width<=len(x)
    y=[]
    try:
        for i in range(0,len(x)-width+1,increment):
            z=x[i:(i+width)]
            y.append(z)
        return y
    except:
        return []
    
    
