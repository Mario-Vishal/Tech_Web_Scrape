from bs4 import BeautifulSoup
import requests
import re

headers = {"Accept":'text/html'}
news_link1 = "https://www.indiatoday.in/technology/news"
source = requests.get(news_link1,headers).text

soup = BeautifulSoup(source,'lxml')
headline = soup.find('div')

temp = headline.main.div
temp1 = temp.find('div',class_="view view-category-wise-content-list view-id-category_wise_content_list view-display-id-section_wise_content_listing view-dom-id- custom")
article = temp1.div.find_all('div',class_='catagory-listing')
news_count=0
print('--------------Tech News from India Today--------------')
print()
for tag in article:

    news_headline = tag.find('div',class_='detail')
    headline = news_headline.h2.text
    headline_link = news_headline.find('a')
    news_count+=1
    print(news_count,"--")
    print(headline)
    print()
    print(news_link1+headline_link.get('href'))
    print('---------------------------------------')
    print()