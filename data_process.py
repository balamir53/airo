import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from pathlib import Path

TOTAL_ROW_NUMBER = 569839590

user = 'lydiausr'
password = 'lydia2024!'
host = '10.255.0.230'
port = '5432'
db = 'lydia'
connection_string = f"postgresql://{user}:{password}@{host}:{port}/{db}"
engine = create_engine(connection_string)
conn = engine.connect().execution_options(
        stream_results=True)
# query = "SELECT classavailable, deptime, arrtime, brand, price FROM airo.daily_price"
offset = 0
chunksize = 1_000_000
# query = f'select classavailable, deptime, arrtime, brand, price FROM airo.daily_price LIMIT {chunksize} OFFSET {offset}'
query = f'select substring(addedtodownloadqueue ,0,11) addedtodownloadqueue, deptime, recordroute, flightno, min(price) price FROM airo.newview group by deptime, flightno, substring(addedtodownloadqueue ,0,11), recordroute limit {chunksize} offset {offset}'
count = 0
folder_path = f'{Path.home()}\\airo\\data'

# for chunk_dataframe in pd.read_sql_query(query , conn, parse_dates = ['deptime', 'arrtime'], dtype={'price': np.int32}, chunksize=5000000):
# for chunk_dataframe in pd.read_sql_query(query , conn, parse_dates = ['deptime', 'arrtime'], dtype={'price': np.int32}):
for i in range(TOTAL_ROW_NUMBER//chunksize):
        # data = pd.read_sql_query(query , conn, parse_dates = ['deptime', 'arrtime'], dtype={'price': np.int32})
        data = pd.read_sql_query(query , conn, dtype={'price': np.int32})
        file_path = folder_path + '/groupby-part%s.pkl' % (count)
        data.to_pickle(file_path)
        print(f'{file_path} has been written with offset:{offset} with chunksize: {chunksize}')
        count += 1
        offset += chunksize
        query = f'select substring(addedtodownloadqueue ,0,11) addedtodownloadqueue, deptime, recordroute, flightno, min(price) price FROM airo.newview group by deptime, flightno, substring(addedtodownloadqueue ,0,11), recordroute limit {chunksize} offset {offset}'