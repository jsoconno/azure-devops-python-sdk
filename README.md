
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
## Get Accounts Client

### GetAccounts
#### Description:
Get a list of accounts for a specific owner or a specific member.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| owner_id | str | ID for the owner of the accounts. |
| member_id | str | ID for a member of the accounts. |
| properties | str |  |
#### Return Type
[Account]
#### Example Usage
```

connection.clients.get_accounts_client().get_accounts(owner_id=None, member_id=None, properties=None)
```
## Get Build Client

### AddBuildTag
#### Description:
Adds a tag to a build.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| build_id | int | The ID of the build. |
| tag | str | The tag to add. |
#### Return Type
[str]
#### Example Usage
```

connection.clients.get_build_client().add_build_tag(project, build_id, tag)
```
### AddBuildTags
#### Description:
Adds tags to a build.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| tags | [str] | The tags to add. |
| project | str | Project ID or project name |
| build_id | int | The ID of the build. |
#### Return Type
[str]
#### Example Usage
```

connection.clients.get_build_client().add_build_tags(tags, project, build_id)
```
### CreateArtifact
#### Description:
Associates an artifact with a build.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| artifact | class | The artifact. |
| project | str | Project ID or project name |
| build_id | int | The ID of the build. |
#### Return Type
:class:<BuildArtifact> <azure.devops.v5_1.build.models.BuildArtifact>
#### Example Usage
```
from azure.devops.v5_1.build.models import BuildArtifact

connection.clients.get_build_client().create_artifact(artifact, project, build_id)
```
### CreateDefinition
#### Description:
Creates a new definition.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| definition | class | The definition. |
| project | str | Project ID or project name |
| definition_to_clone_id | int |  |
| definition_to_clone_revision | int |  |
#### Return Type
:class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition>
#### Example Usage
```
from azure.devops.v5_1.build.models import BuildDefinition

connection.clients.get_build_client().create_definition(definition, project, definition_to_clone_id=None, definition_to_clone_revision=None)
```
### DeleteBuild
#### Description:
Deletes a build.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| build_id | int | The ID of the build. |
#### Return Type
:class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition>
#### Example Usage
```

connection.clients.get_build_client().delete_build(project, build_id)
```
### DeleteBuildTag
#### Description:
Removes a tag from a build.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| build_id | int | The ID of the build. |
| tag | str | The tag to remove. |
#### Return Type
[str]
#### Example Usage
```

connection.clients.get_build_client().delete_build_tag(project, build_id, tag)
```
### DeleteDefinition
#### Description:
Deletes a definition and all associated builds.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| definition_id | int | The ID of the definition. |
#### Return Type
[str]
#### Example Usage
```

connection.clients.get_build_client().delete_definition(project, definition_id)
```
### DeleteTemplate
#### Description:
Deletes a build definition template.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| template_id | str | The ID of the template. |
#### Return Type
[str]
#### Example Usage
```

connection.clients.get_build_client().delete_template(project, template_id)
```
### GetArtifact
#### Description:
Gets a specific artifact for a build.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| build_id | int | The ID of the build. |
| artifact_name | str | The name of the artifact. |
#### Return Type
:class:<BuildArtifact> <azure.devops.v5_1.build.models.BuildArtifact>
#### Example Usage
```

connection.clients.get_build_client().get_artifact(project, build_id, artifact_name)
```
### GetArtifactContentZip
#### Description:
Gets a specific artifact for a build.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| build_id | int | The ID of the build. |
| artifact_name | str | The name of the artifact. |
#### Return Type
object
#### Example Usage
```

connection.clients.get_build_client().get_artifact_content_zip(project, build_id, artifact_name, **kwargs)
```
### GetArtifacts
#### Description:
Gets all artifacts for a build.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| build_id | int | The ID of the build. |
#### Return Type
[BuildArtifact]
#### Example Usage
```

connection.clients.get_build_client().get_artifacts(project, build_id)
```
### GetBuild
#### Description:
Gets a build
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| build_id | int |  |
| property_filters | str |  |
#### Return Type
:class:<Build> <azure.devops.v5_1.build.models.Build>
#### Example Usage
```

connection.clients.get_build_client().get_build(project, build_id, property_filters=None)
```
### GetBuildChanges
#### Description:
Gets the changes associated with a build
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| build_id | int |  |
| continuation_token | str |  |
| top | int | The maximum number of changes to return |
| include_source_change | bool |  |
#### Return Type
:class:<GetBuildChangesResponseValue>
#### Example Usage
```

connection.clients.get_build_client().get_build_changes(project, build_id, continuation_token=None, top=None, include_source_change=None)
```
### GetBuildController
#### Description:
Gets a controller
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| controller_id | int |  |
#### Return Type
:class:<BuildController> <azure.devops.v5_1.build.models.BuildController>
#### Example Usage
```

connection.clients.get_build_client().get_build_controller(controller_id)
```
### GetBuildControllers
#### Description:
Gets controller, optionally filtered by name
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| name | str |  |
#### Return Type
[BuildController]
#### Example Usage
```

connection.clients.get_build_client().get_build_controllers(name=None)
```
### GetBuildLog
#### Description:
Gets an individual log file for a build.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| build_id | int | The ID of the build. |
| log_id | int | The ID of the log file. |
| start_line | long | The start line. |
| end_line | long | The end line. |
#### Return Type
object
#### Example Usage
```

connection.clients.get_build_client().get_build_log(project, build_id, log_id, start_line=None, end_line=None, **kwargs)
```
### GetBuildLogLines
#### Description:
Gets an individual log file for a build.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| build_id | int | The ID of the build. |
| log_id | int | The ID of the log file. |
| start_line | long | The start line. |
| end_line | long | The end line. |
#### Return Type
[str]
#### Example Usage
```

connection.clients.get_build_client().get_build_log_lines(project, build_id, log_id, start_line=None, end_line=None)
```
### GetBuildLogZip
#### Description:
Gets an individual log file for a build.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| build_id | int | The ID of the build. |
| log_id | int | The ID of the log file. |
| start_line | long | The start line. |
| end_line | long | The end line. |
#### Return Type
object
#### Example Usage
```

connection.clients.get_build_client().get_build_log_zip(project, build_id, log_id, start_line=None, end_line=None, **kwargs)
```
### GetBuildLogs
#### Description:
Gets the logs for a build.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| build_id | int | The ID of the build. |
#### Return Type
[BuildLog]
#### Example Usage
```

connection.clients.get_build_client().get_build_logs(project, build_id)
```
### GetBuildLogsZip
#### Description:
Gets the logs for a build.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| build_id | int | The ID of the build. |
#### Return Type
object
#### Example Usage
```

connection.clients.get_build_client().get_build_logs_zip(project, build_id, **kwargs)
```
### GetBuildOptionDefinitions
#### Description:
Gets all build definition options supported by the system.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
#### Return Type
[BuildOptionDefinition]
#### Example Usage
```

connection.clients.get_build_client().get_build_option_definitions(project=None)
```
### GetBuildSettings
#### Description:
Gets the build settings.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
#### Return Type
:class:<BuildSettings> <azure.devops.v5_1.build.models.BuildSettings>
#### Example Usage
```

connection.clients.get_build_client().get_build_settings(project=None)
```
### GetBuildTags
#### Description:
Gets the tags for a build.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| build_id | int | The ID of the build. |
#### Return Type
[str]
#### Example Usage
```

connection.clients.get_build_client().get_build_tags(project, build_id)
```
### GetBuildTimeline
#### Description:
Gets details for a build
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| build_id | int |  |
| timeline_id | str |  |
| change_id | int |  |
| plan_id | str |  |
#### Return Type
:class:<Timeline> <azure.devops.v5_1.build.models.Timeline>
#### Example Usage
```

connection.clients.get_build_client().get_build_timeline(project, build_id, timeline_id=None, change_id=None, plan_id=None)
```
### GetBuildWorkItemsRefs
#### Description:
Gets the work items associated with a build.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| build_id | int | The ID of the build. |
| top | int | The maximum number of work items to return. |
#### Return Type
[ResourceRef]
#### Example Usage
```

connection.clients.get_build_client().get_build_work_items_refs(project, build_id, top=None)
```
### GetBuildWorkItemsRefsFromCommits
#### Description:
Gets the work items associated with a build, filtered to specific commits.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| commit_ids | [str] | A comma-delimited list of commit IDs. |
| project | str | Project ID or project name |
| build_id | int | The ID of the build. |
| top | int | The maximum number of work items to return, or the number of commits to consider if no commit IDs are specified. |
#### Return Type
[ResourceRef]
#### Example Usage
```

connection.clients.get_build_client().get_build_work_items_refs_from_commits(commit_ids, project, build_id, top=None)
```
### GetBuilds
#### Description:
Gets a list of builds.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| definitions | [int] | A comma-delimited list of definition IDs. If specified, filters to builds for these definitions. |
| queues | [int] | A comma-delimited list of queue IDs. If specified, filters to builds that ran against these queues. |
| build_number | str | If specified, filters to builds that match this build number. Append * to do a prefix search. |
| min_time | datetime | If specified, filters to builds that finished/started/queued after this date based on the queryOrder specified. |
| max_time | datetime | If specified, filters to builds that finished/started/queued before this date based on the queryOrder specified. |
| requested_for | str | If specified, filters to builds requested for the specified user. |
| reason_filter | str | If specified, filters to builds that match this reason. |
| status_filter | str | If specified, filters to builds that match this status. |
| result_filter | str | If specified, filters to builds that match this result. |
| tag_filters | [str] | A comma-delimited list of tags. If specified, filters to builds that have the specified tags. |
| properties | [str] | A comma-delimited list of properties to retrieve. |
| top | int | The maximum number of builds to return. |
| continuation_token | str | A continuation token, returned by a previous call to this method, that can be used to return the next set of builds. |
| max_builds_per_definition | int | The maximum number of builds to return per definition. |
| deleted_filter | str | Indicates whether to exclude, include, or only return deleted builds. |
| query_order | str | The order in which builds should be returned. |
| branch_name | str | If specified, filters to builds that built branches that built this branch. |
| build_ids | [int] | A comma-delimited list that specifies the IDs of builds to retrieve. |
| repository_id | str | If specified, filters to builds that built from this repository. |
| repository_type | str | If specified, filters to builds that built from repositories of this type. |
#### Return Type
:class:<GetBuildsResponseValue>
#### Example Usage
```

connection.clients.get_build_client().get_builds(project, definitions=None, queues=None, build_number=None, min_time=None, max_time=None, requested_for=None, reason_filter=None, status_filter=None, result_filter=None, tag_filters=None, properties=None, top=None, continuation_token=None, max_builds_per_definition=None, deleted_filter=None, query_order=None, branch_name=None, build_ids=None, repository_id=None, repository_type=None)
```
### GetDefinition
#### Description:
Gets a definition, optionally at a specific revision.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| definition_id | int | The ID of the definition. |
| revision | int | The revision number to retrieve. If this is not specified, the latest version will be returned. |
| min_metrics_time | datetime | If specified, indicates the date from which metrics should be included. |
| property_filters | [str] | A comma-delimited list of properties to include in the results. |
| include_latest_builds | bool |  |
#### Return Type
:class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition>
#### Example Usage
```

connection.clients.get_build_client().get_definition(project, definition_id, revision=None, min_metrics_time=None, property_filters=None, include_latest_builds=None)
```
### GetDefinitionRevisions
#### Description:
Gets all revisions of a definition.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| definition_id | int | The ID of the definition. |
#### Return Type
[BuildDefinitionRevision]
#### Example Usage
```

connection.clients.get_build_client().get_definition_revisions(project, definition_id)
```
### GetDefinitions
#### Description:
Gets a list of definitions.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| name | str | If specified, filters to definitions whose names match this pattern. |
| repository_id | str | A repository ID. If specified, filters to definitions that use this repository. |
| repository_type | str | If specified, filters to definitions that have a repository of this type. |
| query_order | str | Indicates the order in which definitions should be returned. |
| top | int | The maximum number of definitions to return. |
| continuation_token | str | A continuation token, returned by a previous call to this method, that can be used to return the next set of definitions. |
| min_metrics_time | datetime | If specified, indicates the date from which metrics should be included. |
| definition_ids | [int] | A comma-delimited list that specifies the IDs of definitions to retrieve. |
| path | str | If specified, filters to definitions under this folder. |
| built_after | datetime | If specified, filters to definitions that have builds after this date. |
| not_built_after | datetime | If specified, filters to definitions that do not have builds after this date. |
| include_all_properties | bool | Indicates whether the full definitions should be returned. By default, shallow representations of the definitions are returned. |
| include_latest_builds | bool | Indicates whether to return the latest and latest completed builds for this definition. |
| task_id_filter | str | If specified, filters to definitions that use the specified task. |
| process_type | int | If specified, filters to definitions with the given process type. |
| yaml_filename | str | If specified, filters to YAML definitions that match the given filename. |
#### Return Type
:class:<GetDefinitionsResponseValue>
#### Example Usage
```

connection.clients.get_build_client().get_definitions(project, name=None, repository_id=None, repository_type=None, query_order=None, top=None, continuation_token=None, min_metrics_time=None, definition_ids=None, path=None, built_after=None, not_built_after=None, include_all_properties=None, include_latest_builds=None, task_id_filter=None, process_type=None, yaml_filename=None)
```
### GetFile
#### Description:
Gets a file from the build.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| build_id | int | The ID of the build. |
| artifact_name | str | The name of the artifact. |
| file_id | str | The primary key for the file. |
| file_name | str | The name that the file will be set to. |
#### Return Type
object
#### Example Usage
```

connection.clients.get_build_client().get_file(project, build_id, artifact_name, file_id, file_name, **kwargs)
```
### GetTags
#### Description:
Gets a list of all build and definition tags in the project.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
#### Return Type
[str]
#### Example Usage
```

connection.clients.get_build_client().get_tags(project)
```
### GetTemplate
#### Description:
Gets a specific build definition template.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| template_id | str | The ID of the requested template. |
#### Return Type
:class:<BuildDefinitionTemplate> <azure.devops.v5_1.build.models.BuildDefinitionTemplate>
#### Example Usage
```

connection.clients.get_build_client().get_template(project, template_id)
```
### GetTemplates
#### Description:
Gets all definition templates.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
#### Return Type
[BuildDefinitionTemplate]
#### Example Usage
```

connection.clients.get_build_client().get_templates(project)
```
### QueueBuild
#### Description:
Queues a build
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| build | class |  |
| project | str | Project ID or project name |
| ignore_warnings | bool |  |
| check_in_ticket | str |  |
| source_build_id | int |  |
#### Return Type
:class:<Build> <azure.devops.v5_1.build.models.Build>
#### Example Usage
```
from azure.devops.v5_1.build.models import Build

connection.clients.get_build_client().queue_build(build, project, ignore_warnings=None, check_in_ticket=None, source_build_id=None)
```
### RestoreDefinition
#### Description:
Restores a deleted definition
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| definition_id | int | The identifier of the definition to restore. |
| deleted | bool | When false, restores a deleted definition. |
#### Return Type
:class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition>
#### Example Usage
```

connection.clients.get_build_client().restore_definition(project, definition_id, deleted)
```
### SaveTemplate
#### Description:
Updates an existing build definition template.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| template | class | The new version of the template. |
| project | str | Project ID or project name |
| template_id | str | The ID of the template. |
#### Return Type
:class:<BuildDefinitionTemplate> <azure.devops.v5_1.build.models.BuildDefinitionTemplate>
#### Example Usage
```
from azure.devops.v5_1.build.models import BuildDefinitionTemplate

connection.clients.get_build_client().save_template(template, project, template_id)
```
### UpdateBuild
#### Description:
Updates a build.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| build | class | The build. |
| project | str | Project ID or project name |
| build_id | int | The ID of the build. |
| retry | bool |  |
#### Return Type
:class:<Build> <azure.devops.v5_1.build.models.Build>
#### Example Usage
```
from azure.devops.v5_1.build.models import Build

connection.clients.get_build_client().update_build(build, project, build_id, retry=None)
```
### UpdateBuildSettings
#### Description:
Updates the build settings.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| settings | class | The new settings. |
| project | str | Project ID or project name |
#### Return Type
:class:<BuildSettings> <azure.devops.v5_1.build.models.BuildSettings>
#### Example Usage
```
from azure.devops.v5_1.build.models import BuildSettings

connection.clients.get_build_client().update_build_settings(settings, project=None)
```
### UpdateBuilds
#### Description:
Updates multiple builds.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| builds | [Build] | The builds to update. |
| project | str | Project ID or project name |
#### Return Type
[Build]
#### Example Usage
```

connection.clients.get_build_client().update_builds(builds, project)
```
### UpdateDefinition
#### Description:
Updates an existing definition.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| definition | class | The new version of the definition. |
| project | str | Project ID or project name |
| definition_id | int | The ID of the definition. |
| secrets_source_definition_id | int |  |
| secrets_source_definition_revision | int |  |
#### Return Type
:class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition>
#### Example Usage
```
from azure.devops.v5_1.build.models import BuildDefinition

connection.clients.get_build_client().update_definition(definition, project, definition_id, secrets_source_definition_id=None, secrets_source_definition_revision=None)
```
## Get Core Client

### CreateTeam
#### Description:
Create a team in a team project.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| team | class | The team data used to create the team. |
| project_id | str | The name or ID (GUID) of the team project in which to create the team. |
#### Return Type
:class:<WebApiTeam> <azure.devops.v5_1.core.models.WebApiTeam>
#### Example Usage
```
from azure.devops.v5_1.core.models import WebApiTeam

connection.clients.get_core_client().create_team(team, project_id)
```
### DeleteTeam
#### Description:
Delete a team.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project_id | str | The name or ID (GUID) of the team project containing the team to delete. |
| team_id | str | The name or ID of the team to delete. |
#### Return Type
:class:<WebApiTeam> <azure.devops.v5_1.core.models.WebApiTeam>
#### Example Usage
```

connection.clients.get_core_client().delete_team(project_id, team_id)
```
### GetProcessById
#### Description:
Get a process by ID.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| process_id | str | ID for a process. |
#### Return Type
:class:<Process> <azure.devops.v5_1.core.models.Process>
#### Example Usage
```

connection.clients.get_core_client().get_process_by_id(process_id)
```
### GetProcesses
#### Description:
Get a list of processes.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
#### Return Type
[Process]
#### Example Usage
```

connection.clients.get_core_client().get_processes()
```
### GetProject
#### Description:
Get project with the specified id or name, optionally including capabilities.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project_id | str |  |
| include_capabilities | bool | Include capabilities (such as source control) in the team project result (default: false). |
| include_history | bool | Search within renamed projects (that had such name in the past). |
#### Return Type
:class:<TeamProject> <azure.devops.v5_1.core.models.TeamProject>
#### Example Usage
```

connection.clients.get_core_client().get_project(project_id, include_capabilities=None, include_history=None)
```
### GetProjectCollection
#### Description:
Get project collection with the specified id or name.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| collection_id | str |  |
#### Return Type
:class:<TeamProjectCollection> <azure.devops.v5_1.core.models.TeamProjectCollection>
#### Example Usage
```

connection.clients.get_core_client().get_project_collection(collection_id)
```
### GetProjectCollections
#### Description:
Get project collection references for this application.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| top | int |  |
| skip | int |  |
#### Return Type
[TeamProjectCollectionReference]
#### Example Usage
```

connection.clients.get_core_client().get_project_collections(top=None, skip=None)
```
### GetProjects
#### Description:
Get all projects in the organization that the authenticated user has access to.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| state_filter | str | Filter on team projects in a specific team project state (default: WellFormed). |
| top | int |  |
| skip | int |  |
| continuation_token | str |  |
| get_default_team_image_url | bool |  |
#### Return Type
:class:<GetProjectsResponseValue>
#### Example Usage
```

connection.clients.get_core_client().get_projects(state_filter=None, top=None, skip=None, continuation_token=None, get_default_team_image_url=None)
```
### GetTeam
#### Description:
Get a specific team.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project_id | str | The name or ID (GUID) of the team project containing the team. |
| team_id | str | The name or ID (GUID) of the team. |
| expand_identity | bool | A value indicating whether or not to expand Identity information in the result WebApiTeam object. |
#### Return Type
:class:<WebApiTeam> <azure.devops.v5_1.core.models.WebApiTeam>
#### Example Usage
```

connection.clients.get_core_client().get_team(project_id, team_id, expand_identity=None)
```
### GetTeamMembersWithExtendedProperties
#### Description:
Get a list of members for a specific team.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project_id | str | The name or ID (GUID) of the team project the team belongs to. |
| team_id | str | The name or ID (GUID) of the team . |
| top | int |  |
| skip | int |  |
#### Return Type
[TeamMember]
#### Example Usage
```

connection.clients.get_core_client().get_team_members_with_extended_properties(project_id, team_id, top=None, skip=None)
```
### GetTeams
#### Description:
Get a list of teams.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project_id | str |  |
| mine | bool | If true return all the teams requesting user is member, otherwise return all the teams user has read access. |
| top | int | Maximum number of teams to return. |
| skip | int | Number of teams to skip. |
| expand_identity | bool | A value indicating whether or not to expand Identity information in the result WebApiTeam object. |
#### Return Type
[WebApiTeam]
#### Example Usage
```

connection.clients.get_core_client().get_teams(project_id, mine=None, top=None, skip=None, expand_identity=None)
```
### QueueCreateProject
#### Description:
Queues a project to be created. Use the [GetOperation](../../operations/operations/get) to periodically check for create project status.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project_to_create | class | The project to create. |
#### Return Type
:class:<OperationReference> <azure.devops.v5_1.core.models.OperationReference>
#### Example Usage
```
from azure.devops.v5_1.core.models import TeamProject

connection.clients.get_core_client().queue_create_project(project_to_create)
```
### QueueDeleteProject
#### Description:
Queues a project to be deleted. Use the [GetOperation](../../operations/operations/get) to periodically check for delete project status.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project_id | str | The project id of the project to delete. |
#### Return Type
:class:<OperationReference> <azure.devops.v5_1.core.models.OperationReference>
#### Example Usage
```

connection.clients.get_core_client().queue_delete_project(project_id)
```
### UpdateProject
#### Description:
Update an existing project's name, abbreviation, description, or restore a project.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project_update | class | The updates for the project. The state must be set to wellFormed to restore the project. |
| project_id | str | The project id of the project to update. |
#### Return Type
:class:<OperationReference> <azure.devops.v5_1.core.models.OperationReference>
#### Example Usage
```
from azure.devops.v5_1.core.models import TeamProject

connection.clients.get_core_client().update_project(project_update, project_id)
```
### UpdateTeam
#### Description:
Update a team's name and/or description.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| team_data | class |  |
| project_id | str | The name or ID (GUID) of the team project containing the team to update. |
| team_id | str | The name of ID of the team to update. |
#### Return Type
:class:<WebApiTeam> <azure.devops.v5_1.core.models.WebApiTeam>
#### Example Usage
```
from azure.devops.v5_1.core.models import WebApiTeam

connection.clients.get_core_client().update_team(team_data, project_id, team_id)
```
## Get Git Client

### CreateComment
#### Description:
Create a comment on a specific thread in a pull request (up to 500 comments can be created per thread).
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| comment | class | The comment to create. Comments can be up to 150,000 characters. |
| repository_id | str | The repository ID of the pull request's target branch. |
| pull_request_id | int | ID of the pull request. |
| thread_id | int | ID of the thread that the desired comment is in. |
| project | str | Project ID or project name |
#### Return Type
:class:<Comment> <azure.devops.v5_1.git.models.Comment>
#### Example Usage
```
from azure.devops.v5_1.git.models import Comment

connection.clients.get_git_client().create_comment(comment, repository_id, pull_request_id, thread_id, project=None)
```
### CreateCommitStatus
#### Description:
Create Git commit status.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| git_commit_status_to_create | class | Git commit status object to create. |
| commit_id | str | ID of the Git commit. |
| repository_id | str | ID of the repository. |
| project | str | Project ID or project name |
#### Return Type
:class:<GitStatus> <azure.devops.v5_1.git.models.GitStatus>
#### Example Usage
```
from azure.devops.v5_1.git.models import GitStatus

connection.clients.get_git_client().create_commit_status(git_commit_status_to_create, commit_id, repository_id, project=None)
```
### CreatePullRequest
#### Description:
Create a pull request.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| git_pull_request_to_create | class | The pull request to create. |
| repository_id | str | The repository ID of the pull request's target branch. |
| project | str | Project ID or project name |
| supports_iterations | bool | If true, subsequent pushes to the pull request will be individually reviewable. Set this to false for large pull requests for performance reasons if this functionality is not needed. |
#### Return Type
:class:<GitPullRequest> <azure.devops.v5_1.git.models.GitPullRequest>
#### Example Usage
```
from azure.devops.v5_1.git.models import GitPullRequest

connection.clients.get_git_client().create_pull_request(git_pull_request_to_create, repository_id, project=None, supports_iterations=None)
```
### CreatePullRequestReviewer
#### Description:
Add a reviewer to a pull request or cast a vote.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| reviewer | class | Reviewer's vote.<br />If the reviewer's ID is included here, it must match the reviewerID parameter.<br />Reviewers can set their own vote with this method.  When adding other reviewers, vote must be set to zero. |
| repository_id | str | The repository ID of the pull request’s target branch. |
| pull_request_id | int | ID of the pull request. |
| reviewer_id | str | ID of the reviewer. |
| project | str | Project ID or project name |
#### Return Type
:class:<IdentityRefWithVote> <azure.devops.v5_1.git.models.IdentityRefWithVote>
#### Example Usage
```
from azure.devops.v5_1.git.models>` reviewer: Reviewer's vote.<br />If the reviewer's ID is included here, it must match the reviewerID parameter.<br / import IdentityRefWithVote

connection.clients.get_git_client().create_pull_request_reviewer(reviewer, repository_id, pull_request_id, reviewer_id, project=None)
```
### CreatePullRequestReviewers
#### Description:
Add reviewers to a pull request.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| reviewers | [IdentityRef] | Reviewers to add to the pull request. |
| repository_id | str | The repository ID of the pull request’s target branch. |
| pull_request_id | int | ID of the pull request. |
| project | str | Project ID or project name |
#### Return Type
[IdentityRefWithVote]
#### Example Usage
```

connection.clients.get_git_client().create_pull_request_reviewers(reviewers, repository_id, pull_request_id, project=None)
```
### CreatePush
#### Description:
Push changes to the repository.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| push | class |  |
| repository_id | str | The name or ID of the repository. |
| project | str | Project ID or project name |
#### Return Type
:class:<GitPush> <azure.devops.v5_1.git.models.GitPush>
#### Example Usage
```
from azure.devops.v5_1.git.models import GitPush

connection.clients.get_git_client().create_push(push, repository_id, project=None)
```
### CreateRepository
#### Description:
Create a git repository in a team project.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| git_repository_to_create | class | Specify the repo name, team project and/or parent repository. Team project information can be omitted from gitRepositoryToCreate if the request is project-scoped (i.e., includes project Id). |
| project | str | Project ID or project name |
| source_ref | str | [optional] Specify the source refs to use while creating a fork repo |
#### Return Type
:class:<GitRepository> <azure.devops.v5_1.git.models.GitRepository>
#### Example Usage
```
from azure.devops.v5_1.git.models import GitRepositoryCreateOptions

connection.clients.get_git_client().create_repository(git_repository_to_create, project=None, source_ref=None)
```
### CreateThread
#### Description:
Create a thread in a pull request.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| comment_thread | class | The thread to create. Thread must contain at least one comment. |
| repository_id | str | Repository ID of the pull request's target branch. |
| pull_request_id | int | ID of the pull request. |
| project | str | Project ID or project name |
#### Return Type
:class:<GitPullRequestCommentThread> <azure.devops.v5_1.git.models.GitPullRequestCommentThread>
#### Example Usage
```
from azure.devops.v5_1.git.models import GitPullRequestCommentThread

connection.clients.get_git_client().create_thread(comment_thread, repository_id, pull_request_id, project=None)
```
### DeleteComment
#### Description:
Delete a comment associated with a specific thread in a pull request.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The repository ID of the pull request's target branch. |
| pull_request_id | int | ID of the pull request. |
| thread_id | int | ID of the thread that the desired comment is in. |
| comment_id | int | ID of the comment. |
| project | str | Project ID or project name |
#### Return Type
:class:<GitPullRequestCommentThread> <azure.devops.v5_1.git.models.GitPullRequestCommentThread>
#### Example Usage
```

connection.clients.get_git_client().delete_comment(repository_id, pull_request_id, thread_id, comment_id, project=None)
```
### DeletePullRequestReviewer
#### Description:
Remove a reviewer from a pull request.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The repository ID of the pull request’s target branch. |
| pull_request_id | int | ID of the pull request. |
| reviewer_id | str | ID of the reviewer to remove. |
| project | str | Project ID or project name |
#### Return Type
:class:<GitPullRequestCommentThread> <azure.devops.v5_1.git.models.GitPullRequestCommentThread>
#### Example Usage
```

connection.clients.get_git_client().delete_pull_request_reviewer(repository_id, pull_request_id, reviewer_id, project=None)
```
### DeleteRepository
#### Description:
Delete a git repository
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The name or ID of the repository. |
| project | str | Project ID or project name |
#### Return Type
:class:<GitPullRequestCommentThread> <azure.devops.v5_1.git.models.GitPullRequestCommentThread>
#### Example Usage
```

connection.clients.get_git_client().delete_repository(repository_id, project=None)
```
### GetBlob
#### Description:
Get a single blob.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The name or ID of the repository. |
| sha1 | str | SHA1 hash of the file. You can get the SHA1 of a file using the "Git/Items/Get Item" endpoint. |
| project | str | Project ID or project name |
| download | bool | If true, prompt for a download rather than rendering in a browser. Note: this value defaults to true if $format is zip |
| file_name | str | Provide a fileName to use for a download. |
| resolve_lfs | bool | If true, try to resolve a blob to its LFS contents, if it's an LFS pointer file. Only compatible with octet-stream Accept headers or $format types |
#### Return Type
:class:<GitBlobRef> <azure.devops.v5_1.git.models.GitBlobRef>
#### Example Usage
```

connection.clients.get_git_client().get_blob(repository_id, sha1, project=None, download=None, file_name=None, resolve_lfs=None)
```
### GetBlobContent
#### Description:
Get a single blob.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The name or ID of the repository. |
| sha1 | str | SHA1 hash of the file. You can get the SHA1 of a file using the "Git/Items/Get Item" endpoint. |
| project | str | Project ID or project name |
| download | bool | If true, prompt for a download rather than rendering in a browser. Note: this value defaults to true if $format is zip |
| file_name | str | Provide a fileName to use for a download. |
| resolve_lfs | bool | If true, try to resolve a blob to its LFS contents, if it's an LFS pointer file. Only compatible with octet-stream Accept headers or $format types |
#### Return Type
object
#### Example Usage
```

connection.clients.get_git_client().get_blob_content(repository_id, sha1, project=None, download=None, file_name=None, resolve_lfs=None, **kwargs)
```
### GetBlobZip
#### Description:
Get a single blob.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The name or ID of the repository. |
| sha1 | str | SHA1 hash of the file. You can get the SHA1 of a file using the "Git/Items/Get Item" endpoint. |
| project | str | Project ID or project name |
| download | bool | If true, prompt for a download rather than rendering in a browser. Note: this value defaults to true if $format is zip |
| file_name | str | Provide a fileName to use for a download. |
| resolve_lfs | bool | If true, try to resolve a blob to its LFS contents, if it's an LFS pointer file. Only compatible with octet-stream Accept headers or $format types |
#### Return Type
object
#### Example Usage
```

connection.clients.get_git_client().get_blob_zip(repository_id, sha1, project=None, download=None, file_name=None, resolve_lfs=None, **kwargs)
```
### GetBlobsZip
#### Description:
Gets one or more blobs in a zip file download.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| blob_ids | [str] | Blob IDs (SHA1 hashes) to be returned in the zip file. |
| repository_id | str | The name or ID of the repository. |
| project | str | Project ID or project name |
| filename | str |  |
#### Return Type
object
#### Example Usage
```

connection.clients.get_git_client().get_blobs_zip(blob_ids, repository_id, project=None, filename=None, **kwargs)
```
### GetBranch
#### Description:
Retrieve statistics about a single branch.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The name or ID of the repository. |
| name | str | Name of the branch. |
| project | str | Project ID or project name |
| base_version_descriptor | class | Identifies the commit or branch to use as the base. |
#### Return Type
:class:<GitBranchStats> <azure.devops.v5_1.git.models.GitBranchStats>
#### Example Usage
```
from azure.devops.v5_1.git.models import GitVersionDescriptor

connection.clients.get_git_client().get_branch(repository_id, name, project=None, base_version_descriptor=None)
```
### GetBranches
#### Description:
Retrieve statistics about all branches within a repository.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The name or ID of the repository. |
| project | str | Project ID or project name |
| base_version_descriptor | class | Identifies the commit or branch to use as the base. |
#### Return Type
[GitBranchStats]
#### Example Usage
```
from azure.devops.v5_1.git.models import GitVersionDescriptor

connection.clients.get_git_client().get_branches(repository_id, project=None, base_version_descriptor=None)
```
### GetChanges
#### Description:
Retrieve changes for a particular commit.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| commit_id | str | The id of the commit. |
| repository_id | str | The id or friendly name of the repository. To use the friendly name, projectId must also be specified. |
| project | str | Project ID or project name |
| top | int | The maximum number of changes to return. |
| skip | int | The number of changes to skip. |
#### Return Type
:class:<GitCommitChanges> <azure.devops.v5_1.git.models.GitCommitChanges>
#### Example Usage
```

connection.clients.get_git_client().get_changes(commit_id, repository_id, project=None, top=None, skip=None)
```
### GetComment
#### Description:
Retrieve a comment associated with a specific thread in a pull request.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The repository ID of the pull request's target branch. |
| pull_request_id | int | ID of the pull request. |
| thread_id | int | ID of the thread that the desired comment is in. |
| comment_id | int | ID of the comment. |
| project | str | Project ID or project name |
#### Return Type
:class:<Comment> <azure.devops.v5_1.git.models.Comment>
#### Example Usage
```

connection.clients.get_git_client().get_comment(repository_id, pull_request_id, thread_id, comment_id, project=None)
```
### GetComments
#### Description:
Retrieve all comments associated with a specific thread in a pull request.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The repository ID of the pull request's target branch. |
| pull_request_id | int | ID of the pull request. |
| thread_id | int | ID of the thread. |
| project | str | Project ID or project name |
#### Return Type
[Comment]
#### Example Usage
```

connection.clients.get_git_client().get_comments(repository_id, pull_request_id, thread_id, project=None)
```
### GetCommit
#### Description:
Retrieve a particular commit.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| commit_id | str | The id of the commit. |
| repository_id | str | The id or friendly name of the repository. To use the friendly name, projectId must also be specified. |
| project | str | Project ID or project name |
| change_count | int | The number of changes to include in the result. |
#### Return Type
:class:<GitCommit> <azure.devops.v5_1.git.models.GitCommit>
#### Example Usage
```

connection.clients.get_git_client().get_commit(commit_id, repository_id, project=None, change_count=None)
```
### GetCommitDiffs
#### Description:
Find the closest common commit (the merge base) between base and target commits, and get the diff between either the base and target commits or common and target commits.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The name or ID of the repository. |
| project | str | Project ID or project name |
| diff_common_commit | bool | If true, diff between common and target commits. If false, diff between base and target commits. |
| top | int | Maximum number of changes to return. Defaults to 100. |
| skip | int | Number of changes to skip |
| base_version_descriptor | class | Descriptor for base commit. |
| target_version_descriptor | class | Descriptor for target commit. |
#### Return Type
:class:<GitCommitDiffs> <azure.devops.v5_1.git.models.GitCommitDiffs>
#### Example Usage
```
from azure.devops.v5_1.git.models import GitBaseVersionDescriptor
from azure.devops.v5_1.git.models import GitTargetVersionDescriptor

connection.clients.get_git_client().get_commit_diffs(repository_id, project=None, diff_common_commit=None, top=None, skip=None, base_version_descriptor=None, target_version_descriptor=None)
```
### GetCommits
#### Description:
Retrieve git commits for a project
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The id or friendly name of the repository. To use the friendly name, projectId must also be specified. |
| search_criteria | class |  |
| project | str | Project ID or project name |
| skip | int |  |
| top | int |  |
#### Return Type
[GitCommitRef]
#### Example Usage
```
from azure.devops.v5_1.git.models import GitQueryCommitsCriteria

connection.clients.get_git_client().get_commits(repository_id, search_criteria, project=None, skip=None, top=None)
```
### GetCommitsBatch
#### Description:
Retrieve git commits for a project matching the search criteria
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| search_criteria | class | Search options |
| repository_id | str | The name or ID of the repository. |
| project | str | Project ID or project name |
| skip | int | Number of commits to skip. |
| top | int | Maximum number of commits to return. |
| include_statuses | bool | True to include additional commit status information. |
#### Return Type
[GitCommitRef]
#### Example Usage
```
from azure.devops.v5_1.git.models import GitQueryCommitsCriteria

connection.clients.get_git_client().get_commits_batch(search_criteria, repository_id, project=None, skip=None, top=None, include_statuses=None)
```
### GetItem
#### Description:
Get Item Metadata and/or Content for a single item. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content, which is always returned as a download.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The name or ID of the repository. |
| path | str | The item path. |
| project | str | Project ID or project name |
| scope_path | str | The path scope.  The default is null. |
| recursion_level | str | The recursion level of this request. The default is 'none', no recursion. |
| include_content_metadata | bool | Set to true to include content metadata.  Default is false. |
| latest_processed_change | bool | Set to true to include the latest changes.  Default is false. |
| download | bool | Set to true to download the response as a file.  Default is false. |
| version_descriptor | class | Version descriptor.  Default is the default branch for the repository. |
| include_content | bool | Set to true to include item content when requesting json.  Default is false. |
| resolve_lfs | bool | Set to true to resolve Git LFS pointer files to return actual content from Git LFS.  Default is false. |
#### Return Type
:class:<GitItem> <azure.devops.v5_1.git.models.GitItem>
#### Example Usage
```
from azure.devops.v5_1.git.models import GitVersionDescriptor

connection.clients.get_git_client().get_item(repository_id, path, project=None, scope_path=None, recursion_level=None, include_content_metadata=None, latest_processed_change=None, download=None, version_descriptor=None, include_content=None, resolve_lfs=None)
```
### GetItemContent
#### Description:
Get Item Metadata and/or Content for a single item. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content, which is always returned as a download.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The name or ID of the repository. |
| path | str | The item path. |
| project | str | Project ID or project name |
| scope_path | str | The path scope.  The default is null. |
| recursion_level | str | The recursion level of this request. The default is 'none', no recursion. |
| include_content_metadata | bool | Set to true to include content metadata.  Default is false. |
| latest_processed_change | bool | Set to true to include the latest changes.  Default is false. |
| download | bool | Set to true to download the response as a file.  Default is false. |
| version_descriptor | class | Version descriptor.  Default is the default branch for the repository. |
| include_content | bool | Set to true to include item content when requesting json.  Default is false. |
| resolve_lfs | bool | Set to true to resolve Git LFS pointer files to return actual content from Git LFS.  Default is false. |
#### Return Type
object
#### Example Usage
```
from azure.devops.v5_1.git.models import GitVersionDescriptor

connection.clients.get_git_client().get_item_content(repository_id, path, project=None, scope_path=None, recursion_level=None, include_content_metadata=None, latest_processed_change=None, download=None, version_descriptor=None, include_content=None, resolve_lfs=None, **kwargs)
```
### GetItemText
#### Description:
Get Item Metadata and/or Content for a single item. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content, which is always returned as a download.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The name or ID of the repository. |
| path | str | The item path. |
| project | str | Project ID or project name |
| scope_path | str | The path scope.  The default is null. |
| recursion_level | str | The recursion level of this request. The default is 'none', no recursion. |
| include_content_metadata | bool | Set to true to include content metadata.  Default is false. |
| latest_processed_change | bool | Set to true to include the latest changes.  Default is false. |
| download | bool | Set to true to download the response as a file.  Default is false. |
| version_descriptor | class | Version descriptor.  Default is the default branch for the repository. |
| include_content | bool | Set to true to include item content when requesting json.  Default is false. |
| resolve_lfs | bool | Set to true to resolve Git LFS pointer files to return actual content from Git LFS.  Default is false. |
#### Return Type
object
#### Example Usage
```
from azure.devops.v5_1.git.models import GitVersionDescriptor

connection.clients.get_git_client().get_item_text(repository_id, path, project=None, scope_path=None, recursion_level=None, include_content_metadata=None, latest_processed_change=None, download=None, version_descriptor=None, include_content=None, resolve_lfs=None, **kwargs)
```
### GetItemZip
#### Description:
Get Item Metadata and/or Content for a single item. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content, which is always returned as a download.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The name or ID of the repository. |
| path | str | The item path. |
| project | str | Project ID or project name |
| scope_path | str | The path scope.  The default is null. |
| recursion_level | str | The recursion level of this request. The default is 'none', no recursion. |
| include_content_metadata | bool | Set to true to include content metadata.  Default is false. |
| latest_processed_change | bool | Set to true to include the latest changes.  Default is false. |
| download | bool | Set to true to download the response as a file.  Default is false. |
| version_descriptor | class | Version descriptor.  Default is the default branch for the repository. |
| include_content | bool | Set to true to include item content when requesting json.  Default is false. |
| resolve_lfs | bool | Set to true to resolve Git LFS pointer files to return actual content from Git LFS.  Default is false. |
#### Return Type
object
#### Example Usage
```
from azure.devops.v5_1.git.models import GitVersionDescriptor

connection.clients.get_git_client().get_item_zip(repository_id, path, project=None, scope_path=None, recursion_level=None, include_content_metadata=None, latest_processed_change=None, download=None, version_descriptor=None, include_content=None, resolve_lfs=None, **kwargs)
```
### GetItems
#### Description:
Get Item Metadata and/or Content for a collection of items. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content which is always returned as a download.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The name or ID of the repository. |
| project | str | Project ID or project name |
| scope_path | str | The path scope.  The default is null. |
| recursion_level | str | The recursion level of this request. The default is 'none', no recursion. |
| include_content_metadata | bool | Set to true to include content metadata.  Default is false. |
| latest_processed_change | bool | Set to true to include the latest changes.  Default is false. |
| download | bool | Set to true to download the response as a file.  Default is false. |
| include_links | bool | Set to true to include links to items.  Default is false. |
| version_descriptor | class | Version descriptor.  Default is the default branch for the repository. |
#### Return Type
[GitItem]
#### Example Usage
```
from azure.devops.v5_1.git.models import GitVersionDescriptor

connection.clients.get_git_client().get_items(repository_id, project=None, scope_path=None, recursion_level=None, include_content_metadata=None, latest_processed_change=None, download=None, include_links=None, version_descriptor=None)
```
### GetItemsBatch
#### Description:
Post for retrieving a creating a batch out of a set of items in a repo / project given a list of paths or a long path
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| request_data: Request data attributes: ItemDescriptors, IncludeContentMetadata, LatestProcessedChange, IncludeLinks. ItemDescriptors: Collection of items to fetch, including path, version, and recursion level. IncludeContentMetadata: Whether to include metadata for all items LatestProcessedChange: Whether to include shallow ref to commit that last changed each item. IncludeLinks | class | Whether to include the _links field on the shallow references. |
| repository_id | str | The name or ID of the repository |
| project | str | Project ID or project name |
#### Return Type
[[GitItem]]
#### Example Usage
```
from azure.devops.v5_1.git.models import GitItemRequestData

connection.clients.get_git_client().get_items_batch(request_data, repository_id, project=None)
```
### GetPullRequest
#### Description:
Retrieve a pull request.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The repository ID of the pull request's target branch. |
| pull_request_id | int | The ID of the pull request to retrieve. |
| project | str | Project ID or project name |
| max_comment_length | int | Not used. |
| skip | int | Not used. |
| top | int | Not used. |
| include_commits | bool | If true, the pull request will be returned with the associated commits. |
| include_work_item_refs | bool | If true, the pull request will be returned with the associated work item references. |
#### Return Type
:class:<GitPullRequest> <azure.devops.v5_1.git.models.GitPullRequest>
#### Example Usage
```

connection.clients.get_git_client().get_pull_request(repository_id, pull_request_id, project=None, max_comment_length=None, skip=None, top=None, include_commits=None, include_work_item_refs=None)
```
### GetPullRequestById
#### Description:
Retrieve a pull request.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| pull_request_id | int | The ID of the pull request to retrieve. |
| project | str | Project ID or project name |
#### Return Type
:class:<GitPullRequest> <azure.devops.v5_1.git.models.GitPullRequest>
#### Example Usage
```

connection.clients.get_git_client().get_pull_request_by_id(pull_request_id, project=None)
```
### GetPullRequestCommits
#### Description:
Get the commits for the specified pull request.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | ID or name of the repository. |
| pull_request_id | int | ID of the pull request. |
| project | str | Project ID or project name |
| top | int | Maximum number of commits to return. |
| continuation_token | str | The continuation token used for pagination. |
#### Return Type
:class:<GetPullRequestCommitsResponseValue>
#### Example Usage
```

connection.clients.get_git_client().get_pull_request_commits(repository_id, pull_request_id, project=None, top=None, continuation_token=None)
```
### GetPullRequestIteration
#### Description:
Get the specified iteration for a pull request.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | ID or name of the repository. |
| pull_request_id | int | ID of the pull request. |
| iteration_id | int | ID of the pull request iteration to return. |
| project | str | Project ID or project name |
#### Return Type
:class:<GitPullRequestIteration> <azure.devops.v5_1.git.models.GitPullRequestIteration>
#### Example Usage
```

connection.clients.get_git_client().get_pull_request_iteration(repository_id, pull_request_id, iteration_id, project=None)
```
### GetPullRequestIterationChanges
#### Description:
Retrieve the changes made in a pull request between two iterations.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The repository ID of the pull request's target branch. |
| pull_request_id | int | ID of the pull request. |
| iteration_id | int | ID of the pull request iteration. <br /> Iteration IDs are zero-based with zero indicating the common commit between the source and target branches. Iteration one is the head of the source branch at the time the pull request is created and subsequent iterations are created when there are pushes to the source branch. |
| project | str | Project ID or project name |
| top | int | Optional. The number of changes to retrieve.  The default value is 100 and the maximum value is 2000. |
| skip | int | Optional. The number of changes to ignore.  For example, to retrieve changes 101-150, set top 50 and skip to 100. |
| compare_to | int | ID of the pull request iteration to compare against.  The default value is zero which indicates the comparison is made against the common commit between the source and target branches |
#### Return Type
:class:<GitPullRequestIterationChanges> <azure.devops.v5_1.git.models.GitPullRequestIterationChanges>
#### Example Usage
```

connection.clients.get_git_client().get_pull_request_iteration_changes(repository_id, pull_request_id, iteration_id, project=None, top=None, skip=None, compare_to=None)
```
### GetPullRequestIterationCommits
#### Description:
Get the commits for the specified iteration of a pull request.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | ID or name of the repository. |
| pull_request_id | int | ID of the pull request. |
| iteration_id | int | ID of the iteration from which to get the commits. |
| project | str | Project ID or project name |
| top | int | Maximum number of commits to return. The maximum number of commits that can be returned per batch is 500. |
| skip | int | Number of commits to skip. |
#### Return Type
[GitCommitRef]
#### Example Usage
```

connection.clients.get_git_client().get_pull_request_iteration_commits(repository_id, pull_request_id, iteration_id, project=None, top=None, skip=None)
```
### GetPullRequestIterations
#### Description:
Get the list of iterations for the specified pull request.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | ID or name of the repository. |
| pull_request_id | int | ID of the pull request. |
| project | str | Project ID or project name |
| include_commits | bool | If true, include the commits associated with each iteration in the response. |
#### Return Type
[GitPullRequestIteration]
#### Example Usage
```

connection.clients.get_git_client().get_pull_request_iterations(repository_id, pull_request_id, project=None, include_commits=None)
```
### GetPullRequestQuery
#### Description:
This API is used to find what pull requests are related to a given commit.  It can be used to either find the pull request that created a particular merge commit or it can be used to find all pull requests that have ever merged a particular commit.  The input is a list of queries which each contain a list of commits. For each commit that you search against, you will get back a dictionary of commit -> pull requests.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| queries | class | The list of queries to perform. |
| repository_id | str | ID of the repository. |
| project | str | Project ID or project name |
#### Return Type
:class:<GitPullRequestQuery> <azure.devops.v5_1.git.models.GitPullRequestQuery>
#### Example Usage
```
from azure.devops.v5_1.git.models import GitPullRequestQuery

connection.clients.get_git_client().get_pull_request_query(queries, repository_id, project=None)
```
### GetPullRequestReviewer
#### Description:
Retrieve information about a particular reviewer on a pull request
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The repository ID of the pull request’s target branch. |
| pull_request_id | int | ID of the pull request. |
| reviewer_id | str | ID of the reviewer. |
| project | str | Project ID or project name |
#### Return Type
:class:<IdentityRefWithVote> <azure.devops.v5_1.git.models.IdentityRefWithVote>
#### Example Usage
```

connection.clients.get_git_client().get_pull_request_reviewer(repository_id, pull_request_id, reviewer_id, project=None)
```
### GetPullRequestReviewers
#### Description:
Retrieve the reviewers for a pull request
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The repository ID of the pull request’s target branch. |
| pull_request_id | int | ID of the pull request. |
| project | str | Project ID or project name |
#### Return Type
[IdentityRefWithVote]
#### Example Usage
```

connection.clients.get_git_client().get_pull_request_reviewers(repository_id, pull_request_id, project=None)
```
### GetPullRequestThread
#### Description:
Retrieve a thread in a pull request.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The repository ID of the pull request's target branch. |
| pull_request_id | int | ID of the pull request. |
| thread_id | int | ID of the thread. |
| project | str | Project ID or project name |
| iteration | int | If specified, thread position will be tracked using this iteration as the right side of the diff. |
| base_iteration | int | If specified, thread position will be tracked using this iteration as the left side of the diff. |
#### Return Type
:class:<GitPullRequestCommentThread> <azure.devops.v5_1.git.models.GitPullRequestCommentThread>
#### Example Usage
```

connection.clients.get_git_client().get_pull_request_thread(repository_id, pull_request_id, thread_id, project=None, iteration=None, base_iteration=None)
```
### GetPullRequestWorkItemRefs
#### Description:
Retrieve a list of work items associated with a pull request.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | ID or name of the repository. |
| pull_request_id | int | ID of the pull request. |
| project | str | Project ID or project name |
#### Return Type
[ResourceRef]
#### Example Usage
```

connection.clients.get_git_client().get_pull_request_work_item_refs(repository_id, pull_request_id, project=None)
```
### GetPullRequests
#### Description:
Retrieve all pull requests matching a specified criteria.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The repository ID of the pull request's target branch. |
| search_criteria | class | Pull requests will be returned that match this search criteria. |
| project | str | Project ID or project name |
| max_comment_length | int | Not used. |
| skip | int | The number of pull requests to ignore. For example, to retrieve results 101-150, set top to 50 and skip to 100. |
| top | int | The number of pull requests to retrieve. |
#### Return Type
[GitPullRequest]
#### Example Usage
```
from azure.devops.v5_1.git.models import GitPullRequestSearchCriteria

connection.clients.get_git_client().get_pull_requests(repository_id, search_criteria, project=None, max_comment_length=None, skip=None, top=None)
```
### GetPullRequestsByProject
#### Description:
Retrieve all pull requests matching a specified criteria.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| search_criteria | class | Pull requests will be returned that match this search criteria. |
| max_comment_length | int | Not used. |
| skip | int | The number of pull requests to ignore. For example, to retrieve results 101-150, set top to 50 and skip to 100. |
| top | int | The number of pull requests to retrieve. |
#### Return Type
[GitPullRequest]
#### Example Usage
```
from azure.devops.v5_1.git.models import GitPullRequestSearchCriteria

connection.clients.get_git_client().get_pull_requests_by_project(project, search_criteria, max_comment_length=None, skip=None, top=None)
```
### GetPush
#### Description:
Retrieves a particular push.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The name or ID of the repository. |
| push_id | int | ID of the push. |
| project | str | Project ID or project name |
| include_commits | int | The number of commits to include in the result. |
| include_ref_updates | bool | If true, include the list of refs that were updated by the push. |
#### Return Type
:class:<GitPush> <azure.devops.v5_1.git.models.GitPush>
#### Example Usage
```

connection.clients.get_git_client().get_push(repository_id, push_id, project=None, include_commits=None, include_ref_updates=None)
```
### GetPushCommits
#### Description:
Retrieve a list of commits associated with a particular push.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The id or friendly name of the repository. To use the friendly name, projectId must also be specified. |
| push_id | int | The id of the push. |
| project | str | Project ID or project name |
| top | int | The maximum number of commits to return ("get the top x commits"). |
| skip | int | The number of commits to skip. |
| include_links | bool | Set to false to avoid including REST Url links for resources. Defaults to true. |
#### Return Type
[GitCommitRef]
#### Example Usage
```

connection.clients.get_git_client().get_push_commits(repository_id, push_id, project=None, top=None, skip=None, include_links=None)
```
### GetPushes
#### Description:
Retrieves pushes associated with the specified repository.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The name or ID of the repository. |
| project | str | Project ID or project name |
| skip | int | Number of pushes to skip. |
| top | int | Number of pushes to return. |
| search_criteria: Search criteria attributes: fromDate, toDate, pusherId, refName, includeRefUpdates or includeLinks. fromDate: Start date to search from. toDate: End date to search to. pusherId: Identity of the person who submitted the push. refName: Branch name to consider. includeRefUpdates: If true, include the list of refs that were updated by the push. includeLinks | class | Whether to include the _links field on the shallow references. |
#### Return Type
[GitPush]
#### Example Usage
```
from azure.devops.v5_1.git.models import GitPushSearchCriteria

connection.clients.get_git_client().get_pushes(repository_id, project=None, skip=None, top=None, search_criteria=None)
```
### GetRefs
#### Description:
Queries the provided repository for its refs and returns them.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The name or ID of the repository. |
| project | str | Project ID or project name |
| filter | str | [optional] A filter to apply to the refs (starts with). |
| include_links | bool | [optional] Specifies if referenceLinks should be included in the result. default is false. |
| include_statuses | bool | [optional] Includes up to the first 1000 commit statuses for each ref. The default value is false. |
| include_my_branches | bool | [optional] Includes only branches that the user owns, the branches the user favorites, and the default branch. The default value is false. Cannot be combined with the filter parameter. |
| latest_statuses_only | bool | [optional] True to include only the tip commit status for each ref. This option requires `includeStatuses` to be true. The default value is false. |
| peel_tags | bool | [optional] Annotated tags will populate the PeeledObjectId property. default is false. |
| filter_contains | str | [optional] A filter to apply to the refs (contains). |
| top | int | [optional] Maximum number of refs to return. It cannot be bigger than 1000. If it is not provided but continuationToken is, top will default to 100. |
| continuation_token | str | The continuation token used for pagination. |
#### Return Type
:class:<GetRefsResponseValue>
#### Example Usage
```

connection.clients.get_git_client().get_refs(repository_id, project=None, filter=None, include_links=None, include_statuses=None, include_my_branches=None, latest_statuses_only=None, peel_tags=None, filter_contains=None, top=None, continuation_token=None)
```
### GetRepositories
#### Description:
Retrieve git repositories.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| include_links | bool | [optional] True to include reference links. The default value is false. |
| include_all_urls | bool | [optional] True to include all remote URLs. The default value is false. |
| include_hidden | bool | [optional] True to include hidden repositories. The default value is false. |
#### Return Type
[GitRepository]
#### Example Usage
```

connection.clients.get_git_client().get_repositories(project=None, include_links=None, include_all_urls=None, include_hidden=None)
```
### GetRepository
#### Description:
Retrieve a git repository.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The name or ID of the repository. |
| project | str | Project ID or project name |
#### Return Type
:class:<GitRepository> <azure.devops.v5_1.git.models.GitRepository>
#### Example Usage
```

connection.clients.get_git_client().get_repository(repository_id, project=None)
```
### GetRepositoryWithParent
#### Description:
Retrieve a git repository.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The name or ID of the repository. |
| include_parent | bool | True to include parent repository. Only available in authenticated calls. |
| project | str | Project ID or project name |
#### Return Type
:class:<GitRepository> <azure.devops.v5_1.git.models.GitRepository>
#### Example Usage
```

connection.clients.get_git_client().get_repository_with_parent(repository_id, include_parent, project=None)
```
### GetStatuses
#### Description:
Get statuses associated with the Git commit.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| commit_id | str | ID of the Git commit. |
| repository_id | str | ID of the repository. |
| project | str | Project ID or project name |
| top | int | Optional. The number of statuses to retrieve. Default is 1000. |
| skip | int | Optional. The number of statuses to ignore. Default is 0. For example, to retrieve results 101-150, set top to 50 and skip to 100. |
| latest_only | bool | The flag indicates whether to get only latest statuses grouped by `Context.Name` and `Context.Genre`. |
#### Return Type
[GitStatus]
#### Example Usage
```

connection.clients.get_git_client().get_statuses(commit_id, repository_id, project=None, top=None, skip=None, latest_only=None)
```
### GetThreads
#### Description:
Retrieve all threads in a pull request.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | The repository ID of the pull request's target branch. |
| pull_request_id | int | ID of the pull request. |
| project | str | Project ID or project name |
| iteration | int | If specified, thread positions will be tracked using this iteration as the right side of the diff. |
| base_iteration | int | If specified, thread positions will be tracked using this iteration as the left side of the diff. |
#### Return Type
[GitPullRequestCommentThread]
#### Example Usage
```

connection.clients.get_git_client().get_threads(repository_id, pull_request_id, project=None, iteration=None, base_iteration=None)
```
### GetTree
#### Description:
The Tree endpoint returns the collection of objects underneath the specified tree. Trees are folders in a Git repository.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | Repository Id. |
| sha1 | str | SHA1 hash of the tree object. |
| project | str | Project ID or project name |
| project_id | str | Project Id. |
| recursive | bool | Search recursively. Include trees underneath this tree. Default is false. |
| file_name | str | Name to use if a .zip file is returned. Default is the object ID. |
#### Return Type
:class:<GitTreeRef> <azure.devops.v5_1.git.models.GitTreeRef>
#### Example Usage
```

connection.clients.get_git_client().get_tree(repository_id, sha1, project=None, project_id=None, recursive=None, file_name=None)
```
### GetTreeZip
#### Description:
The Tree endpoint returns the collection of objects underneath the specified tree. Trees are folders in a Git repository.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| repository_id | str | Repository Id. |
| sha1 | str | SHA1 hash of the tree object. |
| project | str | Project ID or project name |
| project_id | str | Project Id. |
| recursive | bool | Search recursively. Include trees underneath this tree. Default is false. |
| file_name | str | Name to use if a .zip file is returned. Default is the object ID. |
#### Return Type
object
#### Example Usage
```

connection.clients.get_git_client().get_tree_zip(repository_id, sha1, project=None, project_id=None, recursive=None, file_name=None, **kwargs)
```
### UpdateComment
#### Description:
Update a comment associated with a specific thread in a pull request.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| comment | class | The comment content that should be updated. Comments can be up to 150,000 characters. |
| repository_id | str | The repository ID of the pull request's target branch. |
| pull_request_id | int | ID of the pull request. |
| thread_id | int | ID of the thread that the desired comment is in. |
| comment_id | int | ID of the comment to update. |
| project | str | Project ID or project name |
#### Return Type
:class:<Comment> <azure.devops.v5_1.git.models.Comment>
#### Example Usage
```
from azure.devops.v5_1.git.models import Comment

connection.clients.get_git_client().update_comment(comment, repository_id, pull_request_id, thread_id, comment_id, project=None)
```
### UpdatePullRequest
#### Description:
Update a pull request
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| git_pull_request_to_update | class | The pull request content that should be updated. |
| repository_id | str | The repository ID of the pull request's target branch. |
| pull_request_id | int | ID of the pull request to update. |
| project | str | Project ID or project name |
#### Return Type
:class:<GitPullRequest> <azure.devops.v5_1.git.models.GitPullRequest>
#### Example Usage
```
from azure.devops.v5_1.git.models import GitPullRequest

connection.clients.get_git_client().update_pull_request(git_pull_request_to_update, repository_id, pull_request_id, project=None)
```
### UpdatePullRequestReviewers
#### Description:
Reset the votes of multiple reviewers on a pull request.  NOTE: This endpoint only supports updating votes, but does not support updating required reviewers (use policy) or display names.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| patch_votes | [IdentityRefWithVote] | IDs of the reviewers whose votes will be reset to zero |
| repository_id | str | The repository ID of the pull request’s target branch. |
| pull_request_id | int | ID of the pull request |
| project | str | Project ID or project name |
#### Return Type
:class:<GitPullRequest> <azure.devops.v5_1.git.models.GitPullRequest>
#### Example Usage
```

connection.clients.get_git_client().update_pull_request_reviewers(patch_votes, repository_id, pull_request_id, project=None)
```
### UpdateRef
#### Description:
Lock or Unlock a branch.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| new_ref_info | class | The ref update action (lock/unlock) to perform |
| repository_id | str | The name or ID of the repository. |
| filter | str | The name of the branch to lock/unlock |
| project | str | Project ID or project name |
| project_id | str | ID or name of the team project. Optional if specifying an ID for repository. |
#### Return Type
:class:<GitRef> <azure.devops.v5_1.git.models.GitRef>
#### Example Usage
```
from azure.devops.v5_1.git.models import GitRefUpdate

connection.clients.get_git_client().update_ref(new_ref_info, repository_id, filter, project=None, project_id=None)
```
### UpdateRefs
#### Description:
Creating, updating, or deleting refs(branches).
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| ref_updates | [GitRefUpdate] | List of ref updates to attempt to perform |
| repository_id | str | The name or ID of the repository. |
| project | str | Project ID or project name |
| project_id | str | ID or name of the team project. Optional if specifying an ID for repository. |
#### Return Type
[GitRefUpdateResult]
#### Example Usage
```

connection.clients.get_git_client().update_refs(ref_updates, repository_id, project=None, project_id=None)
```
### UpdateRepository
#### Description:
Updates the Git repository with either a new repo name or a new default branch.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| new_repository_info | class | Specify a new repo name or a new default branch of the repository |
| repository_id | str | The name or ID of the repository. |
| project | str | Project ID or project name |
#### Return Type
:class:<GitRepository> <azure.devops.v5_1.git.models.GitRepository>
#### Example Usage
```
from azure.devops.v5_1.git.models import GitRepository

connection.clients.get_git_client().update_repository(new_repository_info, repository_id, project=None)
```
### UpdateThread
#### Description:
Update a thread in a pull request.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| comment_thread | class | The thread content that should be updated. |
| repository_id | str | The repository ID of the pull request's target branch. |
| pull_request_id | int | ID of the pull request. |
| thread_id | int | ID of the thread to update. |
| project | str | Project ID or project name |
#### Return Type
:class:<GitPullRequestCommentThread> <azure.devops.v5_1.git.models.GitPullRequestCommentThread>
#### Example Usage
```
from azure.devops.v5_1.git.models import GitPullRequestCommentThread

connection.clients.get_git_client().update_thread(comment_thread, repository_id, pull_request_id, thread_id, project=None)
```
## Get Identity Client

### CreateGroups
#### Description:
:param :class:`<object> <azure.devops.v5_1.identity.models.object>` container:
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| container | class |  |
#### Return Type
[Identity]
#### Example Usage
```
from azure.devops.v5_1.identity.models import object

connection.clients.get_identity_client().create_groups(container)
```
### CreateIdentity
#### Description:
:param :class:`<FrameworkIdentityInfo> <azure.devops.v5_1.identity.models.FrameworkIdentityInfo>` framework_identity_info:
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| framework_identity_info | class |  |
#### Return Type
:class:<Identity> <azure.devops.v5_1.identity.models.Identity>
#### Example Usage
```
from azure.devops.v5_1.identity.models import FrameworkIdentityInfo

connection.clients.get_identity_client().create_identity(framework_identity_info)
```
### DeleteGroup
#### Description:
:param str group_id:
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| group_id | str |  |
#### Return Type
:class:<Identity> <azure.devops.v5_1.identity.models.Identity>
#### Example Usage
```

connection.clients.get_identity_client().delete_group(group_id)
```
### GetIdentityChanges
#### Description:
:param int identity_sequence_id:
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| identity_sequence_id | int |  |
| group_sequence_id | int |  |
| organization_identity_sequence_id | int |  |
| page_size | int |  |
| scope_id | str |  |
#### Return Type
:class:<ChangedIdentities> <azure.devops.v5_1.identity.models.ChangedIdentities>
#### Example Usage
```

connection.clients.get_identity_client().get_identity_changes(identity_sequence_id, group_sequence_id, organization_identity_sequence_id=None, page_size=None, scope_id=None)
```
### GetMaxSequenceId
#### Description:
Read the max sequence id of all the identities.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
#### Return Type
long
#### Example Usage
```

connection.clients.get_identity_client().get_max_sequence_id()
```
### GetSelf
#### Description:
Read identity of the home tenant request user.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
#### Return Type
:class:<IdentitySelf> <azure.devops.v5_1.identity.models.IdentitySelf>
#### Example Usage
```

connection.clients.get_identity_client().get_self()
```
### GetUserIdentityIdsByDomainId
#### Description:
:param str domain_id:
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| domain_id | str |  |
#### Return Type
[str]
#### Example Usage
```

connection.clients.get_identity_client().get_user_identity_ids_by_domain_id(domain_id)
```
### ListGroups
#### Description:
:param str scope_ids:
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| scope_ids | str |  |
| recurse | bool |  |
| deleted | bool |  |
| properties | str |  |
#### Return Type
[Identity]
#### Example Usage
```

connection.clients.get_identity_client().list_groups(scope_ids=None, recurse=None, deleted=None, properties=None)
```
### ReadIdentities
#### Description:
:param str descriptors:
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| descriptors | str |  |
| identity_ids | str |  |
| subject_descriptors | str |  |
| social_descriptors | str |  |
| search_filter | str |  |
| filter_value | str |  |
| query_membership | str |  |
| properties | str |  |
| include_restricted_visibility | bool |  |
| options | str |  |
#### Return Type
[Identity]
#### Example Usage
```

connection.clients.get_identity_client().read_identities(descriptors=None, identity_ids=None, subject_descriptors=None, social_descriptors=None, search_filter=None, filter_value=None, query_membership=None, properties=None, include_restricted_visibility=None, options=None)
```
### ReadIdentitiesByScope
#### Description:
:param str scope_id:
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| scope_id | str |  |
| query_membership | str |  |
| properties | str |  |
#### Return Type
[Identity]
#### Example Usage
```

connection.clients.get_identity_client().read_identities_by_scope(scope_id, query_membership=None, properties=None)
```
### ReadIdentity
#### Description:
:param str identity_id:
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| identity_id | str |  |
| query_membership | str |  |
| properties | str |  |
#### Return Type
:class:<Identity> <azure.devops.v5_1.identity.models.Identity>
#### Example Usage
```

connection.clients.get_identity_client().read_identity(identity_id, query_membership=None, properties=None)
```
### UpdateIdentities
#### Description:
:param :class:`<VssJsonCollectionWrapper> <azure.devops.v5_1.identity.models.VssJsonCollectionWrapper>` identities:
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| identities | class |  |
#### Return Type
[IdentityUpdateData]
#### Example Usage
```
from azure.devops.v5_1.identity.models import VssJsonCollectionWrapper

connection.clients.get_identity_client().update_identities(identities)
```
### UpdateIdentity
#### Description:
:param :class:`<Identity> <azure.devops.v5_1.identity.models.Identity>` identity:
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| identity | class |  |
| identity_id | str |  |
#### Return Type
[IdentityUpdateData]
#### Example Usage
```
from azure.devops.v5_1.identity.models import Identity

connection.clients.get_identity_client().update_identity(identity, identity_id)
```
## Get Notification Client

### CreateSubscription
#### Description:
Create a new subscription.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| create_parameters | class |  |
#### Return Type
:class:<NotificationSubscription> <azure.devops.v5_1.notification.models.NotificationSubscription>
#### Example Usage
```
from azure.devops.v5_1.notification.models import NotificationSubscriptionCreateParameters

connection.clients.get_notification_client().create_subscription(create_parameters)
```
### DeleteSubscription
#### Description:
Delete a subscription.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| subscription_id | str |  |
#### Return Type
:class:<NotificationSubscription> <azure.devops.v5_1.notification.models.NotificationSubscription>
#### Example Usage
```

connection.clients.get_notification_client().delete_subscription(subscription_id)
```
### GetEventType
#### Description:
Get a specific event type.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| event_type | str | The ID of the event type. |
#### Return Type
:class:<NotificationEventType> <azure.devops.v5_1.notification.models.NotificationEventType>
#### Example Usage
```

connection.clients.get_notification_client().get_event_type(event_type)
```
### GetSettings
#### Description:
:rtype: :class:`<NotificationAdminSettings> <azure.devops.v5_1.notification.models.NotificationAdminSettings>`
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
#### Return Type
:class:<NotificationAdminSettings> <azure.devops.v5_1.notification.models.NotificationAdminSettings>
#### Example Usage
```

connection.clients.get_notification_client().get_settings()
```
### GetSubscriber
#### Description:
Get delivery preferences of a notifications subscriber.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| subscriber_id | str | ID of the user or group. |
#### Return Type
:class:<NotificationSubscriber> <azure.devops.v5_1.notification.models.NotificationSubscriber>
#### Example Usage
```

connection.clients.get_notification_client().get_subscriber(subscriber_id)
```
### GetSubscription
#### Description:
Get a notification subscription by its ID.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| subscription_id | str |  |
| query_flags | str |  |
#### Return Type
:class:<NotificationSubscription> <azure.devops.v5_1.notification.models.NotificationSubscription>
#### Example Usage
```

connection.clients.get_notification_client().get_subscription(subscription_id, query_flags=None)
```
### GetSubscriptionDiagnostics
#### Description:
Get the diagnostics settings for a subscription.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| subscription_id | str | The id of the notifications subscription. |
#### Return Type
:class:<SubscriptionDiagnostics> <azure.devops.v5_1.notification.models.SubscriptionDiagnostics>
#### Example Usage
```

connection.clients.get_notification_client().get_subscription_diagnostics(subscription_id)
```
### GetSubscriptionTemplates
#### Description:
Get available subscription templates.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
#### Return Type
[NotificationSubscriptionTemplate]
#### Example Usage
```

connection.clients.get_notification_client().get_subscription_templates()
```
### ListEventTypes
#### Description:
List available event types for this service. Optionally filter by only event types for the specified publisher.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| publisher_id | str | Limit to event types for this publisher |
#### Return Type
[NotificationEventType]
#### Example Usage
```

connection.clients.get_notification_client().list_event_types(publisher_id=None)
```
### ListLogs
#### Description:
Get a list of diagnostic logs for this service.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| source | str | ID specifying which type of logs to check diagnostics for. |
| entry_id | str | The ID of the specific log to query for. |
| start_time | datetime | Start time for the time range to query in. |
| end_time | datetime | End time for the time range to query in. |
#### Return Type
[INotificationDiagnosticLog]
#### Example Usage
```

connection.clients.get_notification_client().list_logs(source, entry_id=None, start_time=None, end_time=None)
```
### ListSubscriptions
#### Description:
Get a list of notification subscriptions, either by subscription IDs or by all subscriptions for a given user or group.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| target_id | str | User or Group ID |
| ids | [str] | List of subscription IDs |
| query_flags | str |  |
#### Return Type
[NotificationSubscription]
#### Example Usage
```

connection.clients.get_notification_client().list_subscriptions(target_id=None, ids=None, query_flags=None)
```
### QuerySubscriptions
#### Description:
Query for subscriptions. A subscription is returned if it matches one or more of the specified conditions.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| subscription_query | class |  |
#### Return Type
[NotificationSubscription]
#### Example Usage
```
from azure.devops.v5_1.notification.models import SubscriptionQuery

connection.clients.get_notification_client().query_subscriptions(subscription_query)
```
### UpdateSettings
#### Description:
:param :class:`<NotificationAdminSettingsUpdateParameters> <azure.devops.v5_1.notification.models.NotificationAdminSettingsUpdateParameters>` update_parameters:
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| update_parameters | class |  |
#### Return Type
:class:<NotificationAdminSettings> <azure.devops.v5_1.notification.models.NotificationAdminSettings>
#### Example Usage
```
from azure.devops.v5_1.notification.models import NotificationAdminSettingsUpdateParameters

connection.clients.get_notification_client().update_settings(update_parameters)
```
### UpdateSubscriber
#### Description:
Update delivery preferences of a notifications subscriber.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| update_parameters | class |  |
| subscriber_id | str | ID of the user or group. |
#### Return Type
:class:<NotificationSubscriber> <azure.devops.v5_1.notification.models.NotificationSubscriber>
#### Example Usage
```
from azure.devops.v5_1.notification.models import NotificationSubscriberUpdateParameters

connection.clients.get_notification_client().update_subscriber(update_parameters, subscriber_id)
```
### UpdateSubscription
#### Description:
Update an existing subscription. Depending on the type of subscription and permissions, the caller can update the description, filter settings, channel (delivery) settings and more.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| update_parameters | class |  |
| subscription_id | str |  |
#### Return Type
:class:<NotificationSubscription> <azure.devops.v5_1.notification.models.NotificationSubscription>
#### Example Usage
```
from azure.devops.v5_1.notification.models import NotificationSubscriptionUpdateParameters

connection.clients.get_notification_client().update_subscription(update_parameters, subscription_id)
```
### UpdateSubscriptionDiagnostics
#### Description:
Update the diagnostics settings for a subscription.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| update_parameters | class |  |
| subscription_id | str | The id of the notifications subscription. |
#### Return Type
:class:<SubscriptionDiagnostics> <azure.devops.v5_1.notification.models.SubscriptionDiagnostics>
#### Example Usage
```
from azure.devops.v5_1.notification.models import UpdateSubscripitonDiagnosticsParameters

connection.clients.get_notification_client().update_subscription_diagnostics(update_parameters, subscription_id)
```
### UpdateSubscriptionUserSettings
#### Description:
Update the specified user's settings for the specified subscription. This API is typically used to opt in or out of a shared subscription. User settings can only be applied to shared subscriptions, like team subscriptions or default subscriptions.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| user_settings | class |  |
| subscription_id | str |  |
| user_id | str | ID of the user |
#### Return Type
:class:<SubscriptionUserSettings> <azure.devops.v5_1.notification.models.SubscriptionUserSettings>
#### Example Usage
```
from azure.devops.v5_1.notification.models import SubscriptionUserSettings

connection.clients.get_notification_client().update_subscription_user_settings(user_settings, subscription_id, user_id)
```
## Get Operations Client

### GetOperation
#### Description:
Gets an operation from the the operationId using the given pluginId.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| operation_id | str | The ID for the operation. |
| plugin_id | str | The ID for the plugin. |
#### Return Type
:class:<Operation> <azure.devops.v5_1.operations.models.Operation>
#### Example Usage
```

connection.clients.get_operations_client().get_operation(operation_id, plugin_id=None)
```
## Get Policy Client

### CreatePolicyConfiguration
#### Description:
Create a policy configuration of a given policy type.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| configuration | class | The policy configuration to create. |
| project | str | Project ID or project name |
| configuration_id | int |  |
#### Return Type
:class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>
#### Example Usage
```
from azure.devops.v5_1.policy.models import PolicyConfiguration

connection.clients.get_policy_client().create_policy_configuration(configuration, project, configuration_id=None)
```
### DeletePolicyConfiguration
#### Description:
Delete a policy configuration by its ID.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| configuration_id | int | ID of the policy configuration to delete. |
#### Return Type
:class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>
#### Example Usage
```

connection.clients.get_policy_client().delete_policy_configuration(project, configuration_id)
```
### GetPolicyConfiguration
#### Description:
Get a policy configuration by its ID.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| configuration_id | int | ID of the policy configuration |
#### Return Type
:class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>
#### Example Usage
```

connection.clients.get_policy_client().get_policy_configuration(project, configuration_id)
```
### GetPolicyConfigurationRevision
#### Description:
Retrieve a specific revision of a given policy by ID.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| configuration_id | int | The policy configuration ID. |
| revision_id | int | The revision ID. |
#### Return Type
:class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>
#### Example Usage
```

connection.clients.get_policy_client().get_policy_configuration_revision(project, configuration_id, revision_id)
```
### GetPolicyConfigurationRevisions
#### Description:
Retrieve all revisions for a given policy.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| configuration_id | int | The policy configuration ID. |
| top | int | The number of revisions to retrieve. |
| skip | int | The number of revisions to ignore. For example, to retrieve results 101-150, set top to 50 and skip to 100. |
#### Return Type
[PolicyConfiguration]
#### Example Usage
```

connection.clients.get_policy_client().get_policy_configuration_revisions(project, configuration_id, top=None, skip=None)
```
### GetPolicyConfigurations
#### Description:
Get a list of policy configurations in a project.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| scope | str | [Provided for legacy reasons] The scope on which a subset of policies is defined. |
| top | int | Maximum number of policies to return. |
| continuation_token | str | The continuation token used for pagination. |
| policy_type | str | Filter returned policies to only this type |
#### Return Type
:class:<GetPolicyConfigurationsResponseValue>
#### Example Usage
```

connection.clients.get_policy_client().get_policy_configurations(project, scope=None, top=None, continuation_token=None, policy_type=None)
```
### GetPolicyType
#### Description:
Retrieve a specific policy type by ID.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| type_id | str | The policy ID. |
#### Return Type
:class:<PolicyType> <azure.devops.v5_1.policy.models.PolicyType>
#### Example Usage
```

connection.clients.get_policy_client().get_policy_type(project, type_id)
```
### GetPolicyTypes
#### Description:
Retrieve all available policy types.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
#### Return Type
[PolicyType]
#### Example Usage
```

connection.clients.get_policy_client().get_policy_types(project)
```
### UpdatePolicyConfiguration
#### Description:
Update a policy configuration by its ID.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| configuration | class | The policy configuration to update. |
| project | str | Project ID or project name |
| configuration_id | int | ID of the existing policy configuration to be updated. |
#### Return Type
:class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>
#### Example Usage
```
from azure.devops.v5_1.policy.models import PolicyConfiguration

connection.clients.get_policy_client().update_policy_configuration(configuration, project, configuration_id)
```
## Get Release Client

### CreateRelease
#### Description:
Create a release.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| release_start_metadata | class | Metadata to create a release. |
| project | str | Project ID or project name |
#### Return Type
:class:<Release> <azure.devops.v5_1.release.models.Release>
#### Example Usage
```
from azure.devops.v5_1.release.models import ReleaseStartMetadata

connection.clients.get_release_client().create_release(release_start_metadata, project)
```
### CreateReleaseDefinition
#### Description:
Create a release definition
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| release_definition | class | release definition object to create. |
| project | str | Project ID or project name |
#### Return Type
:class:<ReleaseDefinition> <azure.devops.v5_1.release.models.ReleaseDefinition>
#### Example Usage
```
from azure.devops.v5_1.release.models import ReleaseDefinition

connection.clients.get_release_client().create_release_definition(release_definition, project)
```
### DeleteReleaseDefinition
#### Description:
Delete a release definition.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| definition_id | int | Id of the release definition. |
| comment | str | Comment for deleting a release definition. |
| force_delete | bool | 'true' to automatically cancel any in-progress release deployments and proceed with release definition deletion . Default is 'false'. |
#### Return Type
:class:<ReleaseDefinition> <azure.devops.v5_1.release.models.ReleaseDefinition>
#### Example Usage
```

connection.clients.get_release_client().delete_release_definition(project, definition_id, comment=None, force_delete=None)
```
### GetApprovals
#### Description:
Get a list of approvals
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| assigned_to_filter | str | Approvals assigned to this user. |
| status_filter | str | Approvals with this status. Default is 'pending'. |
| release_ids_filter | [int] | Approvals for release id(s) mentioned in the filter. Multiple releases can be mentioned by separating them with ',' e.g. releaseIdsFilter=1,2,3,4. |
| type_filter | str | Approval with this type. |
| top | int | Number of approvals to get. Default is 50. |
| continuation_token | int | Gets the approvals after the continuation token provided. |
| query_order | str | Gets the results in the defined order of created approvals. Default is 'descending'. |
| include_my_group_approvals | bool | 'true' to include my group approvals. Default is 'false'. |
#### Return Type
:class:<GetApprovalsResponseValue>
#### Example Usage
```

connection.clients.get_release_client().get_approvals(project, assigned_to_filter=None, status_filter=None, release_ids_filter=None, type_filter=None, top=None, continuation_token=None, query_order=None, include_my_group_approvals=None)
```
### GetDeployments
#### Description:
:param str project: Project ID or project name
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| definition_id | int |  |
| definition_environment_id | int |  |
| created_by | str |  |
| min_modified_time | datetime |  |
| max_modified_time | datetime |  |
| deployment_status | str |  |
| operation_status | str |  |
| latest_attempts_only | bool |  |
| query_order | str |  |
| top | int |  |
| continuation_token | int |  |
| created_for | str |  |
| min_started_time | datetime |  |
| max_started_time | datetime |  |
| source_branch | str |  |
#### Return Type
:class:<GetDeploymentsResponseValue>
#### Example Usage
```

connection.clients.get_release_client().get_deployments(project, definition_id=None, definition_environment_id=None, created_by=None, min_modified_time=None, max_modified_time=None, deployment_status=None, operation_status=None, latest_attempts_only=None, query_order=None, top=None, continuation_token=None, created_for=None, min_started_time=None, max_started_time=None, source_branch=None)
```
### GetManualIntervention
#### Description:
Get manual intervention for a given release and manual intervention id.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| release_id | int | Id of the release. |
| manual_intervention_id | int | Id of the manual intervention. |
#### Return Type
:class:<ManualIntervention> <azure.devops.v5_1.release.models.ManualIntervention>
#### Example Usage
```

connection.clients.get_release_client().get_manual_intervention(project, release_id, manual_intervention_id)
```
### GetManualInterventions
#### Description:
List all manual interventions for a given release.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| release_id | int | Id of the release. |
#### Return Type
[ManualIntervention]
#### Example Usage
```

connection.clients.get_release_client().get_manual_interventions(project, release_id)
```
### GetRelease
#### Description:
Get a Release
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| release_id | int | Id of the release. |
| approval_filters | str | A filter which would allow fetching approval steps selectively based on whether it is automated, or manual. This would also decide whether we should fetch pre and post approval snapshots. Assumes All by default |
| property_filters | [str] | A comma-delimited list of extended properties to be retrieved. If set, the returned Release will contain values for the specified property Ids (if they exist). If not set, properties will not be included. |
| expand | str | A property that should be expanded in the release. |
| top_gate_records | int | Number of release gate records to get. Default is 5. |
#### Return Type
:class:<Release> <azure.devops.v5_1.release.models.Release>
#### Example Usage
```

connection.clients.get_release_client().get_release(project, release_id, approval_filters=None, property_filters=None, expand=None, top_gate_records=None)
```
### GetReleaseDefinition
#### Description:
Get a release definition.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| definition_id | int | Id of the release definition. |
| property_filters | [str] | A comma-delimited list of extended properties to be retrieved. If set, the returned Release Definition will contain values for the specified property Ids (if they exist). If not set, properties will not be included. |
#### Return Type
:class:<ReleaseDefinition> <azure.devops.v5_1.release.models.ReleaseDefinition>
#### Example Usage
```

connection.clients.get_release_client().get_release_definition(project, definition_id, property_filters=None)
```
### GetReleaseDefinitions
#### Description:
Get a list of release definitions.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| search_text | str | Get release definitions with names containing searchText. |
| expand | str | The properties that should be expanded in the list of Release definitions. |
| artifact_type | str | Release definitions with given artifactType will be returned. Values can be Build, Jenkins, GitHub, Nuget, Team Build (external), ExternalTFSBuild, Git, TFVC, ExternalTfsXamlBuild. |
| artifact_source_id | str | Release definitions with given artifactSourceId will be returned. e.g. For build it would be {projectGuid}:{BuildDefinitionId}, for Jenkins it would be {JenkinsConnectionId}:{JenkinsDefinitionId}, for TfsOnPrem it would be {TfsOnPremConnectionId}:{ProjectName}:{TfsOnPremDefinitionId}. For third-party artifacts e.g. TeamCity, BitBucket you may refer 'uniqueSourceIdentifier' inside vss-extension.json at https://github.com/Microsoft/vsts-rm-extensions/blob/master/Extensions. |
| top | int | Number of release definitions to get. |
| continuation_token | str | Gets the release definitions after the continuation token provided. |
| query_order | str | Gets the results in the defined order. Default is 'IdAscending'. |
| path | str | Gets the release definitions under the specified path. |
| is_exact_name_match | bool | 'true'to gets the release definitions with exact match as specified in searchText. Default is 'false'. |
| tag_filter | [str] | A comma-delimited list of tags. Only release definitions with these tags will be returned. |
| property_filters | [str] | A comma-delimited list of extended properties to be retrieved. If set, the returned Release Definitions will contain values for the specified property Ids (if they exist). If not set, properties will not be included. Note that this will not filter out any Release Definition from results irrespective of whether it has property set or not. |
| definition_id_filter | [str] | A comma-delimited list of release definitions to retrieve. |
| is_deleted | bool | 'true' to get release definitions that has been deleted. Default is 'false' |
| search_text_contains_folder_name | bool | 'true' to get the release definitions under the folder with name as specified in searchText. Default is 'false'. |
#### Return Type
:class:<GetReleaseDefinitionsResponseValue>
#### Example Usage
```

connection.clients.get_release_client().get_release_definitions(project, search_text=None, expand=None, artifact_type=None, artifact_source_id=None, top=None, continuation_token=None, query_order=None, path=None, is_exact_name_match=None, tag_filter=None, property_filters=None, definition_id_filter=None, is_deleted=None, search_text_contains_folder_name=None)
```
### GetReleaseRevision
#### Description:
Get release for a given revision number.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| release_id | int | Id of the release. |
| definition_snapshot_revision | int | Definition snapshot revision number. |
#### Return Type
object
#### Example Usage
```

connection.clients.get_release_client().get_release_revision(project, release_id, definition_snapshot_revision, **kwargs)
```
### GetReleases
#### Description:
Get a list of releases
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| definition_id | int | Releases from this release definition Id. |
| definition_environment_id | int |  |
| search_text | str | Releases with names containing searchText. |
| created_by | str | Releases created by this user. |
| status_filter | str | Releases that have this status. |
| environment_status_filter | int |  |
| min_created_time | datetime | Releases that were created after this time. |
| max_created_time | datetime | Releases that were created before this time. |
| query_order | str | Gets the results in the defined order of created date for releases. Default is descending. |
| top | int | Number of releases to get. Default is 50. |
| continuation_token | int | Gets the releases after the continuation token provided. |
| expand | str | The property that should be expanded in the list of releases. |
| artifact_type_id | str | Releases with given artifactTypeId will be returned. Values can be Build, Jenkins, GitHub, Nuget, Team Build (external), ExternalTFSBuild, Git, TFVC, ExternalTfsXamlBuild. |
| source_id | str | Unique identifier of the artifact used. e.g. For build it would be {projectGuid}:{BuildDefinitionId}, for Jenkins it would be {JenkinsConnectionId}:{JenkinsDefinitionId}, for TfsOnPrem it would be {TfsOnPremConnectionId}:{ProjectName}:{TfsOnPremDefinitionId}. For third-party artifacts e.g. TeamCity, BitBucket you may refer 'uniqueSourceIdentifier' inside vss-extension.json https://github.com/Microsoft/vsts-rm-extensions/blob/master/Extensions. |
| artifact_version_id | str | Releases with given artifactVersionId will be returned. E.g. in case of Build artifactType, it is buildId. |
| source_branch_filter | str | Releases with given sourceBranchFilter will be returned. |
| is_deleted | bool | Gets the soft deleted releases, if true. |
| tag_filter | [str] | A comma-delimited list of tags. Only releases with these tags will be returned. |
| property_filters | [str] | A comma-delimited list of extended properties to be retrieved. If set, the returned Releases will contain values for the specified property Ids (if they exist). If not set, properties will not be included. Note that this will not filter out any Release from results irrespective of whether it has property set or not. |
| release_id_filter | [int] | A comma-delimited list of releases Ids. Only releases with these Ids will be returned. |
| path | str | Releases under this folder path will be returned |
#### Return Type
:class:<GetReleasesResponseValue>
#### Example Usage
```

connection.clients.get_release_client().get_releases(project=None, definition_id=None, definition_environment_id=None, search_text=None, created_by=None, status_filter=None, environment_status_filter=None, min_created_time=None, max_created_time=None, query_order=None, top=None, continuation_token=None, expand=None, artifact_type_id=None, source_id=None, artifact_version_id=None, source_branch_filter=None, is_deleted=None, tag_filter=None, property_filters=None, release_id_filter=None, path=None)
```
### UpdateManualIntervention
#### Description:
Update manual intervention.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| manual_intervention_update_metadata | class | Meta data to update manual intervention. |
| project | str | Project ID or project name |
| release_id | int | Id of the release. |
| manual_intervention_id | int | Id of the manual intervention. |
#### Return Type
:class:<ManualIntervention> <azure.devops.v5_1.release.models.ManualIntervention>
#### Example Usage
```
from azure.devops.v5_1.release.models import ManualInterventionUpdateMetadata

connection.clients.get_release_client().update_manual_intervention(manual_intervention_update_metadata, project, release_id, manual_intervention_id)
```
### UpdateRelease
#### Description:
Update a complete release object.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| release | class | Release object for update. |
| project | str | Project ID or project name |
| release_id | int | Id of the release to update. |
#### Return Type
:class:<Release> <azure.devops.v5_1.release.models.Release>
#### Example Usage
```
from azure.devops.v5_1.release.models import Release

connection.clients.get_release_client().update_release(release, project, release_id)
```
### UpdateReleaseApproval
#### Description:
Update status of an approval
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| approval | class | ReleaseApproval object having status, approver and comments. |
| project | str | Project ID or project name |
| approval_id | int | Id of the approval. |
#### Return Type
:class:<ReleaseApproval> <azure.devops.v5_1.release.models.ReleaseApproval>
#### Example Usage
```
from azure.devops.v5_1.release.models import ReleaseApproval

connection.clients.get_release_client().update_release_approval(approval, project, approval_id)
```
### UpdateReleaseDefinition
#### Description:
Update a release definition.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| release_definition | class | Release definition object to update. |
| project | str | Project ID or project name |
#### Return Type
:class:<ReleaseDefinition> <azure.devops.v5_1.release.models.ReleaseDefinition>
#### Example Usage
```
from azure.devops.v5_1.release.models import ReleaseDefinition

connection.clients.get_release_client().update_release_definition(release_definition, project)
```
### UpdateReleaseResource
#### Description:
Update few properties of a release.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| release_update_metadata | class | Properties of release to update. |
| project | str | Project ID or project name |
| release_id | int | Id of the release to update. |
#### Return Type
:class:<Release> <azure.devops.v5_1.release.models.Release>
#### Example Usage
```
from azure.devops.v5_1.release.models import ReleaseUpdateMetadata

connection.clients.get_release_client().update_release_resource(release_update_metadata, project, release_id)
```
## Get Security Client

### HasPermissions
#### Description:
Evaluates whether the caller has the specified permissions on the specified set of security tokens.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| security_namespace_id | str | Security namespace identifier. |
| permissions | int | Permissions to evaluate. |
| tokens | str | One or more security tokens to evaluate. |
| always_allow_administrators | bool | If true and if the caller is an administrator, always return true. |
| delimiter | str | Optional security token separator. Defaults to ",". |
#### Return Type
[bool]
#### Example Usage
```

connection.clients.get_security_client().has_permissions(security_namespace_id, permissions=None, tokens=None, always_allow_administrators=None, delimiter=None)
```
### HasPermissionsBatch
#### Description:
Evaluates multiple permissions for the calling user.  Note: This method does not aggregate the results, nor does it short-circuit if one of the permissions evaluates to false.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| eval_batch | class | The set of evaluation requests. |
#### Return Type
:class:<PermissionEvaluationBatch> <azure.devops.v5_1.security.models.PermissionEvaluationBatch>
#### Example Usage
```
from azure.devops.v5_1.security.models import PermissionEvaluationBatch

connection.clients.get_security_client().has_permissions_batch(eval_batch)
```
### QueryAccessControlLists
#### Description:
Return a list of access control lists for the specified security namespace and token. All ACLs in the security namespace will be retrieved if no optional parameters are provided.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| security_namespace_id | str | Security namespace identifier. |
| token | str | Security token |
| descriptors | str | An optional filter string containing a list of identity descriptors separated by ',' whose ACEs should be retrieved. If this is left null, entire ACLs will be returned. |
| include_extended_info | bool | If true, populate the extended information properties for the access control entries contained in the returned lists. |
| recurse | bool | If true and this is a hierarchical namespace, return child ACLs of the specified token. |
#### Return Type
[AccessControlList]
#### Example Usage
```

connection.clients.get_security_client().query_access_control_lists(security_namespace_id, token=None, descriptors=None, include_extended_info=None, recurse=None)
```
### QuerySecurityNamespaces
#### Description:
List all security namespaces or just the specified namespace.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| security_namespace_id | str | Security namespace identifier. |
| local_only | bool | If true, retrieve only local security namespaces. |
#### Return Type
[SecurityNamespaceDescription]
#### Example Usage
```

connection.clients.get_security_client().query_security_namespaces(security_namespace_id=None, local_only=None)
```
### RemoveAccessControlEntries
#### Description:
Remove the specified ACEs from the ACL belonging to the specified token.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| security_namespace_id | str | Security namespace identifier. |
| token | str | The token whose ACL should be modified. |
| descriptors | str | String containing a list of identity descriptors separated by ',' whose entries should be removed. |
#### Return Type
bool
#### Example Usage
```

connection.clients.get_security_client().remove_access_control_entries(security_namespace_id, token=None, descriptors=None)
```
### RemoveAccessControlLists
#### Description:
Remove access control lists under the specfied security namespace.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| security_namespace_id | str | Security namespace identifier. |
| tokens | str | One or more comma-separated security tokens |
| recurse | bool | If true and this is a hierarchical namespace, also remove child ACLs of the specified tokens. |
#### Return Type
bool
#### Example Usage
```

connection.clients.get_security_client().remove_access_control_lists(security_namespace_id, tokens=None, recurse=None)
```
### RemovePermission
#### Description:
Removes the specified permissions on a security token for a user or group.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| security_namespace_id | str | Security namespace identifier. |
| descriptor | str | Identity descriptor of the user to remove permissions for. |
| permissions | int | Permissions to remove. |
| token | str | Security token to remove permissions for. |
#### Return Type
:class:<AccessControlEntry> <azure.devops.v5_1.security.models.AccessControlEntry>
#### Example Usage
```

connection.clients.get_security_client().remove_permission(security_namespace_id, descriptor, permissions=None, token=None)
```
### SetAccessControlEntries
#### Description:
Add or update ACEs in the ACL for the provided token. The request body contains the target token, a list of [ACEs](https://docs.microsoft.com/en-us/rest/api/azure/devops/security/access%20control%20entries/set%20access%20control%20entries?#accesscontrolentry) and a optional merge parameter. In the case of a collision (by identity descriptor) with an existing ACE in the ACL, the "merge" parameter determines the behavior. If set, the existing ACE has its allow and deny merged with the incoming ACE's allow and deny. If unset, the existing ACE is displaced.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| container | class |  |
| security_namespace_id | str | Security namespace identifier. |
#### Return Type
[AccessControlEntry]
#### Example Usage
```
from azure.devops.v5_1.security.models import object

connection.clients.get_security_client().set_access_control_entries(container, security_namespace_id)
```
### SetAccessControlLists
#### Description:
Create or update one or more access control lists. All data that currently exists for the ACLs supplied will be overwritten.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| access_control_lists | class | A list of ACLs to create or update. |
| security_namespace_id | str | Security namespace identifier. |
#### Return Type
[AccessControlEntry]
#### Example Usage
```
from azure.devops.v5_1.security.models import VssJsonCollectionWrapper

connection.clients.get_security_client().set_access_control_lists(access_control_lists, security_namespace_id)
```
## Get Service Hooks Client

### CreateSubscription
#### Description:
Create a subscription.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| subscription | class | Subscription to be created. |
#### Return Type
:class:<Subscription> <azure.devops.v5_1.service_hooks.models.Subscription>
#### Example Usage
```
from azure.devops.v5_1.service_hooks.models import Subscription

connection.clients.get_service_hooks_client().create_subscription(subscription)
```
### CreateSubscriptionsQuery
#### Description:
Query for service hook subscriptions.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| query | class |  |
#### Return Type
:class:<SubscriptionsQuery> <azure.devops.v5_1.service_hooks.models.SubscriptionsQuery>
#### Example Usage
```
from azure.devops.v5_1.service_hooks.models import SubscriptionsQuery

connection.clients.get_service_hooks_client().create_subscriptions_query(query)
```
### CreateTestNotification
#### Description:
Sends a test notification. This is useful for verifying the configuration of an updated or new service hooks subscription.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| test_notification | class |  |
| use_real_data | bool | Only allow testing with real data in existing subscriptions. |
#### Return Type
:class:<Notification> <azure.devops.v5_1.service_hooks.models.Notification>
#### Example Usage
```
from azure.devops.v5_1.service_hooks.models import Notification

connection.clients.get_service_hooks_client().create_test_notification(test_notification, use_real_data=None)
```
### DeleteSubscription
#### Description:
Delete a specific service hooks subscription.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| subscription_id | str | ID for a subscription. |
#### Return Type
:class:<Notification> <azure.devops.v5_1.service_hooks.models.Notification>
#### Example Usage
```

connection.clients.get_service_hooks_client().delete_subscription(subscription_id)
```
### GetConsumer
#### Description:
Get a specific consumer service. Optionally filter out consumer actions that do not support any event types for the specified publisher.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| consumer_id | str | ID for a consumer. |
| publisher_id | str |  |
#### Return Type
:class:<Consumer> <azure.devops.v5_1.service_hooks.models.Consumer>
#### Example Usage
```

connection.clients.get_service_hooks_client().get_consumer(consumer_id, publisher_id=None)
```
### GetConsumerAction
#### Description:
Get details about a specific consumer action.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| consumer_id | str | ID for a consumer. |
| consumer_action_id | str | ID for a consumerActionId. |
| publisher_id | str |  |
#### Return Type
:class:<ConsumerAction> <azure.devops.v5_1.service_hooks.models.ConsumerAction>
#### Example Usage
```

connection.clients.get_service_hooks_client().get_consumer_action(consumer_id, consumer_action_id, publisher_id=None)
```
### GetEventType
#### Description:
Get a specific event type.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| publisher_id | str | ID for a publisher. |
| event_type_id | str |  |
#### Return Type
:class:<EventTypeDescriptor> <azure.devops.v5_1.service_hooks.models.EventTypeDescriptor>
#### Example Usage
```

connection.clients.get_service_hooks_client().get_event_type(publisher_id, event_type_id)
```
### GetNotification
#### Description:
Get a specific notification for a subscription.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| subscription_id | str | ID for a subscription. |
| notification_id | int |  |
#### Return Type
:class:<Notification> <azure.devops.v5_1.service_hooks.models.Notification>
#### Example Usage
```

connection.clients.get_service_hooks_client().get_notification(subscription_id, notification_id)
```
### GetNotifications
#### Description:
Get a list of notifications for a specific subscription. A notification includes details about the event, the request to and the response from the consumer service.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| subscription_id | str | ID for a subscription. |
| max_results | int | Maximum number of notifications to return. Default is **100**. |
| status | str | Get only notifications with this status. |
| result | str | Get only notifications with this result type. |
#### Return Type
[Notification]
#### Example Usage
```

connection.clients.get_service_hooks_client().get_notifications(subscription_id, max_results=None, status=None, result=None)
```
### GetPublisher
#### Description:
Get a specific service hooks publisher.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| publisher_id | str | ID for a publisher. |
#### Return Type
:class:<Publisher> <azure.devops.v5_1.service_hooks.models.Publisher>
#### Example Usage
```

connection.clients.get_service_hooks_client().get_publisher(publisher_id)
```
### GetSubscription
#### Description:
Get a specific service hooks subscription.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| subscription_id | str | ID for a subscription. |
#### Return Type
:class:<Subscription> <azure.devops.v5_1.service_hooks.models.Subscription>
#### Example Usage
```

connection.clients.get_service_hooks_client().get_subscription(subscription_id)
```
### ListConsumerActions
#### Description:
Get a list of consumer actions for a specific consumer.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| consumer_id | str | ID for a consumer. |
| publisher_id | str |  |
#### Return Type
[ConsumerAction]
#### Example Usage
```

connection.clients.get_service_hooks_client().list_consumer_actions(consumer_id, publisher_id=None)
```
### ListConsumers
#### Description:
Get a list of available service hook consumer services. Optionally filter by consumers that support at least one event type from the specific publisher.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| publisher_id | str |  |
#### Return Type
[Consumer]
#### Example Usage
```

connection.clients.get_service_hooks_client().list_consumers(publisher_id=None)
```
### ListEventTypes
#### Description:
Get the event types for a specific publisher.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| publisher_id | str | ID for a publisher. |
#### Return Type
[EventTypeDescriptor]
#### Example Usage
```

connection.clients.get_service_hooks_client().list_event_types(publisher_id)
```
### ListPublishers
#### Description:
Get a list of publishers.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
#### Return Type
[Publisher]
#### Example Usage
```

connection.clients.get_service_hooks_client().list_publishers()
```
### ListSubscriptions
#### Description:
Get a list of subscriptions.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| publisher_id | str | ID for a subscription. |
| event_type | str | The event type to filter on (if any). |
| consumer_id | str | ID for a consumer. |
| consumer_action_id | str | ID for a consumerActionId. |
#### Return Type
[Subscription]
#### Example Usage
```

connection.clients.get_service_hooks_client().list_subscriptions(publisher_id=None, event_type=None, consumer_id=None, consumer_action_id=None)
```
### QueryInputValues
#### Description:
:param :class:`<InputValuesQuery> <azure.devops.v5_1.service_hooks.models.InputValuesQuery>` input_values_query:
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| input_values_query | class |  |
| publisher_id | str |  |
#### Return Type
:class:<InputValuesQuery> <azure.devops.v5_1.service_hooks.models.InputValuesQuery>
#### Example Usage
```
from azure.devops.v5_1.service_hooks.models import InputValuesQuery

connection.clients.get_service_hooks_client().query_input_values(input_values_query, publisher_id)
```
### QueryNotifications
#### Description:
Query for notifications. A notification includes details about the event, the request to and the response from the consumer service.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| query | class |  |
#### Return Type
:class:<NotificationsQuery> <azure.devops.v5_1.service_hooks.models.NotificationsQuery>
#### Example Usage
```
from azure.devops.v5_1.service_hooks.models import NotificationsQuery

connection.clients.get_service_hooks_client().query_notifications(query)
```
### QueryPublishers
#### Description:
Query for service hook publishers.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| query | class |  |
#### Return Type
:class:<PublishersQuery> <azure.devops.v5_1.service_hooks.models.PublishersQuery>
#### Example Usage
```
from azure.devops.v5_1.service_hooks.models import PublishersQuery

connection.clients.get_service_hooks_client().query_publishers(query)
```
### ReplaceSubscription
#### Description:
Update a subscription. <param name="subscriptionId">ID for a subscription that you wish to update.</param>
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| subscription | class |  |
| subscription_id | str |  |
#### Return Type
:class:<Subscription> <azure.devops.v5_1.service_hooks.models.Subscription>
#### Example Usage
```
from azure.devops.v5_1.service_hooks.models import Subscription

connection.clients.get_service_hooks_client().replace_subscription(subscription, subscription_id=None)
```
## Get Task Agent Client

### AddAgent
#### Description:
Adds an agent to a pool.  You probably don't want to call this endpoint directly. Instead, [configure an agent](https://docs.microsoft.com/azure/devops/pipelines/agents/agents) using the agent download package.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| agent | class | Details about the agent being added |
| pool_id | int | The agent pool in which to add the agent |
#### Return Type
:class:<TaskAgent> <azure.devops.v5_1.task_agent.models.TaskAgent>
#### Example Usage
```
from azure.devops.v5_1.task_agent.models import TaskAgent

connection.clients.get_task_agent_client().add_agent(agent, pool_id)
```
### AddAgentPool
#### Description:
Create an agent pool.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| pool | class | Details about the new agent pool |
#### Return Type
:class:<TaskAgentPool> <azure.devops.v5_1.task_agent.models.TaskAgentPool>
#### Example Usage
```
from azure.devops.v5_1.task_agent.models import TaskAgentPool

connection.clients.get_task_agent_client().add_agent_pool(pool)
```
### DeleteAgent
#### Description:
Delete an agent.  You probably don't want to call this endpoint directly. Instead, [use the agent configuration script](https://docs.microsoft.com/azure/devops/pipelines/agents/agents) to remove an agent from your organization.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| pool_id | int | The pool ID to remove the agent from |
| agent_id | int | The agent ID to remove |
#### Return Type
:class:<TaskAgentPool> <azure.devops.v5_1.task_agent.models.TaskAgentPool>
#### Example Usage
```

connection.clients.get_task_agent_client().delete_agent(pool_id, agent_id)
```
### DeleteAgentPool
#### Description:
Delete an agent pool.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| pool_id | int | ID of the agent pool to delete |
#### Return Type
:class:<TaskAgentPool> <azure.devops.v5_1.task_agent.models.TaskAgentPool>
#### Example Usage
```

connection.clients.get_task_agent_client().delete_agent_pool(pool_id)
```
### GetAgent
#### Description:
Get information about an agent.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| pool_id | int | The agent pool containing the agent |
| agent_id | int | The agent ID to get information about |
| include_capabilities | bool | Whether to include the agent's capabilities in the response |
| include_assigned_request | bool | Whether to include details about the agent's current work |
| include_last_completed_request | bool | Whether to include details about the agents' most recent completed work |
| property_filters | [str] | Filter which custom properties will be returned |
#### Return Type
:class:<TaskAgent> <azure.devops.v5_1.task_agent.models.TaskAgent>
#### Example Usage
```

connection.clients.get_task_agent_client().get_agent(pool_id, agent_id, include_capabilities=None, include_assigned_request=None, include_last_completed_request=None, property_filters=None)
```
### GetAgentPool
#### Description:
Get information about an agent pool.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| pool_id | int | An agent pool ID |
| properties | [str] | Agent pool properties (comma-separated) |
| action_filter | str | Filter by whether the calling user has use or manage permissions |
#### Return Type
:class:<TaskAgentPool> <azure.devops.v5_1.task_agent.models.TaskAgentPool>
#### Example Usage
```

connection.clients.get_task_agent_client().get_agent_pool(pool_id, properties=None, action_filter=None)
```
### GetAgentPools
#### Description:
Get a list of agent pools.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| pool_name | str | Filter by name |
| properties | [str] | Filter by agent pool properties (comma-separated) |
| pool_type | str | Filter by pool type |
| action_filter | str | Filter by whether the calling user has use or manage permissions |
#### Return Type
[TaskAgentPool]
#### Example Usage
```

connection.clients.get_task_agent_client().get_agent_pools(pool_name=None, properties=None, pool_type=None, action_filter=None)
```
### GetAgentPoolsByIds
#### Description:
Get a list of agent pools.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| pool_ids | [int] | pool Ids to fetch |
| action_filter | str | Filter by whether the calling user has use or manage permissions |
#### Return Type
[TaskAgentPool]
#### Example Usage
```

connection.clients.get_task_agent_client().get_agent_pools_by_ids(pool_ids, action_filter=None)
```
### GetAgents
#### Description:
Get a list of agents.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| pool_id | int | The agent pool containing the agents |
| agent_name | str | Filter on agent name |
| include_capabilities | bool | Whether to include the agents' capabilities in the response |
| include_assigned_request | bool | Whether to include details about the agents' current work |
| include_last_completed_request | bool | Whether to include details about the agents' most recent completed work |
| property_filters | [str] | Filter which custom properties will be returned |
| demands | [str] | Filter by demands the agents can satisfy |
#### Return Type
[TaskAgent]
#### Example Usage
```

connection.clients.get_task_agent_client().get_agents(pool_id, agent_name=None, include_capabilities=None, include_assigned_request=None, include_last_completed_request=None, property_filters=None, demands=None)
```
### GetYamlSchema
#### Description:
:rtype: object
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
#### Return Type
object
#### Example Usage
```

connection.clients.get_task_agent_client().get_yaml_schema()
```
### ReplaceAgent
#### Description:
Replace an agent.  You probably don't want to call this endpoint directly. Instead, [use the agent configuration script](https://docs.microsoft.com/azure/devops/pipelines/agents/agents) to remove and reconfigure an agent from your organization.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| agent | class | Updated details about the replacing agent |
| pool_id | int | The agent pool to use |
| agent_id | int | The agent to replace |
#### Return Type
:class:<TaskAgent> <azure.devops.v5_1.task_agent.models.TaskAgent>
#### Example Usage
```
from azure.devops.v5_1.task_agent.models import TaskAgent

connection.clients.get_task_agent_client().replace_agent(agent, pool_id, agent_id)
```
### UpdateAgent
#### Description:
Update agent details.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| agent | class | Updated details about the agent |
| pool_id | int | The agent pool to use |
| agent_id | int | The agent to update |
#### Return Type
:class:<TaskAgent> <azure.devops.v5_1.task_agent.models.TaskAgent>
#### Example Usage
```
from azure.devops.v5_1.task_agent.models import TaskAgent

connection.clients.get_task_agent_client().update_agent(agent, pool_id, agent_id)
```
### UpdateAgentPool
#### Description:
Update properties on an agent pool
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| pool | class | Updated agent pool details |
| pool_id | int | The agent pool to update |
#### Return Type
:class:<TaskAgentPool> <azure.devops.v5_1.task_agent.models.TaskAgentPool>
#### Example Usage
```
from azure.devops.v5_1.task_agent.models import TaskAgentPool

connection.clients.get_task_agent_client().update_agent_pool(pool, pool_id)
```
## Get Task Client

### AppendLogContent
#### Description:
:param object upload_stream: Stream to upload
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| upload_stream | object | Stream to upload |
| scope_identifier | str | The project GUID to scope the request |
| hub_name | str | The name of the server hub: "build" for the Build server or "rm" for the Release Management server |
| plan_id | str |  |
| log_id | int |  |
#### Return Type
:class:<TaskLog> <azure.devops.v5_1.task.models.TaskLog>
#### Example Usage
```

connection.clients.get_task_client().append_log_content(upload_stream, scope_identifier, hub_name, plan_id, log_id, **kwargs)
```
### CreateLog
#### Description:
:param :class:`<TaskLog> <azure.devops.v5_1.task.models.TaskLog>` log:
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| log | class |  |
| scope_identifier | str | The project GUID to scope the request |
| hub_name | str | The name of the server hub: "build" for the Build server or "rm" for the Release Management server |
| plan_id | str |  |
#### Return Type
:class:<TaskLog> <azure.devops.v5_1.task.models.TaskLog>
#### Example Usage
```
from azure.devops.v5_1.task.models import TaskLog

connection.clients.get_task_client().create_log(log, scope_identifier, hub_name, plan_id)
```
### CreateTimeline
#### Description:
:param :class:`<Timeline> <azure.devops.v5_1.task.models.Timeline>` timeline:
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| timeline | class |  |
| scope_identifier | str | The project GUID to scope the request |
| hub_name | str | The name of the server hub: "build" for the Build server or "rm" for the Release Management server |
| plan_id | str |  |
#### Return Type
:class:<Timeline> <azure.devops.v5_1.task.models.Timeline>
#### Example Usage
```
from azure.devops.v5_1.task.models import Timeline

connection.clients.get_task_client().create_timeline(timeline, scope_identifier, hub_name, plan_id)
```
### DeleteTimeline
#### Description:
:param str scope_identifier: The project GUID to scope the request
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| scope_identifier | str | The project GUID to scope the request |
| hub_name | str | The name of the server hub: "build" for the Build server or "rm" for the Release Management server |
| plan_id | str |  |
| timeline_id | str |  |
#### Return Type
:class:<Timeline> <azure.devops.v5_1.task.models.Timeline>
#### Example Usage
```

connection.clients.get_task_client().delete_timeline(scope_identifier, hub_name, plan_id, timeline_id)
```
### GetLog
#### Description:
:param str scope_identifier: The project GUID to scope the request
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| scope_identifier | str | The project GUID to scope the request |
| hub_name | str | The name of the server hub: "build" for the Build server or "rm" for the Release Management server |
| plan_id | str |  |
| log_id | int |  |
| start_line | long |  |
| end_line | long |  |
#### Return Type
[str]
#### Example Usage
```

connection.clients.get_task_client().get_log(scope_identifier, hub_name, plan_id, log_id, start_line=None, end_line=None)
```
### GetLogs
#### Description:
:param str scope_identifier: The project GUID to scope the request
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| scope_identifier | str | The project GUID to scope the request |
| hub_name | str | The name of the server hub: "build" for the Build server or "rm" for the Release Management server |
| plan_id | str |  |
#### Return Type
[TaskLog]
#### Example Usage
```

connection.clients.get_task_client().get_logs(scope_identifier, hub_name, plan_id)
```
### GetRecords
#### Description:
:param str scope_identifier: The project GUID to scope the request
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| scope_identifier | str | The project GUID to scope the request |
| hub_name | str | The name of the server hub: "build" for the Build server or "rm" for the Release Management server |
| plan_id | str |  |
| timeline_id | str |  |
| change_id | int |  |
#### Return Type
[TimelineRecord]
#### Example Usage
```

connection.clients.get_task_client().get_records(scope_identifier, hub_name, plan_id, timeline_id, change_id=None)
```
### GetTimeline
#### Description:
:param str scope_identifier: The project GUID to scope the request
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| scope_identifier | str | The project GUID to scope the request |
| hub_name | str | The name of the server hub: "build" for the Build server or "rm" for the Release Management server |
| plan_id | str |  |
| timeline_id | str |  |
| change_id | int |  |
| include_records | bool |  |
#### Return Type
:class:<Timeline> <azure.devops.v5_1.task.models.Timeline>
#### Example Usage
```

connection.clients.get_task_client().get_timeline(scope_identifier, hub_name, plan_id, timeline_id, change_id=None, include_records=None)
```
### GetTimelines
#### Description:
:param str scope_identifier: The project GUID to scope the request
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| scope_identifier | str | The project GUID to scope the request |
| hub_name | str | The name of the server hub: "build" for the Build server or "rm" for the Release Management server |
| plan_id | str |  |
#### Return Type
[Timeline]
#### Example Usage
```

connection.clients.get_task_client().get_timelines(scope_identifier, hub_name, plan_id)
```
### UpdateRecords
#### Description:
:param :class:`<VssJsonCollectionWrapper> <azure.devops.v5_1.task.models.VssJsonCollectionWrapper>` records:
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| records | class |  |
| scope_identifier | str | The project GUID to scope the request |
| hub_name | str | The name of the server hub: "build" for the Build server or "rm" for the Release Management server |
| plan_id | str |  |
| timeline_id | str |  |
#### Return Type
[TimelineRecord]
#### Example Usage
```
from azure.devops.v5_1.task.models import VssJsonCollectionWrapper

connection.clients.get_task_client().update_records(records, scope_identifier, hub_name, plan_id, timeline_id)
```
## Get Test Client

### AddTestCasesToSuite
#### Description:
Add test cases to suite.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| plan_id | int | ID of the test plan that contains the suite. |
| suite_id | int | ID of the test suite to which the test cases must be added. |
| test_case_ids | str | IDs of the test cases to add to the suite. Ids are specified in comma separated format. |
#### Return Type
[SuiteTestCase]
#### Example Usage
```

connection.clients.get_test_client().add_test_cases_to_suite(project, plan_id, suite_id, test_case_ids)
```
### AddTestResultsToTestRun
#### Description:
Add test results to a test run.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| results | [TestCaseResult] | List of test results to add. |
| project | str | Project ID or project name |
| run_id | int | Test run ID into which test results to add. |
#### Return Type
[TestCaseResult]
#### Example Usage
```

connection.clients.get_test_client().add_test_results_to_test_run(results, project, run_id)
```
### CreateTestRun
#### Description:
Create new test run.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| test_run | class | Run details RunCreateModel |
| project | str | Project ID or project name |
#### Return Type
:class:<TestRun> <azure.devops.v5_1.test.models.TestRun>
#### Example Usage
```
from azure.devops.v5_1.test.models import RunCreateModel

connection.clients.get_test_client().create_test_run(test_run, project)
```
### DeleteTestRun
#### Description:
Delete a test run by its ID.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| run_id | int | ID of the run to delete. |
#### Return Type
:class:<TestRun> <azure.devops.v5_1.test.models.TestRun>
#### Example Usage
```

connection.clients.get_test_client().delete_test_run(project, run_id)
```
### GetActionResults
#### Description:
Gets the action results for an iteration in a test result.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| run_id | int | ID of the test run that contains the result. |
| test_case_result_id | int | ID of the test result that contains the iterations. |
| iteration_id | int | ID of the iteration that contains the actions. |
| action_path | str | Path of a specific action, used to get just that action. |
#### Return Type
[TestActionResultModel]
#### Example Usage
```

connection.clients.get_test_client().get_action_results(project, run_id, test_case_result_id, iteration_id, action_path=None)
```
### GetPoint
#### Description:
Get a test point.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| plan_id | int | ID of the test plan. |
| suite_id | int | ID of the suite that contains the point. |
| point_ids | int | ID of the test point to get. |
| wit_fields | str | Comma-separated list of work item field names. |
#### Return Type
:class:<TestPoint> <azure.devops.v5_1.test.models.TestPoint>
#### Example Usage
```

connection.clients.get_test_client().get_point(project, plan_id, suite_id, point_ids, wit_fields=None)
```
### GetPoints
#### Description:
Get a list of test points.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| plan_id | int | ID of the test plan. |
| suite_id | int | ID of the suite that contains the points. |
| wit_fields | str | Comma-separated list of work item field names. |
| configuration_id | str | Get test points for specific configuration. |
| test_case_id | str | Get test points for a specific test case, valid when configurationId is not set. |
| test_point_ids | str | Get test points for comma-separated list of test point IDs, valid only when configurationId and testCaseId are not set. |
| include_point_details | bool | Include all properties for the test point. |
| skip | int | Number of test points to skip.. |
| top | int | Number of test points to return. |
#### Return Type
[TestPoint]
#### Example Usage
```

connection.clients.get_test_client().get_points(project, plan_id, suite_id, wit_fields=None, configuration_id=None, test_case_id=None, test_point_ids=None, include_point_details=None, skip=None, top=None)
```
### GetResultParameters
#### Description:
Get a list of parameterized results
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| run_id | int | ID of the test run that contains the result. |
| test_case_result_id | int | ID of the test result that contains the iterations. |
| iteration_id | int | ID of the iteration that contains the parameterized results. |
| param_name | str | Name of the parameter. |
#### Return Type
[TestResultParameterModel]
#### Example Usage
```

connection.clients.get_test_client().get_result_parameters(project, run_id, test_case_result_id, iteration_id, param_name=None)
```
### GetTestCaseById
#### Description:
Get a specific test case in a test suite with test case id.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| plan_id | int | ID of the test plan that contains the suites. |
| suite_id | int | ID of the suite that contains the test case. |
| test_case_ids | int | ID of the test case to get. |
#### Return Type
:class:<SuiteTestCase> <azure.devops.v5_1.test.models.SuiteTestCase>
#### Example Usage
```

connection.clients.get_test_client().get_test_case_by_id(project, plan_id, suite_id, test_case_ids)
```
### GetTestCases
#### Description:
Get all test cases in a suite.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| plan_id | int | ID of the test plan that contains the suites. |
| suite_id | int | ID of the suite to get. |
#### Return Type
[SuiteTestCase]
#### Example Usage
```

connection.clients.get_test_client().get_test_cases(project, plan_id, suite_id)
```
### GetTestIteration
#### Description:
Get iteration for a result
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| run_id | int | ID of the test run that contains the result. |
| test_case_result_id | int | ID of the test result that contains the iterations. |
| iteration_id | int | Id of the test results Iteration. |
| include_action_results | bool | Include result details for each action performed in the test iteration. ActionResults refer to outcome (pass/fail) of test steps that are executed as part of a running a manual test. Including the ActionResults flag gets the outcome of test steps in the actionResults section and test parameters in the parameters section for each test iteration. |
#### Return Type
:class:<TestIterationDetailsModel> <azure.devops.v5_1.test.models.TestIterationDetailsModel>
#### Example Usage
```

connection.clients.get_test_client().get_test_iteration(project, run_id, test_case_result_id, iteration_id, include_action_results=None)
```
### GetTestIterations
#### Description:
Get iterations for a result
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| run_id | int | ID of the test run that contains the result. |
| test_case_result_id | int | ID of the test result that contains the iterations. |
| include_action_results | bool | Include result details for each action performed in the test iteration. ActionResults refer to outcome (pass/fail) of test steps that are executed as part of a running a manual test. Including the ActionResults flag gets the outcome of test steps in the actionResults section and test parameters in the parameters section for each test iteration. |
#### Return Type
[TestIterationDetailsModel]
#### Example Usage
```

connection.clients.get_test_client().get_test_iterations(project, run_id, test_case_result_id, include_action_results=None)
```
### GetTestResultById
#### Description:
Get a test result for a test run.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| run_id | int | Test run ID of a test result to fetch. |
| test_case_result_id | int | Test result ID. |
| details_to_include | str | Details to include with test results. Default is None. Other values are Iterations, WorkItems and SubResults. |
#### Return Type
:class:<TestCaseResult> <azure.devops.v5_1.test.models.TestCaseResult>
#### Example Usage
```

connection.clients.get_test_client().get_test_result_by_id(project, run_id, test_case_result_id, details_to_include=None)
```
### GetTestResults
#### Description:
Get test results for a test run.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| run_id | int | Test run ID of test results to fetch. |
| details_to_include | str | Details to include with test results. Default is None. Other values are Iterations and WorkItems. |
| skip | int | Number of test results to skip from beginning. |
| top | int | Number of test results to return. Maximum is 1000 when detailsToInclude is None and 200 otherwise. |
| outcomes | [TestOutcome] | Comma separated list of test outcomes to filter test results. |
#### Return Type
[TestCaseResult]
#### Example Usage
```

connection.clients.get_test_client().get_test_results(project, run_id, details_to_include=None, skip=None, top=None, outcomes=None)
```
### GetTestRunById
#### Description:
Get a test run by its ID.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| run_id | int | ID of the run to get. |
| include_details | bool | Default value is true. It includes details like run statistics, release, build, test environment, post process state, and more. |
#### Return Type
:class:<TestRun> <azure.devops.v5_1.test.models.TestRun>
#### Example Usage
```

connection.clients.get_test_client().get_test_run_by_id(project, run_id, include_details=None)
```
### GetTestRunStatistics
#### Description:
Get test run statistics , used when we want to get summary of a run by outcome.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| run_id | int | ID of the run to get. |
#### Return Type
:class:<TestRunStatistic> <azure.devops.v5_1.test.models.TestRunStatistic>
#### Example Usage
```

connection.clients.get_test_client().get_test_run_statistics(project, run_id)
```
### GetTestRuns
#### Description:
Get a list of test runs.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| build_uri | str | URI of the build that the runs used. |
| owner | str | Team foundation ID of the owner of the runs. |
| tmi_run_id | str |  |
| plan_id | int | ID of the test plan that the runs are a part of. |
| include_run_details | bool | If true, include all the properties of the runs. |
| automated | bool | If true, only returns automated runs. |
| skip | int | Number of test runs to skip. |
| top | int | Number of test runs to return. |
#### Return Type
[TestRun]
#### Example Usage
```

connection.clients.get_test_client().get_test_runs(project, build_uri=None, owner=None, tmi_run_id=None, plan_id=None, include_run_details=None, automated=None, skip=None, top=None)
```
### QueryTestRuns
#### Description:
Query Test Runs based on filters. Mandatory fields are minLastUpdatedDate and maxLastUpdatedDate.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| min_last_updated_date | datetime | Minimum Last Modified Date of run to be queried (Mandatory). |
| max_last_updated_date | datetime | Maximum Last Modified Date of run to be queried (Mandatory, difference between min and max date can be atmost 7 days). |
| state | str | Current state of the Runs to be queried. |
| plan_ids | [int] | Plan Ids of the Runs to be queried, comma separated list of valid ids (limit no. of ids 10). |
| is_automated | bool | Automation type of the Runs to be queried. |
| publish_context | str | PublishContext of the Runs to be queried. |
| build_ids | [int] | Build Ids of the Runs to be queried, comma separated list of valid ids (limit no. of ids 10). |
| build_def_ids | [int] | Build Definition Ids of the Runs to be queried, comma separated list of valid ids (limit no. of ids 10). |
| branch_name | str | Source Branch name of the Runs to be queried. |
| release_ids | [int] | Release Ids of the Runs to be queried, comma separated list of valid ids (limit no. of ids 10). |
| release_def_ids | [int] | Release Definition Ids of the Runs to be queried, comma separated list of valid ids (limit no. of ids 10). |
| release_env_ids | [int] | Release Environment Ids of the Runs to be queried, comma separated list of valid ids (limit no. of ids 10). |
| release_env_def_ids | [int] | Release Environment Definition Ids of the Runs to be queried, comma separated list of valid ids (limit no. of ids 10). |
| run_title | str | Run Title of the Runs to be queried. |
| top | int | Number of runs to be queried. Limit is 100 |
| continuation_token | str | continuationToken received from previous batch or null for first batch. It is not supposed to be created (or altered, if received from last batch) by user. |
#### Return Type
:class:<QueryTestRunsResponseValue>
#### Example Usage
```

connection.clients.get_test_client().query_test_runs(project, min_last_updated_date, max_last_updated_date, state=None, plan_ids=None, is_automated=None, publish_context=None, build_ids=None, build_def_ids=None, branch_name=None, release_ids=None, release_def_ids=None, release_env_ids=None, release_env_def_ids=None, run_title=None, top=None, continuation_token=None)
```
### RemoveTestCasesFromSuiteUrl
#### Description:
The test points associated with the test cases are removed from the test suite. The test case work item is not deleted from the system. See test cases resource to delete a test case permanently.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| plan_id | int | ID of the test plan that contains the suite. |
| suite_id | int | ID of the suite to get. |
| test_case_ids | str | IDs of the test cases to remove from the suite. |
#### Return Type
:class:<QueryTestRunsResponseValue>
#### Example Usage
```

connection.clients.get_test_client().remove_test_cases_from_suite_url(project, plan_id, suite_id, test_case_ids)
```
### UpdateSuiteTestCases
#### Description:
Updates the properties of the test case association in a suite.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| suite_test_case_update_model | class | Model for updation of the properties of test case suite association. |
| project | str | Project ID or project name |
| plan_id | int | ID of the test plan that contains the suite. |
| suite_id | int | ID of the test suite to which the test cases must be added. |
| test_case_ids | str | IDs of the test cases to add to the suite. Ids are specified in comma separated format. |
#### Return Type
[SuiteTestCase]
#### Example Usage
```
from azure.devops.v5_1.test.models import SuiteTestCaseUpdateModel

connection.clients.get_test_client().update_suite_test_cases(suite_test_case_update_model, project, plan_id, suite_id, test_case_ids)
```
### UpdateTestPoints
#### Description:
Update test points.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| point_update_model | class | Data to update. |
| project | str | Project ID or project name |
| plan_id | int | ID of the test plan. |
| suite_id | int | ID of the suite that contains the points. |
| point_ids | str | ID of the test point to get. Use a comma-separated list of IDs to update multiple test points. |
#### Return Type
[TestPoint]
#### Example Usage
```
from azure.devops.v5_1.test.models import PointUpdateModel

connection.clients.get_test_client().update_test_points(point_update_model, project, plan_id, suite_id, point_ids)
```
### UpdateTestResults
#### Description:
Update test results in a test run.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| results | [TestCaseResult] | List of test results to update. |
| project | str | Project ID or project name |
| run_id | int | Test run ID whose test results to update. |
#### Return Type
[TestCaseResult]
#### Example Usage
```

connection.clients.get_test_client().update_test_results(results, project, run_id)
```
### UpdateTestRun
#### Description:
Update test run by its ID.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| run_update_model | class | Run details RunUpdateModel |
| project | str | Project ID or project name |
| run_id | int | ID of the run to update. |
#### Return Type
:class:<TestRun> <azure.devops.v5_1.test.models.TestRun>
#### Example Usage
```
from azure.devops.v5_1.test.models import RunUpdateModel

connection.clients.get_test_client().update_test_run(run_update_model, project, run_id)
```
## Get Test Plan Client

### GetSuitesByTestCaseId
#### Description:
Find the list of all test suites in which a given test case is present. This is helpful if you need to find out which test suites are using a test case, when you need to make changes to a test case.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| test_case_id | int | ID of the test case for which suites need to be fetched. |
#### Return Type
[TestSuite]
#### Example Usage
```

connection.clients.get_test_plan_client().get_suites_by_test_case_id(test_case_id)
```
## Get Test Results Client

### GetTestRunStatistics
#### Description:
Get test run statistics , used when we want to get summary of a run by outcome.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| run_id | int | ID of the run to get. |
#### Return Type
:class:<TestRunStatistic> <azure.devops.v5_1.test_results.models.TestRunStatistic>
#### Example Usage
```

connection.clients.get_test_results_client().get_test_run_statistics(project, run_id)
```
## Get Tfvc Client

### CreateChangeset
#### Description:
Create a new changeset.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| changeset | class |  |
| project | str | Project ID or project name |
#### Return Type
:class:<TfvcChangesetRef> <azure.devops.v5_1.tfvc.models.TfvcChangesetRef>
#### Example Usage
```
from azure.devops.v5_1.tfvc.models import TfvcChangeset

connection.clients.get_tfvc_client().create_changeset(changeset, project=None)
```
### GetBatchedChangesets
#### Description:
Returns changesets for a given list of changeset Ids.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| changesets_request_data | class | List of changeset IDs. |
#### Return Type
[TfvcChangesetRef]
#### Example Usage
```
from azure.devops.v5_1.tfvc.models import TfvcChangesetsRequestData

connection.clients.get_tfvc_client().get_batched_changesets(changesets_request_data)
```
### GetBranch
#### Description:
Get a single branch hierarchy at the given path with parents or children as specified.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| path | str | Full path to the branch.  Default: $/ Examples: $/, $/MyProject, $/MyProject/SomeFolder. |
| project | str | Project ID or project name |
| include_parent | bool | Return the parent branch, if there is one. Default: False |
| include_children | bool | Return child branches, if there are any. Default: False |
#### Return Type
:class:<TfvcBranch> <azure.devops.v5_1.tfvc.models.TfvcBranch>
#### Example Usage
```

connection.clients.get_tfvc_client().get_branch(path, project=None, include_parent=None, include_children=None)
```
### GetBranchRefs
#### Description:
Get branch hierarchies below the specified scopePath
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| scope_path | str | Full path to the branch.  Default: $/ Examples: $/, $/MyProject, $/MyProject/SomeFolder. |
| project | str | Project ID or project name |
| include_deleted | bool | Return deleted branches. Default: False |
| include_links | bool | Return links. Default: False |
#### Return Type
[TfvcBranchRef]
#### Example Usage
```

connection.clients.get_tfvc_client().get_branch_refs(scope_path, project=None, include_deleted=None, include_links=None)
```
### GetBranches
#### Description:
Get a collection of branch roots -- first-level children, branches with no parents.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| include_parent | bool | Return the parent branch, if there is one. Default: False |
| include_children | bool | Return the child branches for each root branch. Default: False |
| include_deleted | bool | Return deleted branches. Default: False |
| include_links | bool | Return links. Default: False |
#### Return Type
[TfvcBranch]
#### Example Usage
```

connection.clients.get_tfvc_client().get_branches(project=None, include_parent=None, include_children=None, include_deleted=None, include_links=None)
```
### GetChangeset
#### Description:
Retrieve a Tfvc Changeset
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| id | int | Changeset Id to retrieve. |
| project | str | Project ID or project name |
| max_change_count | int | Number of changes to return (maximum 100 changes) Default: 0 |
| include_details | bool | Include policy details and check-in notes in the response. Default: false |
| include_work_items | bool | Include workitems. Default: false |
| max_comment_length | int | Include details about associated work items in the response. Default: null |
| include_source_rename | bool | Include renames.  Default: false |
| skip | int | Number of results to skip. Default: null |
| top | int | The maximum number of results to return. Default: null |
| orderby | str | Results are sorted by ID in descending order by default. Use id asc to sort by ID in ascending order. |
| search_criteria: Following criteria available (.itemPath, .version, .versionType, .versionOption, .author, .fromId, .toId, .fromDate, .toDate) Default | class | null |
#### Return Type
:class:<TfvcChangeset> <azure.devops.v5_1.tfvc.models.TfvcChangeset>
#### Example Usage
```
from azure.devops.v5_1.tfvc.models import TfvcChangesetSearchCriteria

connection.clients.get_tfvc_client().get_changeset(id, project=None, max_change_count=None, include_details=None, include_work_items=None, max_comment_length=None, include_source_rename=None, skip=None, top=None, orderby=None, search_criteria=None)
```
### GetChangesetChanges
#### Description:
Retrieve Tfvc changes for a given changeset.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| id | int | ID of the changeset. Default: null |
| skip | int | Number of results to skip. Default: null |
| top | int | The maximum number of results to return. Default: null |
| continuation_token | str | Return the next page of results. Default: null |
#### Return Type
:class:<GetChangesetChangesResponseValue>
#### Example Usage
```

connection.clients.get_tfvc_client().get_changeset_changes(id=None, skip=None, top=None, continuation_token=None)
```
### GetChangesetWorkItems
#### Description:
Retrieves the work items associated with a particular changeset.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| id | int | ID of the changeset. Default: null |
#### Return Type
[AssociatedWorkItem]
#### Example Usage
```

connection.clients.get_tfvc_client().get_changeset_work_items(id=None)
```
### GetChangesets
#### Description:
Retrieve Tfvc Changesets
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| max_comment_length | int | Include details about associated work items in the response. Default: null |
| skip | int | Number of results to skip. Default: null |
| top | int | The maximum number of results to return. Default: null |
| orderby | str | Results are sorted by ID in descending order by default. Use id asc to sort by ID in ascending order. |
| search_criteria: Following criteria available (.itemPath, .version, .versionType, .versionOption, .author, .fromId, .toId, .fromDate, .toDate) Default | class | null |
#### Return Type
[TfvcChangesetRef]
#### Example Usage
```
from azure.devops.v5_1.tfvc.models import TfvcChangesetSearchCriteria

connection.clients.get_tfvc_client().get_changesets(project=None, max_comment_length=None, skip=None, top=None, orderby=None, search_criteria=None)
```
### GetItem
#### Description:
Get Item Metadata and/or Content for a single item. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content which is always returned as a download.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| path | str | Version control path of an individual item to return. |
| project | str | Project ID or project name |
| file_name | str | file name of item returned. |
| download | bool | If true, create a downloadable attachment. |
| scope_path | str | Version control path of a folder to return multiple items. |
| recursion_level | str | None (just the item), or OneLevel (contents of a folder). |
| version_descriptor | class | Version descriptor.  Default is null. |
| include_content | bool | Set to true to include item content when requesting json.  Default is false. |
#### Return Type
:class:<TfvcItem> <azure.devops.v5_1.tfvc.models.TfvcItem>
#### Example Usage
```
from azure.devops.v5_1.tfvc.models import TfvcVersionDescriptor

connection.clients.get_tfvc_client().get_item(path, project=None, file_name=None, download=None, scope_path=None, recursion_level=None, version_descriptor=None, include_content=None)
```
### GetItemContent
#### Description:
Get Item Metadata and/or Content for a single item. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content which is always returned as a download.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| path | str | Version control path of an individual item to return. |
| project | str | Project ID or project name |
| file_name | str | file name of item returned. |
| download | bool | If true, create a downloadable attachment. |
| scope_path | str | Version control path of a folder to return multiple items. |
| recursion_level | str | None (just the item), or OneLevel (contents of a folder). |
| version_descriptor | class | Version descriptor.  Default is null. |
| include_content | bool | Set to true to include item content when requesting json.  Default is false. |
#### Return Type
object
#### Example Usage
```
from azure.devops.v5_1.tfvc.models import TfvcVersionDescriptor

connection.clients.get_tfvc_client().get_item_content(path, project=None, file_name=None, download=None, scope_path=None, recursion_level=None, version_descriptor=None, include_content=None, **kwargs)
```
### GetItemText
#### Description:
Get Item Metadata and/or Content for a single item. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content which is always returned as a download.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| path | str | Version control path of an individual item to return. |
| project | str | Project ID or project name |
| file_name | str | file name of item returned. |
| download | bool | If true, create a downloadable attachment. |
| scope_path | str | Version control path of a folder to return multiple items. |
| recursion_level | str | None (just the item), or OneLevel (contents of a folder). |
| version_descriptor | class | Version descriptor.  Default is null. |
| include_content | bool | Set to true to include item content when requesting json.  Default is false. |
#### Return Type
object
#### Example Usage
```
from azure.devops.v5_1.tfvc.models import TfvcVersionDescriptor

connection.clients.get_tfvc_client().get_item_text(path, project=None, file_name=None, download=None, scope_path=None, recursion_level=None, version_descriptor=None, include_content=None, **kwargs)
```
### GetItemZip
#### Description:
Get Item Metadata and/or Content for a single item. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content which is always returned as a download.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| path | str | Version control path of an individual item to return. |
| project | str | Project ID or project name |
| file_name | str | file name of item returned. |
| download | bool | If true, create a downloadable attachment. |
| scope_path | str | Version control path of a folder to return multiple items. |
| recursion_level | str | None (just the item), or OneLevel (contents of a folder). |
| version_descriptor | class | Version descriptor.  Default is null. |
| include_content | bool | Set to true to include item content when requesting json.  Default is false. |
#### Return Type
object
#### Example Usage
```
from azure.devops.v5_1.tfvc.models import TfvcVersionDescriptor

connection.clients.get_tfvc_client().get_item_zip(path, project=None, file_name=None, download=None, scope_path=None, recursion_level=None, version_descriptor=None, include_content=None, **kwargs)
```
### GetItems
#### Description:
Get a list of Tfvc items
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| scope_path | str | Version control path of a folder to return multiple items. |
| recursion_level | str | None (just the item), or OneLevel (contents of a folder). |
| include_links | bool | True to include links. |
| version_descriptor | class |  |
#### Return Type
[TfvcItem]
#### Example Usage
```
from azure.devops.v5_1.tfvc.models import TfvcVersionDescriptor

connection.clients.get_tfvc_client().get_items(project=None, scope_path=None, recursion_level=None, include_links=None, version_descriptor=None)
```
### GetItemsBatch
#### Description:
Post for retrieving a set of items given a list of paths or a long path. Allows for specifying the recursionLevel and version descriptors for each path.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| item_request_data | class |  |
| project | str | Project ID or project name |
#### Return Type
[[TfvcItem]]
#### Example Usage
```
from azure.devops.v5_1.tfvc.models import TfvcItemRequestData

connection.clients.get_tfvc_client().get_items_batch(item_request_data, project=None)
```
### GetItemsBatchZip
#### Description:
Post for retrieving a set of items given a list of paths or a long path. Allows for specifying the recursionLevel and version descriptors for each path.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| item_request_data | class |  |
| project | str | Project ID or project name |
#### Return Type
object
#### Example Usage
```
from azure.devops.v5_1.tfvc.models import TfvcItemRequestData

connection.clients.get_tfvc_client().get_items_batch_zip(item_request_data, project=None, **kwargs)
```
### GetLabel
#### Description:
Get a single deep label.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| label_id | str | Unique identifier of label |
| request_data | class | maxItemCount |
| project | str | Project ID or project name |
#### Return Type
:class:<TfvcLabel> <azure.devops.v5_1.tfvc.models.TfvcLabel>
#### Example Usage
```
from azure.devops.v5_1.tfvc.models import TfvcLabelRequestData

connection.clients.get_tfvc_client().get_label(label_id, request_data, project=None)
```
### GetLabelItems
#### Description:
Get items under a label.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| label_id | str | Unique identifier of label |
| top | int | Max number of items to return |
| skip | int | Number of items to skip |
#### Return Type
[TfvcItem]
#### Example Usage
```

connection.clients.get_tfvc_client().get_label_items(label_id, top=None, skip=None)
```
### GetLabels
#### Description:
Get a collection of shallow label references.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| request_data | class | labelScope, name, owner, and itemLabelFilter |
| project | str | Project ID or project name |
| top | int | Max number of labels to return, defaults to 100 when undefined |
| skip | int | Number of labels to skip |
#### Return Type
[TfvcLabelRef]
#### Example Usage
```
from azure.devops.v5_1.tfvc.models import TfvcLabelRequestData

connection.clients.get_tfvc_client().get_labels(request_data, project=None, top=None, skip=None)
```
### GetShelveset
#### Description:
Get a single deep shelveset.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| shelveset_id | str | Shelveset's unique ID |
| request_data | class | includeDetails, includeWorkItems, maxChangeCount, and maxCommentLength |
#### Return Type
:class:<TfvcShelveset> <azure.devops.v5_1.tfvc.models.TfvcShelveset>
#### Example Usage
```
from azure.devops.v5_1.tfvc.models import TfvcShelvesetRequestData

connection.clients.get_tfvc_client().get_shelveset(shelveset_id, request_data=None)
```
### GetShelvesetChanges
#### Description:
Get changes included in a shelveset.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| shelveset_id | str | Shelveset's unique ID |
| top | int | Max number of changes to return |
| skip | int | Number of changes to skip |
#### Return Type
[TfvcChange]
#### Example Usage
```

connection.clients.get_tfvc_client().get_shelveset_changes(shelveset_id, top=None, skip=None)
```
### GetShelvesetWorkItems
#### Description:
Get work items associated with a shelveset.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| shelveset_id | str | Shelveset's unique ID |
#### Return Type
[AssociatedWorkItem]
#### Example Usage
```

connection.clients.get_tfvc_client().get_shelveset_work_items(shelveset_id)
```
### GetShelvesets
#### Description:
Return a collection of shallow shelveset references.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| request_data | class | name, owner, and maxCommentLength |
| top | int | Max number of shelvesets to return |
| skip | int | Number of shelvesets to skip |
#### Return Type
[TfvcShelvesetRef]
#### Example Usage
```
from azure.devops.v5_1.tfvc.models import TfvcShelvesetRequestData

connection.clients.get_tfvc_client().get_shelvesets(request_data=None, top=None, skip=None)
```
## Get Wiki Client

### CreateAttachment
#### Description:
Creates an attachment in the wiki.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| upload_stream | object | Stream to upload |
| project | str | Project ID or project name |
| wiki_identifier | str | Wiki Id or name. |
| name | str | Wiki attachment name. |
| version_descriptor | class | GitVersionDescriptor for the page. (Optional in case of ProjectWiki). |
#### Return Type
:class:<WikiAttachmentResponse> <azure.devops.v5_1.wiki.models.WikiAttachmentResponse>
#### Example Usage
```
from azure.devops.v5_1.wiki.models import GitVersionDescriptor

connection.clients.get_wiki_client().create_attachment(upload_stream, project, wiki_identifier, name, version_descriptor=None, **kwargs)
```
### CreateOrUpdatePage
#### Description:
Creates or edits a wiki page.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| parameters | class | Wiki create or update operation parameters. |
| project | str | Project ID or project name |
| wiki_identifier | str | Wiki Id or name. |
| path | str | Wiki page path. |
| version | String | Version of the page on which the change is to be made. Mandatory for `Edit` scenario. To be populated in the If-Match header of the request. |
| comment | str | Comment to be associated with the page operation. |
| version_descriptor | class | GitVersionDescriptor for the page. (Optional in case of ProjectWiki). |
#### Return Type
:class:<WikiPageResponse> <azure.devops.v5_1.wiki.models.WikiPageResponse>
#### Example Usage
```
from azure.devops.v5_1.wiki.models import WikiPageCreateOrUpdateParameters
from azure.devops.v5_1.wiki.models import GitVersionDescriptor

connection.clients.get_wiki_client().create_or_update_page(parameters, project, wiki_identifier, path, version, comment=None, version_descriptor=None)
```
### CreatePageMove
#### Description:
Creates a page move operation that updates the path and order of the page as provided in the parameters.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| page_move_parameters | class | Page more operation parameters. |
| project | str | Project ID or project name |
| wiki_identifier | str | Wiki Id or name. |
| comment | str | Comment that is to be associated with this page move. |
| version_descriptor | class | GitVersionDescriptor for the page. (Optional in case of ProjectWiki). |
#### Return Type
:class:<WikiPageMoveResponse> <azure.devops.v5_1.wiki.models.WikiPageMoveResponse>
#### Example Usage
```
from azure.devops.v5_1.wiki.models import WikiPageMoveParameters
from azure.devops.v5_1.wiki.models import GitVersionDescriptor

connection.clients.get_wiki_client().create_page_move(page_move_parameters, project, wiki_identifier, comment=None, version_descriptor=None)
```
### CreateWiki
#### Description:
Creates the wiki resource.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| wiki_create_params | class | Parameters for the wiki creation. |
| project | str | Project ID or project name |
#### Return Type
:class:<WikiV2> <azure.devops.v5_1.wiki.models.WikiV2>
#### Example Usage
```
from azure.devops.v5_1.wiki.models import WikiCreateParametersV2

connection.clients.get_wiki_client().create_wiki(wiki_create_params, project=None)
```
### DeletePage
#### Description:
Deletes a wiki page.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| wiki_identifier | str | Wiki Id or name. |
| path | str | Wiki page path. |
| comment | str | Comment to be associated with this page delete. |
| version_descriptor | class | GitVersionDescriptor for the page. (Optional in case of ProjectWiki). |
#### Return Type
:class:<WikiPageResponse> <azure.devops.v5_1.wiki.models.WikiPageResponse>
#### Example Usage
```
from azure.devops.v5_1.wiki.models import GitVersionDescriptor

connection.clients.get_wiki_client().delete_page(project, wiki_identifier, path, comment=None, version_descriptor=None)
```
### DeleteWiki
#### Description:
Deletes the wiki corresponding to the wiki name or Id provided.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| wiki_identifier | str | Wiki name or Id. |
| project | str | Project ID or project name |
#### Return Type
:class:<WikiV2> <azure.devops.v5_1.wiki.models.WikiV2>
#### Example Usage
```

connection.clients.get_wiki_client().delete_wiki(wiki_identifier, project=None)
```
### GetAllWikis
#### Description:
Gets all wikis in a project or collection.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
#### Return Type
[WikiV2]
#### Example Usage
```

connection.clients.get_wiki_client().get_all_wikis(project=None)
```
### GetPage
#### Description:
Gets metadata or content of the wiki page for the provided path. Content negotiation is done based on the `Accept` header sent in the request.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| wiki_identifier | str | Wiki Id or name. |
| path | str | Wiki page path. |
| recursion_level | str | Recursion level for subpages retrieval. Defaults to `None` (Optional). |
| version_descriptor | class | GitVersionDescriptor for the page. Defaults to the default branch (Optional). |
| include_content | bool | True to include the content of the page in the response for Json content type. Defaults to false (Optional) |
#### Return Type
:class:<WikiPageResponse> <azure.devops.v5_1.wiki.models.WikiPageResponse>
#### Example Usage
```
from azure.devops.v5_1.wiki.models import GitVersionDescriptor

connection.clients.get_wiki_client().get_page(project, wiki_identifier, path=None, recursion_level=None, version_descriptor=None, include_content=None)
```
### GetPageText
#### Description:
Gets metadata or content of the wiki page for the provided path. Content negotiation is done based on the `Accept` header sent in the request.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| wiki_identifier | str | Wiki Id or name. |
| path | str | Wiki page path. |
| recursion_level | str | Recursion level for subpages retrieval. Defaults to `None` (Optional). |
| version_descriptor | class | GitVersionDescriptor for the page. Defaults to the default branch (Optional). |
| include_content | bool | True to include the content of the page in the response for Json content type. Defaults to false (Optional) |
#### Return Type
object
#### Example Usage
```
from azure.devops.v5_1.wiki.models import GitVersionDescriptor

connection.clients.get_wiki_client().get_page_text(project, wiki_identifier, path=None, recursion_level=None, version_descriptor=None, include_content=None, **kwargs)
```
### GetPageZip
#### Description:
Gets metadata or content of the wiki page for the provided path. Content negotiation is done based on the `Accept` header sent in the request.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| wiki_identifier | str | Wiki Id or name. |
| path | str | Wiki page path. |
| recursion_level | str | Recursion level for subpages retrieval. Defaults to `None` (Optional). |
| version_descriptor | class | GitVersionDescriptor for the page. Defaults to the default branch (Optional). |
| include_content | bool | True to include the content of the page in the response for Json content type. Defaults to false (Optional) |
#### Return Type
object
#### Example Usage
```
from azure.devops.v5_1.wiki.models import GitVersionDescriptor

connection.clients.get_wiki_client().get_page_zip(project, wiki_identifier, path=None, recursion_level=None, version_descriptor=None, include_content=None, **kwargs)
```
### GetWiki
#### Description:
Gets the wiki corresponding to the wiki name or Id provided.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| wiki_identifier | str | Wiki name or id. |
| project | str | Project ID or project name |
#### Return Type
:class:<WikiV2> <azure.devops.v5_1.wiki.models.WikiV2>
#### Example Usage
```

connection.clients.get_wiki_client().get_wiki(wiki_identifier, project=None)
```
### UpdateWiki
#### Description:
Updates the wiki corresponding to the wiki Id or name provided using the update parameters.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| update_parameters | class | Update parameters. |
| wiki_identifier | str | Wiki name or Id. |
| project | str | Project ID or project name |
#### Return Type
:class:<WikiV2> <azure.devops.v5_1.wiki.models.WikiV2>
#### Example Usage
```
from azure.devops.v5_1.wiki.models import WikiUpdateParameters

connection.clients.get_wiki_client().update_wiki(update_parameters, wiki_identifier, project=None)
```
## Get Work Client

### CreatePlan
#### Description:
Add a new plan for the team
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| posted_plan | class | Plan definition |
| project | str | Project ID or project name |
#### Return Type
:class:<Plan> <azure.devops.v5_1.work.models.Plan>
#### Example Usage
```
from azure.devops.v5_1.work.models import CreatePlan

connection.clients.get_work_client().create_plan(posted_plan, project)
```
### DeletePlan
#### Description:
Delete the specified plan
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| id | str | Identifier of the plan |
#### Return Type
:class:<Plan> <azure.devops.v5_1.work.models.Plan>
#### Example Usage
```

connection.clients.get_work_client().delete_plan(project, id)
```
### DeleteTeamIteration
#### Description:
Delete a team's iteration by iterationId
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| team_context | class | The team context for the operation |
| id | str | ID of the iteration |
#### Return Type
:class:<Plan> <azure.devops.v5_1.work.models.Plan>
#### Example Usage
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().delete_team_iteration(team_context, id)
```
### GetBacklogConfigurations
#### Description:
Gets backlog configuration for a team
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| team_context | class | The team context for the operation |
#### Return Type
:class:<BacklogConfiguration> <azure.devops.v5_1.work.models.BacklogConfiguration>
#### Example Usage
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_backlog_configurations(team_context)
```
### GetBoard
#### Description:
Get board
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| team_context | class | The team context for the operation |
| id | str | identifier for board, either board's backlog level name (Eg:"Stories") or Id |
#### Return Type
:class:<Board> <azure.devops.v5_1.work.models.Board>
#### Example Usage
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_board(team_context, id)
```
### GetBoardCardRuleSettings
#### Description:
Get board card Rule settings for the board id or board by name
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| team_context | class | The team context for the operation |
| board | str |  |
#### Return Type
:class:<BoardCardRuleSettings> <azure.devops.v5_1.work.models.BoardCardRuleSettings>
#### Example Usage
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_board_card_rule_settings(team_context, board)
```
### GetBoardCardSettings
#### Description:
Get board card settings for the board id or board by name
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| team_context | class | The team context for the operation |
| board | str |  |
#### Return Type
:class:<BoardCardSettings> <azure.devops.v5_1.work.models.BoardCardSettings>
#### Example Usage
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_board_card_settings(team_context, board)
```
### GetBoardChart
#### Description:
Get a board chart
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| team_context | class | The team context for the operation |
| board | str | Identifier for board, either board's backlog level name (Eg:"Stories") or Id |
| name | str | The chart name |
#### Return Type
:class:<BoardChart> <azure.devops.v5_1.work.models.BoardChart>
#### Example Usage
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_board_chart(team_context, board, name)
```
### GetBoardCharts
#### Description:
Get board charts
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| team_context | class | The team context for the operation |
| board | str | Identifier for board, either board's backlog level name (Eg:"Stories") or Id |
#### Return Type
[BoardChartReference]
#### Example Usage
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_board_charts(team_context, board)
```
### GetBoardColumns
#### Description:
Get columns on a board
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| team_context | class | The team context for the operation |
| board | str | Name or ID of the specific board |
#### Return Type
[BoardColumn]
#### Example Usage
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_board_columns(team_context, board)
```
### GetBoardRows
#### Description:
Get rows on a board
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| team_context | class | The team context for the operation |
| board | str | Name or ID of the specific board |
#### Return Type
[BoardRow]
#### Example Usage
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_board_rows(team_context, board)
```
### GetBoards
#### Description:
Get boards
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| team_context | class | The team context for the operation |
#### Return Type
[BoardReference]
#### Example Usage
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_boards(team_context)
```
### GetCapacitiesWithIdentityRef
#### Description:
Get a team's capacity
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| team_context | class | The team context for the operation |
| iteration_id | str | ID of the iteration |
#### Return Type
[TeamMemberCapacityIdentityRef]
#### Example Usage
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_capacities_with_identity_ref(team_context, iteration_id)
```
### GetCapacityWithIdentityRef
#### Description:
Get a team member's capacity
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| team_context | class | The team context for the operation |
| iteration_id | str | ID of the iteration |
| team_member_id | str | ID of the team member |
#### Return Type
:class:<TeamMemberCapacityIdentityRef> <azure.devops.v5_1.work.models.TeamMemberCapacityIdentityRef>
#### Example Usage
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_capacity_with_identity_ref(team_context, iteration_id, team_member_id)
```
### GetColumnSuggestedValues
#### Description:
Get available board columns in a project
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
#### Return Type
[BoardSuggestedValue]
#### Example Usage
```

connection.clients.get_work_client().get_column_suggested_values(project=None)
```
### GetDeliveryTimelineData
#### Description:
Get Delivery View Data
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| id | str | Identifier for delivery view |
| revision | int | Revision of the plan for which you want data. If the current plan is a different revision you will get an ViewRevisionMismatchException exception. If you do not supply a revision you will get data for the latest revision. |
| start_date | datetime | The start date of timeline |
| end_date | datetime | The end date of timeline |
#### Return Type
:class:<DeliveryViewData> <azure.devops.v5_1.work.models.DeliveryViewData>
#### Example Usage
```

connection.clients.get_work_client().get_delivery_timeline_data(project, id, revision=None, start_date=None, end_date=None)
```
### GetPlan
#### Description:
Get the information for the specified plan
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| id | str | Identifier of the plan |
#### Return Type
:class:<Plan> <azure.devops.v5_1.work.models.Plan>
#### Example Usage
```

connection.clients.get_work_client().get_plan(project, id)
```
### GetPlans
#### Description:
Get the information for all the plans configured for the given team
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
#### Return Type
[Plan]
#### Example Usage
```

connection.clients.get_work_client().get_plans(project)
```
### GetRowSuggestedValues
#### Description:
Get available board rows in a project
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
#### Return Type
[BoardSuggestedValue]
#### Example Usage
```

connection.clients.get_work_client().get_row_suggested_values(project=None)
```
### GetTeamDaysOff
#### Description:
Get team's days off for an iteration
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| team_context | class | The team context for the operation |
| iteration_id | str | ID of the iteration |
#### Return Type
:class:<TeamSettingsDaysOff> <azure.devops.v5_1.work.models.TeamSettingsDaysOff>
#### Example Usage
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_team_days_off(team_context, iteration_id)
```
### GetTeamFieldValues
#### Description:
Get a collection of team field values
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| team_context | class | The team context for the operation |
#### Return Type
:class:<TeamFieldValues> <azure.devops.v5_1.work.models.TeamFieldValues>
#### Example Usage
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_team_field_values(team_context)
```
### GetTeamIteration
#### Description:
Get team's iteration by iterationId
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| team_context | class | The team context for the operation |
| id | str | ID of the iteration |
#### Return Type
:class:<TeamSettingsIteration> <azure.devops.v5_1.work.models.TeamSettingsIteration>
#### Example Usage
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_team_iteration(team_context, id)
```
### GetTeamIterations
#### Description:
Get a team's iterations using timeframe filter
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| team_context | class | The team context for the operation |
| timeframe | str | A filter for which iterations are returned based on relative time. Only Current is supported currently. |
#### Return Type
[TeamSettingsIteration]
#### Example Usage
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_team_iterations(team_context, timeframe=None)
```
### GetTeamSettings
#### Description:
Get a team's settings
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| team_context | class | The team context for the operation |
#### Return Type
:class:<TeamSetting> <azure.devops.v5_1.work.models.TeamSetting>
#### Example Usage
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_team_settings(team_context)
```
### PostTeamIteration
#### Description:
Add an iteration to the team
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| iteration | class | Iteration to add |
| team_context | class | The team context for the operation |
#### Return Type
:class:<TeamSettingsIteration> <azure.devops.v5_1.work.models.TeamSettingsIteration>
#### Example Usage
```
from azure.devops.v5_1.work.models import TeamSettingsIteration
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().post_team_iteration(iteration, team_context)
```
### ReplaceCapacitiesWithIdentityRef
#### Description:
Replace a team's capacity
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| capacities | [TeamMemberCapacityIdentityRef] | Team capacity to replace |
| team_context | class | The team context for the operation |
| iteration_id | str | ID of the iteration |
#### Return Type
[TeamMemberCapacityIdentityRef]
#### Example Usage
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().replace_capacities_with_identity_ref(capacities, team_context, iteration_id)
```
### SetBoardOptions
#### Description:
Update board options
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| options | {str} | options to updated |
| team_context | class | The team context for the operation |
| id | str | identifier for board, either category plural name (Eg:"Stories") or guid |
#### Return Type
{str}
#### Example Usage
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().set_board_options(options, team_context, id)
```
### UpdateBoardCardRuleSettings
#### Description:
Update board card Rule settings for the board id or board by name
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| board_card_rule_settings | class |  |
| team_context | class | The team context for the operation |
| board | str |  |
#### Return Type
:class:<BoardCardRuleSettings> <azure.devops.v5_1.work.models.BoardCardRuleSettings>
#### Example Usage
```
from azure.devops.v5_1.work.models import BoardCardRuleSettings
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().update_board_card_rule_settings(board_card_rule_settings, team_context, board)
```
### UpdateBoardCardSettings
#### Description:
Update board card settings for the board id or board by name
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| board_card_settings_to_save | class |  |
| team_context | class | The team context for the operation |
| board | str |  |
#### Return Type
:class:<BoardCardSettings> <azure.devops.v5_1.work.models.BoardCardSettings>
#### Example Usage
```
from azure.devops.v5_1.work.models import BoardCardSettings
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().update_board_card_settings(board_card_settings_to_save, team_context, board)
```
### UpdateBoardChart
#### Description:
Update a board chart
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| chart | class |  |
| team_context | class | The team context for the operation |
| board | str | Identifier for board, either board's backlog level name (Eg:"Stories") or Id |
| name | str | The chart name |
#### Return Type
:class:<BoardChart> <azure.devops.v5_1.work.models.BoardChart>
#### Example Usage
```
from azure.devops.v5_1.work.models import BoardChart
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().update_board_chart(chart, team_context, board, name)
```
### UpdateBoardColumns
#### Description:
Update columns on a board
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| board_columns | [BoardColumn] | List of board columns to update |
| team_context | class | The team context for the operation |
| board | str | Name or ID of the specific board |
#### Return Type
[BoardColumn]
#### Example Usage
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().update_board_columns(board_columns, team_context, board)
```
### UpdateBoardRows
#### Description:
Update rows on a board
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| board_rows | [BoardRow] | List of board rows to update |
| team_context | class | The team context for the operation |
| board | str | Name or ID of the specific board |
#### Return Type
[BoardRow]
#### Example Usage
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().update_board_rows(board_rows, team_context, board)
```
### UpdateCapacityWithIdentityRef
#### Description:
Update a team member's capacity
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| patch | class | Updated capacity |
| team_context | class | The team context for the operation |
| iteration_id | str | ID of the iteration |
| team_member_id | str | ID of the team member |
#### Return Type
:class:<TeamMemberCapacityIdentityRef> <azure.devops.v5_1.work.models.TeamMemberCapacityIdentityRef>
#### Example Usage
```
from azure.devops.v5_1.work.models import CapacityPatch
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().update_capacity_with_identity_ref(patch, team_context, iteration_id, team_member_id)
```
### UpdatePlan
#### Description:
Update the information for the specified plan
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| updated_plan | class | Plan definition to be updated |
| project | str | Project ID or project name |
| id | str | Identifier of the plan |
#### Return Type
:class:<Plan> <azure.devops.v5_1.work.models.Plan>
#### Example Usage
```
from azure.devops.v5_1.work.models import UpdatePlan

connection.clients.get_work_client().update_plan(updated_plan, project, id)
```
### UpdateTeamDaysOff
#### Description:
Set a team's days off for an iteration
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| days_off_patch | class | Team's days off patch containing a list of start and end dates |
| team_context | class | The team context for the operation |
| iteration_id | str | ID of the iteration |
#### Return Type
:class:<TeamSettingsDaysOff> <azure.devops.v5_1.work.models.TeamSettingsDaysOff>
#### Example Usage
```
from azure.devops.v5_1.work.models import TeamSettingsDaysOffPatch
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().update_team_days_off(days_off_patch, team_context, iteration_id)
```
### UpdateTeamFieldValues
#### Description:
Update team field values
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| patch | class |  |
| team_context | class | The team context for the operation |
#### Return Type
:class:<TeamFieldValues> <azure.devops.v5_1.work.models.TeamFieldValues>
#### Example Usage
```
from azure.devops.v5_1.work.models import TeamFieldValuesPatch
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().update_team_field_values(patch, team_context)
```
### UpdateTeamSettings
#### Description:
Update a team's settings
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| team_settings_patch | class | TeamSettings changes |
| team_context | class | The team context for the operation |
#### Return Type
:class:<TeamSetting> <azure.devops.v5_1.work.models.TeamSetting>
#### Example Usage
```
from azure.devops.v5_1.work.models import TeamSettingsPatch
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().update_team_settings(team_settings_patch, team_context)
```
## Get Work Item Tracking Client

### CreateAttachment
#### Description:
Uploads an attachment.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| upload_stream | object | Stream to upload |
| project | str | Project ID or project name |
| file_name | str | The name of the file |
| upload_type | str | Attachment upload type: Simple or Chunked |
| area_path | str | Target project Area Path |
#### Return Type
:class:<AttachmentReference> <azure.devops.v5_1.work_item_tracking.models.AttachmentReference>
#### Example Usage
```

connection.clients.get_work_item_tracking_client().create_attachment(upload_stream, project=None, file_name=None, upload_type=None, area_path=None, **kwargs)
```
### CreateField
#### Description:
Create a new field.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| work_item_field | class | New field definition |
| project | str | Project ID or project name |
#### Return Type
:class:<WorkItemField> <azure.devops.v5_1.work_item_tracking.models.WorkItemField>
#### Example Usage
```
from azure.devops.v5_1.work_item_tracking.models import WorkItemField

connection.clients.get_work_item_tracking_client().create_field(work_item_field, project=None)
```
### CreateOrUpdateClassificationNode
#### Description:
Create new or update an existing classification node.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| posted_node | class | Node to create or update. |
| project | str | Project ID or project name |
| structure_group | TreeStructureGroup | Structure group of the classification node, area or iteration. |
| path | str | Path of the classification node. |
#### Return Type
:class:<WorkItemClassificationNode> <azure.devops.v5_1.work_item_tracking.models.WorkItemClassificationNode>
#### Example Usage
```
from azure.devops.v5_1.work_item_tracking.models import WorkItemClassificationNode

connection.clients.get_work_item_tracking_client().create_or_update_classification_node(posted_node, project, structure_group, path=None)
```
### CreateQuery
#### Description:
Creates a query, or moves a query.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| posted_query | class | The query to create. |
| project | str | Project ID or project name |
| query | str | The parent id or path under which the query is to be created. |
| validate_wiql_only | bool | If you only want to validate your WIQL query without actually creating one, set it to true. Default is false. |
#### Return Type
:class:<QueryHierarchyItem> <azure.devops.v5_1.work_item_tracking.models.QueryHierarchyItem>
#### Example Usage
```
from azure.devops.v5_1.work_item_tracking.models import QueryHierarchyItem

connection.clients.get_work_item_tracking_client().create_query(posted_query, project, query, validate_wiql_only=None)
```
### CreateWorkItem
#### Description:
Creates a single work item.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| document | class | The JSON Patch document representing the work item |
| project | str | Project ID or project name |
| type | str | The work item type of the work item to create |
| validate_only | bool | Indicate if you only want to validate the changes without saving the work item |
| bypass_rules | bool | Do not enforce the work item type rules on this update |
| suppress_notifications | bool | Do not fire any notifications for this change |
| expand | str | The expand parameters for work item attributes. Possible options are { None, Relations, Fields, Links, All }. |
#### Return Type
:class:<WorkItem> <azure.devops.v5_1.work_item_tracking.models.WorkItem>
#### Example Usage
```
from azure.devops.v5_1.work_item_tracking.models import [JsonPatchOperation]

connection.clients.get_work_item_tracking_client().create_work_item(document, project, type, validate_only=None, bypass_rules=None, suppress_notifications=None, expand=None)
```
### DeleteClassificationNode
#### Description:
Delete an existing classification node.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| structure_group | TreeStructureGroup | Structure group of the classification node, area or iteration. |
| path | str | Path of the classification node. |
| reclassify_id | int | Id of the target classification node for reclassification. |
#### Return Type
:class:<WorkItem> <azure.devops.v5_1.work_item_tracking.models.WorkItem>
#### Example Usage
```

connection.clients.get_work_item_tracking_client().delete_classification_node(project, structure_group, path=None, reclassify_id=None)
```
### DeleteField
#### Description:
Deletes the field.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| field_name_or_ref_name | str | Field simple name or reference name |
| project | str | Project ID or project name |
#### Return Type
:class:<WorkItem> <azure.devops.v5_1.work_item_tracking.models.WorkItem>
#### Example Usage
```

connection.clients.get_work_item_tracking_client().delete_field(field_name_or_ref_name, project=None)
```
### DeleteQuery
#### Description:
Delete a query or a folder. This deletes any permission change on the deleted query or folder and any of its descendants if it is a folder. It is important to note that the deleted permission changes cannot be recovered upon undeleting the query or folder.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| query | str | ID or path of the query or folder to delete. |
#### Return Type
:class:<WorkItem> <azure.devops.v5_1.work_item_tracking.models.WorkItem>
#### Example Usage
```

connection.clients.get_work_item_tracking_client().delete_query(project, query)
```
### DeleteWorkItem
#### Description:
Deletes the specified work item and sends it to the Recycle Bin, so that it can be restored back, if required. Optionally, if the destroy parameter has been set to true, it destroys the work item permanently. WARNING: If the destroy parameter is set to true, work items deleted by this command will NOT go to recycle-bin and there is no way to restore/recover them after deletion. It is recommended NOT to use this parameter. If you do, please use this parameter with extreme caution.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| id | int | ID of the work item to be deleted |
| project | str | Project ID or project name |
| destroy | bool | Optional parameter, if set to true, the work item is deleted permanently. Please note: the destroy action is PERMANENT and cannot be undone. |
#### Return Type
:class:<WorkItemDelete> <azure.devops.v5_1.work_item_tracking.models.WorkItemDelete>
#### Example Usage
```

connection.clients.get_work_item_tracking_client().delete_work_item(id, project=None, destroy=None)
```
### DestroyWorkItem
#### Description:
Destroys the specified work item permanently from the Recycle Bin. This action can not be undone.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| id | int | ID of the work item to be destroyed permanently |
| project | str | Project ID or project name |
#### Return Type
:class:<WorkItemDelete> <azure.devops.v5_1.work_item_tracking.models.WorkItemDelete>
#### Example Usage
```

connection.clients.get_work_item_tracking_client().destroy_work_item(id, project=None)
```
### GetAttachmentContent
#### Description:
Downloads an attachment.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| id | str | Attachment ID |
| project | str | Project ID or project name |
| file_name | str | Name of the file |
| download | bool | If set to <c>true</c> always download attachment |
#### Return Type
object
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_attachment_content(id, project=None, file_name=None, download=None, **kwargs)
```
### GetAttachmentZip
#### Description:
Downloads an attachment.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| id | str | Attachment ID |
| project | str | Project ID or project name |
| file_name | str | Name of the file |
| download | bool | If set to <c>true</c> always download attachment |
#### Return Type
object
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_attachment_zip(id, project=None, file_name=None, download=None, **kwargs)
```
### GetClassificationNode
#### Description:
Gets the classification node for a given node path.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| structure_group | TreeStructureGroup | Structure group of the classification node, area or iteration. |
| path | str | Path of the classification node. |
| depth | int | Depth of children to fetch. |
#### Return Type
:class:<WorkItemClassificationNode> <azure.devops.v5_1.work_item_tracking.models.WorkItemClassificationNode>
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_classification_node(project, structure_group, path=None, depth=None)
```
### GetClassificationNodes
#### Description:
Gets root classification nodes or list of classification nodes for a given list of nodes ids, for a given project. In case ids parameter is supplied you will  get list of classification nodes for those ids. Otherwise you will get root classification nodes for this project.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| ids | [int] | Comma separated integer classification nodes ids. It's not required, if you want root nodes. |
| depth | int | Depth of children to fetch. |
| error_policy | str | Flag to handle errors in getting some nodes. Possible options are Fail and Omit. |
#### Return Type
[WorkItemClassificationNode]
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_classification_nodes(project, ids, depth=None, error_policy=None)
```
### GetDeletedWorkItem
#### Description:
Gets a deleted work item from Recycle Bin.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| id | int | ID of the work item to be returned |
| project | str | Project ID or project name |
#### Return Type
:class:<WorkItemDelete> <azure.devops.v5_1.work_item_tracking.models.WorkItemDelete>
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_deleted_work_item(id, project=None)
```
### GetDeletedWorkItemShallowReferences
#### Description:
Gets a list of the IDs and the URLs of the deleted the work items in the Recycle Bin.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
#### Return Type
[WorkItemDeleteShallowReference]
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_deleted_work_item_shallow_references(project=None)
```
### GetDeletedWorkItems
#### Description:
Gets the work items from the recycle bin, whose IDs have been specified in the parameters
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| ids | [int] | Comma separated list of IDs of the deleted work items to be returned |
| project | str | Project ID or project name |
#### Return Type
[WorkItemDeleteReference]
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_deleted_work_items(ids, project=None)
```
### GetField
#### Description:
Gets information on a specific field.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| field_name_or_ref_name | str | Field simple name or reference name |
| project | str | Project ID or project name |
#### Return Type
:class:<WorkItemField> <azure.devops.v5_1.work_item_tracking.models.WorkItemField>
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_field(field_name_or_ref_name, project=None)
```
### GetFields
#### Description:
Returns information for all fields.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| expand | str | Use ExtensionFields to include extension fields, otherwise exclude them. Unless the feature flag for this parameter is enabled, extension fields are always included. |
#### Return Type
[WorkItemField]
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_fields(project=None, expand=None)
```
### GetQueries
#### Description:
Gets the root queries and their children
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| expand | str | Include the query string (wiql), clauses, query result columns, and sort options in the results. |
| depth | int | In the folder of queries, return child queries and folders to this depth. |
| include_deleted | bool | Include deleted queries and folders |
#### Return Type
[QueryHierarchyItem]
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_queries(project, expand=None, depth=None, include_deleted=None)
```
### GetQueriesBatch
#### Description:
Gets a list of queries by ids (Maximum 1000)
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| query_get_request | class |  |
| project | str | Project ID or project name |
#### Return Type
[QueryHierarchyItem]
#### Example Usage
```
from azure.devops.v5_1.work_item_tracking.models import QueryBatchGetRequest

connection.clients.get_work_item_tracking_client().get_queries_batch(query_get_request, project)
```
### GetQuery
#### Description:
Retrieves an individual query and its children
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| query | str | ID or path of the query. |
| expand | str | Include the query string (wiql), clauses, query result columns, and sort options in the results. |
| depth | int | In the folder of queries, return child queries and folders to this depth. |
| include_deleted | bool | Include deleted queries and folders |
#### Return Type
:class:<QueryHierarchyItem> <azure.devops.v5_1.work_item_tracking.models.QueryHierarchyItem>
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_query(project, query, expand=None, depth=None, include_deleted=None)
```
### GetQueryResultCount
#### Description:
Gets the results of the query given the query ID.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| id | str | The query ID. |
| team_context | class | The team context for the operation |
| time_precision | bool | Whether or not to use time precision. |
| top | int | The max number of results to return. |
#### Return Type
int
#### Example Usage
```
from azure.devops.v5_1.work_item_tracking.models import TeamContext

connection.clients.get_work_item_tracking_client().get_query_result_count(id, team_context=None, time_precision=None, top=None)
```
### GetRelationType
#### Description:
Gets the work item relation type definition.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| relation | str | The relation name |
#### Return Type
:class:<WorkItemRelationType> <azure.devops.v5_1.work_item_tracking.models.WorkItemRelationType>
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_relation_type(relation)
```
### GetRelationTypes
#### Description:
Gets the work item relation types.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
#### Return Type
[WorkItemRelationType]
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_relation_types()
```
### GetReportingLinksByLinkType
#### Description:
Get a batch of work item links
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| link_types | [str] | A list of types to filter the results to specific link types. Omit this parameter to get work item links of all link types. |
| types | [str] | A list of types to filter the results to specific work item types. Omit this parameter to get work item links of all work item types. |
| continuation_token | str | Specifies the continuationToken to start the batch from. Omit this parameter to get the first batch of links. |
| start_date_time | datetime | Date/time to use as a starting point for link changes. Only link changes that occurred after that date/time will be returned. Cannot be used in conjunction with 'watermark' parameter. |
#### Return Type
:class:<ReportingWorkItemLinksBatch> <azure.devops.v5_1.work_item_tracking.models.ReportingWorkItemLinksBatch>
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_reporting_links_by_link_type(project=None, link_types=None, types=None, continuation_token=None, start_date_time=None)
```
### GetRevision
#### Description:
Returns a fully hydrated work item for the requested revision
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| id | int |  |
| revision_number | int |  |
| project | str | Project ID or project name |
| expand | str |  |
#### Return Type
:class:<WorkItem> <azure.devops.v5_1.work_item_tracking.models.WorkItem>
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_revision(id, revision_number, project=None, expand=None)
```
### GetRevisions
#### Description:
Returns the list of fully hydrated work item revisions, paged.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| id | int |  |
| project | str | Project ID or project name |
| top | int |  |
| skip | int |  |
| expand | str |  |
#### Return Type
[WorkItem]
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_revisions(id, project=None, top=None, skip=None, expand=None)
```
### GetRootNodes
#### Description:
Gets root classification nodes under the project.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| depth | int | Depth of children to fetch. |
#### Return Type
[WorkItemClassificationNode]
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_root_nodes(project, depth=None)
```
### GetUpdate
#### Description:
Returns a single update for a work item
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| id | int |  |
| update_number | int |  |
| project | str | Project ID or project name |
#### Return Type
:class:<WorkItemUpdate> <azure.devops.v5_1.work_item_tracking.models.WorkItemUpdate>
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_update(id, update_number, project=None)
```
### GetUpdates
#### Description:
Returns a the deltas between work item revisions
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| id | int |  |
| project | str | Project ID or project name |
| top | int |  |
| skip | int |  |
#### Return Type
[WorkItemUpdate]
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_updates(id, project=None, top=None, skip=None)
```
### GetWorkItem
#### Description:
Returns a single work item.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| id | int | The work item id |
| project | str | Project ID or project name |
| fields | [str] | Comma-separated list of requested fields |
| as_of | datetime | AsOf UTC date time string |
| expand | str | The expand parameters for work item attributes. Possible options are { None, Relations, Fields, Links, All }. |
#### Return Type
:class:<WorkItem> <azure.devops.v5_1.work_item_tracking.models.WorkItem>
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_work_item(id, project=None, fields=None, as_of=None, expand=None)
```
### GetWorkItemIconJson
#### Description:
Get a work item icon given the friendly name and icon color.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| icon | str | The name of the icon |
| color | str | The 6-digit hex color for the icon |
| v | int | The version of the icon (used only for cache invalidation) |
#### Return Type
:class:<WorkItemIcon> <azure.devops.v5_1.work_item_tracking.models.WorkItemIcon>
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_work_item_icon_json(icon, color=None, v=None)
```
### GetWorkItemIconSvg
#### Description:
Get a work item icon given the friendly name and icon color.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| icon | str | The name of the icon |
| color | str | The 6-digit hex color for the icon |
| v | int | The version of the icon (used only for cache invalidation) |
#### Return Type
object
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_work_item_icon_svg(icon, color=None, v=None, **kwargs)
```
### GetWorkItemIconXaml
#### Description:
Get a work item icon given the friendly name and icon color.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| icon | str | The name of the icon |
| color | str | The 6-digit hex color for the icon |
| v | int | The version of the icon (used only for cache invalidation) |
#### Return Type
object
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_work_item_icon_xaml(icon, color=None, v=None, **kwargs)
```
### GetWorkItemIcons
#### Description:
Get a list of all work item icons.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
#### Return Type
[WorkItemIcon]
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_work_item_icons()
```
### GetWorkItemTemplate
#### Description:
Returns a single work item from a template.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| type | str | The work item type name |
| fields | str | Comma-separated list of requested fields |
| as_of | datetime | AsOf UTC date time string |
| expand | str | The expand parameters for work item attributes. Possible options are { None, Relations, Fields, Links, All }. |
#### Return Type
:class:<WorkItem> <azure.devops.v5_1.work_item_tracking.models.WorkItem>
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_work_item_template(project, type, fields=None, as_of=None, expand=None)
```
### GetWorkItemType
#### Description:
Returns a work item type definition.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| type | str | Work item type name |
#### Return Type
:class:<WorkItemType> <azure.devops.v5_1.work_item_tracking.models.WorkItemType>
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_work_item_type(project, type)
```
### GetWorkItemTypeCategories
#### Description:
Get all work item type categories.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
#### Return Type
[WorkItemTypeCategory]
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_work_item_type_categories(project)
```
### GetWorkItemTypeCategory
#### Description:
Get specific work item type category by name.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| category | str | The category name |
#### Return Type
:class:<WorkItemTypeCategory> <azure.devops.v5_1.work_item_tracking.models.WorkItemTypeCategory>
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_work_item_type_category(project, category)
```
### GetWorkItemTypeFieldWithReferences
#### Description:
Get a field for a work item type with detailed references.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| type | str | Work item type. |
| field | str |  |
| expand | str | Expand level for the API response. Properties: to include allowedvalues, default value, isRequired etc. as a part of response; None: to skip these properties. |
#### Return Type
:class:<WorkItemTypeFieldWithReferences> <azure.devops.v5_1.work_item_tracking.models.WorkItemTypeFieldWithReferences>
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_work_item_type_field_with_references(project, type, field, expand=None)
```
### GetWorkItemTypeFieldsWithReferences
#### Description:
Get a list of fields for a work item type with detailed references.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| type | str | Work item type. |
| expand | str | Expand level for the API response. Properties: to include allowedvalues, default value, isRequired etc. as a part of response; None: to skip these properties. |
#### Return Type
[WorkItemTypeFieldWithReferences]
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_work_item_type_fields_with_references(project, type, expand=None)
```
### GetWorkItemTypes
#### Description:
Returns the list of work item types
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
#### Return Type
[WorkItemType]
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_work_item_types(project)
```
### GetWorkItems
#### Description:
Returns a list of work items (Maximum 200)
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| ids | [int] | The comma-separated list of requested work item ids. (Maximum 200 ids allowed). |
| project | str | Project ID or project name |
| fields | [str] | Comma-separated list of requested fields |
| as_of | datetime | AsOf UTC date time string |
| expand | str | The expand parameters for work item attributes. Possible options are { None, Relations, Fields, Links, All }. |
| error_policy | str | The flag to control error policy in a bulk get work items request. Possible options are {Fail, Omit}. |
#### Return Type
[WorkItem]
#### Example Usage
```

connection.clients.get_work_item_tracking_client().get_work_items(ids, project=None, fields=None, as_of=None, expand=None, error_policy=None)
```
### GetWorkItemsBatch
#### Description:
Gets work items for a list of work item ids (Maximum 200)
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| work_item_get_request | class |  |
| project | str | Project ID or project name |
#### Return Type
[WorkItem]
#### Example Usage
```
from azure.devops.v5_1.work_item_tracking.models import WorkItemBatchGetRequest

connection.clients.get_work_item_tracking_client().get_work_items_batch(work_item_get_request, project=None)
```
### QueryById
#### Description:
Gets the results of the query given the query ID.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| id | str | The query ID. |
| team_context | class | The team context for the operation |
| time_precision | bool | Whether or not to use time precision. |
| top | int | The max number of results to return. |
#### Return Type
:class:<WorkItemQueryResult> <azure.devops.v5_1.work_item_tracking.models.WorkItemQueryResult>
#### Example Usage
```
from azure.devops.v5_1.work_item_tracking.models import TeamContext

connection.clients.get_work_item_tracking_client().query_by_id(id, team_context=None, time_precision=None, top=None)
```
### QueryByWiql
#### Description:
Gets the results of the query given its WIQL.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| wiql | class | The query containing the WIQL. |
| team_context | class | The team context for the operation |
| time_precision | bool | Whether or not to use time precision. |
| top | int | The max number of results to return. |
#### Return Type
:class:<WorkItemQueryResult> <azure.devops.v5_1.work_item_tracking.models.WorkItemQueryResult>
#### Example Usage
```
from azure.devops.v5_1.work_item_tracking.models import Wiql
from azure.devops.v5_1.work_item_tracking.models import TeamContext

connection.clients.get_work_item_tracking_client().query_by_wiql(wiql, team_context=None, time_precision=None, top=None)
```
### ReadReportingRevisionsGet
#### Description:
Get a batch of work item revisions with the option of including deleted items
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| fields | [str] | A list of fields to return in work item revisions. Omit this parameter to get all reportable fields. |
| types | [str] | A list of types to filter the results to specific work item types. Omit this parameter to get work item revisions of all work item types. |
| continuation_token | str | Specifies the watermark to start the batch from. Omit this parameter to get the first batch of revisions. |
| start_date_time | datetime | Date/time to use as a starting point for revisions, all revisions will occur after this date/time. Cannot be used in conjunction with 'watermark' parameter. |
| include_identity_ref | bool | Return an identity reference instead of a string value for identity fields. |
| include_deleted | bool | Specify if the deleted item should be returned. |
| include_tag_ref | bool | Specify if the tag objects should be returned for System.Tags field. |
| include_latest_only | bool | Return only the latest revisions of work items, skipping all historical revisions |
| expand | str | Return all the fields in work item revisions, including long text fields which are not returned by default |
| include_discussion_changes_only | bool | Return only the those revisions of work items, where only history field was changed |
| max_page_size | int | The maximum number of results to return in this batch |
#### Return Type
:class:<ReportingWorkItemRevisionsBatch> <azure.devops.v5_1.work_item_tracking.models.ReportingWorkItemRevisionsBatch>
#### Example Usage
```

connection.clients.get_work_item_tracking_client().read_reporting_revisions_get(project=None, fields=None, types=None, continuation_token=None, start_date_time=None, include_identity_ref=None, include_deleted=None, include_tag_ref=None, include_latest_only=None, expand=None, include_discussion_changes_only=None, max_page_size=None)
```
### ReadReportingRevisionsPost
#### Description:
Get a batch of work item revisions. This request may be used if your list of fields is large enough that it may run the URL over the length limit.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| filter: An object that contains request settings | class | field filter, type filter, identity format |
| project | str | Project ID or project name |
| continuation_token | str | Specifies the watermark to start the batch from. Omit this parameter to get the first batch of revisions. |
| start_date_time | datetime | Date/time to use as a starting point for revisions, all revisions will occur after this date/time. Cannot be used in conjunction with 'watermark' parameter. |
| expand | str |  |
#### Return Type
:class:<ReportingWorkItemRevisionsBatch> <azure.devops.v5_1.work_item_tracking.models.ReportingWorkItemRevisionsBatch>
#### Example Usage
```
from azure.devops.v5_1.work_item_tracking.models import ReportingWorkItemRevisionsFilter

connection.clients.get_work_item_tracking_client().read_reporting_revisions_post(filter, project=None, continuation_token=None, start_date_time=None, expand=None)
```
### RestoreWorkItem
#### Description:
Restores the deleted work item from Recycle Bin.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| payload | class | Paylod with instructions to update the IsDeleted flag to false |
| id | int | ID of the work item to be restored |
| project | str | Project ID or project name |
#### Return Type
:class:<WorkItemDelete> <azure.devops.v5_1.work_item_tracking.models.WorkItemDelete>
#### Example Usage
```
from azure.devops.v5_1.work_item_tracking.models import WorkItemDeleteUpdate

connection.clients.get_work_item_tracking_client().restore_work_item(payload, id, project=None)
```
### SearchQueries
#### Description:
Searches all queries the user has access to in the current project
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| project | str | Project ID or project name |
| filter | str | The text to filter the queries with. |
| top | int | The number of queries to return (Default is 50 and maximum is 200). |
| expand | str |  |
| include_deleted | bool | Include deleted queries and folders |
#### Return Type
:class:<QueryHierarchyItemsResult> <azure.devops.v5_1.work_item_tracking.models.QueryHierarchyItemsResult>
#### Example Usage
```

connection.clients.get_work_item_tracking_client().search_queries(project, filter, top=None, expand=None, include_deleted=None)
```
### UpdateClassificationNode
#### Description:
Update an existing classification node.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| posted_node | class | Node to create or update. |
| project | str | Project ID or project name |
| structure_group | TreeStructureGroup | Structure group of the classification node, area or iteration. |
| path | str | Path of the classification node. |
#### Return Type
:class:<WorkItemClassificationNode> <azure.devops.v5_1.work_item_tracking.models.WorkItemClassificationNode>
#### Example Usage
```
from azure.devops.v5_1.work_item_tracking.models import WorkItemClassificationNode

connection.clients.get_work_item_tracking_client().update_classification_node(posted_node, project, structure_group, path=None)
```
### UpdateQuery
#### Description:
Update a query or a folder. This allows you to update, rename and move queries and folders.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| query_update | class | The query to update. |
| project | str | Project ID or project name |
| query | str | The ID or path for the query to update. |
| undelete_descendants | bool | Undelete the children of this folder. It is important to note that this will not bring back the permission changes that were previously applied to the descendants. |
#### Return Type
:class:<QueryHierarchyItem> <azure.devops.v5_1.work_item_tracking.models.QueryHierarchyItem>
#### Example Usage
```
from azure.devops.v5_1.work_item_tracking.models import QueryHierarchyItem

connection.clients.get_work_item_tracking_client().update_query(query_update, project, query, undelete_descendants=None)
```
### UpdateWorkItem
#### Description:
Updates a single work item.
#### Parameters:
| Name | Type | Description |
| --- | --- | --- |
| document | class | The JSON Patch document representing the update |
| id | int | The id of the work item to update |
| project | str | Project ID or project name |
| validate_only | bool | Indicate if you only want to validate the changes without saving the work item |
| bypass_rules | bool | Do not enforce the work item type rules on this update |
| suppress_notifications | bool | Do not fire any notifications for this change |
| expand | str | The expand parameters for work item attributes. Possible options are { None, Relations, Fields, Links, All }. |
#### Return Type
:class:<WorkItem> <azure.devops.v5_1.work_item_tracking.models.WorkItem>
#### Example Usage
```
from azure.devops.v5_1.work_item_tracking.models import [JsonPatchOperation]

connection.clients.get_work_item_tracking_client().update_work_item(document, id, project=None, validate_only=None, bypass_rules=None, suppress_notifications=None, expand=None)
```
