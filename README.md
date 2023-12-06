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

Data_Lake_EDA.ipynb in the Project_Code folder covers the Exploratory Data Analysis (EDA) of the dataset in detail. The Credit Card Transactions Fraud Detection Dataset is a high-quality dataset and the following points support this argument which are also covered in the EDA done in Data_Lake_EDA.ipynb file.
The data can be considered high-quality data as the data is free from any missing data, null values, and inconsistent data. The data generally does not have extreme outliers. There are outlier points in the "amt" column which can be considered normal as transaction amounts depend on person to person.
The data is also highly imbalanced which can be considered normal in this case as we would expect the fraudulent transactions to be minimal compared to the non-fraudulent transactions.
The data is also accurate as the values in each of the respective columns are what one would usually expect and there are no unusual values. The data is also complete and there are no missing values.


## Data Transformation Models used

We are fetching the Credit Card Transactions Fraud Detection Dataset in batch using the Kaggle API. For extracting data from Kaggle we need to use the Kaggle API credentials. Detailed steps for extracting data using the Kaggle API are explained in the link below.

Link- https://technowhisp.com/kaggle-api-python-documentation/

The raw data is extracted using the Kaggle API and loaded into the Data Lake which is an Amazon S3 bucket. Next, we perform Exploratory Data Analysis (EDA) on the extracted data and perform data cleaning on the data in the Data lake which includes getting rid of irrelevant columns amongst others, and pushing it to the Amazon S3 Data Warehouse.   

Next, we perform featurization on the data in the Data Warehouse which includes one hot encoding for categorical features Standard scaling for numerical features, and feature extraction where we form new features from the existing features. As our data is highly imbalanced with fraudulent transactions being in the minority class and fraudulent transactions being in the majority class we use SMOTE which is an oversampling technique that generates synthetic samples from the minority class. New features formed after feature engineering are pushed to an AWS S3 bucket for subsequent steps. After this step, we train classification algorithms like Decision Trees, Random Forests, and XGBoost on our data after feature engineering. Finally, we use our trained machine learning models to make predictions on the test data and we can predict whether the transaction is fraudulent or genuine. From the predictions, we can see how well our machine learning models perform on the test data by using plots of the confusion matrix and ROC curve and performance metrics like Accuracy, Precision, Recall, F1 score, and AUC.


## Infographic

![image](https://github.com/rahulsatoskar/Credit-Card-Transactions-Fraud-Detection/assets/96548287/65cabd8d-f2d9-4e1f-a527-fb251bbc5542)

## Figure 1- Batch Ingestion Machine Learning Visualization Data Pipeline
## Picture Credits- Dr.Nektara Tryfona Virginia Tech
We will store our trained machine learning models and the predicted outputs along with predicted probability outputs as pickle files in the Amazon S3 buckets. We will download these pickle files into our local machine and do visualizations in our local machine as shown above in Jupyter notebooks, Pycharm, or any other suitable tool. The Project_code folder has a model_predict.ipynb file where we have plotted the confusion matrix and ROC curve and performance metrics like Accuracy, Precision, Recall, F1 score, and AUC of the machine learning models used as shown below.

![image](https://github.com/rahulsatoskar/Credit-Card-Transactions-Fraud-Detection/assets/96548287/4f3eed88-b615-44d1-b3f5-9c2f2b68b99c)

## Figure 2- Confusion Matrix of Decision Tree.

![image](https://github.com/rahulsatoskar/Credit-Card-Transactions-Fraud-Detection/assets/96548287/7630fc20-9dd8-427e-9966-803a4bc8ac18)

## Figure 3- ROC Curve of Decision Tree.

![image](https://github.com/rahulsatoskar/Credit-Card-Transactions-Fraud-Detection/assets/96548287/34bd6ec3-49fe-4334-a202-bc6bfc3b6653)

## Figure 4- Confusion Matrix of Random Forest.

![image](https://github.com/rahulsatoskar/Credit-Card-Transactions-Fraud-Detection/assets/96548287/9e0f0729-8d27-44f6-9e23-aa08f6db9353)

## Figure 5- ROC Curve of Random Forest.

![image](https://github.com/rahulsatoskar/Credit-Card-Transactions-Fraud-Detection/assets/96548287/6c309aa8-214c-444b-83ba-763a28bee54f)

## Figure 6- Confusion Matrix of XGBoost.

![image](https://github.com/rahulsatoskar/Credit-Card-Transactions-Fraud-Detection/assets/96548287/82ea28ee-1eb5-48d3-b1d4-56afdedb5657)

## Figure 7- ROC Curve of XGBoost.


## Code 
Code for this project is stored in the Project_Code folder in this GitHub repository

## Github Repository Link- https://github.com/rahulsatoskar/Credit-Card-Transactions-Fraud-Detection.git


## Thorough Investigation

This credit card transaction fraud detection project serves as a prototype to build real-world real-time industrial systems to detect fraud detection. However, the current prototype would need significant additions and improvements for it to robustly perform in an industrial setting.

To build a real-world industrial fraud detection system we need high-quality real-world customer data which is updated from time to time. Synthetically generated data as used for this project would not suffice for a real-world setting. Our machine learning models would have to be trained periodically with new incoming customer data for it to be up to date to deal with the latest customer frauds that are happening in the market. To further improve the accuracy of our predictions and other performance metrics cascading classifiers can be used which are a concatenation of several classifiers. Deep learning algorithms can also be used to improve the accuracy of our predictions.

The current data pipeline that is used for this project will not be able to handle real-time customer data and process a huge amount of customer data. To process real-world data we need high-end processors and storage so that the system is robust and can process huge amounts of real-time customer data instantly and give the most accurate predictions in time-constrained environments. Industrial Credit card fraud detection systems have to be robust and accurate as even a small mistake can potentially lead to a loss of millions of dollars.














