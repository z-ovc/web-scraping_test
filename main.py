import requests
import selectorlib
import smtplib, ssl
import os

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

    receiver = "statistiker74@gamil.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context = context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)                                                                                                                                                                                                                                                               

def store(extracted):
    with open("data.txt","a") as file:
        file.write(extracted + "\n")

def read(extracted):
    with open("data.txt","r") as file:
        return file.read()


if __name__ == "__main__":
    scraped = scrape(url = URL)
    extracted = extract(scraped)
    print(extracted)
    
    content = read(extracted)
    if extracted != "No upcoming tours":
        if extracted not in content:
            store(extracted)
            send_email(message = extracted)
            print("mail sent")



