import string
from collections import defaultdict
def encrypt_message(message,fname):
    '''
    encrypt message
    '''
    assert type(message)==str
    assert type(fname)==str
    assert len(message)>0
    f=open(fname)
    word_dic=defaultdict(list)
    line_index=0
    punc_table = str.maketrans({key: None for key in string.punctuation})
    for line in f:
        li=line.lower()
        li = str(li).translate(punc_table)
        words=li.strip().split(' ')
        word_index=0
        for w in words:
            if w !='':
                word_dic[w].append((line_index,word_index))
                word_index+=1
        line_index+=1
    encrypt=[]
    words=message.strip().split(' ')
    for w in words:
        if w!='':
            assert w in word_dic.keys()
            assert len(word_dic[w])>0
            encrypt.append(word_dic[w][-1])
            word_dic[w].pop()
    return encrypt

def decrypt_message(inlist,fname):
    """
    decrypt message
    """
    assert type(inlist)==list
    assert len(inlist)>0
    assert type(fname)==str
    message=''
    f=open(fname)
    word_dic=defaultdict(list)
    line_index=0
    punc_table = str.maketrans({key: None for key in string.punctuation})
    for line in f:
        li=line.lower()
        li = str(li).translate(punc_table)
        words=li.strip().split(' ')
        word_index=0
        for w in words:
            if w !='':
                word_dic[w].append((line_index,word_index))
                word_index+=1
        line_index+=1
    count=defaultdict(int)
    for t in inlist:
        count[t]+=1
    for t in inlist:
        present=0
        assert count[t]==1
        for w in word_dic:
            if t in word_dic[w]:
                message=message+' '+w
                present=1
        assert present==1
    message=message.strip()
    return message
    

