def myFun(str):
    dic={}
    for i in str:
        dic[i] =  str.count(i) #覆盖的问题
print(myFun(str="hahahahha"))