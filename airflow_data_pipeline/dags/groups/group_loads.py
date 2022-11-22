from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import PythonOperator
from dags.preprocess.connection import get_conn
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime
import pandas as pd
import logging

 
 
 #obtain data from the selected table and save it to the desitnaged path
@get_conn(conn_id="mysql_solar") 
def save_data(**context):
    try:
        #load datea from sql dateabse
        sql_data=context['mysqlServer'].get_pandas_df(sql=context['params']['sql'])
        #save datearame to designated path
        sql_data.to_csv(context['params']['dest_path'])
    except ConnectionAbortedError:
        logging.error("fail to save the data")    
             

               
def load_data():
    with TaskGroup("convert_to_csv",tooltip="Check if the tables are available") as group:
        today=datetime.now().strftime("%Y-%m-%d")
        path="/opt/airflow/storage/input/{}".format(today)
        
        check_folder=BashOperator(
            task_id="check_input_folder",
            bash_command="{{params.Bash}} {{params.File}}",
            params={
                'Bash':"/opt/airflow/utilities/make_folder.sh", 
                'File':"{}".format(path)}
            )
        
        sql_weather="SELECT * FROM weather_info "
        download_a=PythonOperator(
            task_id="extract_weather_info",
            python_callable=save_data,
            params={'sql':sql_weather,'dest_path':path+"/weather.csv"},
            provide_context=True
        )
        
        sql_geo="SELECT * FROM geography"
        download_b=PythonOperator(
            task_id="extract_geography_info",
            python_callable=save_data,
            params={'sql':sql_geo,'dest_path':path+"/geography.csv"},
            provide_context=True
        )
        
        check_folder >>[download_a,download_b]
    
        return group
        
        

