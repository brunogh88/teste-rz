FROM puckel/docker-airflow:1.10.9

COPY airflow.cfg ${AIRFLOW_HOME}/airflow.cfg

COPY requirements-airflow.txt /requirements-airflow.txt
RUN pip install -r /requirements-airflow.txt