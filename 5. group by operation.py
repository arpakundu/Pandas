##group by operation##

import pandas as pd
df = pd.read_csv('weather_data_cities.csv')
df

g = df.groupby('city') ##group the data frame on the basis of city column##
g

for city, city_df in g:
    print(city)
    print(city_df)
