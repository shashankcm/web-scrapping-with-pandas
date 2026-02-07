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
    for season in range(20, 25):
        season_name = str(season) + str(season + 1)
        df = pd.read_csv(f"{root}{season_name}/{league}.csv", encoding='unicode_escape')
        df.insert(1, 'season', season)
        frames.append(df)


print(len(frames))
print(frames[24])

