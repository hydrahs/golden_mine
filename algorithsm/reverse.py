""" str = "dafjlsk"
def myFunction(str):
    str
print(myFunction(str)) """

s =  input()
# the first way
result = s[::-1]
""" 
b = a[i:j]   表示复制a[i]到a[j-1]，以生成新的list对象
a = [0,1,2,3,4,5,6,7,8,9]
b = a[1:3]   # [1,2]
当i缺省时，默认为0，即 a[:3]相当于 a[0:3]
当j缺省时，默认为len(alist), 即a[1:]相当于a[1:10]
当i,j都缺省时，a[:]就相当于完整复制一份a

b = a[i:j:s]表示：i,j与上面的一样，但s表示步进，缺省为1.
所以a[i:j:1]相当于a[i:j]
当s<0时，i缺省时，默认为-1. j缺省时，默认为-len(a)-1
所以a[::-1]相当于 a[-1:-len(a)-1:-1]，也就是从最后一个元素到第一个元素复制一遍，即倒序 """

# the second way
l = list(s)
result = "".join(l[::-1])
