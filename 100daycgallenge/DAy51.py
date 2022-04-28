class A:
    def __init__(self):
        print("This is init A")

    def Feature1(self):
        print("This is feature1")

    def Feature2(self):
        print("This is feature2")

class B:
    def __init__(self):
        # super().__init__
        print("Init in B")
    def Feature3(self):
        print("This is feature3")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("Init in c ")
b1=B()
a1=C()
# a1.Feature2