from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from helpers import get_methods, get_arguments, to_dict_recursive, flatten_dict
import pandas as pd
import datetime

# Fill in with your personal access token and org URL
personal_access_token = 'your_pat'
organization_url = 'your_org'

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

client = connection.clients.get_release_client()
deployments = client.get_deployments(
    project="KpmgAdvisoryCloud")

data = []

# for release in releases:
index = 0
while deployments is not None:
    for deployment in deployments.value:
        r = to_dict_recursive(deployment)

        # Create this as a function later
        for k, v in r.items():
            if type(v) == list and len(v) > 0:
                r[k] = r[k][0]
            else:
                pass

        r = flatten_dict(r)
        data.append(r)

        print(index)
        index += 1

    if deployments.continuation_token is not None and deployments.continuation_token != "":
        deployments = client.get_deployments(
            project="KpmgAdvisoryCloud", continuation_token=deployments.continuation_token)
    else:
        deployments = None


df = pd.DataFrame.from_dict(data)
print(df.info())
df.to_csv('out.csv')

# for post_deploy_approval in r["post_deploy_approvals"]:
#     print(post_deploy_approval)
