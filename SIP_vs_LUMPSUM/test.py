import json
import math
import random
import matplotlib.pyplot as plt

data_dir = "/Users/dbarochiya/Desktop/me/workspace/finance/data"
tickers = ["TATASTEEL","HINDALCO","JSWSTEEL","ADANIPORTS","SBILIFE","BAJAJFINSV","HDFC","IOC","M&M","NTPC","BHARTIARTL","COALINDIA","ULTRACEMCO","ITC","BPCL","ONGC","HDFCBANK","HINDUNILVR","SBIN","TCS","WIPRO","MARUTI","TECHM","BRITANNIA","DRREDDY","ASIANPAINT","SHREECEM","NESTLEIND","INDUSINDBK","HDFCLIFE","LT","TATAMOTORS","GRASIM","CIPLA","HCLTECH","SUNPHARMA","AXISBANK","ICICIBANK","RELIANCE","TITAN","KOTAKBANK","POWERGRID","INFY","DIVISLAB","BAJFINANCE","UPL","EICHERMOT","BAJAJ-AUTO","HEROMOTOCO","TATACONSUM"]
ticker = tickers[random.randint(0,len(tickers))]
exhange = "BSE"
data_file = open(data_dir + '/' + ticker + '.' + exhange + '.json')
mydata = json.load(data_file)

n = len(mydata["Time Series (Daily)"])
sigma = 0

changes = { }

for day in mydata["Time Series (Daily)"]:
    day_close = float(mydata["Time Series (Daily)"][day]["4. close"])
    day_open = float(mydata["Time Series (Daily)"][day]["1. open"])
    day_change = day_close - day_open
    
    if day_change in changes:
        changes[day_change] += 1
    else :
        changes[day_change] = 1

    sigma += day_change

sigma = sigma / n
print("sigma : ",sigma)
total_variance = 0
std = 0
for day in mydata["Time Series (Daily)"]:
    day_close = float(mydata["Time Series (Daily)"][day]["4. close"])
    day_open = float(mydata["Time Series (Daily)"][day]["1. open"])
    day_change = day_close - day_open 
    variance = sigma - day_change
    variance = variance ** 2
    total_variance += variance

std = math.sqrt(total_variance / (n-1))
print("std : ",std)
plt.plot(*zip(*sorted(changes.items())))
plt.title(ticker)
plt.show()


#find SIP return
def get_sip_return(sip,start):
    pass

#find lumpsum return (< 10%)
def get_lumpsum_return():
    pass