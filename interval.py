class Interval(object):
    """ Doc string """
    def __init__(self,a,b):
        """
        :a: integer
        :b: integer
        """
        assert a<b
        assert isinstance(a,int)
        assert isinstance(b,int)
        self.a = a
        self.b = b
        
    def __repr__(self):
        """
        defines the statemetn of the interval
        """
        return 'Interval(%d,%d)'%(self.a,self.b)

    def __eq__(self,other):
        """
        equal
        """
        assert isinstance(other,Interval)
        assert isinstance(self,Interval)
        if self.a==other.a and self.b==other.b:
            return True
        else:
            return False
        

    def __add__(self,other):
        """
        adding the sequence
        """
        assert isinstance(other,Interval)
        assert isinstance(self,Interval)
        if max(self.a,other.a)<min(self.b,other.b):
            return Interval(min(self.a,other.a),max(self.b,other.b))
        else:
            return [self,other]
