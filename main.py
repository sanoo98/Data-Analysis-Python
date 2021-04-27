#Website Scraping methods 
#API
#Beautiful Soup

#Install requiremtns
#pip install requests
#pip install bs4
#pip install html5lib

import requests 
from bs4 import BeautifulSoup
url= "https://codewithharry.com"

#Getting HTML
r= requests.get(url)
htmlContent=r.content
#print (htmlContent)

#Parse the HTML / Beautification of code
soup= BeautifulSoup(htmlContent, 'html.parser')
#print(soup)

#Transvering the tree/ HTML is a tree

#Getting title of HTML page 
title = soup.title

#Commonlu used types of objects 
#1.Tag , 2.Navigable String , 3.BeautifulSoup, 4.Comment

#print(type(title)) #Tag
#print(type(soup))  #Beautiful Soup
#print(type(title.string)) #Navigable String

markup= "<p><!-- Comment --></p>"
soup2= BeautifulSoup(markup)
#print(soup2.p.string)


#Get all paragraphs from page 
paras= soup.find_all('p')
#print(paras)

#Get all anchor tags from page 
anchors= soup.find_all('a')
#print(anchors)

#Get first element in HTML Page
#print(soup.find('p'))

#Get classes of any element in HTML Page
#print(soup.find('p')['class'])

#Find all the elements with class lead
#print(soup.find_all("p",class_="lead"))

#Get the text from the elements/tags/soup
#print(soup.find('p').get_text())
#print(soup.get_text())


all_links=set()
#Get all the links in the page 
for link in anchors:
    if(link.get('href') != '#'):
        linkText ="https://codewithharry.com" + link.get('href')
        all_links.add(link)
        #print(linkText)


