#---------------------------------------------------IMPORTS-------------------------------------------------------------
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import pprint
import re
#-----------------------------------------------------------------------------------------------------------------------

#---------------------------------------------Mess Menu Scraper - START-------------------------------------------------
ua = UserAgent()

header = {'user-agent':ua.chrome}

page = requests.get('http://messmenu.snu.in/messMenu.php',timeout=3)

# Extracting the source code of the page.
data = page.text
#pprint.pprint(page.text)

# Passing the source code to Beautiful Soup to create a BeautifulSoup object for it.
soup = BeautifulSoup(data, 'html.parser')
#print(soup.prettify())

# menu date
date = soup.find('td', class_="center").label.text.strip()
pprint.pprint(date)


dh1_breakfast = []
dh1_lunch = []
dh1_dinner = []
dh2_breakfast = []
dh2_lunch = []
dh2_dinner = []
i=1

for p in soup.find_all('td', class_="", limit=6):
    if i==1:
        dh1_breakfast = p.text.replace(u'\xa0', u'*').replace(u'\n', u'*').replace(u'\r', u'*').split("*")
        dh1_breakfast[:] = (value.strip() for value in dh1_breakfast if value != "" if value != " ")
        i+=1

    elif i==2:
        dh1_lunch = p.text.replace(u'\xa0', u'*').replace(u'\n', u'*').replace(u'\r', u'*').split("*")
        dh1_lunch[:] = (value.strip() for value in dh1_lunch if value != "" if value != " ")
        i+=1

    elif i==3:
        dh1_dinner = p.text.replace(u'\xa0', u'*').replace(u'\n', u'*').replace(u'\r', u'*').split("*")
        dh1_dinner[:] = (value.strip() for value in dh1_dinner if value != "" if value != " ")
        i+=1

    elif i==4:
        dh2_breakfast = p.text.replace(u'\xa0', u'*').replace(u'\n', u'*').replace(u'\r', u'*').split("*")
        dh2_breakfast[:] = (value.strip() for value in dh2_breakfast if value != "" if value != " ")
        i+=1

    elif i==5:
        dh2_lunch = p.text.replace(u'\xa0', u'*').replace(u'\n', u'*').replace(u'\r', u'*').split("*")
        dh2_lunch[:] = (value.strip() for value in dh2_lunch if value != "" if value != " ")
        i+=1

    elif i==6:
        dh2_dinner = p.text.replace(u'\xa0', u'*').replace(u'\n', u'*').replace(u'\r', u'*').split("*")
        dh2_dinner[:] = (value.strip() for value in dh2_dinner if value != "" if value != " ")
        i+=1

    elif i==7:
        break

print(dh1_breakfast)
print(dh1_lunch)
print(dh1_dinner)
print(dh2_breakfast)
print(dh2_lunch)
print(dh2_dinner)

#---------------------------------------------Mess Menu Scraper - END---------------------------------------------------