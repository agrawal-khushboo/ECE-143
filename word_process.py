def get_average_word_length(words):
    """
    average length of words
    """
    dic={}
    assert type(words)==list
    assert len(words)>0
    for w in words:
        assert type(w)==str
        dic[w]=len(w)
    l=dic.values()
    avgl=sum(l)/len(l)
    return avgl

def get_longest_word(words):
    """
    longest word
    """
    word=''
    l=0
    assert type(words)==list
    assert len(words)>0
    for w in words:
        assert type(w)==str
        if len(w)>l:
            word=w
            l=len(w)
    return word
    
def get_longest_words_startswith(words,start):
    """
    longest word that starts with a single letter
    """
    word=''
    l=0
    assert type(words)==list
    assert type(start)==str
    assert len(start)==1
    assert len(words)>0
    for w in words:
        assert type(w)==str
        if w[0]==start:
            if len(w)>l:
                word=w
                l=len(w)
    return word
            
def get_most_common_start(words):
    """
    def most common starting letter    
    """
    dic={}
    assert type(words)==list
    assert len(words)>0
    for w in words:
        assert type(w)==str
        dic[w[0]]=0
    for w in words:
        dic[w[0]]+=1
    word=sorted(dic.items(), key=lambda item: item[1],reverse=True)
    letter=word[0][0]
    return letter

def get_most_common_end(words):
    """
    the most common ending letter 
    """
    dic={}
    assert type(words)==list
    assert len(words)>0
    for w in words:
        assert type(w)==str
        dic[w[-1]]=0
    for w in words:
        dic[w[-1]]+=1
    word=sorted(dic.items(), key=lambda item: item[1],reverse=True)
    letter=word[0][0]
    return letter
    
    
