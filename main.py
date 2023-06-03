import requests
import sqlite3
from bs4 import BeautifulSoup
from time import sleep
from random import randint

url = 'https://alta.ge/phones-and-communications/smartphones.html'
page_counter = 1

#ვქმნი SQL ბაზას
conn = sqlite3.connect('phonesalta.db')
c = conn.cursor()
c.execute('''CREATE TABLE phones
                  (id INTEGER PRIMARY KEY,
                  name TEXT,
                  price TEXT)''')


#ამ კოდს შეცდომების გამო ვიყენებდი თეიბლის წასაშლელად
# c.execute("DROP TABLE IF EXISTS phones")


#შევქმენი მონაცემების შეტანის ფუნქცია სიქუელში
def insert_data(name, price):
    c.execute("INSERT INTO phones (name, price) VALUES (?, ?)", (name, price))


while url and page_counter < 6:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    #მოგვაქვს ტელეფონების სახელები და ფასები
    all_phones_names = soup.find_all('div', class_='ty-grid-list__item-name')
    all_phones_prices = soup.find_all('span', class_='ty-price-num')
    #რახან ერთის ფასი დივში წერია, მეორე კი სპანში, ორი ცალკეული ფუნქციის მაგივრად ვამჯობინე
    #ციკლი ორივეზე მეწარმოებინა ერთად, ზიპ ჩაშენებული ფუნქციის გამოყენებით
    for name, price in zip(all_phones_names, all_phones_prices):
        title = name.a.text
        price_text = price.text
        print(title, price_text)
        insert_data(title, price_text)



    #ვპოულობთ შემდეგი გვერდის მისამართს, HTML-ში ვწვდები ალტას ბათონს, რომელსაც გადაყავს შემდეგ გვერდზე მომხმარებელი
    #ხოლო შემდეგი გვერდის ლინკი კი href-ში წერია, შეიძლებოდა ამის გაკეთება replace- მეთოდითაც, თუმცა ვფიქრობ ასე უფრო
    #მოსახერხებელია
    pagination = soup.find('a', class_='ty-pagination__item ty-pagination__btn ty-pagination__next cm-history cm-ajax')
    if pagination:
        url = pagination.get('href')
    else:
        url = None

    #ვზრდით ფეიჯების მთვლელს თითო იტერაციაზე ერთით
    page_counter += 1

    #ვიყენებთ დაყოვნებას, რომ სერვერი არ გადავტვირტოთ
    sleep(randint(15, 20))

#ცვლილებების ასახვის შემდეგ ვხურავ ბაზასთან კავშირს.
conn.commit()
conn.close()