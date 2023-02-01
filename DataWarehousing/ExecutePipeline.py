# Import required modules
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import RunFilterParameters

# Connect to the data factory management API
data_factory_client = DataFactoryManagementClient.create_from_service_principal_credentials(
    client_id='<client_id>',
    secret='<secret>',
    tenant='<tenant>',
    subscription_id='<subscription_id>'
)

# Define the resource group
resource_group = '<resource_group_name>'

# Define the data factory name
data_factory_name = '<data_factory_name>'

# Define the pipeline name
pipeline_name = '<pipeline_name>'

# Define the pipeline run ID
pipeline_run_id = data_factory_client.pipelines.create_run(
    resource_group,
    data_factory_name,
    pipeline_name
)

# Get the pipeline run details
pipeline_run = data_factory_client.pipeline_runs.get(
    resource_group,
    data_factory_name,
    pipeline_run_id.run_id
)

# Check the pipeline run status
while pipeline_run.status == 'InProgress':
    pipeline_run = data_factory_client.pipeline_runs.get(
        resource_group,
        data_factory_name,
        pipeline_run.run_id
    )

# Print the pipeline run status
print('Pipeline run status:', pipeline_run.status)
