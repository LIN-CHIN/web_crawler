import getDcard
# url = "https://www.dcard.tw/_api/forums/dcard/posts?popular=false" Dcard版
#↓北商版
url = "https://www.dcard.tw/_api/forums/ntub/posts?popular=false"
res = getDcard.getDcard(url)

#找共有幾篇文章
count = 0
while(1):
    if (res):
        for i in range(30) :
            count += 1
            print("第",count,"篇文章-",res[i]["title"])
        url = "https://www.dcard.tw/_api/forums/ntub/posts?popular=false&limit=30&before=" + (str)(res[-1]["id"])
        res = getDcard.getDcard(url)
    else:
        break
