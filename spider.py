import requests
url = "https://www.amazon.cn/dp/B00A72VKR8/"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
        print("爬取失败")