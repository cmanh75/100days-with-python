import requests
from twilio.rest import Client
from account import account_sid, auth_token, STOCK_API_KEY, NEWS_API_KEY, whatsapp_number, my_number

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_END_POINT = "https://newsapi.org/v2/everything"

parameter = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": STOCK_API_KEY,
}

data = requests.get(url=STOCK_ENDPOINT, params=parameter)
data.raise_for_status()
json_data = data.json()[f"Time Series ({parameter["interval"]})"]
data_list = [value for (key, value) in json_data.items()]

newest_data_closing_price = float(data_list[0]["4. close"])
second_newest_data_closing_price = float(data_list[1]["4. close"])

difference = float(abs(newest_data_closing_price - second_newest_data_closing_price))
diff_percent = difference / newest_data_closing_price * 100

if diff_percent > 0.01:
    news_param = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
    }
    news_data = requests.get(url=NEWS_END_POINT, params=news_param)
    three_articles = news_data.json()["articles"][:3]
    formatted_articles = [f"Headlines: {article['title']}. \n Brief: {article['description']}" for article in three_articles]

    client = Client(account_sid, auth_token)

    for article in formatted_articles:
        message = client.messages.create(
            from_=f"whatsapp:{whatsapp_number}",
            body=article,
            to=f"whatsapp:{my_number}",
        )