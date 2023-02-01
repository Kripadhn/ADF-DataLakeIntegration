from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import LinkedService
from azure.common.credentials import ServicePrincipalCredentials

# Create a Data Factory Management Client
credentials = ServicePrincipalCredentials(
    client_id="<client_id>",
    secret="<client_secret>",
    tenant="<tenant_id>"
)
data_factory_client = DataFactoryManagementClient(credentials, "<subscription_id>")

# Create a linked service definition for Data Lake Storage
linked_service = LinkedService(
    type='Microsoft.DataLakeStore',
    type_properties={
        'accountName': '<datalake_storage_account_name>'
    }
)

# Create the linked service
data_factory_client.linked_services.create_or_update(
    "<data_factory_name>",
    "DataLakeStoreLinkedService",
    linked_service
)
