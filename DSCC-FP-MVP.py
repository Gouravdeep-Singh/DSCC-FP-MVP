import pandas as pd
from yahooquery import Ticker
from data_collection import StockData
from data_storage import S3
import json

def readjson(file):
    with open(file,'r') as json_file:
        cred=json.load(json_file)
        return cred
    
if __name__ == "__main__":
    symbols = ['AAPL', '005930.KS']  # Apple and Samsung stock symbols
    start_date = '2021-01-01'
    end_date = '2021-12-31'
    csv_filename = 'stock_data_2021.csv'

    retriever = StockData(symbols, start_date, end_date)
    stock_data = retriever.retrieve_data() #getting the retrived data

    if stock_data is not None:
        retriever.save_to_csv(stock_data, csv_filename)#saving to csv displaying in tabular formar
        
    #reading the json file
    cred=readjson("DSCC-FP-MVP-configuration.json")
    if cred:
        # Extract credentials from the loaded JSON
        aws_access_key = cred["aws_access_key"]
        aws_secret_key = cred["aws_secret_key"]
        bucket_name = cred["bucket_name"]

    s3 = S3(aws_access_key, aws_secret_key, bucket_name)

    # Upload a file
    s3.upload_file("stock_data_2021.csv", "savedfile/stock_data_2021.csv")

    # Download a file
    s3.download_file("savedfile/stock_data_2021.csv", "stock_data_2021.csv")