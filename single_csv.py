import pandas as pd

# Target Websiste - https://www.football-data.co.uk/data.php

# reading 1 csv file from the webiste

df_premier_26 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2526/E0.csv')

# show dataframes
print(df_premier_26)

# rename columns
df_premier_26.rename(columns={'FTHG': 'home_goals', 'FTAG': 'away_goals'}, inplace=True)

# show dataframes
print(df_premier_26.head())