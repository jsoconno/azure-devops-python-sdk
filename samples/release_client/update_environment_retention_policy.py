from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from azure.devops.v6_0.release.models import ReleaseDefinition, ReleaseDefinitionEnvironment
from azure.devops.v6_0.release.models import EnvironmentRetentionPolicy
import os
import pandas as pd
import datetime

# Fill in with your personal access token and org URL
personal_access_token = os.environ.get('PAT')
organization_url = os.environ.get('ORG')

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

client = connection.clients.get_release_client()
release_definitions = client.get_release_definitions(
    project="KpmgAdvisoryCloud")

for release_definition in release_definitions.value:
    if "sandbox-training-environment" in release_definition.name:
        # print(f'{release_definition.id}: {release_definition.name}')

        release_definition = client.get_release_definition(
            project="KpmgAdvisoryCloud",
            definition_id=release_definition.id
        )

        environments = []
        updates_required = False

        for environment in release_definition.environments:
            # print(f'-- {environment.name}: {environment.retention_policy}')

            if environment.retention_policy.days_to_keep != 365:
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
                updates_required = True
            else:
                environments.append(environment)
        # must set retention policy for each environment (stage)

        if updates_required:
            release_definition_update = ReleaseDefinition(
                description="This is a sandbox for training purposes",
                name=release_definition.name,
                id=release_definition.id,
                environments=environments,
                revision=release_definition.revision,
                release_name_format=release_definition.release_name_format,
                path=release_definition.path,
                artifacts=release_definition.artifacts,
                variable_groups=release_definition.variable_groups,
                variables=release_definition.variables,
                properties=release_definition.properties,
                comment="Automated update to pipeline from Release Bot.",
                url=release_definition.url,
            )

            try:
                client.update_release_definition(
                    release_definition=release_definition_update,
                    project="KpmgAdvisoryCloud"
                )

                print(
                    f'{release_definition.id}: {release_definition.name} has been updated.')
            except Exception as e:
                print(
                    f'{release_definition.id}: {release_definition.name} could not be updated.  {e}')
        else:
            print(
                f'{release_definition.id}: {release_definition.name} is already up-to-date.')
