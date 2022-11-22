
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator,MySqlHook
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup



def group_check_tables():
    with TaskGroup("checkfiles",tooltip="Check if the tables are available") as group:
        current_path="/opt/airflow"
        
        with open("./utilities/schema.sql".format(current_path)) as sql:
            sql_iters=sql.read()
        sql_=sql_iters.split(";")
        

        check_a=MySqlOperator(
            task_id="check_weather_table",
            mysql_conn_id="mysql_solar",
            sql=sql_[0])
        
        check_b=MySqlOperator(
            task_id="check_solar_table",
            mysql_conn_id="mysql_solar",
            sql=sql_[1])
        
    
        
        #according to non-discolsure aggrement,
        #unable to make the file public
        current_path="/opt/airflow/utilities"
        check_files_1=BashOperator(
            task_id="check_energy_file_1",
            bash_command="{{params.Bash}} {{params.File}}",
            params={
                'Bash':"{}/check_file.sh".format(current_path), 
                'File':"{}/storage/{}".format(current_path,"energy_1.csv")}
            )
        
        #according to non-discolsure aggrement,
        #unable to make the file public
        check_files_2=BashOperator(
            task_id="check_energy_file_2",
            bash_command="{{params.Bash}} {{params.File}}",
            params={
                'Bash':"{}/check_file.sh".format(current_path), 
                'File':"{}/storage/{}".format(current_path,"energy_2.csv")}
            )
        

        return group
        
        

