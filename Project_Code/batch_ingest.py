"""
References

1- Using Kaggle API from local python | How to use Kaggle API from python | Using Kaggle API
Link- https://www.youtube.com/watch?v=DgGFhQmfxHo&t=134s

2- How-to use the Kaggle API in Python
Link- https://www.youtube.com/watch?v=DgGFhQmfxHo&t=134s

3- Kaggle API – The Missing Python Documentation
Link- https://technowhisp.com/kaggle-api-python-documentation/

4- Convert CSV to Pandas Dataframe
Link- https://www.geeksforgeeks.org/convert-csv-to-pandas-dataframe/

"""

import s3fs
from s3fs.core import S3FileSystem
import numpy as np
import pickle
# import pandas module
import pandas as pd
import zipfile

# Importing data using Kaggle API
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

def ingest_data():
    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files('kartik2112/fraud-detection')

    with zipfile.ZipFile('fraud-detection.zip', 'r') as zipref:
        zipref.extractall()

    # making dataframe
    train_df = pd.read_csv("fraudTrain.csv")
    test_df = pd.read_csv("fraudTest.csv")

    s3 = S3FileSystem()
    # S3 bucket directory
    DIR = 's3://ece5984-bucket-rahulsatoskar/FINAL_PROJECT/Data_Lake'                        #Enter your S3 directory
    # Push data to S3 bucket as a pickle file
    with s3.open('{}/{}'.format(DIR, 'train_data.pkl'), 'wb') as f:
        f.write(pickle.dumps(train_df))

    with s3.open('{}/{}'.format(DIR, 'test_data.pkl'), 'wb') as f:
        f.write(pickle.dumps(test_df))