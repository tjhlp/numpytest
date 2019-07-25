import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

web_stats = {'Day': [1, 2, 3, 4, 5],
             'Visitors': [31, 32, 33, 34, 35],
             'Bounce Rate': [61, 62, 63, 46, 65],
             }

df = pd.DataFrame(web_stats)
# print(df.tail(2))
df.set_index('Day', inplace=True)
print(df)
df['Visitors'].plot()
plt.show()
df.plot()
plt.show()
