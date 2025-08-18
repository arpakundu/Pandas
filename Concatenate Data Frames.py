import pandas as pd
india_weather = pd.DataFrame({
    "city" : ["mumbai","delhi","banglore"],
    "temperature" : [32,45,30],
    "humidity" : [80,60,78]
})
india_weather

us_weather = pd.DataFrame({
    "city" : ["new york","chicago","orlando"],
    "temperature" : [21,14,35],
    "humidity" : [68,65,75]
})
us_weather

##concate two dataframes
df = pd.concat([india_weather,us_weather])
df 
##but it gives non continuous index

##to get continuous index
df = pd.concat([india_weather,us_weather],ignore_index=True)
df

##if we want to concat them rowwise 
df = pd.concat([india_weather,us_weather],axis=1)
df
