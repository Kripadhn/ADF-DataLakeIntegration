To implement data processing using Azure Data Factory (ADF) and load into Data Lake Storage, you can follow these steps:

Log in to the Azure portal and go to your Azure Data Factory.

Create a source dataset: This is where your data is coming from. You can use a variety of sources including Azure Blob Storage, Azure SQL Database, etc. To create a dataset, go to the "Author & Monitor" section and click on "Datasets" on the left side panel. Click on the "New" button and select the type of dataset you want to create. Fill in the required information and click on "Create".

Create a destination dataset: This is where you want to store your processed data. The destination dataset can also be in Azure Blob Storage, Azure SQL Database, etc. To create a destination dataset, follow the same steps as creating the source dataset.

Create a pipeline: A pipeline is a logical grouping of activities that perform a certain task. To create a pipeline, go to the "Author & Monitor" section and click on "Pipelines" on the left side panel. Click on the "New" button and select the type of pipeline you want to create.

Add a data processing activity to the pipeline: You can use different data processing activities such as data transformation, data mapping, data filtering, etc. To add an activity to the pipeline, go to the "Author & Monitor" section and click on the pipeline you created. On the pipeline canvas, click on "New activity" and select the type of activity you want to add.

Connect the source and destination datasets to the data processing activity: To connect the datasets to the activity, click on the activity and select the source and destination datasets from the drop-down list.

Configure the data processing activity: Depending on the type of activity you selected, you may need to configure it to match your needs.

Save and publish the pipeline: Once you are satisfied with your pipeline, save and publish it.

Execute the pipeline: To execute the pipeline, go to the "Author & Monitor" section and click on the pipeline you created. Click on the "Publish all" button and then click on "Trigger now". The pipeline will start processing the data and loading it into the destination dataset.