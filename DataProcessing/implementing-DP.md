To implement data processing using ADF and loading into Data Lake Storage, follow these steps:

Create a data source:
In Azure Data Factory, create a new data source connection to the source data, for example a database, an on-premises file server, or cloud storage.
Create a data sink:
In Azure Data Factory, create a new data sink connection to Data Lake Storage, where the processed data will be stored.
Create a pipeline:
In Azure Data Factory, create a new pipeline.
Create a dataset:
In Azure Data Factory, create a new dataset that represents the source data.

Map the columns in the source dataset to the columns in the destination dataset.

Create a data processing activity:
In the pipeline, add a new data processing activity, for example, a SQL script or a custom .NET code activity, to process the data.
Link the data source and data sink to the pipeline:
Connect the source dataset and the processed data to the pipeline.
Execute the pipeline:
Click on the 'Debug' button in the pipeline menu and select the 'Debug' option.

Wait for the pipeline to finish executing.

Monitor the pipeline execution:
Go to the 'Monitor and Manage' section of Azure Data Factory and view the status of the pipeline execution.

After the pipeline has completed executing, verify the data in Data Lake Storage to see if it has been successfully processed and loaded.

Note: The actual code for implementing data processing will vary depending on the type of data processing activity used, but the overall process remains the same.