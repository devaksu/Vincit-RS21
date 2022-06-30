from datetime import datetime

def clean_price_data(dataset:list, diff:int) -> list:
# Make list of times and prices depending on data provided by Coingecko API

    data = dataset['prices']
    clean_list = []

    if diff < 90:                                           # Check if data is hourly (range under 90 days)
        for i in range(len(data)):
            time = str(data[i][0])
            time = datetime.fromtimestamp(int(time[:-3]))   # Slice Coingecko's epoch and make dt object
            price = float(data[i][1])
            if time.hour == 0:                              # Check if time is midnight
                clean_list.append([time,price])
    else:                                                   # If range over 90, data is daily -> no needs to manipulate
        for i in range(len(data)):
            price = float(data[i][1])
            clean_list.append([time,price])
    
    return clean_list


def best_case(data:list) -> None:
# Look for best profit (sell price - buy price)
    max_profit = 0

    for i in data:
        start_price = i[1]
        start_date = i[0]
        
        for j in data:
            end_price = j[1]
            end_date = j[0]
            price_diff = end_price - start_price
            
            if price_diff > max_profit and end_date > start_date:
                max_profit = price_diff
                buy_date = start_date
                buy_price = start_price
                sell_date = end_date
                sell_price = end_price

    if buy_date < sell_date:
        print(f'Buy {buy_date:%d.%m.%Y} at {buy_price:.2f} and sell {sell_date:%d.%m.%Y} at {sell_price:.2f} for {max_profit:.2f} euros profit')

    else:
        print('No suitable trading opportunities!')
