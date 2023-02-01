# Import required modules
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.datafactory import DataFactoryManagementClient

# Connect to the resource management API
resource_client = ResourceManagementClient.create_from_service_principal_credentials(
    client_id='<client_id>',
    secret='<secret>',
    tenant='<tenant>',
    subscription_id='<subscription_id>'
)

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

# Create the data factory
data_factory = data_factory_client.data_factories.create_or_update(
    resource_group,
    data_factory_name,
    {
        'location': '<location>',
        'tags': {
            'tag_key': 'tag_value'
        }
    }
)
