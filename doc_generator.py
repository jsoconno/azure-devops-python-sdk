from helpers import to_dict_recursive, flatten_dict, get_methods, get_arguments, create_docs
from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication

# Fill in with your personal access token and org URL
personal_access_token = 'your_pat'
organization_url = 'your_org'

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

# Example of how to write documentation to file
clients = get_methods(connection.clients)

header_content = '''
# Azure DevOps SDK for Python
This repo is documents all of python-sdk clients as well as their methods and attributes.  It was created to help those looking to get started with this development kit by providing more information about each client to a new user and real world examples to help you get started.

For more information, check out the original repo here:
https://github.com/microsoft/azure-devops-python-api

# Table of Contents
* [Getting Started](#getting-started)
* [Installing the SDK](#installing-the-sdk)
* [Authenticating with an Azure DevOps PAT Token](#authenticating-with-an-azure-devops-pat-token)
* [Using a Client](#using-a-client)
* [Clients](#clients)
* [Get Accounts Client](#get-accounts-client)
* [Get Build Client](#get-build-client)
* [Get Cloud Load Test Client](#get-cloud-load-test-client)
* [Get Core Client](#get-core-client)
* [Get Git Client](#get-git-client)
* [Get Identity Client](#get-identity-client)
* [Get Notification Client](#get-notification-client)
* [Get Operations Client](#get-operations-client)
* [Get Policy Client](#get-policy-client)
* [Get Profile Client](#get-profile-client)
* [Get Release Client](#get-release-client)
* [Get Security Client](#get-security-client)
* [Get Service Hooks Client](#get-service-hooks-client)
* [Get Task Agent Client](#get-task-agent-client)
* [Get Task Client](#get-task-client)
* [Get Test Client](#get-test-client)
* [Get Test Plan Client](#get-test-plan-client)
* [Get Test Results Client](#get-test-results-client)
* [Get Tfvc Client](#get-tfvc-client)
* [Get Wiki Client](#get-wiki-client)
* [Get Work Client](#get-work-client)
* [Get Work Item Tracking Client](#get-work-item-tracking-client)

# Getting Started
## Installing the SDK
Open the terminal and type the following command:

`pip install azure-devops`

## Authenticating with an Azure DevOps PAT Token
To use the API, establish a connection using a personal access token and the URL to your Azure DevOps organization. Then get a client from the connection and make API calls.

```
from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication

# Fill in with your personal access token and org URL
personal_access_token = 'your_pat'
organization_url = 'your_org'

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)
```

## Using a Client
Now you can use this connection to connect with a client.  Here is a basic example:

```
# Get the Git client
git_client = connection.clients.get_git_client()

# Get all repositories with the get_repositories() method
repos = git_client.get_repositories()

# Print all repository ids using the .id attribute
for repo in repos:
    print(repo.id)
```

More examples can be found in this repository or at https://github.com/Microsoft/azure-devops-python-samples.

# Clients
Details on  each client can be found in this section.
'''

f = open('README.md', 'w')
documentation = header_content

for client in clients:
    try:
        current_client = getattr(connection.clients, client)()
        documentation += create_docs(current_client,
                                     client, output_markup=True)
    except Exception as e:
        print(e)

f.write(documentation)
