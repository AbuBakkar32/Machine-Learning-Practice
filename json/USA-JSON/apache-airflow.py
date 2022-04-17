import json
import warnings
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.hooks.gcs import GCSHook
from dependencies.applications import parse_xml_claims_v1

warnings.warn(
    "This module is deprecated. Please use `airflow.providers.google.cloud.hooks.gcs`.",
    DeprecationWarning,
    stacklevel=2,
)
default_args = {
    "owner": "PSAI Data Engineering",
    "email": ["psai@uspto.gov"],
    "depends_on_past": False,
    "start_date": datetime(2001, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "priority_weight": 1000,
}

CONN_PARAMS_DICT = {
    "gcp_project": "patents-search-ai",
    "gcp_conn_id": "google_cloud_default",
}

PROCESS_PARAMS_DICT = {
    "gcp_gcs_bucket": "search-ai-data-landing",
    # TODO(jordan): don't use static filename here.
    "object_name": "12018718-FBSJ2D4VPPOPPY4-CLM.xml",
}

dag_name = "applications_processing_v1"


def list_files(ds, **kwargs):
    """Lists all files in GCS bucket based on the prefix."""
    gcs_hook = GCSHook(CONN_PARAMS_DICT.get("gcp_conn_id", ""))

    file_list = gcs_hook.list(
        bucket_name=PROCESS_PARAMS_DICT.get("gcp_gcs_bucket", ""), prefix="2022-04-04/"
    )

    for file in file_list:
        print(file)


def process_data(ds, **kwargs):
    """Reads data from GCE, processes, and saves to new GCS file"""
    gcs_hook = GCSHook(CONN_PARAMS_DICT.get("gcp_conn_id", ""))

    filename = "tmp-{}".format(PROCESS_PARAMS_DICT.get("object_name", ""))
    object_name = "2022-04-04/{}".format(PROCESS_PARAMS_DICT.get("object_name", ""))
    gcs_hook.download(
        bucket_name=PROCESS_PARAMS_DICT.get("gcp_gcs_bucket", ""),
        object_name=object_name,
        filename=filename,
    )

    xml_string = ""
    f = open(filename, "r")
    values = f.readlines()
    for value in values:
        xml_string = xml_string + value.rstrip("\r\n")

    document = parse_xml_claims_v1(xml_string.encode("utf-8"))
    json_document = json.dumps(document, indent=2)

    print(json_document)


with DAG(dag_name, default_args=default_args, schedule_interval="@once") as dag:
    # Task to process and parse XML file
    t1 = PythonOperator(
        task_id="list-files", python_callable=list_files, provide_context=True
    )

    # Task to process and parse XML file
    t2 = PythonOperator(
        task_id="process-data", python_callable=process_data, provide_context=True
    )

    [t1, t2]

# TASK_PARAMS_DICT = {
#    "dataset_id": "firestore_dev_click_data",
#    "project_id": "patents-search-ai",
#    "gcp_conn_id": "google_cloud_default",
# }
