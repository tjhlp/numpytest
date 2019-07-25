import pandas as pd

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states', header=None)
print(fiddy_states)
