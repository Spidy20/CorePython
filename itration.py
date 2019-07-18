import quandl
quandl.ApiConfig.api_key = 'cEwafLSxcxfDwzNREWup'
k = quandl.get('NSE/TITAN')

import pandas as pd
data = pd.DataFrame(k)
data.to_csv('DELL.csv')
print(k)