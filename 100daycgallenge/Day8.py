dic = {
    "name":"Susmita Shiwakoti",
    "place":"kathmandu",
    'grade': "bachelor",
    "year":2022,#can't allow duplicate value
    'year':2019,
}
print(dic)
print(len(dic))
print(type(dic))
dic["F_memeber"] = "Dhurba",'sarita ','yasoda','sabin' #Adding value
print(dic)
x = dic.keys() #only keys print
print(x)
y = dic.items
print(x)
dic.update({'name':'Ariya shiwakoti'}) #update new value
print(dic)
myfamily ={ # ues a neasted loop
    "child1":{
        'name':'yasoda shiwakoti',
        'year':2022
    },
    "chlid2":{
        "name":"sabin shiwakoti"
    }   
}
print(myfamily)