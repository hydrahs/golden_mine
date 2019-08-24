""" print("请输入你的求和数字: ")
a = int(input())
print("答案是: ", int(a/10%10)+a%10+int(a/100)) """

""" print("请输入你的求和数字: ")
str = input()
len =  len(str)
a = int(str)

sum = 0
for(int i=1, i<len, i=++)
 sum += a/10*len  """

while 1: 
    print ("请输入数字:")
    sum = 0
    str = input()
    if str.isdigit():
        array=[]
        for element in str:
            array.append(element)
        for a in array:
            sum += int(a)
        print(sum)
    else:
        print ("请输入数字!")

