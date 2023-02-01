from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.common.credentials import ServicePrincipalCredentials

# Create a Data Factory Management Client
credentials = ServicePrincipalCredentials(
    client_id="<client_id>",
    secret="<client_secret>",
    tenant="<tenant_id>"
)
data_factory_client = DataFactoryManagementClient(credentials, "<subscription_id>")

# Start the pipeline run
pipeline_run = data_factory_client.pipelines.create_run("<data_factory_name>", "Pipeline-SQL-to-DataLake", {})

# Wait for the pipeline run to complete
pipeline_run = data_factory_client.pipeline_runs.wait_for_completion(
    "<data_factory_name>",
    "Pipeline-SQL-to-DataLake",
    pipeline_run.run_id,
    timeout=60
)

# Check the status of the pipeline run
if pipeline_run.status == "Succeeded":
    print("Pipeline run completed successfully")
else:
    print("Pipeline run failed")
