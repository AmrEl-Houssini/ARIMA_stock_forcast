import pandas_datareader as pdr
import pandas as pd
import matplotlib.pyplot as plt


def get_data(data_set='AAPL'):
   
    df = pdr.DataReader(data_set, data_source='yahoo', start='2014-01-01', end='2019-09-30')

    # visualize Line pattern of 'Close' Feature to see how it looks like
    plt.figure(figsize=(10, 6))
    plt.plot(df['Close'])
    plt.title("Close Price History")
    plt.xlabel('Date', fontsize=15)
    plt.ylabel('Close Price US ($)', fontsize=15)
    plt.show()
    # Convert the date index into a datetime 
    df.index = pd.to_datetime(df.index, format="%Y/%m/%d")

    # Convert to Series to run Dickey-Fuller test
    df = pd.Series(df['Close'])
   
    return df

