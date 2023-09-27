import pandas as pd
from yahooquery import Ticker

class StockData:
    def __init__(self, symbols, start_date, end_date):
        self.symbols = symbols #defining the variables for collecting data
        self.start_date = start_date
        self.end_date = end_date

    def retrieve_data(self):
        data = []
        for symbol in self.symbols:
            try:
                ticker = Ticker(symbol)#getting data for Apple and samsung ticker
                hist_data = ticker.history(start=self.start_date, end=self.end_date)
                if not hist_data.empty:
                    data.append(hist_data.assign(Symbol=symbol))  # Add 'Symbol' column to match column names avoiidng concatinatioin error
            except Exception as e:
                print(f"Error retrieving data for {symbol}: {str(e)}")

        if not data:
            print("No data retrieved.")
            return None

        return pd.concat(data)

    def save_to_csv(self, data, filename):
        if data is not None:
            data.to_csv(filename)
            print(f"Data saved to {filename}")
