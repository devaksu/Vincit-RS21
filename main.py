from TASK_A import get_price_data, longest_downtrend
from TASK_B import get_trading_vol_data, highest_vol
from TASK_C import best_case, clean_price_data
from datetime import datetime,timedelta
import requests

def get_starting_day() -> tuple[datetime, int]:
# Format user inputted starting day to datetime and epoch
    
    starting = input(str('Please enter starting day as DD.MM.YYYY: '))
    start_dt = datetime.strptime(starting, '%d.%m.%Y')
    start_epoch = int(start_dt.timestamp())

    return start_dt, start_epoch


def get_ending_day() -> tuple[datetime, int]:
# Format user inputted ending day to datetime and epoch

    ending = input(str('Please enter ending day as DD.MM.YYYY: '))
    end_dt = datetime.strptime(ending, '%d.%m.%Y')
    end_epoch = int(end_dt.timestamp()) + 3600 # add 1hr to include last day's value if after midnight

    return end_dt, end_epoch


def date_diff(start:datetime, end:datetime) -> int:
# Calculate difference between start and end for API's behaviour

    d_diff = end - start
    if d_diff > timedelta(days=0):
        return d_diff.days
    else:
        raise ValueError("Give proper dates")


def main() -> None:
    
    start_day, start_epoch = get_starting_day()
    end_day, end_epoch = get_ending_day()
    difference = date_diff(start_day, end_day)
    
    api_address = f'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=eur&from={start_epoch}&to={end_epoch}'
    data = requests.get(f'{api_address}').json()
  
    # TASK A Get longest downtrend
    price_data = get_price_data(data, difference)
    longest_downtrend(price_data)

    # TASK B get maximum trading volume in euro
    vol_data = get_trading_vol_data(data, difference)
    highest_vol(vol_data)

    # TASK C get best dates to buy and sell bitcoin
    clean_data = clean_price_data(data, difference)
    best_case(clean_data) 


if __name__ == '__main__':
    main()


