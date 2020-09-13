from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication

# Fill in with your personal access token and org URL
personal_access_token = 'your_pat'
organization_url = 'your_org'

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

client = connection.clients.get_accounts_client()
accounts = client.get_accounts()

# for account in accounts:
#     print(account)
