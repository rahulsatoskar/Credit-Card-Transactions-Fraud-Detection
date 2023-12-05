# Credit-Card-Transactions-Fraud-Detection

Data Engineering project using batch ingestion and ML pipeline to detect whether a transaction is false or not 

## Title

Credit Card Transactions Fraud Detection using Batch Ingestion and Machine Learning Pipeline.

## Project’s function

As e-commerce and Fintech boom, these systems must be as robust as possible. In countries with high credit card usage, particularly the US credit card companies should be able to distinguish fraudulent vs genuine transactions in real time with high precision so that customers are not charged for fraudulent transactions.
This project will use a simulated credit card transaction dataset using Sparkov extracted using a Kaggle API using batch ingestion. A data pipeline will be used to process this data and suitable transformations on the data will be done. Finally, a machine learning pipeline will be used to classify a transaction as Fraudulent or Genuine. We will plot a confusion matrix and ROC curve and display performance metrics like Accuracy, Precision, Recall, F1 score, and AUC to see how well each of the machine learning models used is performing on our dataset.

## Dataset

This project will use a simulated credit card transaction dataset containing legitimate and fraudulent transactions from the duration of 1st Jan 2019 to 31st Dec 2020. It covers the credit cards of 1000 customers doing transactions with a pool of 800 merchants.

Link- https://www.kaggle.com/datasets/kartik2112/frauddetection

This data was generated using Sparkov Data Generation
GitHub tool created by Brandon Harris.

Link https://github.com/namebrandon/Sparkov_Data_Generation

## Pipeline / Architecture

Data Pipeline used- Batch Ingestion with Machine Learning and Visualization Pipeline.

- Cloud - [**Amazon Web Services**](https://aws.amazon.com/free/?gclid=CjwKCAiAjrarBhAWEiwA2qWdCObCd_owlFH0urkD8Ek2df-o9_z27R7Eh_47HYXaXqcxAFw8DrpoIRoCGLEQAvD_BwE&trk=fce796e8-4ceb-48e0-9767-89f7873fac3d&sc_channel=ps&ef_id=CjwKCAiAjrarBhAWEiwA2qWdCObCd_owlFH0urkD8Ek2df-o9_z27R7Eh_47HYXaXqcxAFw8DrpoIRoCGLEQAvD_BwE:G:s&s_kwcid=AL!4422!3!432339156150!e!!g!!aws!1644045032!68366401852)
- Orchestration - [**Airflow**](https://airflow.apache.org)
- Transformation - [**Pandas**](https://pandas.pydata.org/)
- Data Lake - [**Amazon S3**](https://aws.amazon.com/pm/serv-s3/?gclid=CjwKCAiAjrarBhAWEiwA2qWdCMeSmoX4RDFT2fz97d6LdpX5TjAPMLhbgXLYGNgEjSNORKGj7h9l7BoCzZMQAvD_BwE&trk=fecf68c9-3874-4ae2-a7ed-72b6d19c8034&sc_channel=ps&ef_id=CjwKCAiAjrarBhAWEiwA2qWdCMeSmoX4RDFT2fz97d6LdpX5TjAPMLhbgXLYGNgEjSNORKGj7h9l7BoCzZMQAvD_BwE:G:s&s_kwcid=AL!4422!3!536452728638!e!!g!!aws%20s3!11204620052!112938567994#Learn_More_About_Amazon_S3)
- Data Warehouse - [**Amazon S3**](https://aws.amazon.com/pm/serv-s3/?gclid=CjwKCAiAjrarBhAWEiwA2qWdCMeSmoX4RDFT2fz97d6LdpX5TjAPMLhbgXLYGNgEjSNORKGj7h9l7BoCzZMQAvD_BwE&trk=fecf68c9-3874-4ae2-a7ed-72b6d19c8034&sc_channel=ps&ef_id=CjwKCAiAjrarBhAWEiwA2qWdCMeSmoX4RDFT2fz97d6LdpX5TjAPMLhbgXLYGNgEjSNORKGj7h9l7BoCzZMQAvD_BwE:G:s&s_kwcid=AL!4422!3!536452728638!e!!g!!aws%20s3!11204620052!112938567994#Learn_More_About_Amazon_S3)
- Data Visualization - [**Matplotlib**](https://matplotlib.org/)
- Language - [**Python**](https://www.python.org)
- Machine Learning library - [**Scikit-learn**](https://scikit-learn.org/stable/)

## Data Quality Assessment

The Credit Card Transactions Fraud Detection Dataset is a high-quality dataset and the following points support this argument. Data_Lake_EDA.ipynb in the Project_Code folder covers the Exploratory Data Analysis of the dataset in detail.
The data can be considered high-quality data as the data is free from any missing data, null values, and inconsistent data. The data generally does not have extreme outliers. There are outlier points in the "amt" column which can be considered normal as transaction amounts depend on person to person.
The data is also highly imbalanced which can be considered normal in this case as we would expect the fraudulent transactions to be minimal compared to the non-fraudulent transactions.










