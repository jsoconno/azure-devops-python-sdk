from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import pandas as pd
import datetime

# Fill in with your personal access token and org URL
personal_access_token = 'your_pat'
organization_url = 'your_org'

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

client = connection.clients.get_policy_client()
policy_configurations = client.get_policy_configurations(
    project="KpmgAdvisoryCloud")

for policy_configuration in policy_configurations.value:
    print(policy_configuration)
