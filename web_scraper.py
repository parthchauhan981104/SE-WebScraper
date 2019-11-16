# ---------------------------------------------------IMPORTS------------------------------------------------------------

import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import pprint
import re
from selenium import webdriver
import sqlite3
from time import sleep

# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------------------SCRAPER CLASS CODE STARTS-------------------------------------------------
class Scraper(object):
    def __init__(self):
        self.ua = UserAgent()
        self.header = {'user-agent': self.ua.chrome}
        self.init_db()

    # ----------------------------------------------DATABASE CODE STARTS------------------------------------------------

    def init_db(self):

        conn = sqlite3.connect('ws.db')
        print("Opened database successfully")

        # conn.execute('''DROP TABLE IF EXISTS COMPANY;''')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS USERS(
                         ID INTEGER PRIMARY KEY NOT NULL,
                         NAME           TEXT    NOT NULL,
                         USERNAME       CHAR(50),
                         PASSWORD         CHAR(50));''')
        print("Table created successfully")

        cur.execute("INSERT INTO USERS (NAME,USERNAME,PASSWORD) \
                      VALUES ('Paul', 'California', 'lala' )");

        cur.execute("INSERT INTO USERS (NAME,USERNAME,PASSWORD) \
                      VALUES ('Allen', 'Texas', 'ljwdsn' )");

        cur.execute("INSERT INTO USERS (NAME,USERNAME,PASSWORD) \
                      VALUES ('Teddy', 'Norway', 'kasd' )");

        cur.execute("INSERT INTO USERS (NAME,USERNAME,PASSWORD) \
                      VALUES ('Mark', 'Rich-Mond ', 'kadh' )");

        conn.commit()
        print("Records created successfully")

        cursor = conn.execute("SELECT id, name, username, password from USERS")
        for row in cursor:
            print("ID = ", row[0])
            print("NAME = ", row[1])
            print("USERNAME= ", row[2])
            print("PASSWORD = ", row[3], "\n")

        print("Operation done successfully")

        conn.close()

    # -----------------------------------------------DATABASE CODE ENDS-------------------------------------------------

    # -------------------------------------------SNU Mess Menu Scraper - START------------------------------------------
    def mess_menu(self):

        page = requests.get('http://messmenu.snu.in/messMenu.php', timeout=3)

        # Extracting the source code of the page.
        data = page.text
        # pprint.pprint(page.text)

        # Passing the source code to Beautiful Soup to create a BeautifulSoup object for it.
        soup = BeautifulSoup(data, 'html.parser')
        # print(soup.prettify())

        # menu date
        date = soup.find('td', class_="center").label.text.strip()
        pprint.pprint(date)

        dh1_breakfast = []
        dh1_lunch = []
        dh1_dinner = []
        dh2_breakfast = []
        dh2_lunch = []
        dh2_dinner = []
        i = 1

        for p in soup.find_all('td', class_="", limit=6):
            if i == 1:
                dh1_breakfast = p.text.replace(u'\xa0', u'*').replace(u'\n', u'*').replace(u'\r', u'*').split("*")
                dh1_breakfast[:] = (value.strip() for value in dh1_breakfast if value != "" if value != " ")
                i += 1

            elif i == 2:
                dh1_lunch = p.text.replace(u'\xa0', u'*').replace(u'\n', u'*').replace(u'\r', u'*').split("*")
                dh1_lunch[:] = (value.strip() for value in dh1_lunch if value != "" if value != " ")
                i += 1

            elif i == 3:
                dh1_dinner = p.text.replace(u'\xa0', u'*').replace(u'\n', u'*').replace(u'\r', u'*').split("*")
                dh1_dinner[:] = (value.strip() for value in dh1_dinner if value != "" if value != " ")
                i += 1

            elif i == 4:
                dh2_breakfast = p.text.replace(u'\xa0', u'*').replace(u'\n', u'*').replace(u'\r', u'*').split("*")
                dh2_breakfast[:] = (value.strip() for value in dh2_breakfast if value != "" if value != " ")
                i += 1

            elif i == 5:
                dh2_lunch = p.text.replace(u'\xa0', u'*').replace(u'\n', u'*').replace(u'\r', u'*').split("*")
                dh2_lunch[:] = (value.strip() for value in dh2_lunch if value != "" if value != " ")
                i += 1

            elif i == 6:
                dh2_dinner = p.text.replace(u'\xa0', u'*').replace(u'\n', u'*').replace(u'\r', u'*').split("*")
                dh2_dinner[:] = (value.strip() for value in dh2_dinner if value != "" if value != " ")
                i += 1

            elif i == 7:
                break

        print(dh1_breakfast)
        print(dh1_lunch)
        print(dh1_dinner)
        print(dh2_breakfast)
        print(dh2_lunch)
        print(dh2_dinner)

    # ---------------------------------------------Mess Menu Scraper - END----------------------------------------------

    # -----------------------------------------Brainy Quote Scraper - START---------------------------------------------
    def quote(self):

        page = requests.get('https://www.brainyquote.com/quote_of_the_day', timeout=3)

        # Extracting the source code of the page.
        data = page.text
        # pprint.pprint(page.text)

        # Passing the source code to Beautiful Soup to create a BeautifulSoup object for it.
        soup = BeautifulSoup(data, 'html.parser')
        # print(soup.prettify())

        # quote date
        date = soup.find('div', class_="qotdSubt").text.strip()
        pprint.pprint(date)

        quote_of_the_day = soup.find('div', class_="clearfix").text.strip().split("\n")
        quote_of_the_day[:] = (value.strip() for value in quote_of_the_day if value != "" if value != " ")
        pprint.pprint(quote_of_the_day)

    # -----------------------------------------Brainy Quote Scraper - END-----------------------------------------------

    # ----------------------------------------Times of India Scraper - START--------------------------------------------
    def news(self):

        page = requests.get('https://timesofindia.indiatimes.com/briefs', timeout=3)

        # Extracting the source code of the page.
        data = page.text
        # pprint.pprint(page.text)

        # Passing the source code to Beautiful Soup to create a BeautifulSoup object for it.
        soup = BeautifulSoup(data, 'html.parser')
        # print(soup.prettify())

        all_h = soup.find_all('h2', limit=10)  # 10 headlines
        headlines = {}
        base_url = 'https://timesofindia.indiatimes.com'
        for h in all_h:
            headlines.update({h.text: base_url + h.a['href']})
        pprint.pprint(headlines)

    # ----------------------------------------Times of India Scraper - END----------------------------------------------

    # ------------------------------------------IMDB Scraper - START----------------------------------------------------
    def movie(self):

        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)

        movie_name = "blackkklansman"
        driver.get('https://www.imdb.com/find?q=' + movie_name.replace(" ", "+"))

        base_url = 'https://www.imdb.com'
        movie = {}

        soup = BeautifulSoup(driver.page_source, 'lxml')
        tr = soup.find_all('tr', limit=1, class_="findResult odd")
        for x in tr:
            movie.update({'movie_link': base_url + x.a['href']})

        driver.get(movie['movie_link'])
        soup = BeautifulSoup(driver.page_source, 'lxml')
        div_rating = soup.find_all('div', limit=1, class_="ratingValue")
        for div in div_rating:
            movie.update({'movie_rating': div.strong['title']})

        div_subtext = soup.find_all('div', limit=1, class_="subtext")
        for div in div_subtext:
            h1 = soup.h1
            siblings = [sib for sib in h1.next_siblings if sib != '\n']
            # print(siblings)
            texts = []
            for sib in siblings:
                for x in sib.text.lstrip().rstrip().replace("\n", "").split("|"):
                    texts.append(x.strip())
            # print(texts)
            movie.update({'content_rating': texts[0]})
            movie.update({'movie_length': texts[1]})
            movie.update({'genre': texts[2]})
            movie.update({'release_info': texts[3]})

        div_summary = soup.find_all('div', limit=1, class_="summary_text")
        for div in div_summary:
            movie.update({'summary': div.text.lstrip().rstrip()})

        div_meta = soup.find_all('div', limit=1, class_="metacriticScore score_favorable titleReviewBarSubItem")
        for div in div_meta:
            movie.update({'metacritic score': div.text.lstrip().rstrip()})

        texts = []
        h4_credits = soup.find_all('h4', class_="inline", limit=3)
        for h in h4_credits:
            siblings = [sib for sib in h.next_siblings if sib != '\n' if sib != ' ']
            # print(siblings)
            s = ''
            for sib in siblings:
                # print(sib)
                s += sib.string.strip()
            texts.append(s)
            # print(texts)
        movie.update({'directors': texts[0]})
        regex = re.compile('\\|\w more credits»|\\|\w more credit»')
        movie.update({'writers': regex.sub("", texts[1])})
        movie.update({'stars': texts[2].replace('|See full cast & crew»', "")})

        pprint.pprint(movie)

        sleep(2)

        driver.close()

    # -------------------------------------------IMDB Scraper - END-----------------------------------------------------


# --------------------------------------------SCRAPER CLASS CODE ENDS---------------------------------------------------

if __name__ == '__main__':
    sc = Scraper()
    sc.movie()
    sc.mess_menu()
    sc.news()
    sc.quote()
