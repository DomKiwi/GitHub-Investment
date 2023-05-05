import cryptocompare
import requests
import time
import datetime
import typing
import os
from typing import Union, Optional, List, Dict

cryptocompare.cryptocompare._set_api_key_parameter('c85c3b2f3587434f246f8bdac14aada50a7c24651c172b7b09c0d0dedd349f2e')

coinList = cryptocompare.get_coin_list(format=True)
print(coinList)

# cryptocompare.get_price('BTC')
# # or
# cryptocompare.get_price('BTC', currency='USD', full=True)
# # or
# cryptocompare.get_price(['BTC', 'ETH'], ['EUR', 'GBP'])

# {'BTC': {'EUR': 3709.04, 'GBP': 3354.78},
#  'ETH': {'EUR': 258.1, 'GBP': 241.25}}



#Historical Prices
# pass either datetime or time instance
cryptocompare.get_historical_price('XMR', timestamp=datetime.datetime(2017,6,6), exchange='CCCAGG')
# or
cryptocompare.get_historical_price('XMR', 'EUR', datetime.datetime(2017,6,6))

#DAY
cryptocompare.get_historical_price_day('BTC', currency='EUR')
cryptocompare.get_historical_price_day('BTC', currency='EUR', limit=30)
cryptocompare.get_historical_price_day('BTC', 'EUR', limit=24, exchange='CCCAGG', toTs=datetime.datetime(2019,6,6))
# or
cryptocompare.get_historical_price_day('BTC', 'EUR', limit=24, exchange='CCCAGG', toTs=datetime.datetime(2019,6,6))

#HOUR
cryptocompare.get_historical_price_hour('BTC', currency='EUR')
cryptocompare.get_historical_price_hour('BTC', currency='EUR', limit=24)
cryptocompare.get_historical_price_hour('BTC', 'EUR', limit=24, exchange='CCCAGG')
cryptocompare.get_historical_price_hour('BTC', 'EUR', limit=24, exchange='CCCAGG', toTs=datetime.datetime(2019,6,6,12))
# or
cryptocompare.get_historical_price_hour('BTC', 'EUR', limit=24, exchange='CCCAGG', toTs=datetime.datetime(2019,6,6))

#MINUTE
cryptocompare.get_historical_price_minute('BTC', currency='EUR')
cryptocompare.get_historical_price_minute('BTC', currency='EUR', limit=1440)
cryptocompare.get_historical_price_minute('BTC', 'EUR', limit=24, exchange='CCCAGG', toTs=datetime.datetime.now())

#AVERAGE
cryptocompare.get_avg('BTC', currency='EUR', exchange='Kraken')
# {
# 'MARKET': 'CUSTOMAGG',
# 'FROMSYMBOL': 'BTC',
# 'TOSYMBOL': 'EUR',
# 'FLAGS': 0,
# 'PRICE': 3610,
# 'LASTUPDATE': 1503066719,
# 'LASTVOLUME': 0.5,
# 'LASTVOLUMETO': 1805,
# 'LASTTRADEID': 1503066719.7584,
# 'VOLUME24HOUR': 12614.509997469995,
# 'VOLUME24HOURTO': 46397723.00499387,
# 'OPEN24HOUR': 3847.9,
# 'HIGH24HOUR': 3848.96,
# 'LOW24HOUR': 3555,
# 'LASTMARKET': 'Kraken',
# 'CHANGE24HOUR': -237.9000000000001,
# 'CHANGEPCT24HOUR': -6.182593102731363
# }

#EXCHANGES
cryptocompare.get_exchanges()

#PAIRS
cryptocompare.get_pairs()
pairs = cryptocompare.get_pairs(exchange='Kraken')
