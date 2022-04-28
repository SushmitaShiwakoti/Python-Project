def funargs (normal, *arg, **kwarg):
    print(normal)
    for item in arg:
        print(item)
    print("\n Now I would like to to introduce my family member")
    for key, value in kwarg.item():
        print(f"{key} is a {value}")

family =["Dhurba Shiwakoti","Sarita Shiwakoti", "Susmita Shiwakoti", "Yasoda Shiwakoti","Sabin Shiwakoti"]

normal= "I am Susmita Shiwakoti and I learned about python program."
kw={
    "Name":" Susmita Shiwakoti",
    "Age": 40,
    "Address":" kathmandu",
    "Susmita":"Developer"
}
funargs(normal, *family, **kw)