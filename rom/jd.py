import requests
from lxml import etree

url = "https://search.jd.com/Search?keyword=python&enc=utf-8&wq=python&pvid=df33721fed494f97b0df5e5bc85afeff"
header  = {"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}
response = requests.get(url, headers=header)
html = response.content.decode("utf-8")
elements = etree.HTML(html)
price = elements.xpath("")


