#to scrape a website
#1.use the api
#2.html web scraping use tool like bs4
import requests
from bs4 import BeautifulSoup
url='https://codewithharry.com'
#step 1: get the html
r=requests.get(url)
htmlcontent=r.content
#print(htmlcontent)
#step2: parse the html
soup=BeautifulSoup(htmlcontent,'html.parser')
#print(soup.prettify) 
#nsc=soup.find(id='navbarSupportedContent')
#print(nsc)
#commonly used type of object
#1. tag
#2.NavigableString
#3.Beautiful soup
#4. comment
#get the title of Html page
title=soup.title
#get the paragraph
para=soup.find_all('p')
#print(para)
#get the anchor tag
anc=soup.find_all('a')
all_links=set()

#print(soup.find('p')['class'])
#find all the elements with class lead
#print(soup.find_all('p',class_='lead'))
#get the text
#print(soup.find('p').get_text())
#for link in anc:
 #   if (link.get('href')!='#'):
  #      linktext='https://codewithharry.com'+link.get('href')
   #     all_links.add(link)
    #    print(linktext)

nsc=soup.find(id='navbarSupportedContent')
nsc.contents  
#for em in nsc.children:
 #   print(em)
#for item in nsc.strings:
 #   print(item)

#for item in nsc.parents:
 #   print(item.name)

#print(nsc.next_sibling.next_sibling)
print(nsc.previous_sibling.previous_sibling)
print(soup.select('.modal-footer'))