#!/usr/bin/env python
# coding: utf-8

# In[26]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import connects

dbname=input("Enter Database name:")
connects.connect(dbname)
url="https://www.goibibo.com/hotels/intl-hotels-in-maldives-ct/"
req=requests.get(url)
content=req.content
#print(content)
soup=BeautifulSoup(content,"html.parser")
all_items = soup.find_all("div",{"class":"HotelCardstyles__OuterWrapperDiv-sc-1s80tyk-0 eXWmAQ"})
scraped_item_list=[]
for item in all_items:
    item_dict={}
    item_dict["Hotel Name"]=item.find("div",{"class":"HotelCardstyles__HotelNameWrapperDiv-sc-1s80tyk-14 byFNaN"}).text
    item_dict["Hotel Address"]=item.find("div",{"class":"PersuasionHoverTextstyles__TextWrapperSpan-sc-1c06rw1-14 dlEtqh"}).text
    item_dict["Hotel rating"]=item.find("span",{"class":"ReviewAndRatingsstyles__AverageReviewText-sc-1nxmeoo-6 jVFGfi"}).text
    item_dict["Hotel ambiance"]=item.find("span",{"class":"HotelCardstyles__RoomTypeTextWrapper-sc-1s80tyk-18 kGHtUO"}).text
    scraped_item_list.append(item_dict)
    connects.insert_into_table(dbname,tuple(item_dict.values()))
    
dataFrame=pd.DataFrame(scraped_item_list)
print("Creating CSV file...")
dataFrame.to_csv("goibibo.csv")
connects.get_Hotel_info(dbname)
   
   
    


# In[ ]:





# In[ ]:




