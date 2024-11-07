from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

link = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

headers = {
    "Accept-Language": "vi,en-US;q=0.9,en;q=0.8", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36", 
}

response = requests.get(url=link, headers=headers)
website_html = BeautifulSoup(response.text, "html.parser")
price = float(website_html.find(class_="aok-offscreen").getText().split("$")[1])
product_title = " ".join(website_html.find(id="productTitle").getText().split())

buy_price = 130

if buy_price > price:
    body = f"{product_title} is on sale for {price}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(os.environ["email_address"], os.environ["email_password"])
        connection.sendmail(
            from_addr=os.environ["email_address"],
            to_addrs=os.environ["email_address"],
            msg=f"Subject: Amazon Price Alert!\n\n{body}\n{link}".encode("utf-8")
        )
