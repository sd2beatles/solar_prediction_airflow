from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import PythonOperator
from dags.preprocess.connection import get_conn
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup
from google.cloud import storage
from datetime import datetime
import pandas as pd
import logging
import re
import os

  
def save_to_google_stroage(**context):
    bucket=context['params']['bucket']
    input_path=context['params']['input_path']
    sub_dir=context['params']["sub_dir"]
    bucket="test_bucket_david_kr"
    client=storage.Client()
   
    
    bucket=client.get_bucket(bucket)
   
    try:
        path_date=re.search("[0-9]{,4}-[0-9]{2}-[0-9]{2}",input_path).group()
    except ValueError as e:
        print("The input path must conatin datetime information")
   
    bucket_full_path="{}/{}.csv".format(sub_dir,path_date)
    blob=bucket.blob(bucket_full_path)
    blob.upload_from_filename(input_path)
    


def group_storage():
    with TaskGroup("storage",tooltip="preprocessing raw datea") as group:
        today=datetime.now().strftime("%Y-%m-%d")
        input_path="./storage/output/{}".format(today)
        bucket_name=os.getenv("BUCKET_NAME")
        
        #path_information
        current_path="/opt/airflow/utilities"
        storage="/opt/airflow/storage/output/{}".format(today)
        
        check_files=BashOperator(
            task_id="check_input_files",
            bash_command="{{params.Bash}} {{params.file1}} {{params.file2}}",
            params={
                'Bash':"{}/check_both_files.sh".format(current_path), 
                'file1':"{}/{}".format(storage,"weather.csv"),
                'file2':"{}/{}".format(storage,"geography.csv")}
            )
        
        
        weather=PythonOperator(
            task_id="save_weather_data",
            python_callable=save_to_google_stroage,
            params={'input_path':input_path+"/weather.csv",'bucket':bucket_name,'sub_dir':'weather'},
            provide_context=True
        )
        
        geography=PythonOperator(
            task_id="save_geography_data",
            python_callable=save_to_google_stroage,
            params={'input_path':input_path+"/geography.csv",'bucket':bucket_name,'sub_dir':'geography'},
            provide_context=True
        )
      
        
        #according to non-disclourse aggrement
        #unable to make it public
        energy=BashOperator(
            task_id="save_energy",
            bash_command="sleep 1 "
        )
        check_files >> [weather,geography,energy]
    return group

 

