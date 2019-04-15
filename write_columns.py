def write_columns(data,fname):
    """
    Using this data

    data=[5,4,6,1,9,0,3,9,2,7,10,8,4,7,1,2,7,6,5,2,8,2,0,1,1,1,2,10,6,2]

    Write a function that can write the following formula to three columns to a comma-separated file:

    data_value, data_value**2, (data_value+data_value**2)/3.

    Here is your function signature write_columns(data,fname).
    """
    assert type(fname)==str
    assert type(sum(data))
    f=open(fname,'w') 
    for d in data:
        d1=d
        d2=d**2
        d3=(d1+d2)/3
        f.write(str(d1)+','+str(d2)+','+str(d3)+'\n')
    f.close()
    
        
    
