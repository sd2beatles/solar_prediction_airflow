from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup




# def group_downloads():
#     with TaskGroup("downloads",tooltip="Download tasks") as group:
        
#         download_a=