import pandas as pd
df = pd.read_csv('weather_data_cities.csv')
df

g = df.groupby('city') ##group the data frame on the basis of city column##
g

for city, city_df in g:
    print(city)
    print(city_df)


##get a specific group##
g.get_group('new york')


##find maximum temperature and other attributes of each of the cities ##
print(g.max())
print(g.mean()) #for mean data finding
print(g.describe())
