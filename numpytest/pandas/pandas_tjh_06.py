import pandas as pd

df1 = pd.DataFrame({
    'HPI': [80, 85, 88, 85],
    'Int_rate': [2, 3, 4, 4],
    'US_GDP_Thousands': [50, 55, 65, 55]},
    index=[2001, 2002, 2003, 2004])
df2 = pd.DataFrame({
    'HPI': [80, 85, 88, 85],
    'Int_rate': [2, 3, 4, 4],
    'US_GDP_Thousands': [50, 55, 65, 55]},
    index=[2005, 2006, 2007, 2008]
)
df3 = pd.DataFrame({
    'HPI': [80, 85, 88, 85],
    'Unemployment': [2, 3, 4, 4],
    'LOW_GDP_Thousands': [50, 55, 65, 55], },
    index=[2009, 2010, 2011, 2012]
)
# concat = pd.concat([df1, df2])
# print(concat)

# print('-'*50)
#
# df4 = df1.append(df3)
# print(df4)

# 使用pd.merge 能合并相同类型的列表
print(pd.merge(df1, df2, on=['HPI', 'Int_rate']))
