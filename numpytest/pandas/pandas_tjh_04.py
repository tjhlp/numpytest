import pandas as pd
import quandl

"""
简单使用读取csv函数
df = pd.read_csv('../data/ZILLOW-M1300_MPPRSF.csv', index_col=0)
# df.to_csv('newcsv4.csv', header=False)
df.to_html('example.html')
print(df.head())

"""

# 使用quandl获取网上的数据
with open('QuanlAPIKey.txt', 'r') as Q:
    api_key = Q.read()

df = quandl.get("FMAC/HPI_TX", authtoken=api_key)
print(df.head())
