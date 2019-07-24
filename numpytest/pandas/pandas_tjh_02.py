import datetime
import pandas_datareader.data as web
import fix_yahoo_finance as yf
yf.pdr_override()

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)
df = web.get_data_yahoo('AAPL', start, end)
print(df)
