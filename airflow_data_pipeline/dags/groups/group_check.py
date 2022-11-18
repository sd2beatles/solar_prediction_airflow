from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator,MySqlHook
from airflow.utils.task_group import TaskGroup



def group_check_tables():
    with TaskGroup("tables",tooltip="Check if the tables are available") as group:
        
        
        check_a=MySqlOperator(
            task_id="check_a",
            mysql_conn_id="mysql_solar",
            sql='''
            CREATE TABLE IF NOT EXISTS weather_info(
                locdatetime VARCHAR(40),
                location VARCHAR(40),
                updated_date VARCHAR(13),
                temperature FLOAT,
                precipitation_form FLOAT,
                precipitation_prob FLOAT,
                humidity FLOAT,
                wind_speed FLOAT,
                wind_direction FLOAT,
                cloud FLOAT,
                primary key(locdatetime,location));
                ''')
        
        check_b=MySqlOperator(
            task_id="check_b",
            mysql_conn_id="mysql_solar",
            sql='''
            CREATE TABLE IF NOT EXISTS geography(
                locdatetime VARCHAR(40),
                location VARCHAR(40),
                updated_date VARCHAR(13),
                temperature FLOAT,
                precipitation_form FLOAT,
                precipitation_prob FLOAT,
                humidity FLOAT,
                wind_speed FLOAT,
                wind_direction FLOAT,
                cloud FLOAT,
                primary key(locdatetime,location));
                ''')
        
        
        return group
        
        

