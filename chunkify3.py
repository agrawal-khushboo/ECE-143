import os
def split_by_n(fname,n=3):
    '''
    split file by n
    '''
    assert type(fname)==str
    assert type(n)==int
    assert n>=1 and n<100
    f=open(fname)
    size=os.path.getsize(fname)
    b=0
    lines=f.readlines()
    chunk_size=len(lines)//n
    for i in range(n):
        if i==n-1:
            file=open('%s_%02d.txt'%(fname,i),'wt')
            line=lines[i*chunk_size:]
            for l in line:
                file.write(l)
            b+=file.tell()
        else:
            file=open('%s_%02d.txt'%(fname,i),'wt')
            line=lines[i*chunk_size:((i+1)*chunk_size)]
            for l in line:
                file.write(l)
            b+=file.tell()
    
