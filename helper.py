# Replace . to , in df pandas column
df['range'] = df['range'].str.replace(',','-')

# View types columns

df1.dtypes
