from airflow.providers.mysql.operators.mysql import MySqlHook
import logging

def get_conn(conn_id):
    def access_db(function):
        def inner_function(**kwargs):
            try:
                mysqlServer=MySqlHook(mysql_conn_id=conn_id)
                kwargs['mysqlServer']=mysqlServer
            except ConnectionError:
                logging.error("Failed to acess database")
            return function(**kwargs)
        return inner_function
    return access_db
    