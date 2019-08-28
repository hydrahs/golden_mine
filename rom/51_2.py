import requests
from lxml import etree
#发送请求头
#模拟浏览器来应对反扒机制
# header = {"user-agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"} 
url = "https://search.jd.com/Search?keyword=python&enc=utf-8&wq=python&pvid=df33721fed494f97b0df5e5bc85afeff"
response = requests.get( url ,headers = header)
#response.content
#print(response.content)#获取的是字节类型
jd_html = response.content.decode("utf-8")
elements =  etree.HTML(jd_html)#解析节点/元素
# r = elements.xpath("//p[@class = 'nlink']/a[1]/text()")
# r = elements.xpath("//div[@class = 'price g_price g_price-highlight']/strong/text()")
#一般用class去找自己想要的文本 一个标签之中可能有多个class：用包含的方式：//h1[contents(@class,'t')] || //h1[@class]
mylist = elements.xpath("//div[@class = 'el']")

for el in el_list:
    #基于当前元素
    el.xpath("./p[@class = "t1"]/san/a/text()")
     
#有些属性的值比起标签里的文本更好获取