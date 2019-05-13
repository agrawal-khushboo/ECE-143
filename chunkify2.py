import os,sys
def split_by_n(fname,n=3):
    """
    split the file by n
    """
    assert type(n)==int
    assert n>=1
    assert type(fname)==str
    f=open(fname)
    size=os.path.getsize(fname)
    chunk_size=size//n
    i=0
    file=open('%s_%02d.txt'%(fname,i),'wt')
    for line in f:
        size_line=sys.getsizeof(line)
        size = file.tell()
        size=size+size_line
        if size <=chunk_size or i==n-1:
            file.write(line)
        else:
            i+=1
            file=open('%s_%02d.txt'%(fname,i),'wt')


