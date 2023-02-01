{
    "name": "DataProcessingActivity",
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
            "type": "DatasetReference",
            "referenceName": "SourceDatasetName"
        },
        "sink": {
            "type": "DatasetReference",
            "referenceName": "DestinationDatasetName"
        },
        "transformation": {
            "type": "DataFlow",
            "sink": {
                "type": "DatasetReference",
                "referenceName": "DestinationDatasetName"
            }
        }
    }
}
