import s3fs
from s3fs.core import S3FileSystem
import pickle
import pandas as pd
import numpy as np
import datetime as dt


def transform_data():
    s3 = S3FileSystem()
    # S3 bucket directory (data lake)
    DIR = 's3://ece5984-bucket-rahulsatoskar/FINAL_PROJECT/Data_Lake'  # Insert here
    # Get data from S3 bucket as a pickle file
    train_df = np.load(s3.open('{}/{}'.format(DIR, 'train_data.pkl')), allow_pickle=True)
    test_df = np.load(s3.open('{}/{}'.format(DIR, 'test_data.pkl')), allow_pickle=True)

    dropped_columns = ['first', 'last', 'trans_num', 'unix_time', 'Unnamed: 0', 'cc_num', 'street', 'zip', 'merchant',
                       'city', 'job', 'state']
    train_df.drop(columns=dropped_columns, inplace=True)
    test_df.drop(columns=dropped_columns, inplace=True)

    train_df['dob'] = pd.to_datetime(train_df['dob'])

    # Calculating age of customer
    train_df['age'] = dt.date.today().year - train_df['dob'].dt.year

    test_df['dob'] = pd.to_datetime(test_df['dob'])

    # Calculating age of customer
    test_df['age'] = dt.date.today().year - test_df['dob'].dt.year

    # Calculating distance between the merchant and the customer
    train_df['lat_distance'] = abs(round(train_df['merch_lat'] - train_df['lat'], 3))
    train_df['long_distance'] = abs(round(train_df['merch_long'] - train_df['long'], 3))

    test_df['lat_distance'] = abs(round(test_df['merch_lat'] - test_df['lat'], 3))
    test_df['long_distance'] = abs(round(test_df['merch_long'] - test_df['long'], 3))

    dropped_columns = ['trans_date_trans_time', 'lat', 'long', 'dob', 'merch_lat', 'merch_long']
    train_df.drop(columns=dropped_columns, inplace=True)
    test_df.drop(columns=dropped_columns, inplace=True)

    # Push cleaned data to S3 bucket warehouse
    DIR_wh = 's3://ece5984-bucket-rahulsatoskar/FINAL_PROJECT/Data_Warehouse'  # Insert here
    with s3.open('{}/{}'.format(DIR_wh, 'clean_train_data.pkl'), 'wb') as f:
        f.write(pickle.dumps(train_df))
    with s3.open('{}/{}'.format(DIR_wh, 'clean_test_data.pkl'), 'wb') as f:
        f.write(pickle.dumps(test_df))
