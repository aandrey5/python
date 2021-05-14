# Replace . to , in df pandas column - IN PLACE
df2['sum_purchase_nds'].str.replace(',' , '.')

# OR

df[list_cols] = df[list_cols].apply(lambda s: s.str.replace(',' , '.')

# View types columns

df1.dtypes
