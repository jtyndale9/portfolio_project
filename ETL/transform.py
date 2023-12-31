from datetime import datetime
import pandas as pd
import numpy as np
import sys

todays_date = datetime.now().strftime("%m_%d_%Y")


def normalize_data(data, column):
    
    # This is returning different ranges of outputs....
    #normalized_data = preprocessing.normalize([data])
    
    #scaler = preprocessing.MinMaxScaler()
    #scaler.fit(data) # Compute the minimum and maximum to be used for later scaling.
    #scaler.transform(data) # Scale features of X according to feature_range.
    #return  scaler.transform(data)
    
    # By-hand calculation
    # zi = (xi – min(x)) / (max(x) – min(x)) * 100
    data[column] = (data[column] - min(data[column])) / (max(data[column]) - min(data[column])) * 100
    return data





def get_data():
    filename = f'housing_data_{todays_date}.csv'

    data = (
        pd.read_csv(filename)
        .assign(Date=lambda data: pd.to_datetime(data["DATE"], format="%Y/%m/%d"))
        .sort_values(by="DATE")
    )

    #savings_data = savings_data[['Date', 'PSAVERT']]
    #print(data)
    #savings_data['PSAVERT'] = normalize_data(savings_data['PSAVERT'])
    #savings_data = savings_data[(savings_data['Date'] > dt.datetime(1974,12,31)) & ((savings_data['Date'] < dt.datetime(2022,11,1)))]
    print(data.columns)
    data.drop(['DATE'],  axis=1, inplace=True)
    return data

def clean_aspus():
    data = get_data()
    print(data)
    normalized_data = normalize_data(data, 'ASPUS')
    print(normalized_data)
    return normalized_data

