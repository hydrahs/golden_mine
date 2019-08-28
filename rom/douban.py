import json
import requests
import csv

f = open("c:/movie.csv","a")
csv_f =  csv.writer(f)

#get
url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=100&page_start=0"
#requests.get()
response = requests.get(url)
response.text#二进制数据使用content
#解析字符串json
r = json.loads(response.text)
#通过key获取元素
movie_list = r["subjects"]
for movie in movie_list:
    print()
    csv_f.writerow([movie["title"],movie["rate"]])
#存储为csv
#need to create a file
f.close()
