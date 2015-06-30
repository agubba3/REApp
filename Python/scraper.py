import requests
from bs4 import BeautifulSoup
import re

keyword = "market"
url1 = "http://www.abraaj.com/"
url = "http://www.abraaj.com/"
response = requests.get(url)
# parse html
page = str(BeautifulSoup(response.content))


def getURL(page):

    start_link = page.find("a href")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote

def extract_html(url2):
    html = requests.get(url2)
    texting = BeautifulSoup(html.content)
    return str(texting) + ("\n\n\n")

count = 0;
while True:
    url, n = getURL(page)
    page = page[n:]
    if url:
        url_string = str(url)
        if url_string[0:7] != "http://":
            url = url1+url_string
            out = "^^^URL: " + url + extract_html(url) 
            temp = [m.start() for m in re.finditer(keyword, out)]
            count = count + len(temp);
            print("URL: " + url + " "+ str(temp) + " The word " + keyword + " happens " + str(len(temp))
            + " times on this webpage with this url. \n"); 
    else:
        break

print("\n The word " + keyword + " happens a total of " + str(count) + " times.");

