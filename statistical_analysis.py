import pandas as pd

class Stats:
    def maximum(seld,df):
        return df.max()
    
    def minimum(self,df):
        return df.min()
    
    def central_tendency(self,df):
        mean=df.mean(numeric_only=True)
        median=df.median(numeric_only=True)
        return mean,median
    
df=pd.read_csv("stock_data_2021.csv")
s=Stats()
#max values
print(s.maximum(df))
#min values
print(s.minimum(df))
#central tendency
print(s.central_tendency(df))