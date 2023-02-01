from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import Dataset
from azure.common.credentials import ServicePrincipalCredentials

# Create a Data Factory Management Client
credentials = ServicePrincipalCredentials(
    client_id="<client_id>",
    secret="<client_secret>",
    tenant="<tenant_id>"
)
data_factory_client = DataFactoryManagementClient(credentials, "<subscription_id>")

# Create a dataset definition for Data Lake Storage
dataset = Dataset(
    type='Microsoft.DataLakeStore/file',
    linked_service_name='DataLakeStoreLinkedService',
    schema=[
        {
            'name': 'column1',
            'type': 'String'
        },
        {
            'name': 'column2',
            'type': 'Int32'
        }
    ],
    type_properties={
        'fileName': '<datalake_file_path>',
        'format': {
            'type': 'TextFormat',
            'columnDelimiter': ','
        }
    }
)

# Create the dataset
data_factory_client.datasets.create_or_update(
    "<data_factory_name>",
    "DataLakeStoreDataset",
    dataset
)
