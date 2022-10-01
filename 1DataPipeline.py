from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
import pandas as pd

def data_processing():
    #Reading both files in single dataframe
    df = pd.concat(map(pd.read_csv, [r'C:\Users\narora\Desktop\dataset1.csv',r'C:\Users\narora\Desktop\dataset2.csv']))

    # To delete rows with null values. Doing this as first operation to clean/reduce the data
    notnull_names = pd.notnull(df.name)
    df = df[notnull_names]

    # Remove any zeros prepended to the price field
    df.price = df.price.apply(float)

    # If we want to remove salutations and then get first and last names
    # print(df1['name'].replace(regex=r"(?:Mr\.|Mrs\.|Ms\.|Dr\.)",value=''))

    # Below code splits using ' ' except for names with Salutations. With salutation first name will split at second space
    df[['first_name', 'last_name']] = df.name.str.split(r"(?<!Dr\.)(?<!Ms\.)(?<!Mr\.)(?<!Mrs\.) ",1,expand=True)

    # new field named above_100, which is true if the price is strictly greater than 10
    df['above_100'] = df['price'] > 100

    # Export results to CSV
    df.to_csv(r'C:\Users\narora\Desktop\processed.csv', index=False, columns=['name','first_name','last_name','price','above_100'])

default_args = {
    'owner':"NA",
    'start_date':datetime.now(),
    'email':'na@abc.com',
    'retries':1,
    'retry_delay':timedelta(minutes=10),
}
dag = DAG(
    dag_id='CSV Data Pipeline',
    schedule_interval='0 1 * * *',
    default_args=default_args,
    description='Section 1 Data Processing',
)
etl_task = PythonOperator(
    task_id='etl_task',
    python_callable=data_processing,
    dag=dag,
)

# task pipeline
etl_task