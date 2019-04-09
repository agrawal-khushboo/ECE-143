def is_string_integer(s):
    """
    Write a function that takes a single string character (i.e., 'a','b','c') 
    as input and returns True or False if that character represents a valid integer in base 10. 
    The function should be named is_string_integer.
    """
    
    assert type(s)==str
    assert len(s)==1
    try:
        if int(s) in range(10):
            return True
        else:
            return False
    except:
        return False
