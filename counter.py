from time import sleep
import random
from datetime import datetime
import itertools as it
 
def producer():
    'produce timestamps'
    starttime = datetime.now()
    while True:
        sleep(random.uniform(0,0.2))
        yield datetime.now()-starttime
p = producer()
import types
def tracker(p,limit=3):
    '''
    tracks odd seconds
    '''
    assert type(limit)==int
    assert limit>=0
    assert isinstance(p, types.GeneratorType)
    c=0
    while c<=limit:
        l=yield c
        if l is not None:
            assert l>limit
            assert type(l)==int
            limit=l
        x=next(p)
        if x.seconds//2==1:
            c+=1
            
