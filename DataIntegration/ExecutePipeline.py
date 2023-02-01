from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.common.credentials import ServicePrincipalCredentials

# Create a Data Factory Management Client
credentials = ServicePrincipalCredentials(
    client_id="<client_id>",
    secret="<client_secret>",
    tenant="<tenant_id>"
)
data_factory_client = DataFactoryManagementClient(credentials, "<subscription_id
