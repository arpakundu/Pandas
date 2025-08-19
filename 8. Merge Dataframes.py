temperature_df = pd.DataFrame({
    "city" : ["mumbai","delhi","banglore","hyderabad"],
    "temperature" : [32,45,30,40]
})
temperature_df

humidity_df = pd.DataFrame({
    "city" : ["delhi","mumbai","banglore"],
    "humidity" : [68,65,75]
})
humidity_df

#merge two dataframes without explicitly mention index (kind of inner join)
df = pd.merge(temperature_df,humidity_df,on = 'city')
df

#outer join
df = pd.merge(temperature_df,humidity_df,on = 'city',how = 'outer')
df
