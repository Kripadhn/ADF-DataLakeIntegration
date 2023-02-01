from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import (
    AzureDataLakeStoreSink,
    AzureDataLakeStoreDataset,
    DatasetReference,
    CopyActivity,
    Pipeline,
    PipelineResource,
    SqlSource,
)
from azure.common.credentials import ServicePrincipalCredentials

# Create a Data Factory Management Client
credentials = ServicePrincipalCredentials(
    client_id="<client_id>",
    secret="<client_secret>",
    tenant="<tenant_id>"
)
data_factory_client = DataFactoryManagementClient(credentials, "<subscription_id>")

# Define the source SQL Server dataset
sql_server_dataset = AzureDataLakeStoreDataset(
    "SQL-Dataset",
    linked_service_name="SQL-Server-Linked-Service",
    type_props=SqlSource(
        "SELECT * FROM [dbo].[MyTable]"
    )
)

# Define the destination Data Lake Storage dataset
data_lake_dataset = AzureDataLakeStoreDataset(
    "DataLake-Dataset",
    linked_service_name="DataLake-Linked-Service",
    type_props=AzureDataLakeStoreSink()
)

# Define the copy activity
copy_activity = CopyActivity(
    "Copy-Data-to-DataLake",
    source=DatasetReference(sql_server_dataset.name),
    sink=DatasetReference(data_lake_dataset.name)
)

# Define the pipeline
pipeline = PipelineResource(
    activities=[copy_activity],
    parameters={}
)

# Create the pipeline
data_factory_client.pipelines.create_or_update("<data_factory_name>", "Pipeline-SQL-to-DataLake", pipeline)
