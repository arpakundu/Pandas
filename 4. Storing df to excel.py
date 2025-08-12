#storing df to excel
#for that we need to install openpyxl
pip3 install openpyxl 
df.to_excel('new.xlsx', sheet_name='weather_data')
