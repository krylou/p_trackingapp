#initial version 1.0.
import requests
from bs4 import BeautifulSoup


def telegram_bot_sendtext(bot_message):

    bot_token = '2069908837:AAG8j-hfypwDMn_Tdizk4YoS-iFmAW-C6sQ'
    bot_chatID = '-653326421'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


url = 'https://zoommer.ge/apple-iphone-13-128gb-blue'
page = requests.get(url)
#print(page.status_code)
stock = []

soup = BeautifulSoup(page.text, "html.parser")
stock_block=soup.find_all(class_="stock-block")

for data in stock_block:
    if data.find('span') is not None:
        stock.append(data.text)
stock_str = str(stock)
print(stock_str)

en = "Out" in stock_str
ru = "Нет" in stock_str
ge = "არ" in stock_str
print (en, ru, ge)

if en == 1 or ru == 1 or ge == 1:
    actual_stock = "Нет в наличии!"
#    telegram_bot_sendtext(actual_stock + stock_str)
else:
    actual_stock = "Есть в наличии!!"
    telegram_bot_sendtext(actual_stock + stock_str)    
print(actual_stock)