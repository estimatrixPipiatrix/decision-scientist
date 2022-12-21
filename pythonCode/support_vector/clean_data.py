import pandas as pd

mushrooms = pd.read_csv('mushrooms.csv')

# convert letters to numbers
for n in range(0,mushrooms.shape[1]):
    mushrooms.iloc[:,n] = [ord(x) - 97 \
          for x in mushrooms[mushrooms.columns[n]]]

mushrooms.to_csv('mushrooms_clean.csv',index=False)
