import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport

df=pd.read_excel("Hindalco.xlsx")
# print(df)



# generate a report
profile=ProfileReport(df,title="Data")
profile.to_file(output_file="hindalco.html")