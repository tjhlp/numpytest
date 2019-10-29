import pandas as pd

with open('./docs_tage.info', 'r', encoding='utf-8') as r:
    contents = r.readlines()

res = []
for content in contents:
    sp = content.split(' ')
    while True:
        try:
            sp.remove('')
        except:
            break

    res.append(sp)

df = pd.DataFrame(res, columns=['id', 'tar', 'time', 'time'])
print(df)
print(df.shape)
input_str = '肺结核病因预防和检查指标'





