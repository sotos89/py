import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL = 'https://www.skroutz.gr/s/14357325/%CE%95%CF%80%CE%B1%CE%B3%CE%B3%CE%B5%CE%BB%CE%BC%CE%B1%CF%84%CE%B9%CE%BA%CF%8C-%CE%93%CF%81%CE%B1%CF%86%CE%B5%CE%AF%CE%BF-Senior-180x75x75cm-030-000007.html'
# URL = 'https://www.skroutz.gr/s/18617547/%CE%93%CF%81%CE%B1%CF%86%CE%B5%CE%AF%CE%BF-Place-140x70x75cm-24-0487.html/'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

def check_price():
    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    productName = soup.find("h1", {"class": "page-title"}).get_text()
    # shopName = soup.find("div", {"class": "shop-name"}).get_text()
    getprice = soup.find("li", {"class": "selected card card-variant with-image"}).get_text()
    test = soup.find("span", {"class": "price-details"}).get_text()
    one, price, thre = getprice.split()
    value = price.replace(",",".")
    converted_price = float(value[0:5])

    if(converted_price < 200):
        send_email()

    print(price)
    print(converted_price)

    # print("Κατάστημα: ", shopName)
    print("Προϊόν: ", productName.strip())
    print("Τιμή: ", price.strip())
    print(test.strip())


    if(converted_price < 50):
        send_email()


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('john.ce9@gmail.com', 'ljpovhtqcsicrfmt')

    subject = 'Hey the price fell down!!'
    body = "Check the link: "+ URL+ ""
    msg = f"Subject : {subject}\n\n{body}"

    server.sendmail(
        'john.ce9@gmail.com',
        'janis_s89@hotmail.com',
        msg
    )
    print("Email has been send!!")
    server.quit()

while(True):
    check_price()
    time.sleep(60 * 60 * 6)