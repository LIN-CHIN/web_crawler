from urllib.request import urlopen,Request
import json
#--------網址設定--------------
# url = "https://www.dcard.tw/_api/forums/dcard/posts?popular=false"
#北商版
url = "https://www.dcard.tw/_api/forums/ntub/posts?popular=false"
r = Request(url)
r.add_header("user-agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
response = urlopen(r)
res = json.load(response)
times = 0
#找幾篇文章
while(1):
    if (res):
        for i in range(30) :
            times += 1
            print("第",times,"篇文章-",res[i]["title"])

        url = "https://www.dcard.tw/_api/forums/ntub/posts?popular=false&limit=30&before=" + (str)(res[-1]["id"])
        r = Request(url)
        r.add_header("user-agent",
                     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36")
        response = urlopen(r)
        res = json.load(response)
    else:
        break
