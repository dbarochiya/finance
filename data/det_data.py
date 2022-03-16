import requests
import json
import time
API = "X4P0054QMBXB255H"
base_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&apikey=" + API
tickers = ["TATASTEEL","HINDALCO","JSWSTEEL","ADANIPORTS","SBILIFE","BAJAJFINSV","HDFC","IOC","M&M","NTPC","BHARTIARTL","COALINDIA","ULTRACEMCO","ITC","BPCL","ONGC","HDFCBANK","HINDUNILVR","SBIN","TCS","WIPRO","MARUTI","TECHM","BRITANNIA","DRREDDY","ASIANPAINT","SHREECEM","NESTLEIND","INDUSINDBK","HDFCLIFE","LT","TATAMOTORS","GRASIM","CIPLA","HCLTECH","SUNPHARMA","AXISBANK","ICICIBANK","RELIANCE","TITAN","KOTAKBANK","POWERGRID","INFY","DIVISLAB","BAJFINANCE","UPL","EICHERMOT","BAJAJ-AUTO","HEROMOTOCO","TATACONSUM"]
exchange = "BSE"

for ticker in tickers:
    #get data
    time.sleep(15)
    data_url = base_url + '&symbol=' + ticker + '.' + exchange
    response = requests.get(data_url)
    json_obj = response.json()

    #write to file
    data_dir = "/Users/dbarochiya/Desktop/me/workspace/finance/data"
    with open(data_dir + '/' + ticker + '.' + exchange + '.json', 'w') as outfile :
        json.dump(json_obj, outfile) 

# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo
# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=HDFC.BSE&outputsize=full&apikey=X4P0054QMBXB255H