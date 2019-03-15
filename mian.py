from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
# import requests
url = "https://www.dcard.tw/f"
r = Request(url)
r.add_header("user-agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36")
response = urlopen(r)
html = BeautifulSoup(response)
# 取得標籤內容
res = html.find_all("h3",class_="PostEntry_title_H5o4dj")
for r in res :
   print(r.text)