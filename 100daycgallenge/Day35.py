class A:
    def met(self):
        print("This is a meyhod from A")

class B(A):
    def met(self):
        print("This is a method from B")

class C(A):
    def met(self):
        print("This is a method from C")
class D(B, C):
    pass
class E(C,B):
    pass

d=D()
d.met()
c=C()
c.met()
