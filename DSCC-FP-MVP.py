import pandas as pd
from yahooquery import Ticker
from data_collection import StockData
from prettytable import PrettyTable


if __name__ == "__main__":
    symbols = ['AAPL', '005930.KS']  # Apple and Samsung stock symbols
    start_date = '2021-01-01'
    end_date = '2021-12-31'
    csv_filename = 'stock_data_2021.csv'

    retriever = StockData(symbols, start_date, end_date)
    stock_data = retriever.retrieve_data() #getting the retrived data

    if stock_data is not None:
        retriever.save_to_csv(stock_data, csv_filename)#saving to csv displaying in tabular formar
        
