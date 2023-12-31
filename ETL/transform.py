import pandas as pd
import sys
import numpy as np
from datetime import datetime

todays_date = datetime.now().strftime("%m_%d_%Y")


def normalize_data(data):
    
    # This is returning different ranges of outputs....
    #normalized_data = preprocessing.normalize([data])
    
    #scaler = preprocessing.MinMaxScaler()
    #scaler.fit(data) # Compute the minimum and maximum to be used for later scaling.
    #scaler.transform(data) # Scale features of X according to feature_range.
    #return  scaler.transform(data)
    
    # By-hand calculation
    # zi = (xi – min(x)) / (max(x) – min(x)) * 100
    data = (data - min(data)) / (max(data) - min(data)) * 100
    return data





def get_data():
    filename = f'housing_data_{todays_date}.csv'

    data = (
        pd.read_csv(filename)
        .assign(Date=lambda data: pd.to_datetime(data["DATE"], format="%Y/%m/%d"))
        .sort_values(by="DATE")
    )

    #savings_data = savings_data[['Date', 'PSAVERT']]
    print(data)
    #savings_data['PSAVERT'] = normalize_data(savings_data['PSAVERT'])
    #savings_data = savings_data[(savings_data['Date'] > dt.datetime(1974,12,31)) & ((savings_data['Date'] < dt.datetime(2022,11,1)))]
    return data

