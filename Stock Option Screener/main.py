import pandas as pd
from yahoo_fin import options


stock="AAPL"

print(options.get_expiration_dates(stock))


pd.set_option('display.max_columns',None)
# chain=options.get_options_chain(stock,'August 20, 2021')
# chain=options.get_puts(stock,'August 20, 2021')
# print(chain)

chain=options.get_calls(stock,'August 20, 2021')

# print(chain['calls'])

chain=(chain[chain['Implied Volatility'] < 100] )

print(chain[chain['Ask'] < 100][chain['Strike']<100]) 