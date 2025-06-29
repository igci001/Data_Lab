import os
from fredapi import Fred
import requests
import pandas as pd


pre = "CampusFile_"
hk_p_df = pd.read_stata(f'./panel/{pre}HK_cities.dta')
min = hk_p_df['adat'].min()
max = hk_p_df['adat'].max()

print(min, max)

# FED
fed_api_key = os.environ.get('FedApiKey')

fred = Fred(api_key=fed_api_key)
data = fred.get_series('FEDFUNDS', min, max)
data.to_csv('fed.csv')
print(data)
