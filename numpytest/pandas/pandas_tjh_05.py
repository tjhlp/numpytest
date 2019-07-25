import pandas as pd

fiddy_states = pd.read_html('../data/List of U.S. states - Simple English Wikipedia, the free encyclopedia.html')
print(fiddy_states[0])
