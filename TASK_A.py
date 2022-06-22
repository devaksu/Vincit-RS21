from datetime import datetime

def get_price_data(dataset, diff:int) -> list:
# Make list of just prices depending on data provided by Coingecko API

    data = dataset['prices']
    prices_list = []

    if diff < 90:   # Coingecko API provides hourly data for 90 days
        for i in range(len(data)):
            time = str(data[i][0])
            time = datetime.fromtimestamp(int(time[:-3]))   # Slice Coingecko's epoch
            price = float(data[i][1])
            if time.hour == 0:
                prices_list.append(price)
    else:
        for i in range(len(data)):
            price = float(data[i][1])
            prices_list.append(price)

    return prices_list


def longest_downtrend(prices:list) -> None:
# Calculate if today's price is smaller than yesterday's
    
    current_streak = 0
    max_streak = 0
    yesterday = float(0)

    for price in prices:
        if price < yesterday:
            current_streak = current_streak + 1
            if current_streak > max_streak:     # If current streak is longer than previous longest -> new longest streak
                max_streak = current_streak
        
        else:
            current_streak = 0      # If prices are higher than yesterday's downtrend is gone

        yesterday = price   # Finally set today's price as a yesterday's value for next iteration

    print(f'Longest downtrend: {max_streak}')
