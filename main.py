import requests
import selectorlib
import smtplib, ssl
import os
import time
import sqlite3


connection = sqlite3.connect("dataa.db")

"INSERT INTO events VALUES ('Trigers', 'Triger City', '2088.10.20')"
"SELECT * FROM events WHERE date='2088.10.20'"


URL = "http://programmer100.pythonanywhere.com/tours/"

def scrape(url):
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tour"]
    return value


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "zazaovc44@gmail.com"
    password = "***"

    receiver = "statistiker74@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context = context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)                                                                                                                                                                                                                                                               

def store(extracted):
    row = extracted.split(',')
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES (?,?,?)",row)
    connection.commit()
    

def read(extracted):
    row = extracted.split(',')
    row = [item.strip() for item in row]
    print(row)
    band, city, date = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?",(band,city,date))
    rows = cursor.fetchall()
    return rows

if __name__ == "__main__":
    while True:
        scraped = scrape(url = URL)
        extracted = extract(scraped)
        print(extracted,'*****************************')
        if extracted != "No upcoming tours":
            row = read(extracted)
            if not row:
                if extracted not in row:
                    store(extracted)
                    print("stored************************")
                    send_email(message = extracted)
                    print("mail sent")
            time.sleep(2)



