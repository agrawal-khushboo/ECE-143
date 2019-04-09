def compute_average_word_length(instring,unique=False):
    """
    Given the following string


'''Mary had a little lamb
its fleece was white as snow
and everywhere that Mary went
the lamb was sure to go'''

Write a compute_average_word_length function to compute the average 
length of the words in this string. Supply an option to your function to exclude redundancies in the words, 
re-compute the average length of the words. The words are case-sensitive.
    """
    assert type(instring)==str
    words=[w for w in instring.split()]
    s=0
    try:
        if unique==True:
            words=set(words)
            n=len(words)
            for w in words:
                s+=len(w)
            return s/n
        else:
            n=len(words)
            for w in words:
                s+=len(w)
            return s/n
    except:
        return 0
            
            
        
    

