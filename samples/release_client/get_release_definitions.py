from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from azure.devops.v6_0.release.models import ReleaseDefinition, ReleaseDefinitionEnvironment, EnvironmentRetentionPolicy
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

client = connection.clients.get_release_client()
release_definitions = client.get_release_definitions(
    project="KpmgAdvisoryCloud")

release_definition_list = []

for release_definition in release_definitions.value:
    release_definition_list.append(release_definition)
    print(f'{release_definition.id}: {release_definition.name}')

release_definition = client.get_release_definition(
    project="KpmgAdvisoryCloud",
    definition_id=266,
    property_filters=None
)

environments = []

for environment in release_definition.environments:
    environments.append(
        ReleaseDefinitionEnvironment(
            badge_url=environment.badge_url,
            conditions=environment.conditions,
            current_release=environment.current_release,
            demands=environment.demands,
            deploy_phases=environment.deploy_phases,
            deploy_step=environment.deploy_step,
            environment_options=environment.environment_options,
            environment_triggers=environment.environment_triggers,
            execution_policy=environment.execution_policy,
            id=environment.id,
            name=environment.name,
            owner=environment.owner,
            post_deploy_approvals=environment.post_deploy_approvals,
            post_deployment_gates=environment.post_deployment_gates,
            pre_deploy_approvals=environment.pre_deploy_approvals,
            pre_deployment_gates=environment.pre_deployment_gates,
            process_parameters=environment.process_parameters,
            properties=environment.properties,
            queue_id=environment.queue_id,
            rank=environment.rank,
            retention_policy=EnvironmentRetentionPolicy(
                days_to_keep=365,
                releases_to_keep=10,
                retain_build=True
            ),
            run_options=environment.run_options,
            schedules=environment.schedules,
            variable_groups=environment.variable_groups,
            variables=environment.variables
        )
    )
    # must set retention policy for each environment (stage)

release_definition_update = ReleaseDefinition(
    description="This is a demo project test.",
    name=release_definition.name,
    id=release_definition.id,
    environments=environments,
    revision=release_definition.revision,
    release_name_format=release_definition.release_name_format,
    # retention_policy=retention_policy,
)

client.update_release_definition(
    release_definition=release_definition_update,
    project="KpmgAdvisoryCloud"
)
