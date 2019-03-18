from urllib.request import urlopen,Request
import json
def getDcard(url) :
    r = Request(url)
    r.add_header("user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
    response = urlopen(r)
    res = json.load(response)
    return res
