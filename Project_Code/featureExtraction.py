import s3fs
from s3fs.core import S3FileSystem
import numpy as np
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

def feature_extract():
    s3 = S3FileSystem()
    # S3 bucket directory (data warehouse)
    DIR_wh = 's3://ece5984-bucket-rahulsatoskar/FINAL_PROJECT/Data_Warehouse'  # Insert here
    # Get data from S3 bucket as a pickle file
    clean_train_df = np.load(s3.open('{}/{}'.format(DIR_wh, 'clean_train_data.pkl')), allow_pickle=True)
    clean_test_df = np.load(s3.open('{}/{}'.format(DIR_wh, 'clean_test_data.pkl')), allow_pickle=True)

    # Converting a categorical column gender to a numerical column
    clean_train_df.gender = clean_train_df.gender.apply(lambda x: 1 if x == "M" else 0)
    clean_test_df.gender = clean_test_df.gender.apply(lambda x: 1 if x == "M" else 0)

    # One Hot Encoding of Categorical columns
    # https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html

    clean_train_df = pd.get_dummies(clean_train_df, columns=['category'], prefix='category')
    clean_test_df = pd.get_dummies(clean_test_df, columns=['category'], prefix='category')

    # Splitting Train and Test Data
    X_train = clean_train_df.drop('is_fraud', axis=1)
    y_train = clean_train_df['is_fraud']
    X_test = clean_test_df.drop('is_fraud', axis=1)
    y_test = clean_test_df['is_fraud']

    # Handling imbalanced data
    smote = SMOTE(random_state=30)
    X_train, y_train = smote.fit_resample(X_train, y_train)

    #Standardizing data
    scaler = StandardScaler()
    scaler.fit(X_train)

    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    # Push extracted features to data warehouse
    DIR = 's3://ece5984-bucket-rahulsatoskar/FINAL_PROJECT/FeatureExtraction'  # Insert here
    with s3.open('{}/{}'.format(DIR, 'X_train.pkl'), 'wb') as f:
        f.write(pickle.dumps(X_train))
    with s3.open('{}/{}'.format(DIR, 'X_test.pkl'), 'wb') as f:
        f.write(pickle.dumps(X_test))
    with s3.open('{}/{}'.format(DIR, 'y_train.pkl'), 'wb') as f:
        f.write(pickle.dumps(y_train))
    with s3.open('{}/{}'.format(DIR, 'y_test.pkl'), 'wb') as f:
        f.write(pickle.dumps(y_test))

