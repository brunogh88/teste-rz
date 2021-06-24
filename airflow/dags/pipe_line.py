from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.docker_operator import DockerOperator

ARGS = {
    'owner'            : 'brunoHeleodoro',
    'description'      : 'App Test Raizen',
    'depend_on_past'   : False,
    'start_date'       : datetime.now(),
    'email_on_failure' : False,
    'email_on_retry'   : False,
    'retries'          : 1,
    'retry_delay'      : timedelta(minutes=1)
}


with DAG('app-pipeline', default_args=ARGS, schedule_interval='0 0 * * *', catchup=False) as dag:

    pipe_run = DockerOperator(
        task_id='pipe-test-raizen',
        image='testeraizen',
        api_version='auto',
        auto_remove=True,
        command='echo teste',        
        docker_url="unix://var/run/docker.sock",
        network_mode='bridge'
    )

    pipe_run 