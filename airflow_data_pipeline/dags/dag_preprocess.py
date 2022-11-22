from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator,MySqlHook
from datetime import datetime
from groups.group_check import group_check_tables
from groups.group_loads import load_data
from groups.group_transform import group_transform
import logging



with DAG("etl_solar",start_date=datetime(2022,11,18),
         schedule_interval="@daily",catchup=False) as dag:
  
     check_input=group_check_tables()
     
     check_status=BashOperator(
        task_id="check_input_status",
        bash_command="echo 'success'",
        trigger_rule="all_success")
     
     check_downloads=load_data()
     
     check_load_status=BashOperator(
        task_id="check_load_status",
        bash_command="echo 'success'",
        trigger_rule="all_success")
     
     transform_data=group_transform()
     
     check_transform_status=BashOperator(
        task_id="check_transform_status",
        bash_command="echo 'success'",
        trigger_rule="all_success")
     
     #load to s3bucket 
     
   
     check_input >> check_status >> check_downloads>> check_load_status >> transform_data\
        >> check_transform_status
     
     
     
    






