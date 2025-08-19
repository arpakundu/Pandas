#Numerical indexing (.loc vs iloc)
df = pd.DataFrame([1,2,3,4,5,6,7,8,9,19],index = [49,48,47,46,45,1,2,3,4,5])
df

df.loc[46] #give value as per the given index
df.iloc[:2] #give value as per the row wise index
