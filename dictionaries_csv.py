import pandas as pd

dict_countries = {
    'Spanish La Liga': 'SP1',
    'Spanish Segunda Division': 'SP2',
    'Germany Bundesliga': 'D1',
    'English Premier League': 'E0',
    'English League 1': 'E2',
    'English League 2': 'E3',
}

root = 'https://www.football-data.co.uk/mmz4281/'
#leagues = ['E0', 'E1', 'E2', 'E3', 'EC']
dict_historical_data = {}

for league in dict_countries:
    frames = []
    for season in range(20, 25):
        season_name = str(season) + str(season + 1)
        df = pd.read_csv(f"{root}{season_name}/{dict_countries[league]}.csv", encoding='unicode_escape')
        df.insert(1, 'season', season)
        frames.append(df)
    df_concat = pd.concat(frames)
    dict_historical_data[league] = df_concat

print(dict_historical_data.keys())
print(dict_historical_data['English Premier League'])
