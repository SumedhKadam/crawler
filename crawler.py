import requests
from bs4 import BeautifulSoup

def spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "http://www.ebook-dl.com/page/" + str(page)
        source_code = requests.get(url)

        plain_text = source_code.text

        soup = BeautifulSoup(plain_text,"html.parser")
        for link1 in soup.findAll('div', {'class': 'portfolio-item design artwork'}):
            str1 = str(link1)
            for link2 in soup.findAll('a'):
                str2 = str(link2)
                for link3 in soup.findAll('img'):
                    str3 = str(link3)
                    if str2 in str1 and str3 in str1:
                        str3 = "http://www.ebook-dl.com" + str(link2.get('href'))
                        print(str3)
                        print(str(link3.get('alt')))
        page += 1

spider(10)