#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#OFFICIAL VERSION - WHO DELETED YOU AND WHO YOU ADDED TO FRIENDS ON FACEBOOK
#TESTED IN JULY 2022
#REQUIRES REPORTS FROM FACEBOOK (YOU CAN DOWNLOAD IN SETTINGS)

from bs4 import BeautifulSoup
import os.path
import re
import pandas as pd
#path to reports (new and old for comparison, first path uses function, second path is full, it could be changed)
friends_1=os.path.join(os.getcwd(),"Downloads","facebook-igorszczesny04 (10)","friends.html")
friends_2=("C://Users//igors//Downloads//facebook-igorszczesny04 (11)//friends.html")

tab_1 = pd.DataFrame()
tab_2 = pd.DataFrame()

for friends in [friends_1, friends_2]:
    HTMLFile = open(friends, encoding="UTF-8")
  
    index = HTMLFile.read()
    S = BeautifulSoup(index, 'lxml')
    w = re.finditer(r"2ph_ _a6-h", str(S))
    tab = pd.DataFrame()
    j=0
    
    s = {
    friends_1 : tab_1,
    friends_2 : tab_2
    }

    
    for i in w:
        j=j+1
        s[friends].loc[j-1,"start"] = str(S)[i.start()+18:i.start()+18+str(S)[i.start()+18:i.end()+45].find("</d")]

    s[friends] = s[friends].drop_duplicates()




combined_dfs = pd.concat([tab_1, tab_2])
symmetric_difference = combined_dfs.drop_duplicates(keep=False)
symmetric_difference["dodany?"] = "usunięty"
symmetric_difference=symmetric_difference.reset_index()
symmetric_difference=symmetric_difference.drop(columns=['index'])

for count,i in enumerate(symmetric_difference.values[:,0]):
    if i in tab_2["start"].values:
        symmetric_difference.loc[count,"dodany?"]="dodany"
        
symmetric_difference

