import requests
from datetime import datetime
from json import dump,load

def get_starting_day():
# Convert user inputted starting day to epoch
    starting = input(str('Please enter startng day as DD.MM.YYYY: '))
    starting = starting.split('.')
    start_day = int(starting[0])
    start_month = int(starting[1])
    start_year = int(starting[2])
    starting_epoch = int(datetime(start_year, start_month, start_day, 0,0).timestamp())

    return starting_epoch

def get_ending_day():
# Convert user inputted ending day to epoch and add 1hr to include last day's value if after midnight

    ending = input(str('Please enter ending day as DD.MM.YYYY: '))
    ending = ending.split('.')
    end_day = int(ending[0])
    end_month = int(ending[1])
    end_year = int(ending[2])
    ending_epoch = int(datetime(end_year, end_month, end_day, 0,0).timestamp()) + 3600

    return ending_epoch


def get_data(file,start,end):
#Get data from coingecko api, ditch marketcap & volume and save it
    
    API_ADDR = f'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=eur&from={start}&to={end}'

    data = requests.get(f'{API_ADDR}').json()
    data = data['prices']

    with open(file, 'w') as f:
        dump(data,f)


def get_midnight_data(file):
# Get only datapoints as close to midnight as possible and save as list

    with open(file) as f:
        data = load(f)

    midnights = []    
    for i in range(len(data)):
        time = str(data[i][0])
        time = datetime.fromtimestamp(int(time[:-3]))
        price = float(data[i][1])
        if time.strftime('%H') == '00':
            midnights.append(price)
    
    with open('mn.json', 'w') as f:
        dump(midnights,f)

    return midnights


def longest_downtrend(prices):
# Calculate longest downtrend
    
    streak = 0
    max_streak = 0
    yesterday = float(0)

    for item in prices:
        if item < yesterday:
            streak = streak + 1

            if streak > max_streak:
                max_streak = streak
        else:
            streak = 0

        yesterday = item

    print(f'Longest streak: {max_streak}')


def main():
    starting_epoch = 1577829600
    ending_epoch = 1580594400
    ending_epoch = ending_epoch +3600
    file = 'retrieved.json'
    get_data(file,starting_epoch, ending_epoch)
    #get_data(file, get_starting_day(), get_ending_day())
    longest_downtrend(get_midnight_data(file))

if __name__ == '__main__':
    main()

    


