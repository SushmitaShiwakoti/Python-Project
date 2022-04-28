class A:
  classvar1 = "HI I am Susmita Shiwakoti"
  def __init__(self) -> None:
      self.var1="Today I Learned about override and supper"
      self.var2= "Challenge accepeted"
      self.var3= "Susmita Shiwakoti"
class B(A):
    classvar1="I am Sush"
    def __init__(self) -> None:
        self.var1= "I have completed my 34 day of 100 day challenge"'\n'
        self.classvar1= "Today is 34 day of my challenge"

a=A()
b=B()
print(b.var1, b.classvar1)
print(a.var1,a.var2 )