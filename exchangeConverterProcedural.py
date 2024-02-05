import requests
import csv 
import datetime
import sys

base_url = "https://openexchangerates.org/api/latest.json"
app_id = '07e863ba70934494bf190c60aebc7f96'
file_name = 'day_rates.csv'
currencies_list = ['AUD','CAD','CHF','CNH','EUR','GBP','HKD','JPY','NZD','USD']


def get_rate(currencies,api_key):
    url = base_url+'?app_id='+api_key+'&symbols='+','.join(currencies)
    try:
        response = requests.get(url)
        response.raise_for_status()
        #response_dict = response.json()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(err.args[0])
        sys.exit(1)

def csv_out(file_name, currency_data):
    with open(file_name, mode='w') as rates_out:
        rates_write = csv.writer(rates_out,  delimiter=',')
        columns = ['Rate Type', 'Date', 'Currency_From', 'Currency_From_Value', 'Currency_To', 'Currency_To_Value']
        date = datetime.datetime.now().strftime("%x")

        rates_write.writerow(columns)
        for currency in currency_data['rates']:
            rates_write.writerow(["Day rate", date, "USD", 1, currency, currency_data['rates'][currency]])

response_dict = get_rate(currencies_list,app_id)
csv_out(file_name,response_dict)