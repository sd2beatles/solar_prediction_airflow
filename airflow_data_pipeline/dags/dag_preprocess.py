import os
import sys
sys.path.append('.')
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator,MySqlHook
from preprocess.preprocess import extract_stamp
from groups.group_check import group_check_tables
from datetime import datetime
import logging


with DAG("etl_solar",start_date=datetime(2022,11,18),
         schedule_interval="@daily",catchup=False) as dag:
  
    
     downloads=group_check_tables()
     
     check_files=BashOperator(
        task_id="check_files",
        bash_command="echo 'success'")
     
     downloads >> check_files
     
     
    






