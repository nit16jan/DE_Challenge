# DE_Challenge

Section 1 - Created Python function to perform metioned task and used Airflow to schedule it

Section 2 - Submitted DDLs, ER Diagram and SELECT queries. Have not worked on creating docker images, would need more time to explore it

Section 3 - For System Design, submitted a proposed architecture with components that can be used from Google Cloud. 
Here the architecture is for App which is used to collect and store image data only. If we have Customer/User related information to be stored as well, we can use **Dataflow/Data Fusion** for creating the data pipelines to bring data to BigQuery Warehouse. 
The transaction db for storing user data can be **GCP Firestore**
For the other app providing Kafka streams, this can be patched with **Google Pub/sub** in case required as per usecase.

Section 4 - Used Python requests library to download the data and Tableau Public to create vizualization

Section 5 - Machine Learning. I tried with different classifcation algorithms - Naive Baisse, SVMs and Adaboost. Got maximum accuracy with Adaboost using set of hyper parameters mentioned in the code attached.

Predict Buying for
 Maintenance = High (LabelEncoder = 0)
 Number of doors = 4 (LabelEncoder = 2)
 Lug Boot Size = Big (LabelEncoder = 0)
 Safety = High  (LabelEncoder = 0)
 Class Value = Good  (LabelEncoder = 1)

Output is 1 (Decoded buying value "high")
