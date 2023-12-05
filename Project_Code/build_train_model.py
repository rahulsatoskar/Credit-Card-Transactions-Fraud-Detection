import s3fs
from s3fs.core import S3FileSystem
import numpy as np
import pickle
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb


def build_train():

    s3 = S3FileSystem()
    # S3 bucket directory (data warehouse)
    DIR = 's3://ece5984-bucket-rahulsatoskar/FINAL_PROJECT/FeatureExtraction'                       # Insert here

    X_train = np.load(s3.open('{}/{}'.format(DIR, 'X_train.pkl')), allow_pickle=True)
    X_test = np.load(s3.open('{}/{}'.format(DIR, 'X_test.pkl')), allow_pickle=True)
    y_train = np.load(s3.open('{}/{}'.format(DIR, 'y_train.pkl')), allow_pickle=True)
    y_test = np.load(s3.open('{}/{}'.format(DIR, 'y_test.pkl')), allow_pickle=True)

    DIR_model = 's3://ece5984-bucket-rahulsatoskar/FINAL_PROJECT/TrainedModel'

    # Training ML models
    # 1- Decision tree classifier
    # Initializing and fitting the Decision Tree classifier on the training data
    clf_dt = DecisionTreeClassifier(random_state=20)
    clf_dt.fit(X_train, y_train)

    # Predictions on Test data for Decision tree
    y_pred_dt = clf_dt.predict(X_test)
    y_score_dt= clf_dt.predict_proba(X_test)[:, 1]

    # Saving y_pred_dt and y_score_dt in S3 bucket
    with s3.open('{}/{}'.format(DIR_model, 'y_pred_dt.pkl'), 'wb') as f:
        f.write(pickle.dumps(y_pred_dt))

    with s3.open('{}/{}'.format(DIR_model, 'y_score_dt.pkl'), 'wb') as f:
        f.write(pickle.dumps(y_score_dt))



    # 2- Random forest classifier
    # Initializing and fitting the Random Forest classifier on the training data
    clf_rf = RandomForestClassifier(n_estimators=100, random_state=25)
    clf_rf.fit(X_train, y_train)

    # Predictions on Test data
    y_pred_rf = clf_rf.predict(X_test)
    y_score_rf= clf_rf.predict_proba(X_test)[:, 1]

    # Saving y_pred_rf and y_score_rf in S3 bucket
    with s3.open('{}/{}'.format(DIR_model, 'y_pred_rf.pkl'), 'wb') as f:
        f.write(pickle.dumps(y_pred_rf))

    with s3.open('{}/{}'.format(DIR_model, 'y_score_rf.pkl'), 'wb') as f:
        f.write(pickle.dumps(y_score_rf))


    # Create an XGBoost classifier
    clf_xgboost = xgb.XGBClassifier(
        learning_rate=0.1,  # Learning rate (controls step size during training)
        n_estimators=90,  # Number of boosting rounds (trees)
        max_depth=4,  # Maximum tree depth
        objective='binary:logistic',  # Binary classification problem
        random_state=20
    )

    # Train the classifier on the training data
    clf_xgboost.fit(X_train, y_train)

    y_pred_xgboost  = clf_xgboost.predict(X_test)
    y_score_xgboost = clf_xgboost.predict_proba(X_test)[:, 1]

    # Saving y_pred_xgboost and y_score_xgboost in S3 bucket
    with s3.open('{}/{}'.format(DIR_model, 'y_pred_xgboost.pkl'), 'wb') as f:
        f.write(pickle.dumps(y_pred_xgboost))

    with s3.open('{}/{}'.format(DIR_model, 'y_score_xgboost.pkl'), 'wb') as f:
        f.write(pickle.dumps(y_score_xgboost))


    # Save model in pickle file
    with s3.open('{}/{}'.format(DIR_model, 'clf_dt.pkl'), 'wb') as f:
        f.write(pickle.dumps(clf_dt))

    # Save model in pickle file
    with s3.open('{}/{}'.format(DIR_model, 'clf_rf.pkl'), 'wb') as f:
        f.write(pickle.dumps(clf_rf))

    # Save model in pickle file
    with s3.open('{}/{}'.format(DIR_model, 'clf_xgboost.pkl'), 'wb') as f:
        f.write(pickle.dumps(clf_xgboost))


















