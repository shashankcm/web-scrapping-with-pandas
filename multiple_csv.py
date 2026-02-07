import pandas as pd

# https://www.football-data.co.uk/mmz4281/2526/E0.csv
# https://www.football-data.co.uk/mmz4281/2526/E1.csv
# https://www.football-data.co.uk/mmz4281/2526/E2.csv
# https://www.football-data.co.uk/mmz4281/2526/E3.csv
# https://www.football-data.co.uk/mmz4281/2526/EC.csv

root = 'https://www.football-data.co.uk/mmz4281/'
leagues = ['E0', 'E1', 'E2', 'E3', 'EC']
frames = []

for league in leagues:
     df = pd.read_csv(f"{root}2526/{league}.csv", encoding='unicode_escape')
     frames.append(df)

print(len(frames))
print(frames[4])