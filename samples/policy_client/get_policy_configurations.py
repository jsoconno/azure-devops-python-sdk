from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import os
import pandas as pd
import datetime


def to_dict_recursive(obj, classkey=None):
    '''
    Recusively converts DevOps objects to dictionaries.
    obj: The DevOps object to convert.
    '''
    if isinstance(obj, dict):
        data = {}
        for (k, v) in obj.items():
            data[k] = to_dict_recursive(v, classkey)
        return data
    elif hasattr(obj, "_ast"):
        return to_dict_recursive(obj._ast())
    elif hasattr(obj, "__iter__") and not isinstance(obj, str):
        return [to_dict_recursive(v, classkey) for v in obj]
    elif hasattr(obj, "__dict__"):
        data = dict([(key, to_dict_recursive(value, classkey))
                     for key, value in obj.__dict__.items()
                     if not callable(value) and not key.startswith('_')])
        if classkey is not None and hasattr(obj, "__class__"):
            data[classkey] = obj.__class__.__name__
        return data
    else:
        return obj


def flatten_dict(nested_dict, separator='.', prefix=''):
    '''
    Recursively flattens a nested dictionary.
    nested_dict: The nested dictionary to be flattened.
    separator: The seperator to be used when renaming keys in the flattened dictionary.
    '''
    return {prefix + separator + k if prefix else k: v
            for kk, vv in nested_dict.items()
            for k, v in flatten_dict(vv, separator, kk).items()
            } if isinstance(nested_dict, dict) else {prefix: nested_dict}


# Fill in with your personal access token and org URL
personal_access_token = os.environ.get('PAT')
organization_url = os.environ.get('ORG')

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

client = connection.clients.get_policy_client()
policy_configurations = client.get_policy_configurations(
    project="KpmgAdvisoryCloud")

for policy_configuration in policy_configurations.value:
    print(policy_configuration)
