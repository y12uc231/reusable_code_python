class A :
    def __init__(self, a):
        super(A, self).__init__()
        self.a = a
        
    def do_something(self, a):
        print("print a {}".format(a))

class B():
    def __init__(self, d):
        super(B, self).__init__()
        self.d = d
        

objA = A(1)
objB = B(objA.do_something)

objB.d(3)
        