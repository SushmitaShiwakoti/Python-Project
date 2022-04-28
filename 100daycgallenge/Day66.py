FirstOperand= input("Enter First Number(Any Numerical value): ")
FirstOperand = int(FirstOperand)
operator = input("Enter Operator(+,-,*,/,%)\n")
SecondOperand = input("Enter Second Number: ")
SecondOperand = int(SecondOperand)
#claculate answer base on entered operator

if(operator=='+'):
    Answer = FirstOperand+SecondOperand

if(operator=='-'):
    Answer = FirstOperand-SecondOperand
if(operator=='*'):
    Answer = FirstOperand*SecondOperand
if(operator=='/'):
    Answer = FirstOperand/SecondOperand
if(operator=='%'):
    Answer = FirstOperand%SecondOperand
print("The Answer is: ", Answer)
