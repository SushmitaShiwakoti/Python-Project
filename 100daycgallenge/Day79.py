Height = float(input("Enter your height in centimeter: "))
Weight = float(input("Enter your weight in kg: "))
Height = Height/100

BMI = Weight/(Height*Height)

print("Your Body mass Index is: ", BMI)
if(BMI>0):
    if(BMI<=16):
        print("You are several underweight")

    elif(BMI<=18):
        print("You are underweight")

    elif(BMI<=25):
        print("You are Healhty")

    elif(BMI<=30):
        print("You are overweight")

    else:
        print("You are severaly overweight")
else:
    print("Enter valiad detail")