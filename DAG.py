import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator
import pendulum


titanic_dag = DAG(
    "titanic_dag",
    start_date=pendulum.today('UTC').add(days=-0)
    )

def download_titanic_dataset():
    df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
    df.to_csv("df.csv")

download_dataframe = PythonOperator(
    task_id='download_titanic_dataset',
    python_callable=download_titanic_dataset,
    dag=titanic_dag
)

def transform_titanic_dataset():
    df = pd.read_csv("df.csv")
    gr = df.groupby("Pclass").agg({"Survived": "mean"})
    gr.to_csv("output.csv")


transform_dataframe = PythonOperator(
    task_id='transform_dataframe',
    python_callable=transform_titanic_dataset,
    dag=titanic_dag
)


download_dataframe >> transform_dataframe
