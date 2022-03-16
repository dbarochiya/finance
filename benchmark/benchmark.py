from jugaad_data.nse import stock_csv, stock_df
import datetime 
import pandas as pd
import json

# Read investment data
file_path = './data.xlsx'
df = pd.read_excel(file_path)
investment_data = df.to_dict('list')

# Download historical index data
df = stock_df(symbol="NIFTYBEES", from_date=datetime.date(2015,1,1),to_date=datetime.date(2021,9,8), series="EQ")
index_data = df[['DATE','CLOSE']].to_dict('list')
for i in range(len(index_data['DATE'])) :
    index_data['DATE'][i] = index_data['DATE'][i].date()


def getClosePrice(input_date):
    date_time_obj = input_date.date()
    count = 0 
    price = -1
    while True:
        if date_time_obj in index_data['DATE']:
            index = index_data['DATE'].index(date_time_obj)
            price = index_data['CLOSE'][index]
            break
        else :
            count += 1 
            date_time_obj -= datetime.timedelta(days=1)
    
    # if(count > 0) :
    #     print('adjusted on ', date_time_obj, count)
    return price

total_lots = 0 
for i in range(len(investment_data['Date'])):    
    close_price = getClosePrice(investment_data['Date'][i])
    amount_int = float (investment_data['Amount'][i])
    allotted_lots = amount_int / close_price
    total_lots += allotted_lots

present_day = datetime.datetime.now()
present_value = getClosePrice(present_day) *  total_lots
print('total lots : ', total_lots)
print('valuations : ', present_value)