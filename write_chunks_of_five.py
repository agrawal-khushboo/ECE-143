def write_chunks_of_five(words,fname):
    """
    Using corpus of 10,000 common English words, create a new file that consists of each 
    consecutive non-overlapping sequence of five lines merged into one line. Here are the first 10 lines:

    the of and to a
    in for is on that
    by this with i you
    it not or be are
    from at as your all
    have new more an was
    we will home can us
    about if page my has
    search free but our one
    other do no information time
    If the last group has less than five at the end, just write out the last group. 
    Here is your function signature: write_chunks_of_five(words,fname). 
    The words is a list of words from the above corpus and fname is the output filename string.
    """
    assert type(fname)==str
    for w in words:
        assert type(w)==str
    try:
        f=open(fname,'w')
        l=len(words)//5
        if l!=0:
            for i in range(l):
                f.write(words[5*i]+' '+words[(5*i)+1]+' '+words[(5*i)+2]+' '+words[(5*i)+3]+' '+words[(5*i)+4]+'\n')
            for i in range(5*(l),len(words)):
                f.write(words[i]+' ')
        elif l==0:
            for i in range(len(words)):
                f.write(words[i]+' ')
        f.close()
    except:
        return 

