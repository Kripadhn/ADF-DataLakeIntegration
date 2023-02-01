from azure.datalake.store import DataLakeStoreAccount

# Connect to the Data Lake Storage account
dl_account = DataLakeStoreAccount("<account_name>.azuredatalakestore.net", "<client_id>", "<client_secret>", tenant="<tenant_id>")

# Load data into Data Lake Storage
dl_account.write("<path_to_data_lake_storage>/<data_file>", "<data_file_contents>")
