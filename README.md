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

- Cloud - [**Amazon Web Services**](https://aws.amazon.com/free/?gclid=CjwKCAiAjrarBhAWEiwA2qWdCObCd_owlFH0urkD8Ek2df-o9_z27R7Eh_47HYXaXqcxAFw8DrpoIRoCGLEQAvD_BwE&trk=fce796e8-4ceb-48e0-9767-89f7873fac3d&sc_channel=ps&ef_id=CjwKCAiAjrarBhAWEiwA2qWdCObCd_owlFH0urkD8Ek2df-o9_z27R7Eh_47HYXaXqcxAFw8DrpoIRoCGLEQAvD_BwE:G:s&s_kwcid=AL!4422!3!432339156150!e!!g!!aws!1644045032!68366401852)
- Infrastructure as Code software - [**Terraform**](https://www.terraform.io)
- Containerization - [**Docker**](https://www.docker.com), [**Docker Compose**](https://docs.docker.com/compose/)
- Stream Processing - [**Kafka**](https://kafka.apache.org), [**Spark Streaming**](https://spark.apache.org/docs/latest/streaming-programming-guide.html)
- Orchestration - [**Airflow**](https://airflow.apache.org)
- Transformation - [**dbt**](https://www.getdbt.com)
- Data Lake - [**Google Cloud Storage**](https://cloud.google.com/storage)
- Data Warehouse - [**BigQuery**](https://cloud.google.com/bigquery)
- Data Visualization - [**Data Studio**](https://datastudio.google.com/overview)
- Language - [**Python**](https://www.python.org)



