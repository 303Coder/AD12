# Library that sends HTTP requests to the web
import requests

# Data parsing library to extract data from HTML from requests library
from bs4 import BeautifulSoup



#Specific Amazon product number to search for
def initialize(ASIN):
    global ASINNUM
    ASINNUM = ASIN

    global userHeaders
    # Headers to simulate a real web browser sending request
    userHeaders={"accept-language": "en-US,en;q=0.9","accept-encoding": "gzip, deflate, br","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}

    global url
    # Link to specific Amazon product
    url="https://www.amazon.com/dp/"+ ASIN

    global resp
    # HTTP request to Amazon using the headers
    resp = requests.get(url, headers=userHeaders)
    #print(resp.status_code)


    global soup
    # Beautifulsoup taking in the HTTP request as variable
    soup=BeautifulSoup(resp.text,'html.parser')




def find():

    l=[]
    o={}
    global errors
    errors = []


    #<span id="tp_price_block_total_price_ww" class="a-price" data-a-size="m" data-a-color="base"><span class="a-offscreen">$2.99</span>
    try:
        o["price"]=soup.find("span",{"class":"a-price"}).find("span").text
    except:
        o["price"]=None
        errors.append(ASINNUM)


    return o.get("price")


def returnErrors():
    return errors


def printFindings():

    l=[]
    o={}


    #<span id="tp_price_block_total_price_ww" class="a-price" data-a-size="m" data-a-color="base"><span class="a-offscreen">$2.99</span>
    try:
        o["price"]=soup.find("span",{"class":"a-price"}).find("span").text
    except:
        o["price"]=None

    print(o.get("price"))