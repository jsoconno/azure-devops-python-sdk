from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import os

# Fill in with your personal access token and org URL
personal_access_token = os.environ.get('PAT')
organization_url = os.environ.get('ORG')

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

client = connection.clients.get_accounts_client()
accounts = client.get_accounts()

# for account in accounts:
#     print(account)
