import pandas as pd
import requests


def get_url_original(from_currency, to_currency, amount):
    return f"https://www.xe.com/currencyconverter/convert/?Amount={amount}&From={from_currency}&To={to_currency}"


def get_url_exchange_rates(from_currency, to_currency=None, amount=None):
    return f"https://api.exchangeratesapi.io/latest?base={from_currency}"


df = pd.read_excel('Data Conversion.xlsx', sheet_name='Sheet1')
df_list = df.values.tolist()
# print("----------------LIST CONVERTED-----------------")
# print(df_list)
# print("-----------------------------------------------")

rates_list = []
for i in df_list:
    response = requests.get(get_url_exchange_rates(from_currency=i[1])).json()
    try:
        rate = response["rates"]["INR"]
    except KeyError:
        rate = 0
    # print(response)
    rates_list.append(i[0]*rate)

# print("----------------RATE LIST----------------------")
# print(rates_list)
# print("-----------------------------------------------")

df["Converted Amount"] = rates_list
df.to_excel('Data Conversion.xlsx', sheet_name='Sheet1')
