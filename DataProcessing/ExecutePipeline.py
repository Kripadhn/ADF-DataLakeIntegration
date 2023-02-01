pipeline = adf_client.pipelines.create_or_update(
    resource_group_name,
    data_factory_name,
    pipeline_name,
    pipeline_definition
)
