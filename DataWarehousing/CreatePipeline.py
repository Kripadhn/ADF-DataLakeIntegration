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

# Define the pipeline name
pipeline_name = '<pipeline_name>'

# Define the pipeline activities
pipeline_activities = [
    {
        'name': '<activity_1_name>',
        'type': '<activity_1_type>',
        'inputs': [
            {
                'name': '<input_dataset_1_name>'
            }
        ],
        'outputs': [
            {
                'name': '<output_dataset_1_name>'
            }
        ],
        'typeProperties': {
            '<activity_1_property_1_name>': '<activity_1_property_1_value>',
            '<activity_1_property_2_name>': '<activity_1_property_2_value>',
            ...
        }
    },
    {
        'name': '<activity_2_name>',
        'type': '<activity_2_type>',
        'inputs': [
            {
                'name': '<input_dataset_2_name>'
            }
        ],
        'outputs': [
            {
                'name': '<output_dataset_2_name>'
            }
        ],
        'typeProperties': {
            '<activity_2_property_1_name>': '<activity_2_property_1_value>',
            '<activity_2_property_2_name>': '<activity_2_property_2_value>',
            ...
        }
    }
]

# Create the pipeline
pipeline = data_factory_client.pipelines.create_or_update(
    resource_group,
    data_factory_name,
    pipeline_name,
    {
        'activities': pipeline_activities
    }
)
