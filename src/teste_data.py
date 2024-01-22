import pandas as pd

d='2015-01-08 22:44:09'
date=pd.to_datetime(d).date()
print(date)