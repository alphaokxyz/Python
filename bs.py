import requests
from bs4 import BeautifulSoup
url = "https://python123.io/ws/demo.html"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    
    demo = r.text
    soup = BeautifulSoup(demo , "html.parser")
    print(soup.prettify())
except:
        print("爬取失败")