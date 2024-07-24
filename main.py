import requests
import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "jaedanparsons@gmail.com"
    #password = "eguynewtngwsbnmy"
    password = os.getenv("python_email_news_password")
    #old_password = os.getenv("python_email_password")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, username, message)

topic = "tesla"

api_key = "7dd4541b873c4df4853d279dd12b6e20"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2024-06-24&"
       "sortBy=publishedAt&"
       "apiKey=7dd4541b873c4df4853d279dd12b6e20&"
       "language=en")


get_req = requests.get(url)
content = get_req.json()

message_header = """\
Subject: Today's news from newsapi

Here is the list of articles about Tesla:
"""
article_message = """"""
for article in content['articles'][:20]:
    if article["title"] is not None:
        article_message += (f"\n"
                            f"{article['title']}\n"
                            f"{article['description']}\n"
                            f"{article['url']}\n")

email_message = message_header + article_message
email_message = email_message.encode("utf-8")

send_email(email_message)