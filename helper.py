# Groupby for text Dataframes

df.groupby(['id'])['lead_id'].apply(','.join).reset_index()


# add new column in dataframe with sourcename for next validation
df.loc[:, 'source'] = source_name



# Divide to many parts as a count of rows in chunk_size

chunk_size=1080000
batch_no=1
for chunk in pd.read_csv('Solopharm.csv',delimiter=";", chunksize=chunk_size, low_memory=False):
    chunk.to_csv('chunk'+str(batch_no)+'.csv',index=False, sep=";")
    batch_no+=1


# Replace . to , in df pandas column - IN PLACE
df2['sum_purchase_nds'].str.replace(',' , '.')

# OR

df[list_cols] = df[list_cols].apply(lambda s: s.str.replace(',' , '.')

# View types columns

df1.dtypes

# SOLVING PROBLEMS WITH CONDA KERNEL                                    
                                    
Install pywin32 using conda install pywin32, and
Uninstall pywin32 using pip uninstall pywin32 - not nessesary
                                    
                                    
                                    
# RUN SQL STATEMENT BY PYTHON / psycopg2
                                    
import psycopg2

q = """
create table log (
       source_launch_id    int
     , target_schema       text
     , target_table        text  
     , target_launch_id    int
     , processed_dttm      timestamp default now()
     , row_count           int
     , duration            interval
     , load_date           date
)
"""


conn_string= "host='192.168.147.128' port=54320 dbname='my_database' user='root' password='postgres'" 
with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
    cursor.execute(q)
