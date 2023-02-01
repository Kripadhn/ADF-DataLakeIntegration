# Import required modules
import os
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import Dataset

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

# Define the source database table
source_db_table = '<source_db_table>'

# Define the destination data lake path
destination_datalake_path = '<destination_datalake_path>'

# Create the source database dataset
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

# Create the destination data lake dataset
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

# Create the datasets in the data factory
data_factory_client.datasets.create_or_update(
    resource_group,
    data_factory_name,
    'source_dataset',
    source_dataset
)

data_factory_client.datasets.create_or_update(
    resource_group,
    data_factory_name,
    'destination_dataset',
    destination_dataset
)
