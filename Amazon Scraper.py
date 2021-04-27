import requests 
from bs4 import BeautifulSoup


#Url of the product page goes here
url= 'https://www.amazon.com/DEGOL-Skipping-Tangle-Free-Bearings-Endurance/dp/B07P2F2YHT/ref=sr_1_1?dchild=1&fst=as%3Aoff&pf_rd_i=16225014011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=a3460e00-9eac-4cab-9814-093998a3f6d8&pf_rd_r=9G7GK6FSATCVES1VH8J2&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1489015681&rnid=10971181011&s=sporting-goods&sr=1-1'
#Search google "My user agent and past it in between {}"
#It tells your browswe information
headers={"User-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}

#returns data from website
page = requests.get(url, headers=headers)

#beautifies the code 
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)

title = soup.find(id="productTitle")
print(title)