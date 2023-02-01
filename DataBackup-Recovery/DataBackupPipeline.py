# Import necessary libraries
import azure.mgmt.datafactory.models as models
import azure.mgmt.datafactory.operations as operations
from azure.mgmt.datafactory.operations import DataFactoryOperations
from azure.mgmt.datafactory import DataFactoryManagementClient

# Create a Data Factory management client
adf_client = DataFactoryManagementClient(credentials, subscription_id)

# Create an Azure Data Factory
adf_name = '<your_adf_name>'
location = '<your_location>'
adf_resource_group = '<your_resource_group_name>'
adf = models.DataFactory(location=location)
adf_client.factories.create_or_update(adf_resource_group, adf_name, adf)

# Create a Data Lake Storage linked service
dls_linked_service = models.LinkedService(
    type='AzureDataLakeStore',
    connection_string=dls_connection_string
)
dls_linked_service_name = '<your_dls_linked_service_name>'
adf_client.linked_services.create_or_update(adf_resource_group, adf_name, dls_linked_service_name, dls_linked_service)

# Create an input dataset
input_data_set = models.Dataset(
    type='AzureDataLakeStore',
    linked_service_name=dls_linked_service_name,
    structure=[
        {
            "name": "Column1",
            "type": "String"
        },
        {
            "name": "Column2",
            "type": "Int32"
        }
    ],
    location={"fileSystem": dls_file_system, "path": dls_input_folder}
)
input_data_set_name = '<your_input_dataset_name>'
adf_client.datasets.create_or_update(adf_resource_group, adf_name, input_data_set_name, input_data_set)

# Create an output dataset
output_data_set = models.Dataset(
type='AzureDataLakeStore',
linked_service_name=dls_linked_service_name,
structure=[
{
"name": "Column1",
"type": "String"
},
{
"name": "Column2",
"type": "Int32"
}
],
location={"fileSystem": dls_file_system, "path": dls_output_folder}
)
output_data_set_name = '<your_output_dataset_name>'
adf_client.datasets.create_or_update(adf_resource_group, adf_name, output_data_set_name, output_data_set)

# Create a pipeline
copy_activity = models.CopyActivity(
name='<your_copy_activity_name>',
input_dataset=input_data_set_name,
output_dataset=output_data_set_name,
source=models.Source(type='AzureDataLakeStore'),
sink=models.Sink(type='AzureDataLakeStore')
)
pipeline = models.Pipeline(activities=[copy_activity])
pipeline_name = '<your_pipeline_name>'
adf_client.pipelines.create_or_update(adf_resource_group, adf_name, pipeline_name, pipeline)

# Execute the pipeline
pipeline_run = adf_client.pipelines.create_run(adf_resource_group, adf_name, pipeline_name, models.Run())

# Above code creates an Azure Data Factory, a linked service for Data Lake Storage, input and output datasets, and a pipeline with a copy activity. Finally, it executes the pipeline to copy data from the input dataset to the output dataset in Data Lake Storage. You can modify this code as per your requirements and data sources.


# Recovery Pipeline Code:
# Create a linked service for input data source
input_data_source_linked_service_name = '<your_input_data_source_linked_service_name>'
input_data_source_linked_service = models.LinkedService(
    type='<your_input_data_source_type>',
    connection_string='<your_input_data_source_connection_string>'
)
adf_client.linked_services.create_or_update(adf_resource_group, adf_name, input_data_source_linked_service_name, input_data_source_linked_service)

# Create an input dataset
input_data_set = models.Dataset(
    type='<your_input_dataset_type>',
    linked_service_name=input_data_source_linked_service_name,
    location={"<input_dataset_location_property1>": "<input_dataset_location_value1>", "<input_dataset_location_property2>": "<input_dataset_location_value2>"}
)
input_data_set_name = '<your_input_dataset_name>'
adf_client.datasets.create_or_update(adf_resource_group, adf_name, input_data_set_name, input_data_set)

# Create an output dataset
output_data_set = models.Dataset(
    type='AzureDataLakeStore',
    linked_service_name=dls_linked_service_name,
    structure=[
        {
            "name": "Column1",
            "type": "String"
        },
        {
            "name": "Column2",
            "type": "Int32"
        }
    ],
    location={"fileSystem": dls_file_system, "path": dls_input_folder}
)
output_data_set_name = '<your_output_dataset_name>'
adf_client.datasets.create_or_update(adf_resource_group, adf_name, output_data_set_name, output_data_set)

# Create a pipeline
copy_activity = models.CopyActivity(
    name='<your_copy_activity_name>',
    input_dataset=input_data_set_name,
    output_dataset=output_data_set_name,
    source=models.Source(type='AzureDataLakeStore'),
    sink=models.Sink(type='<your_input_dataset_type>')
)
pipeline = models.Pipeline(activities=[copy_activity])
pipeline_name = '<your_pipeline_name>'
adf_client.pipelines.create_or_update(adf_resource_group, adf_name, pipeline_name, pipeline)

# Execute the pipeline
pipeline_run = adf_client.pipelines.create_run(adf_resource_group, adf_name)

# Trigger pipeline
# Get the pipeline run ID
pipeline_run = adf_client.pipelines.create_run(adf_resource_group, adf_name, pipeline_name)
pipeline_run_id = pipeline_run.run_id

# Wait for the pipeline run to complete
time.sleep(30)
pipeline_run = adf_client.pipeline_runs.get(adf_resource_group, adf_name, pipeline_run_id)
while pipeline_run.status not in ['Succeeded', 'Failed']:
    time.sleep(30)
    pipeline_run = adf_client.pipeline_runs.get(adf_resource_group, adf_name, pipeline_run_id)

# Check the pipeline run status
if pipeline_run.status == 'Succeeded':
    print('Pipeline run completed successfully!')
else:
    print('Pipeline run failed!')


# This code will wait for 30 seconds before checking the status of the pipeline run, and then continuously check the status until it's either succeeded or failed. 
# Once the pipeline run is complete, you can check the status to see if the data recovery was successful.

