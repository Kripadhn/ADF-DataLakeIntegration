# Import required modules
from azure.mgmt.datafactory import DataFactoryManagementClient

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

# Define the data source name
data_source_name = '<data_source_name>'

# Define the data source connection string
data_source_connection_string = '<data_source_connection_string>'

# Create the data source
data_source = data_factory_client.data_sources.create_or_update(
    resource_group,
    data_factory_name,
    data_source_name,
    {
        'properties': {
            'connectionString': data_source_connection_string,
            'type': '<data_source_type>'
        }
    }
)
