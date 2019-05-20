import pandas as pd
def add_month_yr(x):
    """
    add month year
    """
    assert isinstance(x,pd.DataFrame)
    x1=x['Timestamp']
    values=[]
    def monthyr(m,y):
        year=str(y)
        m=int(m)
        mo=''
        if m==1:
            mo='Jan'
        elif m==2:
            mo='Feb'
        elif m==3:
            mo='Mar'
        elif m==4:
            mo='Apr'
        elif m==5:
            mo='May'
        elif m==6:
            mo='Jun'
        elif m==7:
            mo='Jul'
        elif m==8:
            mo='Aug'
        elif m==9:
            mo='Sep'
        elif m==10:
            mo='Oct'
        elif m==11:
            mo='Nov'
        elif m==12:
            mo='Dec'
        s=mo+'-'+year
        return s     
    for i in x1:
        i=i.split(' ')
        i=i[0].split('/')
        values.append(monthyr(i[0],i[2]))
    x['month-yr']=values
    return x

def count_month_yr(x):
    """
    count the month yr
    """
    assert isinstance(x,pd.DataFrame)
    x=add_month_yr(x)
    x1=x['month-yr']
    counts={}
    for idx in x1:
        ind=idx.strip()
        counts[ind]=0
    for idx in x1:
        ind=idx.strip()
        counts[ind]+=1
    index=[c for c in counts.keys()]
    values=pd.Series([c for c in counts.values()],index=index)
    d={'Timestamp':values}
    df = pd.DataFrame(d,index=index)
    df.index.name = 'month-yr'
    return df
    
