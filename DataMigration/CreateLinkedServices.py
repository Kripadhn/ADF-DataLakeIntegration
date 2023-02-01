# Import required modules
import os
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import LinkedService

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

# Define the source database connection string
source_db_conn_str = '<source_db_connection_string>'

# Define the data lake store connection string
datalake_store_conn_str = '<data_lake_store_connection_string>'

# Create the linked service for the source database
source_db_linked_service = LinkedService(
    type='AzureSqlDatabase',
    name='source_db_linked_service',
    connection_string=source_db_conn_str
)

# Create the linked service for the data lake store
datalake_store_linked_service = LinkedService(
    type='AzureDataLakeStore',
    name='datalake_store_linked_service',
    connection_string=datalake_store_conn_str
)

# Create the linked services in the data factory
data_factory_client.linked_services.create_or_update(
    resource_group,
    data_factory_name,
    'source_db_linked_service',
    source_db_linked_service
)

data_factory_client.linked_services.create_or_update(
    resource_group,
    data_factory_name,
    'datalake_store_linked_service',
    datalake_store_linked_service
)
