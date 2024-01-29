# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 16:40:25 2023

@author: igors
"""

"""
https://slaskie.travel/
https://invest-in-silesia.pl/
https://transformacja.slaskie.pl/
https://www.silesiakultura.pl/
https://industriada.pl/
https://www.juromania.pl/
https://festiwalgornejodry.pl/
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup

url="https://slaskie.travel/"
classes="container container-templates"
response=requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
div = soup.find_all("div")
div
div[1]

for i in range(200,300):
    print(i, div[i])

for i in range(1350,1500):
    print(i, div[i])


div[1490]
    

def find_name(text, start, end):
    """Finding name in xml file"""
    name_1 = text.index(start)
    name_2 = text.index(end)
    len_name_1 = len(start)
    return text[name_1 + len_name_1 : name_2]

i = 0
list_places=[]
for line in div[1490]:
    line=str(line)
    i+=1
    if "data-title" in line:
        print("yes")
        list_places.append(line)

list_places2 = []
for i in list_places:
    list_places2.append(i.split("data-link"))
    

place_list = []
for place in list_places2:
    for i in place:
        if "data-title" in i:
            place_list.append(i[:i.index("far fa-heart")])



links = []
places = []
for place in place_list:
    links.append(place[2 : place.index("data-title")-2])
    places.append(place[place.index("data-title")+12:-13])

#zborów
opisy = []
for j in links:
    url2="https://slaskie.travel" + j
    classes="descriptionFontText initLinkChecker"
    response=requests.get(url2)
    soup = BeautifulSoup(response.text, "html.parser")
    div2 = soup.find_all("div")

    indeks = links.index(j)

    string_div2 = []
    for i in range(len(div2)):
        string_div2.append(str(div2[i]))
    opisy.append("ATRAKCJA: " + places[indeks])
    description = []
    description=string_div2[1429].split("<p>")
    if "descriptionFontText initLinkChecker" in string_div2[1429]:
        for i in range(len(description)):
            if (description[i][0]!="<") and (description[i][1]!= "<"):
                opisy.append(description[i].replace("</p","").replace("\n", ""))
            #description.append((find_name(i,"<strong>","</strong"), i[i.index("<p>")+3:]))


    description = []   
    description=string_div2[1422].split("<p>")
    if "descriptionFontText initLinkChecker" in string_div2[1422]:
        for i in range(len(description)):
            if (description[i][0:5]!="<span") and (description[i][0:4]!= "<img"):
                opisy.append(description[i].replace("<strong>","").replace("</p>", "").replace("n<ul>\n<li>"," ").replace("\n","").replace("</strong>",""))
            #description.append((find_name(i,"<strong>","</strong"), i[i.index("<p>")+3:]))

#description = list(dict.fromkeys(description))
n=0
for j in opisy:
    if "ATRAKCJA" in j:
        n=n+1
print(n)

df_opisy = pd.DataFrame(opisy)
df_opisy.to_excel(r"C:\Users\igors\OneDrive\Dokumenty\slaskie.xlsx")


#
url2="https://slaskie.travel/poi/15636"
classes="descriptionFontText initLinkChecker"
response=requests.get(url2)
soup = BeautifulSoup(response.text, "html.parser")
div2 = soup.find_all("div")

string_div2 = []
for i in range(len(div2)):
    string_div2.append(str(div2[i]))

for i in range(len(string_div2)):
    if "Zamek Ogrodzieniec to najwi" in string_div2[i]:
        print(i)

string_div2[1409]






######################33
description = []
description2 = []
for i in links:
    url2="https://slaskie.travel" + i
    classes="descriptionFontText initLinkChecker"
    response=requests.get(url2)
    soup = BeautifulSoup(response.text, "html.parser")
    div2 = soup.find_all("div")

    string_div2 = []
    for i in range(len(div2)):
        string_div2.append(str(div2[i]))

    for line in string_div2:
        if "zborów" in line:
            for i in line.split("</p>"):
                if "</h2>" in i:
                    description.append(i)
                    """try:
                        description.append((find_name(i,"<strong>","</strong"), i[i.index("<p>")+3:]))
                    except:
                        pass"""
                if "zb" in i:
                    description2.append(i)
    
description = list(dict.fromkeys(description))

#####################################44
opisy = []
for i in links[:7]:
    url2="https://slaskie.travel" + i
    classes="descriptionFontText initLinkChecker"
    response=requests.get(url2)
    soup = BeautifulSoup(response.text, "html.parser")
    div2 = soup.find_all("div")

    string_div2 = []
    for i in range(len(div2)):
        string_div2.append(str(div2[i]))



    description = []
    description=string_div2[1409].split("descriptionFontText initLinkChecker")
    for i in range(len(description)):
        opisy.append(description[i])
            #description.append((find_name(i,"<strong>","</strong"), i[i.index("<p>")+3:]))

for i in opisy:
    print("                    NOWY                    ", i)
description = list(dict.fromkeys(description))



