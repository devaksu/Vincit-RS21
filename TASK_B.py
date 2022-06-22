from datetime import datetime

def get_trading_vol_data(dataset, diff:int) -> list:
# Make list of just prices depending on data provided by Coingecko API

    data = dataset['total_volumes']
    volumes_list = []
    
    if diff < 90:   # Coingecko API provides hourly data for 90 days
        for i in range(len(data)):
            time_str = str(data[i][0])
            time = datetime.fromtimestamp(int(time_str[:-3]))   # Slice Coingecko's epoch
            if time.hour == 0:
                volume = float(data[i][1])
                time = time.strftime('%d.%m.%Y')
                volumes_list.append([time,volume])
    
    else:
        for i in range(len(data)):
            time = str(data[i][0])
            time = datetime.fromtimestamp(int(time[:-3]))
            time = time.strftime('%d.%m.%Y')
            volume = float(data[i][1])
            volumes_list.append([time,volume])

    return volumes_list



def highest_vol(volumes:list) -> None:
# Calculate if today's price is smaller than yesterday's
    
    max_vol = float(0)

    for i in range(len(volumes)):
        vol = volumes[i][1]
        if vol > max_vol:
            max_vol = vol
            max_vol_date = volumes[i][0]

    print(f'Maximum trading volume {max_vol:,.2f}€ was in {max_vol_date}')

    