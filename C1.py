from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

html = urlopen("http://pythonscraping.com/pages/page1.html")
bs = BS(html, "html.parser")
# bs = BS(html, "lxml")
# bs = BS(html, "html5lib")
# %% Deal with error
# 网页不存在于该服务器-> HTTPError
from urllib.error import HTTPError

# 服务器不存在 -> URLError
from urllib.error import URLError

# %% Extract tag text
url = 'https://www.pythonscraping.com/pages/warandpeace.html'
html = urlopen(url)
bs = BS(html, "html.parser")
namelist = bs.findAll("span", {"class": "green"})
for name in namelist:
    print(name.get_text())
text = bs.findAll(text="the prince")
print(text)

# %% Extract children tag
url = 'https://www.pythonscraping.com/pages/page3.html'
html = urlopen(url)
bs = BS(html, "html.parser")
# for child in bs.find("table", {"id": "giftList"}).children:
#     print(child)

# next_siblings, previous_siblings 打印除开始行以外的所有下一行/上一行
for nextsibling in bs.find("table", {"id": "giftList"}).tr.next_siblings:
    print(nextsibling)

# %% regular expression
# Example: <img src="../img/gifts/img3.jpg">
import re

figure_re = r"\.\.\/img\/gifts\/img.*\.jpg"
for img in bs.findAll("img", {"src": re.compile(figure_re)}):
    print(img)

#%% lambda function
# for text in bs.findAll(lambda tag: len(tag.attrs) == 2):
#     print(text)
for text in bs.findAll(lambda tag:tag.name == "img"):
    print(text)
