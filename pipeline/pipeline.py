import sys
import pandas as pd

month = int(sys.argv[1])

df = pd.DataFrame({ "daiy" : [1,2], "number_passangers" : [3,4]})
df['month'] = month
print(df.head())

df.to_parquet(f'output_{month}.parquet')

