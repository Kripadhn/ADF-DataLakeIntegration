{
    "name": "SourceDatasetName",
    "properties": {
        "type": "Microsoft.DataFactory/datasets",
        "linkedServiceName": "SourceLinkedServiceName",
        "typeProperties": {
            "fileName": "SourceFileName",
            "folderPath": "SourceFolderPath",
            "format": {
                "type": "TextFormat",
                "columnDelimiter": ","
            }
        },
        "schema": [
            {
                "name": "Column1Name",
                "type": "String"
            },
            {
                "name": "Column2Name",
                "type": "Int32"
            }
        ]
    }
}
