# Import required modules
import os
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import Dataset
from azure.mgmt.datafactory.models import LinkedService
from azure.mgmt.datafactory.models import CopyActivity
from azure.mgmt.datafactory.models import CopySink
from azure.mgmt.datafactory.models import Pipeline
from azure.mgmt.datafactory.models import AzureDataLakeStoreSink

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

# Define the source database table name
source_db_table = '<source_db_table_name>'

# Define the destination data lake store path
destination_datalake_path = '<destination_data_lake_store_path>'

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

# Create the source dataset
source_dataset = Dataset(
    type='AzureSqlTable',
    name='source_dataset',
    linked_service_name='source_db_linked_service',
    structure=[
        {
            'name': 'column1',
            'type': 'string'
        },
        {
            'name': 'column2',
            'type': 'int'
        }
    ],
    table_name=source_db_table
)

# Create the destination dataset
destination_dataset = Dataset(
    type='AzureDataLakeStore',
    name='destination_dataset',
    linked_service_name='datalake_store_linked_service',
    structure=[
        {
            'name': 'column1',
            'type': 'string'
        },
        {
            'name': 'column2',
            'type': 'int'
        }
    ],
    file_name=destination_datalake_path
)

# Create the destination dataset
destination_dataset = Dataset(
type='AzureDataLakeStore',
name='destination_dataset',
linked_service_name='datalake_store_linked_service',
structure=[
{
'name': 'column1',
'type': 'string'
},
{
'name': 'column2',
'type': 'int'
}
],
file_name=destination_datalake_path
)
