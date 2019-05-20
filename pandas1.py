import pandas as pd
def split_count(x):
    """
    dataframe as output
    """
    assert x.name=='Is there anything in particular you want to use Python for?'
    assert isinstance(x,pd.Series)
    counts={}
    for idx in x:
        indices=idx.strip().split(',')
        for i in indices:
            i=i.strip()
            counts[i]=0
    for idx in x:
        indices=idx.strip().split(',')
        for i in indices:
            i=i.strip()
            counts[i]+=1
    index=[c for c in counts.keys()]
    values=pd.Series([c for c in counts.values()],index=index)
    d={'count':values}
    df = pd.DataFrame(d,index=index)
    df=df.sort_values('count')
    return df

