{
    "name": "PipelineName",
    "properties": {
        "activities": [
            {
                "name": "CopyActivityName",
                "type": "Copy",
                "inputs": [
                    {
                        "name": "SourceDatasetName"
                    }
                ],
                "outputs": [
                    {
                        "name": "DestinationDatasetName"
                    }
                ],
                "typeProperties": {
                    "source": {
                        "type": "TabularSource"
                    },
                    "sink": {
                        "type": "TabularSink",
                        "writeBatchSize": 0,
                        "writeBatchTimeout": "00:00:00"
                    }
                }
            }
        ]
    }
}
