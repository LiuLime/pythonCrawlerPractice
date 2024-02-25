from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
import re
link1 = "https://en.wikipedia.org/wiki/Eric_Idle"
link2 = "https://en.wikipedia.org/wiki/Kevin_Baco"

html = urlopen(link1)
bs=BS(html,"html.parser")

# for link in bs.findAll("a",href=True):
#     print(link["href"])

for link in bs.findAll("a", attrs={"href":re.compile(r"^\/wiki\/*")}):
    print(link["href"])

#%%
for link in bs.findAll("div", attrs={"id":"bodyContent"}):
    print(link)
    break