from azure.datafactory.models import CopyActivity, CopySource, CopySink

# Define the source and destination of the copy
copy_source = CopySource(
    type="<source_type>",
    <source_details>
)
copy_sink = CopySink(
    type="<destination_type>",
    <destination_details>
)

# Create the copy activity
copy_activity = CopyActivity(
    name="<copy_activity_name>",
    source=copy_source,
    sink=copy_sink
)
