from datetime import datetime

def get_trading_vol_data(dataset:list, diff:int) -> list:
# Make list of just dates and volumes depending on data provided by Coingecko API

    data = dataset['total_volumes']
    volumes_list = []
    
    if diff < 90:                                               # Check if data is hourly (range under 90 days)
        for i in range(len(data)):
            time_str = str(data[i][0])                          # Get timestamp  
            time = datetime.fromtimestamp(int(time_str[:-3]))   # Slice Coingecko's epoch and make datetime object
            if time.hour == 0:                                  
                volume = float(data[i][1])
                time = time.strftime('%d.%m.%Y')                # Format dt object nicely
                volumes_list.append([time,volume])
    
    else:                                                       # If range over 90, data is daily -> no needs to manipulate
        for i in range(len(data)):
            time = str(data[i][0])
            time = datetime.fromtimestamp(int(time[:-3]))   
            time = time.strftime('%d.%m.%Y')                    
            volume = float(data[i][1])
            volumes_list.append([time,volume])
    
    return volumes_list


def highest_vol(volumes:list) -> None:
# Iterate through list to find day with highest volume and corresponding date
    
    max_vol = float(0)

    for i in range(len(volumes)):
        vol = volumes[i][1]
        if vol > max_vol:
            max_vol = vol
            max_vol_date = volumes[i][0]

    print(f'Maximum trading volume {max_vol:,.0f}€ was in {max_vol_date}')

    