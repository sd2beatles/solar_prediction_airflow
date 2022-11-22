from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import PythonOperator
from dags.preprocess.preprocess import weather_preprocess,geography_preprocess,energy_preprocess
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup
import pandas as pd
from datetime import datetime
import logging



def group_transform():
    with TaskGroup("transform",tooltip="preprocessing raw datea") as group:
        today=datetime.now().strftime("%Y-%m-%d")
        input_path="./storage/input/{}".format(today)
        output_path="/opt/airflow/storage/output/{}".format(today)
        
        check_folder=BashOperator(
            task_id="check_output_folder",
            bash_command="{{params.Bash}} {{params.File}}",
            params={
                'Bash':"/opt/airflow/utilities/make_folder.sh", 
                'File':"{}".format(output_path)}
            )
        
        
        
        weather=PythonOperator(
            task_id="preprocess_weather",
            python_callable=weather_preprocess,
            params={'start_path':input_path+"/weather.csv",'dest_path':output_path+'/weather.csv'},
            provide_context=True
        )
        
        geography=PythonOperator(
            task_id="preprocess_geography",
            python_callable=geography_preprocess,
            params={'start_path':input_path+"/geography.csv",'dest_path':output_path+'/geography.csv'},
            provide_context=True
        )
        
        #according to non-disclourse aggrement
        #unable to make it public
        energy=BashOperator(
            task_id="preprocess_energy",
            bash_command="sleep 1 "
        )
        check_folder >> [weather,geography,energy]
    return group
        
        
        
        

    














