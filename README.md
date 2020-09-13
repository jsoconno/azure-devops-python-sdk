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

* `:param str owner_id: ID for the owner of the accounts.`
* `:param str member_id: ID for a member of the accounts.`
* `:param str properties:`
#### Example usage:
```
connection.clients.get_accounts_client().get_accounts(owner_id=None, member_id=None, properties=None)
```


#### Return Type:
`:rtype: [Account]`
## Get Build Client
### AddBuildTag
#### Description:
Adds a tag to a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param str tag: The tag to add.`
#### Example usage:
```
connection.clients.get_build_client().add_build_tag(project, build_id, tag)
```


#### Return Type:
`:rtype: [str]`
### AddBuildTags
#### Description:
Adds tags to a build.

* `:param [str] tags: The tags to add.`
* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
#### Example usage:
```
connection.clients.get_build_client().add_build_tags(tags, project, build_id)
```


#### Return Type:
`:rtype: [str]`
### CreateArtifact
#### Description:
Associates an artifact with a build.

* `:param :class:<BuildArtifact> <azure.devops.v5_1.build.models.BuildArtifact> artifact: The artifact.`
* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
#### Example usage:
```
from azure.devops.v5_1.build.models import BuildArtifact

connection.clients.get_build_client().create_artifact(artifact, project, build_id)
```


#### Return Type:
`:rtype: :class:<BuildArtifact> <azure.devops.v5_1.build.models.BuildArtifact>`
### CreateDefinition
#### Description:
Creates a new definition.

* `:param :class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition> definition: The definition.`
* `:param str project: Project ID or project name`
* `:param int definition_to_clone_id:`
* `:param int definition_to_clone_revision:`
#### Example usage:
```
from azure.devops.v5_1.build.models import BuildDefinition

connection.clients.get_build_client().create_definition(definition, project, definition_to_clone_id=None, definition_to_clone_revision=None)
```


#### Return Type:
`:rtype: :class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition>`
### DeleteBuild
#### Description:
Deletes a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
#### Example usage:
```
connection.clients.get_build_client().delete_build(project, build_id)
```


#### Return Type:
`:rtype: :class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition>`
### DeleteBuildTag
#### Description:
Removes a tag from a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param str tag: The tag to remove.`
#### Example usage:
```
connection.clients.get_build_client().delete_build_tag(project, build_id, tag)
```


#### Return Type:
`:rtype: [str]`
### DeleteDefinition
#### Description:
Deletes a definition and all associated builds.

* `:param str project: Project ID or project name`
* `:param int definition_id: The ID of the definition.`
#### Example usage:
```
connection.clients.get_build_client().delete_definition(project, definition_id)
```


#### Return Type:
`:rtype: [str]`
### DeleteTemplate
#### Description:
Deletes a build definition template.

* `:param str project: Project ID or project name`
* `:param str template_id: The ID of the template.`
#### Example usage:
```
connection.clients.get_build_client().delete_template(project, template_id)
```


#### Return Type:
`:rtype: [str]`
### GetArtifact
#### Description:
Gets a specific artifact for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param str artifact_name: The name of the artifact.`
#### Example usage:
```
connection.clients.get_build_client().get_artifact(project, build_id, artifact_name)
```


#### Return Type:
`:rtype: :class:<BuildArtifact> <azure.devops.v5_1.build.models.BuildArtifact>`
### GetArtifactContentZip
#### Description:
Gets a specific artifact for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param str artifact_name: The name of the artifact.`
#### Example usage:
```
connection.clients.get_build_client().get_artifact_content_zip(project, build_id, artifact_name, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetArtifacts
#### Description:
Gets all artifacts for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
#### Example usage:
```
connection.clients.get_build_client().get_artifacts(project, build_id)
```


#### Return Type:
`:rtype: [BuildArtifact]`
### GetBuild
#### Description:
Gets a build

* `:param str project: Project ID or project name`
* `:param int build_id:`
* `:param str property_filters:`
#### Example usage:
```
connection.clients.get_build_client().get_build(project, build_id, property_filters=None)
```


#### Return Type:
`:rtype: :class:<Build> <azure.devops.v5_1.build.models.Build>`
### GetBuildChanges
#### Description:
Gets the changes associated with a build

* `:param str project: Project ID or project name`
* `:param int build_id:`
* `:param str continuation_token:`
* `:param int top: The maximum number of changes to return`
* `:param bool include_source_change:`
#### Example usage:
```
connection.clients.get_build_client().get_build_changes(project, build_id, continuation_token=None, top=None, include_source_change=None)
```


#### Return Type:
`:rtype: :class:<GetBuildChangesResponseValue>`
### GetBuildController
#### Description:
Gets a controller

* `:param int controller_id:`
#### Example usage:
```
connection.clients.get_build_client().get_build_controller(controller_id)
```


#### Return Type:
`:rtype: :class:<BuildController> <azure.devops.v5_1.build.models.BuildController>`
### GetBuildControllers
#### Description:
Gets controller, optionally filtered by name

* `:param str name:`
#### Example usage:
```
connection.clients.get_build_client().get_build_controllers(name=None)
```


#### Return Type:
`:rtype: [BuildController]`
### GetBuildLog
#### Description:
Gets an individual log file for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param int log_id: The ID of the log file.`
* `:param long start_line: The start line.`
* `:param long end_line: The end line.`
#### Example usage:
```
connection.clients.get_build_client().get_build_log(project, build_id, log_id, start_line=None, end_line=None, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetBuildLogLines
#### Description:
Gets an individual log file for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param int log_id: The ID of the log file.`
* `:param long start_line: The start line.`
* `:param long end_line: The end line.`
#### Example usage:
```
connection.clients.get_build_client().get_build_log_lines(project, build_id, log_id, start_line=None, end_line=None)
```


#### Return Type:
`:rtype: [str]`
### GetBuildLogZip
#### Description:
Gets an individual log file for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param int log_id: The ID of the log file.`
* `:param long start_line: The start line.`
* `:param long end_line: The end line.`
#### Example usage:
```
connection.clients.get_build_client().get_build_log_zip(project, build_id, log_id, start_line=None, end_line=None, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetBuildLogs
#### Description:
Gets the logs for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
#### Example usage:
```
connection.clients.get_build_client().get_build_logs(project, build_id)
```


#### Return Type:
`:rtype: [BuildLog]`
### GetBuildLogsZip
#### Description:
Gets the logs for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
#### Example usage:
```
connection.clients.get_build_client().get_build_logs_zip(project, build_id, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetBuildOptionDefinitions
#### Description:
Gets all build definition options supported by the system.

* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_build_client().get_build_option_definitions(project=None)
```


#### Return Type:
`:rtype: [BuildOptionDefinition]`
### GetBuildSettings
#### Description:
Gets the build settings.

* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_build_client().get_build_settings(project=None)
```


#### Return Type:
`:rtype: :class:<BuildSettings> <azure.devops.v5_1.build.models.BuildSettings>`
### GetBuildTags
#### Description:
Gets the tags for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
#### Example usage:
```
connection.clients.get_build_client().get_build_tags(project, build_id)
```


#### Return Type:
`:rtype: [str]`
### GetBuildTimeline
#### Description:
Gets details for a build

* `:param str project: Project ID or project name`
* `:param int build_id:`
* `:param str timeline_id:`
* `:param int change_id:`
* `:param str plan_id:`
#### Example usage:
```
connection.clients.get_build_client().get_build_timeline(project, build_id, timeline_id=None, change_id=None, plan_id=None)
```


#### Return Type:
`:rtype: :class:<Timeline> <azure.devops.v5_1.build.models.Timeline>`
### GetBuildWorkItemsRefs
#### Description:
Gets the work items associated with a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param int top: The maximum number of work items to return.`
#### Example usage:
```
connection.clients.get_build_client().get_build_work_items_refs(project, build_id, top=None)
```


#### Return Type:
`:rtype: [ResourceRef]`
### GetBuildWorkItemsRefsFromCommits
#### Description:
Gets the work items associated with a build, filtered to specific commits.

* `:param [str] commit_ids: A comma-delimited list of commit IDs.`
* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param int top: The maximum number of work items to return, or the number of commits to consider if no commit IDs are specified.`
#### Example usage:
```
connection.clients.get_build_client().get_build_work_items_refs_from_commits(commit_ids, project, build_id, top=None)
```


#### Return Type:
`:rtype: [ResourceRef]`
### GetBuilds
#### Description:
Gets a list of builds.

* `:param str project: Project ID or project name`
* `:param [int] definitions: A comma-delimited list of definition IDs. If specified, filters to builds for these definitions.`
* `:param [int] queues: A comma-delimited list of queue IDs. If specified, filters to builds that ran against these queues.`
* `:param str build_number: If specified, filters to builds that match this build number. Append * to do a prefix search.`
* `:param datetime min_time: If specified, filters to builds that finished/started/queued after this date based on the queryOrder specified.`
* `:param datetime max_time: If specified, filters to builds that finished/started/queued before this date based on the queryOrder specified.`
* `:param str requested_for: If specified, filters to builds requested for the specified user.`
* `:param str reason_filter: If specified, filters to builds that match this reason.`
* `:param str status_filter: If specified, filters to builds that match this status.`
* `:param str result_filter: If specified, filters to builds that match this result.`
* `:param [str] tag_filters: A comma-delimited list of tags. If specified, filters to builds that have the specified tags.`
* `:param [str] properties: A comma-delimited list of properties to retrieve.`
* `:param int top: The maximum number of builds to return.`
* `:param str continuation_token: A continuation token, returned by a previous call to this method, that can be used to return the next set of builds.`
* `:param int max_builds_per_definition: The maximum number of builds to return per definition.`
* `:param str deleted_filter: Indicates whether to exclude, include, or only return deleted builds.`
* `:param str query_order: The order in which builds should be returned.`
* `:param str branch_name: If specified, filters to builds that built branches that built this branch.`
* `:param [int] build_ids: A comma-delimited list that specifies the IDs of builds to retrieve.`
* `:param str repository_id: If specified, filters to builds that built from this repository.`
* `:param str repository_type: If specified, filters to builds that built from repositories of this type.`
#### Example usage:
```
connection.clients.get_build_client().get_builds(project, definitions=None, queues=None, build_number=None, min_time=None, max_time=None, requested_for=None, reason_filter=None, status_filter=None, result_filter=None, tag_filters=None, properties=None, top=None, continuation_token=None, max_builds_per_definition=None, deleted_filter=None, query_order=None, branch_name=None, build_ids=None, repository_id=None, repository_type=None)
```


#### Return Type:
`:rtype: :class:<GetBuildsResponseValue>`
### GetDefinition
#### Description:
Gets a definition, optionally at a specific revision.

* `:param str project: Project ID or project name`
* `:param int definition_id: The ID of the definition.`
* `:param int revision: The revision number to retrieve. If this is not specified, the latest version will be returned.`
* `:param datetime min_metrics_time: If specified, indicates the date from which metrics should be included.`
* `:param [str] property_filters: A comma-delimited list of properties to include in the results.`
* `:param bool include_latest_builds:`
#### Example usage:
```
connection.clients.get_build_client().get_definition(project, definition_id, revision=None, min_metrics_time=None, property_filters=None, include_latest_builds=None)
```


#### Return Type:
`:rtype: :class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition>`
### GetDefinitionRevisions
#### Description:
Gets all revisions of a definition.

* `:param str project: Project ID or project name`
* `:param int definition_id: The ID of the definition.`
#### Example usage:
```
connection.clients.get_build_client().get_definition_revisions(project, definition_id)
```


#### Return Type:
`:rtype: [BuildDefinitionRevision]`
### GetDefinitions
#### Description:
Gets a list of definitions.

* `:param str project: Project ID or project name`
* `:param str name: If specified, filters to definitions whose names match this pattern.`
* `:param str repository_id: A repository ID. If specified, filters to definitions that use this repository.`
* `:param str repository_type: If specified, filters to definitions that have a repository of this type.`
* `:param str query_order: Indicates the order in which definitions should be returned.`
* `:param int top: The maximum number of definitions to return.`
* `:param str continuation_token: A continuation token, returned by a previous call to this method, that can be used to return the next set of definitions.`
* `:param datetime min_metrics_time: If specified, indicates the date from which metrics should be included.`
* `:param [int] definition_ids: A comma-delimited list that specifies the IDs of definitions to retrieve.`
* `:param str path: If specified, filters to definitions under this folder.`
* `:param datetime built_after: If specified, filters to definitions that have builds after this date.`
* `:param datetime not_built_after: If specified, filters to definitions that do not have builds after this date.`
* `:param bool include_all_properties: Indicates whether the full definitions should be returned. By default, shallow representations of the definitions are returned.`
* `:param bool include_latest_builds: Indicates whether to return the latest and latest completed builds for this definition.`
* `:param str task_id_filter: If specified, filters to definitions that use the specified task.`
* `:param int process_type: If specified, filters to definitions with the given process type.`
* `:param str yaml_filename: If specified, filters to YAML definitions that match the given filename.`
#### Example usage:
```
connection.clients.get_build_client().get_definitions(project, name=None, repository_id=None, repository_type=None, query_order=None, top=None, continuation_token=None, min_metrics_time=None, definition_ids=None, path=None, built_after=None, not_built_after=None, include_all_properties=None, include_latest_builds=None, task_id_filter=None, process_type=None, yaml_filename=None)
```


#### Return Type:
`:rtype: :class:<GetDefinitionsResponseValue>`
### GetFile
#### Description:
Gets a file from the build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param str artifact_name: The name of the artifact.`
* `:param str file_id: The primary key for the file.`
* `:param str file_name: The name that the file will be set to.`
#### Example usage:
```
connection.clients.get_build_client().get_file(project, build_id, artifact_name, file_id, file_name, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetTags
#### Description:
Gets a list of all build and definition tags in the project.

* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_build_client().get_tags(project)
```


#### Return Type:
`:rtype: [str]`
### GetTemplate
#### Description:
Gets a specific build definition template.

* `:param str project: Project ID or project name`
* `:param str template_id: The ID of the requested template.`
#### Example usage:
```
connection.clients.get_build_client().get_template(project, template_id)
```


#### Return Type:
`:rtype: :class:<BuildDefinitionTemplate> <azure.devops.v5_1.build.models.BuildDefinitionTemplate>`
### GetTemplates
#### Description:
Gets all definition templates.

* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_build_client().get_templates(project)
```


#### Return Type:
`:rtype: [BuildDefinitionTemplate]`
### QueueBuild
#### Description:
Queues a build

* `:param :class:<Build> <azure.devops.v5_1.build.models.Build> build:`
* `:param str project: Project ID or project name`
* `:param bool ignore_warnings:`
* `:param str check_in_ticket:`
* `:param int source_build_id:`
#### Example usage:
```
from azure.devops.v5_1.build.models import Build

connection.clients.get_build_client().queue_build(build, project, ignore_warnings=None, check_in_ticket=None, source_build_id=None)
```


#### Return Type:
`:rtype: :class:<Build> <azure.devops.v5_1.build.models.Build>`
### RestoreDefinition
#### Description:
Restores a deleted definition

* `:param str project: Project ID or project name`
* `:param int definition_id: The identifier of the definition to restore.`
* `:param bool deleted: When false, restores a deleted definition.`
#### Example usage:
```
connection.clients.get_build_client().restore_definition(project, definition_id, deleted)
```


#### Return Type:
`:rtype: :class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition>`
### SaveTemplate
#### Description:
Updates an existing build definition template.

* `:param :class:<BuildDefinitionTemplate> <azure.devops.v5_1.build.models.BuildDefinitionTemplate> template: The new version of the template.`
* `:param str project: Project ID or project name`
* `:param str template_id: The ID of the template.`
#### Example usage:
```
from azure.devops.v5_1.build.models import BuildDefinitionTemplate

connection.clients.get_build_client().save_template(template, project, template_id)
```


#### Return Type:
`:rtype: :class:<BuildDefinitionTemplate> <azure.devops.v5_1.build.models.BuildDefinitionTemplate>`
### UpdateBuild
#### Description:
Updates a build.

* `:param :class:<Build> <azure.devops.v5_1.build.models.Build> build: The build.`
* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param bool retry:`
#### Example usage:
```
from azure.devops.v5_1.build.models import Build

connection.clients.get_build_client().update_build(build, project, build_id, retry=None)
```


#### Return Type:
`:rtype: :class:<Build> <azure.devops.v5_1.build.models.Build>`
### UpdateBuildSettings
#### Description:
Updates the build settings.

* `:param :class:<BuildSettings> <azure.devops.v5_1.build.models.BuildSettings> settings: The new settings.`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.build.models import BuildSettings

connection.clients.get_build_client().update_build_settings(settings, project=None)
```


#### Return Type:
`:rtype: :class:<BuildSettings> <azure.devops.v5_1.build.models.BuildSettings>`
### UpdateBuilds
#### Description:
Updates multiple builds.

* `:param [Build] builds: The builds to update.`
* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_build_client().update_builds(builds, project)
```


#### Return Type:
`:rtype: [Build]`
### UpdateDefinition
#### Description:
Updates an existing definition.

* `:param :class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition> definition: The new version of the definition.`
* `:param str project: Project ID or project name`
* `:param int definition_id: The ID of the definition.`
* `:param int secrets_source_definition_id:`
* `:param int secrets_source_definition_revision:`
#### Example usage:
```
from azure.devops.v5_1.build.models import BuildDefinition

connection.clients.get_build_client().update_definition(definition, project, definition_id, secrets_source_definition_id=None, secrets_source_definition_revision=None)
```


#### Return Type:
`:rtype: :class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition>`
## Get Cloud Load Test Client
### AddBuildTag
#### Description:
Adds a tag to a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param str tag: The tag to add.`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().add_build_tag(project, build_id, tag)
```


#### Return Type:
`:rtype: [str]`
### AddBuildTags
#### Description:
Adds tags to a build.

* `:param [str] tags: The tags to add.`
* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().add_build_tags(tags, project, build_id)
```


#### Return Type:
`:rtype: [str]`
### CreateArtifact
#### Description:
Associates an artifact with a build.

* `:param :class:<BuildArtifact> <azure.devops.v5_1.build.models.BuildArtifact> artifact: The artifact.`
* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
#### Example usage:
```
from azure.devops.v5_1.build.models import BuildArtifact

connection.clients.get_cloud_load_test_client().create_artifact(artifact, project, build_id)
```


#### Return Type:
`:rtype: :class:<BuildArtifact> <azure.devops.v5_1.build.models.BuildArtifact>`
### CreateDefinition
#### Description:
Creates a new definition.

* `:param :class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition> definition: The definition.`
* `:param str project: Project ID or project name`
* `:param int definition_to_clone_id:`
* `:param int definition_to_clone_revision:`
#### Example usage:
```
from azure.devops.v5_1.build.models import BuildDefinition

connection.clients.get_cloud_load_test_client().create_definition(definition, project, definition_to_clone_id=None, definition_to_clone_revision=None)
```


#### Return Type:
`:rtype: :class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition>`
### DeleteBuild
#### Description:
Deletes a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().delete_build(project, build_id)
```


#### Return Type:
`:rtype: :class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition>`
### DeleteBuildTag
#### Description:
Removes a tag from a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param str tag: The tag to remove.`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().delete_build_tag(project, build_id, tag)
```


#### Return Type:
`:rtype: [str]`
### DeleteDefinition
#### Description:
Deletes a definition and all associated builds.

* `:param str project: Project ID or project name`
* `:param int definition_id: The ID of the definition.`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().delete_definition(project, definition_id)
```


#### Return Type:
`:rtype: [str]`
### DeleteTemplate
#### Description:
Deletes a build definition template.

* `:param str project: Project ID or project name`
* `:param str template_id: The ID of the template.`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().delete_template(project, template_id)
```


#### Return Type:
`:rtype: [str]`
### GetArtifact
#### Description:
Gets a specific artifact for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param str artifact_name: The name of the artifact.`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().get_artifact(project, build_id, artifact_name)
```


#### Return Type:
`:rtype: :class:<BuildArtifact> <azure.devops.v5_1.build.models.BuildArtifact>`
### GetArtifactContentZip
#### Description:
Gets a specific artifact for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param str artifact_name: The name of the artifact.`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().get_artifact_content_zip(project, build_id, artifact_name, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetArtifacts
#### Description:
Gets all artifacts for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().get_artifacts(project, build_id)
```


#### Return Type:
`:rtype: [BuildArtifact]`
### GetBuild
#### Description:
Gets a build

* `:param str project: Project ID or project name`
* `:param int build_id:`
* `:param str property_filters:`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().get_build(project, build_id, property_filters=None)
```


#### Return Type:
`:rtype: :class:<Build> <azure.devops.v5_1.build.models.Build>`
### GetBuildChanges
#### Description:
Gets the changes associated with a build

* `:param str project: Project ID or project name`
* `:param int build_id:`
* `:param str continuation_token:`
* `:param int top: The maximum number of changes to return`
* `:param bool include_source_change:`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().get_build_changes(project, build_id, continuation_token=None, top=None, include_source_change=None)
```


#### Return Type:
`:rtype: :class:<GetBuildChangesResponseValue>`
### GetBuildController
#### Description:
Gets a controller

* `:param int controller_id:`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().get_build_controller(controller_id)
```


#### Return Type:
`:rtype: :class:<BuildController> <azure.devops.v5_1.build.models.BuildController>`
### GetBuildControllers
#### Description:
Gets controller, optionally filtered by name

* `:param str name:`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().get_build_controllers(name=None)
```


#### Return Type:
`:rtype: [BuildController]`
### GetBuildLog
#### Description:
Gets an individual log file for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param int log_id: The ID of the log file.`
* `:param long start_line: The start line.`
* `:param long end_line: The end line.`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().get_build_log(project, build_id, log_id, start_line=None, end_line=None, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetBuildLogLines
#### Description:
Gets an individual log file for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param int log_id: The ID of the log file.`
* `:param long start_line: The start line.`
* `:param long end_line: The end line.`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().get_build_log_lines(project, build_id, log_id, start_line=None, end_line=None)
```


#### Return Type:
`:rtype: [str]`
### GetBuildLogZip
#### Description:
Gets an individual log file for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param int log_id: The ID of the log file.`
* `:param long start_line: The start line.`
* `:param long end_line: The end line.`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().get_build_log_zip(project, build_id, log_id, start_line=None, end_line=None, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetBuildLogs
#### Description:
Gets the logs for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().get_build_logs(project, build_id)
```


#### Return Type:
`:rtype: [BuildLog]`
### GetBuildLogsZip
#### Description:
Gets the logs for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().get_build_logs_zip(project, build_id, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetBuildOptionDefinitions
#### Description:
Gets all build definition options supported by the system.

* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().get_build_option_definitions(project=None)
```


#### Return Type:
`:rtype: [BuildOptionDefinition]`
### GetBuildSettings
#### Description:
Gets the build settings.

* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().get_build_settings(project=None)
```


#### Return Type:
`:rtype: :class:<BuildSettings> <azure.devops.v5_1.build.models.BuildSettings>`
### GetBuildTags
#### Description:
Gets the tags for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().get_build_tags(project, build_id)
```


#### Return Type:
`:rtype: [str]`
### GetBuildTimeline
#### Description:
Gets details for a build

* `:param str project: Project ID or project name`
* `:param int build_id:`
* `:param str timeline_id:`
* `:param int change_id:`
* `:param str plan_id:`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().get_build_timeline(project, build_id, timeline_id=None, change_id=None, plan_id=None)
```


#### Return Type:
`:rtype: :class:<Timeline> <azure.devops.v5_1.build.models.Timeline>`
### GetBuildWorkItemsRefs
#### Description:
Gets the work items associated with a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param int top: The maximum number of work items to return.`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().get_build_work_items_refs(project, build_id, top=None)
```


#### Return Type:
`:rtype: [ResourceRef]`
### GetBuildWorkItemsRefsFromCommits
#### Description:
Gets the work items associated with a build, filtered to specific commits.

* `:param [str] commit_ids: A comma-delimited list of commit IDs.`
* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param int top: The maximum number of work items to return, or the number of commits to consider if no commit IDs are specified.`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().get_build_work_items_refs_from_commits(commit_ids, project, build_id, top=None)
```


#### Return Type:
`:rtype: [ResourceRef]`
### GetBuilds
#### Description:
Gets a list of builds.

* `:param str project: Project ID or project name`
* `:param [int] definitions: A comma-delimited list of definition IDs. If specified, filters to builds for these definitions.`
* `:param [int] queues: A comma-delimited list of queue IDs. If specified, filters to builds that ran against these queues.`
* `:param str build_number: If specified, filters to builds that match this build number. Append * to do a prefix search.`
* `:param datetime min_time: If specified, filters to builds that finished/started/queued after this date based on the queryOrder specified.`
* `:param datetime max_time: If specified, filters to builds that finished/started/queued before this date based on the queryOrder specified.`
* `:param str requested_for: If specified, filters to builds requested for the specified user.`
* `:param str reason_filter: If specified, filters to builds that match this reason.`
* `:param str status_filter: If specified, filters to builds that match this status.`
* `:param str result_filter: If specified, filters to builds that match this result.`
* `:param [str] tag_filters: A comma-delimited list of tags. If specified, filters to builds that have the specified tags.`
* `:param [str] properties: A comma-delimited list of properties to retrieve.`
* `:param int top: The maximum number of builds to return.`
* `:param str continuation_token: A continuation token, returned by a previous call to this method, that can be used to return the next set of builds.`
* `:param int max_builds_per_definition: The maximum number of builds to return per definition.`
* `:param str deleted_filter: Indicates whether to exclude, include, or only return deleted builds.`
* `:param str query_order: The order in which builds should be returned.`
* `:param str branch_name: If specified, filters to builds that built branches that built this branch.`
* `:param [int] build_ids: A comma-delimited list that specifies the IDs of builds to retrieve.`
* `:param str repository_id: If specified, filters to builds that built from this repository.`
* `:param str repository_type: If specified, filters to builds that built from repositories of this type.`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().get_builds(project, definitions=None, queues=None, build_number=None, min_time=None, max_time=None, requested_for=None, reason_filter=None, status_filter=None, result_filter=None, tag_filters=None, properties=None, top=None, continuation_token=None, max_builds_per_definition=None, deleted_filter=None, query_order=None, branch_name=None, build_ids=None, repository_id=None, repository_type=None)
```


#### Return Type:
`:rtype: :class:<GetBuildsResponseValue>`
### GetDefinition
#### Description:
Gets a definition, optionally at a specific revision.

* `:param str project: Project ID or project name`
* `:param int definition_id: The ID of the definition.`
* `:param int revision: The revision number to retrieve. If this is not specified, the latest version will be returned.`
* `:param datetime min_metrics_time: If specified, indicates the date from which metrics should be included.`
* `:param [str] property_filters: A comma-delimited list of properties to include in the results.`
* `:param bool include_latest_builds:`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().get_definition(project, definition_id, revision=None, min_metrics_time=None, property_filters=None, include_latest_builds=None)
```


#### Return Type:
`:rtype: :class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition>`
### GetDefinitionRevisions
#### Description:
Gets all revisions of a definition.

* `:param str project: Project ID or project name`
* `:param int definition_id: The ID of the definition.`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().get_definition_revisions(project, definition_id)
```


#### Return Type:
`:rtype: [BuildDefinitionRevision]`
### GetDefinitions
#### Description:
Gets a list of definitions.

* `:param str project: Project ID or project name`
* `:param str name: If specified, filters to definitions whose names match this pattern.`
* `:param str repository_id: A repository ID. If specified, filters to definitions that use this repository.`
* `:param str repository_type: If specified, filters to definitions that have a repository of this type.`
* `:param str query_order: Indicates the order in which definitions should be returned.`
* `:param int top: The maximum number of definitions to return.`
* `:param str continuation_token: A continuation token, returned by a previous call to this method, that can be used to return the next set of definitions.`
* `:param datetime min_metrics_time: If specified, indicates the date from which metrics should be included.`
* `:param [int] definition_ids: A comma-delimited list that specifies the IDs of definitions to retrieve.`
* `:param str path: If specified, filters to definitions under this folder.`
* `:param datetime built_after: If specified, filters to definitions that have builds after this date.`
* `:param datetime not_built_after: If specified, filters to definitions that do not have builds after this date.`
* `:param bool include_all_properties: Indicates whether the full definitions should be returned. By default, shallow representations of the definitions are returned.`
* `:param bool include_latest_builds: Indicates whether to return the latest and latest completed builds for this definition.`
* `:param str task_id_filter: If specified, filters to definitions that use the specified task.`
* `:param int process_type: If specified, filters to definitions with the given process type.`
* `:param str yaml_filename: If specified, filters to YAML definitions that match the given filename.`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().get_definitions(project, name=None, repository_id=None, repository_type=None, query_order=None, top=None, continuation_token=None, min_metrics_time=None, definition_ids=None, path=None, built_after=None, not_built_after=None, include_all_properties=None, include_latest_builds=None, task_id_filter=None, process_type=None, yaml_filename=None)
```


#### Return Type:
`:rtype: :class:<GetDefinitionsResponseValue>`
### GetFile
#### Description:
Gets a file from the build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param str artifact_name: The name of the artifact.`
* `:param str file_id: The primary key for the file.`
* `:param str file_name: The name that the file will be set to.`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().get_file(project, build_id, artifact_name, file_id, file_name, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetTags
#### Description:
Gets a list of all build and definition tags in the project.

* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().get_tags(project)
```


#### Return Type:
`:rtype: [str]`
### GetTemplate
#### Description:
Gets a specific build definition template.

* `:param str project: Project ID or project name`
* `:param str template_id: The ID of the requested template.`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().get_template(project, template_id)
```


#### Return Type:
`:rtype: :class:<BuildDefinitionTemplate> <azure.devops.v5_1.build.models.BuildDefinitionTemplate>`
### GetTemplates
#### Description:
Gets all definition templates.

* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().get_templates(project)
```


#### Return Type:
`:rtype: [BuildDefinitionTemplate]`
### QueueBuild
#### Description:
Queues a build

* `:param :class:<Build> <azure.devops.v5_1.build.models.Build> build:`
* `:param str project: Project ID or project name`
* `:param bool ignore_warnings:`
* `:param str check_in_ticket:`
* `:param int source_build_id:`
#### Example usage:
```
from azure.devops.v5_1.build.models import Build

connection.clients.get_cloud_load_test_client().queue_build(build, project, ignore_warnings=None, check_in_ticket=None, source_build_id=None)
```


#### Return Type:
`:rtype: :class:<Build> <azure.devops.v5_1.build.models.Build>`
### RestoreDefinition
#### Description:
Restores a deleted definition

* `:param str project: Project ID or project name`
* `:param int definition_id: The identifier of the definition to restore.`
* `:param bool deleted: When false, restores a deleted definition.`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().restore_definition(project, definition_id, deleted)
```


#### Return Type:
`:rtype: :class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition>`
### SaveTemplate
#### Description:
Updates an existing build definition template.

* `:param :class:<BuildDefinitionTemplate> <azure.devops.v5_1.build.models.BuildDefinitionTemplate> template: The new version of the template.`
* `:param str project: Project ID or project name`
* `:param str template_id: The ID of the template.`
#### Example usage:
```
from azure.devops.v5_1.build.models import BuildDefinitionTemplate

connection.clients.get_cloud_load_test_client().save_template(template, project, template_id)
```


#### Return Type:
`:rtype: :class:<BuildDefinitionTemplate> <azure.devops.v5_1.build.models.BuildDefinitionTemplate>`
### UpdateBuild
#### Description:
Updates a build.

* `:param :class:<Build> <azure.devops.v5_1.build.models.Build> build: The build.`
* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param bool retry:`
#### Example usage:
```
from azure.devops.v5_1.build.models import Build

connection.clients.get_cloud_load_test_client().update_build(build, project, build_id, retry=None)
```


#### Return Type:
`:rtype: :class:<Build> <azure.devops.v5_1.build.models.Build>`
### UpdateBuildSettings
#### Description:
Updates the build settings.

* `:param :class:<BuildSettings> <azure.devops.v5_1.build.models.BuildSettings> settings: The new settings.`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.build.models import BuildSettings

connection.clients.get_cloud_load_test_client().update_build_settings(settings, project=None)
```


#### Return Type:
`:rtype: :class:<BuildSettings> <azure.devops.v5_1.build.models.BuildSettings>`
### UpdateBuilds
#### Description:
Updates multiple builds.

* `:param [Build] builds: The builds to update.`
* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_cloud_load_test_client().update_builds(builds, project)
```


#### Return Type:
`:rtype: [Build]`
### UpdateDefinition
#### Description:
Updates an existing definition.

* `:param :class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition> definition: The new version of the definition.`
* `:param str project: Project ID or project name`
* `:param int definition_id: The ID of the definition.`
* `:param int secrets_source_definition_id:`
* `:param int secrets_source_definition_revision:`
#### Example usage:
```
from azure.devops.v5_1.build.models import BuildDefinition

connection.clients.get_cloud_load_test_client().update_definition(definition, project, definition_id, secrets_source_definition_id=None, secrets_source_definition_revision=None)
```


#### Return Type:
`:rtype: :class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition>`
## Get Core Client
### CreateTeam
#### Description:
Create a team in a team project.

* `:param :class:<WebApiTeam> <azure.devops.v5_1.core.models.WebApiTeam> team: The team data used to create the team.`
* `:param str project_id: The name or ID (GUID) of the team project in which to create the team.`
#### Example usage:
```
from azure.devops.v5_1.core.models import WebApiTeam

connection.clients.get_core_client().create_team(team, project_id)
```


#### Return Type:
`:rtype: :class:<WebApiTeam> <azure.devops.v5_1.core.models.WebApiTeam>`
### DeleteTeam
#### Description:
Delete a team.

* `:param str project_id: The name or ID (GUID) of the team project containing the team to delete.`
* `:param str team_id: The name or ID of the team to delete.`
#### Example usage:
```
connection.clients.get_core_client().delete_team(project_id, team_id)
```


#### Return Type:
`:rtype: :class:<WebApiTeam> <azure.devops.v5_1.core.models.WebApiTeam>`
### GetProcessById
#### Description:
Get a process by ID.

* `:param str process_id: ID for a process.`
#### Example usage:
```
connection.clients.get_core_client().get_process_by_id(process_id)
```


#### Return Type:
`:rtype: :class:<Process> <azure.devops.v5_1.core.models.Process>`
### GetProcesses
#### Description:
Get a list of processes.

#### Example usage:
```
connection.clients.get_core_client().get_processes()
```


#### Return Type:
`:rtype: [Process]`
### GetProject
#### Description:
Get project with the specified id or name, optionally including capabilities.

* `:param str project_id:`
* `:param bool include_capabilities: Include capabilities (such as source control) in the team project result (default: false).`
* `:param bool include_history: Search within renamed projects (that had such name in the past).`
#### Example usage:
```
connection.clients.get_core_client().get_project(project_id, include_capabilities=None, include_history=None)
```


#### Return Type:
`:rtype: :class:<TeamProject> <azure.devops.v5_1.core.models.TeamProject>`
### GetProjectCollection
#### Description:
Get project collection with the specified id or name.

* `:param str collection_id:`
#### Example usage:
```
connection.clients.get_core_client().get_project_collection(collection_id)
```


#### Return Type:
`:rtype: :class:<TeamProjectCollection> <azure.devops.v5_1.core.models.TeamProjectCollection>`
### GetProjectCollections
#### Description:
Get project collection references for this application.

* `:param int top:`
* `:param int skip:`
#### Example usage:
```
connection.clients.get_core_client().get_project_collections(top=None, skip=None)
```


#### Return Type:
`:rtype: [TeamProjectCollectionReference]`
### GetProjects
#### Description:
Get all projects in the organization that the authenticated user has access to.

* `:param str state_filter: Filter on team projects in a specific team project state (default: WellFormed).`
* `:param int top:`
* `:param int skip:`
* `:param str continuation_token:`
* `:param bool get_default_team_image_url:`
#### Example usage:
```
connection.clients.get_core_client().get_projects(state_filter=None, top=None, skip=None, continuation_token=None, get_default_team_image_url=None)
```


#### Return Type:
`:rtype: :class:<GetProjectsResponseValue>`
### GetTeam
#### Description:
Get a specific team.

* `:param str project_id: The name or ID (GUID) of the team project containing the team.`
* `:param str team_id: The name or ID (GUID) of the team.`
* `:param bool expand_identity: A value indicating whether or not to expand Identity information in the result WebApiTeam object.`
#### Example usage:
```
connection.clients.get_core_client().get_team(project_id, team_id, expand_identity=None)
```


#### Return Type:
`:rtype: :class:<WebApiTeam> <azure.devops.v5_1.core.models.WebApiTeam>`
### GetTeamMembersWithExtendedProperties
#### Description:
Get a list of members for a specific team.

* `:param str project_id: The name or ID (GUID) of the team project the team belongs to.`
* `:param str team_id: The name or ID (GUID) of the team .`
* `:param int top:`
* `:param int skip:`
#### Example usage:
```
connection.clients.get_core_client().get_team_members_with_extended_properties(project_id, team_id, top=None, skip=None)
```


#### Return Type:
`:rtype: [TeamMember]`
### GetTeams
#### Description:
Get a list of teams.

* `:param str project_id:`
* `:param bool mine: If true return all the teams requesting user is member, otherwise return all the teams user has read access.`
* `:param int top: Maximum number of teams to return.`
* `:param int skip: Number of teams to skip.`
* `:param bool expand_identity: A value indicating whether or not to expand Identity information in the result WebApiTeam object.`
#### Example usage:
```
connection.clients.get_core_client().get_teams(project_id, mine=None, top=None, skip=None, expand_identity=None)
```


#### Return Type:
`:rtype: [WebApiTeam]`
### QueueCreateProject
#### Description:
Queues a project to be created. Use the [GetOperation](../../operations/operations/get) to periodically check for create project status.

* `:param :class:<TeamProject> <azure.devops.v5_1.core.models.TeamProject> project_to_create: The project to create.`
#### Example usage:
```
from azure.devops.v5_1.core.models import TeamProject

connection.clients.get_core_client().queue_create_project(project_to_create)
```


#### Return Type:
`:rtype: :class:<OperationReference> <azure.devops.v5_1.core.models.OperationReference>`
### QueueDeleteProject
#### Description:
Queues a project to be deleted. Use the [GetOperation](../../operations/operations/get) to periodically check for delete project status.

* `:param str project_id: The project id of the project to delete.`
#### Example usage:
```
connection.clients.get_core_client().queue_delete_project(project_id)
```


#### Return Type:
`:rtype: :class:<OperationReference> <azure.devops.v5_1.core.models.OperationReference>`
### UpdateProject
#### Description:
Update an existing project's name, abbreviation, description, or restore a project.

* `:param :class:<TeamProject> <azure.devops.v5_1.core.models.TeamProject> project_update: The updates for the project. The state must be set to wellFormed to restore the project.`
* `:param str project_id: The project id of the project to update.`
#### Example usage:
```
from azure.devops.v5_1.core.models import TeamProject

connection.clients.get_core_client().update_project(project_update, project_id)
```


#### Return Type:
`:rtype: :class:<OperationReference> <azure.devops.v5_1.core.models.OperationReference>`
### UpdateTeam
#### Description:
Update a team's name and/or description.

* `:param :class:<WebApiTeam> <azure.devops.v5_1.core.models.WebApiTeam> team_data:`
* `:param str project_id: The name or ID (GUID) of the team project containing the team to update.`
* `:param str team_id: The name of ID of the team to update.`
#### Example usage:
```
from azure.devops.v5_1.core.models import WebApiTeam

connection.clients.get_core_client().update_team(team_data, project_id, team_id)
```


#### Return Type:
`:rtype: :class:<WebApiTeam> <azure.devops.v5_1.core.models.WebApiTeam>`
## Get Git Client
### CreateComment
#### Description:
Create a comment on a specific thread in a pull request (up to 500 comments can be created per thread).

* `:param :class:<Comment> <azure.devops.v5_1.git.models.Comment> comment: The comment to create. Comments can be up to 150,000 characters.`
* `:param str repository_id: The repository ID of the pull request's target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param int thread_id: ID of the thread that the desired comment is in.`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.git.models import Comment

connection.clients.get_git_client().create_comment(comment, repository_id, pull_request_id, thread_id, project=None)
```


#### Return Type:
`:rtype: :class:<Comment> <azure.devops.v5_1.git.models.Comment>`
### CreateCommitStatus
#### Description:
Create Git commit status.

* `:param :class:<GitStatus> <azure.devops.v5_1.git.models.GitStatus> git_commit_status_to_create: Git commit status object to create.`
* `:param str commit_id: ID of the Git commit.`
* `:param str repository_id: ID of the repository.`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.git.models import GitStatus

connection.clients.get_git_client().create_commit_status(git_commit_status_to_create, commit_id, repository_id, project=None)
```


#### Return Type:
`:rtype: :class:<GitStatus> <azure.devops.v5_1.git.models.GitStatus>`
### CreatePullRequest
#### Description:
Create a pull request.

* `:param :class:<GitPullRequest> <azure.devops.v5_1.git.models.GitPullRequest> git_pull_request_to_create: The pull request to create.`
* `:param str repository_id: The repository ID of the pull request's target branch.`
* `:param str project: Project ID or project name`
* `:param bool supports_iterations: If true, subsequent pushes to the pull request will be individually reviewable. Set this to false for large pull requests for performance reasons if this functionality is not needed.`
#### Example usage:
```
from azure.devops.v5_1.git.models import GitPullRequest

connection.clients.get_git_client().create_pull_request(git_pull_request_to_create, repository_id, project=None, supports_iterations=None)
```


#### Return Type:
`:rtype: :class:<GitPullRequest> <azure.devops.v5_1.git.models.GitPullRequest>`
### CreatePullRequestReviewer
#### Description:
Add a reviewer to a pull request or cast a vote.

* `:param :class:<IdentityRefWithVote> <azure.devops.v5_1.git.models.IdentityRefWithVote> reviewer: Reviewer's vote.<br />If the reviewer's ID is included here, it must match the reviewerID parameter.<br />Reviewers can set their own vote with this method.  When adding other reviewers, vote must be set to zero.`
* `:param str repository_id: The repository ID of the pull request’s target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param str reviewer_id: ID of the reviewer.`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.git.models>` reviewer: Reviewer's vote.<br />If the reviewer's ID is included here, it must match the reviewerID parameter.<br / import IdentityRefWithVote

connection.clients.get_git_client().create_pull_request_reviewer(reviewer, repository_id, pull_request_id, reviewer_id, project=None)
```


#### Return Type:
`:rtype: :class:<IdentityRefWithVote> <azure.devops.v5_1.git.models.IdentityRefWithVote>`
### CreatePullRequestReviewers
#### Description:
Add reviewers to a pull request.

* `:param [IdentityRef] reviewers: Reviewers to add to the pull request.`
* `:param str repository_id: The repository ID of the pull request’s target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_git_client().create_pull_request_reviewers(reviewers, repository_id, pull_request_id, project=None)
```


#### Return Type:
`:rtype: [IdentityRefWithVote]`
### CreatePush
#### Description:
Push changes to the repository.

* `:param :class:<GitPush> <azure.devops.v5_1.git.models.GitPush> push:`
* `:param str repository_id: The name or ID of the repository.`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.git.models import GitPush

connection.clients.get_git_client().create_push(push, repository_id, project=None)
```


#### Return Type:
`:rtype: :class:<GitPush> <azure.devops.v5_1.git.models.GitPush>`
### CreateRepository
#### Description:
Create a git repository in a team project.

* `:param :class:<GitRepositoryCreateOptions> <azure.devops.v5_1.git.models.GitRepositoryCreateOptions> git_repository_to_create: Specify the repo name, team project and/or parent repository. Team project information can be omitted from gitRepositoryToCreate if the request is project-scoped (i.e., includes project Id).`
* `:param str project: Project ID or project name`
* `:param str source_ref: [optional] Specify the source refs to use while creating a fork repo`
#### Example usage:
```
from azure.devops.v5_1.git.models import GitRepositoryCreateOptions

connection.clients.get_git_client().create_repository(git_repository_to_create, project=None, source_ref=None)
```


#### Return Type:
`:rtype: :class:<GitRepository> <azure.devops.v5_1.git.models.GitRepository>`
### CreateThread
#### Description:
Create a thread in a pull request.

* `:param :class:<GitPullRequestCommentThread> <azure.devops.v5_1.git.models.GitPullRequestCommentThread> comment_thread: The thread to create. Thread must contain at least one comment.`
* `:param str repository_id: Repository ID of the pull request's target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.git.models import GitPullRequestCommentThread

connection.clients.get_git_client().create_thread(comment_thread, repository_id, pull_request_id, project=None)
```


#### Return Type:
`:rtype: :class:<GitPullRequestCommentThread> <azure.devops.v5_1.git.models.GitPullRequestCommentThread>`
### DeleteComment
#### Description:
Delete a comment associated with a specific thread in a pull request.

* `:param str repository_id: The repository ID of the pull request's target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param int thread_id: ID of the thread that the desired comment is in.`
* `:param int comment_id: ID of the comment.`
* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_git_client().delete_comment(repository_id, pull_request_id, thread_id, comment_id, project=None)
```


#### Return Type:
`:rtype: :class:<GitPullRequestCommentThread> <azure.devops.v5_1.git.models.GitPullRequestCommentThread>`
### DeletePullRequestReviewer
#### Description:
Remove a reviewer from a pull request.

* `:param str repository_id: The repository ID of the pull request’s target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param str reviewer_id: ID of the reviewer to remove.`
* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_git_client().delete_pull_request_reviewer(repository_id, pull_request_id, reviewer_id, project=None)
```


#### Return Type:
`:rtype: :class:<GitPullRequestCommentThread> <azure.devops.v5_1.git.models.GitPullRequestCommentThread>`
### DeleteRepository
#### Description:
Delete a git repository

* `:param str repository_id: The name or ID of the repository.`
* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_git_client().delete_repository(repository_id, project=None)
```


#### Return Type:
`:rtype: :class:<GitPullRequestCommentThread> <azure.devops.v5_1.git.models.GitPullRequestCommentThread>`
### GetBlob
#### Description:
Get a single blob.

* `:param str repository_id: The name or ID of the repository.`
* `:param str sha1: SHA1 hash of the file. You can get the SHA1 of a file using the "Git/Items/Get Item" endpoint.`
* `:param str project: Project ID or project name`
* `:param bool download: If true, prompt for a download rather than rendering in a browser. Note: this value defaults to true if $format is zip`
* `:param str file_name: Provide a fileName to use for a download.`
* `:param bool resolve_lfs: If true, try to resolve a blob to its LFS contents, if it's an LFS pointer file. Only compatible with octet-stream Accept headers or $format types`
#### Example usage:
```
connection.clients.get_git_client().get_blob(repository_id, sha1, project=None, download=None, file_name=None, resolve_lfs=None)
```


#### Return Type:
`:rtype: :class:<GitBlobRef> <azure.devops.v5_1.git.models.GitBlobRef>`
### GetBlobContent
#### Description:
Get a single blob.

* `:param str repository_id: The name or ID of the repository.`
* `:param str sha1: SHA1 hash of the file. You can get the SHA1 of a file using the "Git/Items/Get Item" endpoint.`
* `:param str project: Project ID or project name`
* `:param bool download: If true, prompt for a download rather than rendering in a browser. Note: this value defaults to true if $format is zip`
* `:param str file_name: Provide a fileName to use for a download.`
* `:param bool resolve_lfs: If true, try to resolve a blob to its LFS contents, if it's an LFS pointer file. Only compatible with octet-stream Accept headers or $format types`
#### Example usage:
```
connection.clients.get_git_client().get_blob_content(repository_id, sha1, project=None, download=None, file_name=None, resolve_lfs=None, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetBlobZip
#### Description:
Get a single blob.

* `:param str repository_id: The name or ID of the repository.`
* `:param str sha1: SHA1 hash of the file. You can get the SHA1 of a file using the "Git/Items/Get Item" endpoint.`
* `:param str project: Project ID or project name`
* `:param bool download: If true, prompt for a download rather than rendering in a browser. Note: this value defaults to true if $format is zip`
* `:param str file_name: Provide a fileName to use for a download.`
* `:param bool resolve_lfs: If true, try to resolve a blob to its LFS contents, if it's an LFS pointer file. Only compatible with octet-stream Accept headers or $format types`
#### Example usage:
```
connection.clients.get_git_client().get_blob_zip(repository_id, sha1, project=None, download=None, file_name=None, resolve_lfs=None, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetBlobsZip
#### Description:
Gets one or more blobs in a zip file download.

* `:param [str] blob_ids: Blob IDs (SHA1 hashes) to be returned in the zip file.`
* `:param str repository_id: The name or ID of the repository.`
* `:param str project: Project ID or project name`
* `:param str filename:`
#### Example usage:
```
connection.clients.get_git_client().get_blobs_zip(blob_ids, repository_id, project=None, filename=None, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetBranch
#### Description:
Retrieve statistics about a single branch.

* `:param str repository_id: The name or ID of the repository.`
* `:param str name: Name of the branch.`
* `:param str project: Project ID or project name`
* `:param :class:<GitVersionDescriptor> <azure.devops.v5_1.git.models.GitVersionDescriptor> base_version_descriptor: Identifies the commit or branch to use as the base.`
#### Example usage:
```
from azure.devops.v5_1.git.models import GitVersionDescriptor

connection.clients.get_git_client().get_branch(repository_id, name, project=None, base_version_descriptor=None)
```


#### Return Type:
`:rtype: :class:<GitBranchStats> <azure.devops.v5_1.git.models.GitBranchStats>`
### GetBranches
#### Description:
Retrieve statistics about all branches within a repository.

* `:param str repository_id: The name or ID of the repository.`
* `:param str project: Project ID or project name`
* `:param :class:<GitVersionDescriptor> <azure.devops.v5_1.git.models.GitVersionDescriptor> base_version_descriptor: Identifies the commit or branch to use as the base.`
#### Example usage:
```
from azure.devops.v5_1.git.models import GitVersionDescriptor

connection.clients.get_git_client().get_branches(repository_id, project=None, base_version_descriptor=None)
```


#### Return Type:
`:rtype: [GitBranchStats]`
### GetChanges
#### Description:
Retrieve changes for a particular commit.

* `:param str commit_id: The id of the commit.`
* `:param str repository_id: The id or friendly name of the repository. To use the friendly name, projectId must also be specified.`
* `:param str project: Project ID or project name`
* `:param int top: The maximum number of changes to return.`
* `:param int skip: The number of changes to skip.`
#### Example usage:
```
connection.clients.get_git_client().get_changes(commit_id, repository_id, project=None, top=None, skip=None)
```


#### Return Type:
`:rtype: :class:<GitCommitChanges> <azure.devops.v5_1.git.models.GitCommitChanges>`
### GetComment
#### Description:
Retrieve a comment associated with a specific thread in a pull request.

* `:param str repository_id: The repository ID of the pull request's target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param int thread_id: ID of the thread that the desired comment is in.`
* `:param int comment_id: ID of the comment.`
* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_git_client().get_comment(repository_id, pull_request_id, thread_id, comment_id, project=None)
```


#### Return Type:
`:rtype: :class:<Comment> <azure.devops.v5_1.git.models.Comment>`
### GetComments
#### Description:
Retrieve all comments associated with a specific thread in a pull request.

* `:param str repository_id: The repository ID of the pull request's target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param int thread_id: ID of the thread.`
* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_git_client().get_comments(repository_id, pull_request_id, thread_id, project=None)
```


#### Return Type:
`:rtype: [Comment]`
### GetCommit
#### Description:
Retrieve a particular commit.

* `:param str commit_id: The id of the commit.`
* `:param str repository_id: The id or friendly name of the repository. To use the friendly name, projectId must also be specified.`
* `:param str project: Project ID or project name`
* `:param int change_count: The number of changes to include in the result.`
#### Example usage:
```
connection.clients.get_git_client().get_commit(commit_id, repository_id, project=None, change_count=None)
```


#### Return Type:
`:rtype: :class:<GitCommit> <azure.devops.v5_1.git.models.GitCommit>`
### GetCommitDiffs
#### Description:
Find the closest common commit (the merge base) between base and target commits, and get the diff between either the base and target commits or common and target commits.

* `:param str repository_id: The name or ID of the repository.`
* `:param str project: Project ID or project name`
* `:param bool diff_common_commit: If true, diff between common and target commits. If false, diff between base and target commits.`
* `:param int top: Maximum number of changes to return. Defaults to 100.`
* `:param int skip: Number of changes to skip`
* `:param :class:<GitBaseVersionDescriptor> <azure.devops.v5_1.git.models.GitBaseVersionDescriptor> base_version_descriptor: Descriptor for base commit.`
* `:param :class:<GitTargetVersionDescriptor> <azure.devops.v5_1.git.models.GitTargetVersionDescriptor> target_version_descriptor: Descriptor for target commit.`
#### Example usage:
```
from azure.devops.v5_1.git.models import GitBaseVersionDescriptor
from azure.devops.v5_1.git.models import GitTargetVersionDescriptor

connection.clients.get_git_client().get_commit_diffs(repository_id, project=None, diff_common_commit=None, top=None, skip=None, base_version_descriptor=None, target_version_descriptor=None)
```


#### Return Type:
`:rtype: :class:<GitCommitDiffs> <azure.devops.v5_1.git.models.GitCommitDiffs>`
### GetCommits
#### Description:
Retrieve git commits for a project

* `:param str repository_id: The id or friendly name of the repository. To use the friendly name, projectId must also be specified.`
* `:param :class:<GitQueryCommitsCriteria> <azure.devops.v5_1.git.models.GitQueryCommitsCriteria> search_criteria:`
* `:param str project: Project ID or project name`
* `:param int skip:`
* `:param int top:`
#### Example usage:
```
from azure.devops.v5_1.git.models import GitQueryCommitsCriteria

connection.clients.get_git_client().get_commits(repository_id, search_criteria, project=None, skip=None, top=None)
```


#### Return Type:
`:rtype: [GitCommitRef]`
### GetCommitsBatch
#### Description:
Retrieve git commits for a project matching the search criteria

* `:param :class:<GitQueryCommitsCriteria> <azure.devops.v5_1.git.models.GitQueryCommitsCriteria> search_criteria: Search options`
* `:param str repository_id: The name or ID of the repository.`
* `:param str project: Project ID or project name`
* `:param int skip: Number of commits to skip.`
* `:param int top: Maximum number of commits to return.`
* `:param bool include_statuses: True to include additional commit status information.`
#### Example usage:
```
from azure.devops.v5_1.git.models import GitQueryCommitsCriteria

connection.clients.get_git_client().get_commits_batch(search_criteria, repository_id, project=None, skip=None, top=None, include_statuses=None)
```


#### Return Type:
`:rtype: [GitCommitRef]`
### GetItem
#### Description:
Get Item Metadata and/or Content for a single item. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content, which is always returned as a download.

* `:param str repository_id: The name or ID of the repository.`
* `:param str path: The item path.`
* `:param str project: Project ID or project name`
* `:param str scope_path: The path scope.  The default is null.`
* `:param str recursion_level: The recursion level of this request. The default is 'none', no recursion.`
* `:param bool include_content_metadata: Set to true to include content metadata.  Default is false.`
* `:param bool latest_processed_change: Set to true to include the latest changes.  Default is false.`
* `:param bool download: Set to true to download the response as a file.  Default is false.`
* `:param :class:<GitVersionDescriptor> <azure.devops.v5_1.git.models.GitVersionDescriptor> version_descriptor: Version descriptor.  Default is the default branch for the repository.`
* `:param bool include_content: Set to true to include item content when requesting json.  Default is false.`
* `:param bool resolve_lfs: Set to true to resolve Git LFS pointer files to return actual content from Git LFS.  Default is false.`
#### Example usage:
```
from azure.devops.v5_1.git.models import GitVersionDescriptor

connection.clients.get_git_client().get_item(repository_id, path, project=None, scope_path=None, recursion_level=None, include_content_metadata=None, latest_processed_change=None, download=None, version_descriptor=None, include_content=None, resolve_lfs=None)
```


#### Return Type:
`:rtype: :class:<GitItem> <azure.devops.v5_1.git.models.GitItem>`
### GetItemContent
#### Description:
Get Item Metadata and/or Content for a single item. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content, which is always returned as a download.

* `:param str repository_id: The name or ID of the repository.`
* `:param str path: The item path.`
* `:param str project: Project ID or project name`
* `:param str scope_path: The path scope.  The default is null.`
* `:param str recursion_level: The recursion level of this request. The default is 'none', no recursion.`
* `:param bool include_content_metadata: Set to true to include content metadata.  Default is false.`
* `:param bool latest_processed_change: Set to true to include the latest changes.  Default is false.`
* `:param bool download: Set to true to download the response as a file.  Default is false.`
* `:param :class:<GitVersionDescriptor> <azure.devops.v5_1.git.models.GitVersionDescriptor> version_descriptor: Version descriptor.  Default is the default branch for the repository.`
* `:param bool include_content: Set to true to include item content when requesting json.  Default is false.`
* `:param bool resolve_lfs: Set to true to resolve Git LFS pointer files to return actual content from Git LFS.  Default is false.`
#### Example usage:
```
from azure.devops.v5_1.git.models import GitVersionDescriptor

connection.clients.get_git_client().get_item_content(repository_id, path, project=None, scope_path=None, recursion_level=None, include_content_metadata=None, latest_processed_change=None, download=None, version_descriptor=None, include_content=None, resolve_lfs=None, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetItemText
#### Description:
Get Item Metadata and/or Content for a single item. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content, which is always returned as a download.

* `:param str repository_id: The name or ID of the repository.`
* `:param str path: The item path.`
* `:param str project: Project ID or project name`
* `:param str scope_path: The path scope.  The default is null.`
* `:param str recursion_level: The recursion level of this request. The default is 'none', no recursion.`
* `:param bool include_content_metadata: Set to true to include content metadata.  Default is false.`
* `:param bool latest_processed_change: Set to true to include the latest changes.  Default is false.`
* `:param bool download: Set to true to download the response as a file.  Default is false.`
* `:param :class:<GitVersionDescriptor> <azure.devops.v5_1.git.models.GitVersionDescriptor> version_descriptor: Version descriptor.  Default is the default branch for the repository.`
* `:param bool include_content: Set to true to include item content when requesting json.  Default is false.`
* `:param bool resolve_lfs: Set to true to resolve Git LFS pointer files to return actual content from Git LFS.  Default is false.`
#### Example usage:
```
from azure.devops.v5_1.git.models import GitVersionDescriptor

connection.clients.get_git_client().get_item_text(repository_id, path, project=None, scope_path=None, recursion_level=None, include_content_metadata=None, latest_processed_change=None, download=None, version_descriptor=None, include_content=None, resolve_lfs=None, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetItemZip
#### Description:
Get Item Metadata and/or Content for a single item. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content, which is always returned as a download.

* `:param str repository_id: The name or ID of the repository.`
* `:param str path: The item path.`
* `:param str project: Project ID or project name`
* `:param str scope_path: The path scope.  The default is null.`
* `:param str recursion_level: The recursion level of this request. The default is 'none', no recursion.`
* `:param bool include_content_metadata: Set to true to include content metadata.  Default is false.`
* `:param bool latest_processed_change: Set to true to include the latest changes.  Default is false.`
* `:param bool download: Set to true to download the response as a file.  Default is false.`
* `:param :class:<GitVersionDescriptor> <azure.devops.v5_1.git.models.GitVersionDescriptor> version_descriptor: Version descriptor.  Default is the default branch for the repository.`
* `:param bool include_content: Set to true to include item content when requesting json.  Default is false.`
* `:param bool resolve_lfs: Set to true to resolve Git LFS pointer files to return actual content from Git LFS.  Default is false.`
#### Example usage:
```
from azure.devops.v5_1.git.models import GitVersionDescriptor

connection.clients.get_git_client().get_item_zip(repository_id, path, project=None, scope_path=None, recursion_level=None, include_content_metadata=None, latest_processed_change=None, download=None, version_descriptor=None, include_content=None, resolve_lfs=None, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetItems
#### Description:
Get Item Metadata and/or Content for a collection of items. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content which is always returned as a download.

* `:param str repository_id: The name or ID of the repository.`
* `:param str project: Project ID or project name`
* `:param str scope_path: The path scope.  The default is null.`
* `:param str recursion_level: The recursion level of this request. The default is 'none', no recursion.`
* `:param bool include_content_metadata: Set to true to include content metadata.  Default is false.`
* `:param bool latest_processed_change: Set to true to include the latest changes.  Default is false.`
* `:param bool download: Set to true to download the response as a file.  Default is false.`
* `:param bool include_links: Set to true to include links to items.  Default is false.`
* `:param :class:<GitVersionDescriptor> <azure.devops.v5_1.git.models.GitVersionDescriptor> version_descriptor: Version descriptor.  Default is the default branch for the repository.`
#### Example usage:
```
from azure.devops.v5_1.git.models import GitVersionDescriptor

connection.clients.get_git_client().get_items(repository_id, project=None, scope_path=None, recursion_level=None, include_content_metadata=None, latest_processed_change=None, download=None, include_links=None, version_descriptor=None)
```


#### Return Type:
`:rtype: [GitItem]`
### GetItemsBatch
#### Description:
Post for retrieving a creating a batch out of a set of items in a repo / project given a list of paths or a long path

* `:param :class:<GitItemRequestData> <azure.devops.v5_1.git.models.GitItemRequestData> request_data: Request data attributes: ItemDescriptors, IncludeContentMetadata, LatestProcessedChange, IncludeLinks. ItemDescriptors: Collection of items to fetch, including path, version, and recursion level. IncludeContentMetadata: Whether to include metadata for all items LatestProcessedChange: Whether to include shallow ref to commit that last changed each item. IncludeLinks: Whether to include the _links field on the shallow references.`
* `:param str repository_id: The name or ID of the repository`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.git.models import GitItemRequestData

connection.clients.get_git_client().get_items_batch(request_data, repository_id, project=None)
```


#### Return Type:
`:rtype: [[GitItem]]`
### GetPullRequest
#### Description:
Retrieve a pull request.

* `:param str repository_id: The repository ID of the pull request's target branch.`
* `:param int pull_request_id: The ID of the pull request to retrieve.`
* `:param str project: Project ID or project name`
* `:param int max_comment_length: Not used.`
* `:param int skip: Not used.`
* `:param int top: Not used.`
* `:param bool include_commits: If true, the pull request will be returned with the associated commits.`
* `:param bool include_work_item_refs: If true, the pull request will be returned with the associated work item references.`
#### Example usage:
```
connection.clients.get_git_client().get_pull_request(repository_id, pull_request_id, project=None, max_comment_length=None, skip=None, top=None, include_commits=None, include_work_item_refs=None)
```


#### Return Type:
`:rtype: :class:<GitPullRequest> <azure.devops.v5_1.git.models.GitPullRequest>`
### GetPullRequestById
#### Description:
Retrieve a pull request.

* `:param int pull_request_id: The ID of the pull request to retrieve.`
* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_git_client().get_pull_request_by_id(pull_request_id, project=None)
```


#### Return Type:
`:rtype: :class:<GitPullRequest> <azure.devops.v5_1.git.models.GitPullRequest>`
### GetPullRequestCommits
#### Description:
Get the commits for the specified pull request.

* `:param str repository_id: ID or name of the repository.`
* `:param int pull_request_id: ID of the pull request.`
* `:param str project: Project ID or project name`
* `:param int top: Maximum number of commits to return.`
* `:param str continuation_token: The continuation token used for pagination.`
#### Example usage:
```
connection.clients.get_git_client().get_pull_request_commits(repository_id, pull_request_id, project=None, top=None, continuation_token=None)
```


#### Return Type:
`:rtype: :class:<GetPullRequestCommitsResponseValue>`
### GetPullRequestIteration
#### Description:
Get the specified iteration for a pull request.

* `:param str repository_id: ID or name of the repository.`
* `:param int pull_request_id: ID of the pull request.`
* `:param int iteration_id: ID of the pull request iteration to return.`
* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_git_client().get_pull_request_iteration(repository_id, pull_request_id, iteration_id, project=None)
```


#### Return Type:
`:rtype: :class:<GitPullRequestIteration> <azure.devops.v5_1.git.models.GitPullRequestIteration>`
### GetPullRequestIterationChanges
#### Description:
Retrieve the changes made in a pull request between two iterations.

* `:param str repository_id: The repository ID of the pull request's target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param int iteration_id: ID of the pull request iteration. <br /> Iteration IDs are zero-based with zero indicating the common commit between the source and target branches. Iteration one is the head of the source branch at the time the pull request is created and subsequent iterations are created when there are pushes to the source branch.`
* `:param str project: Project ID or project name`
* `:param int top: Optional. The number of changes to retrieve.  The default value is 100 and the maximum value is 2000.`
* `:param int skip: Optional. The number of changes to ignore.  For example, to retrieve changes 101-150, set top 50 and skip to 100.`
* `:param int compare_to: ID of the pull request iteration to compare against.  The default value is zero which indicates the comparison is made against the common commit between the source and target branches`
#### Example usage:
```
connection.clients.get_git_client().get_pull_request_iteration_changes(repository_id, pull_request_id, iteration_id, project=None, top=None, skip=None, compare_to=None)
```


#### Return Type:
`:rtype: :class:<GitPullRequestIterationChanges> <azure.devops.v5_1.git.models.GitPullRequestIterationChanges>`
### GetPullRequestIterationCommits
#### Description:
Get the commits for the specified iteration of a pull request.

* `:param str repository_id: ID or name of the repository.`
* `:param int pull_request_id: ID of the pull request.`
* `:param int iteration_id: ID of the iteration from which to get the commits.`
* `:param str project: Project ID or project name`
* `:param int top: Maximum number of commits to return. The maximum number of commits that can be returned per batch is 500.`
* `:param int skip: Number of commits to skip.`
#### Example usage:
```
connection.clients.get_git_client().get_pull_request_iteration_commits(repository_id, pull_request_id, iteration_id, project=None, top=None, skip=None)
```


#### Return Type:
`:rtype: [GitCommitRef]`
### GetPullRequestIterations
#### Description:
Get the list of iterations for the specified pull request.

* `:param str repository_id: ID or name of the repository.`
* `:param int pull_request_id: ID of the pull request.`
* `:param str project: Project ID or project name`
* `:param bool include_commits: If true, include the commits associated with each iteration in the response.`
#### Example usage:
```
connection.clients.get_git_client().get_pull_request_iterations(repository_id, pull_request_id, project=None, include_commits=None)
```


#### Return Type:
`:rtype: [GitPullRequestIteration]`
### GetPullRequestQuery
#### Description:
This API is used to find what pull requests are related to a given commit.  It can be used to either find the pull request that created a particular merge commit or it can be used to find all pull requests that have ever merged a particular commit.  The input is a list of queries which each contain a list of commits. For each commit that you search against, you will get back a dictionary of commit -> pull requests.

* `:param :class:<GitPullRequestQuery> <azure.devops.v5_1.git.models.GitPullRequestQuery> queries: The list of queries to perform.`
* `:param str repository_id: ID of the repository.`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.git.models import GitPullRequestQuery

connection.clients.get_git_client().get_pull_request_query(queries, repository_id, project=None)
```


#### Return Type:
`:rtype: :class:<GitPullRequestQuery> <azure.devops.v5_1.git.models.GitPullRequestQuery>`
### GetPullRequestReviewer
#### Description:
Retrieve information about a particular reviewer on a pull request

* `:param str repository_id: The repository ID of the pull request’s target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param str reviewer_id: ID of the reviewer.`
* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_git_client().get_pull_request_reviewer(repository_id, pull_request_id, reviewer_id, project=None)
```


#### Return Type:
`:rtype: :class:<IdentityRefWithVote> <azure.devops.v5_1.git.models.IdentityRefWithVote>`
### GetPullRequestReviewers
#### Description:
Retrieve the reviewers for a pull request

* `:param str repository_id: The repository ID of the pull request’s target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_git_client().get_pull_request_reviewers(repository_id, pull_request_id, project=None)
```


#### Return Type:
`:rtype: [IdentityRefWithVote]`
### GetPullRequestThread
#### Description:
Retrieve a thread in a pull request.

* `:param str repository_id: The repository ID of the pull request's target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param int thread_id: ID of the thread.`
* `:param str project: Project ID or project name`
* `:param int iteration: If specified, thread position will be tracked using this iteration as the right side of the diff.`
* `:param int base_iteration: If specified, thread position will be tracked using this iteration as the left side of the diff.`
#### Example usage:
```
connection.clients.get_git_client().get_pull_request_thread(repository_id, pull_request_id, thread_id, project=None, iteration=None, base_iteration=None)
```


#### Return Type:
`:rtype: :class:<GitPullRequestCommentThread> <azure.devops.v5_1.git.models.GitPullRequestCommentThread>`
### GetPullRequestWorkItemRefs
#### Description:
Retrieve a list of work items associated with a pull request.

* `:param str repository_id: ID or name of the repository.`
* `:param int pull_request_id: ID of the pull request.`
* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_git_client().get_pull_request_work_item_refs(repository_id, pull_request_id, project=None)
```


#### Return Type:
`:rtype: [ResourceRef]`
### GetPullRequests
#### Description:
Retrieve all pull requests matching a specified criteria.

* `:param str repository_id: The repository ID of the pull request's target branch.`
* `:param :class:<GitPullRequestSearchCriteria> <azure.devops.v5_1.git.models.GitPullRequestSearchCriteria> search_criteria: Pull requests will be returned that match this search criteria.`
* `:param str project: Project ID or project name`
* `:param int max_comment_length: Not used.`
* `:param int skip: The number of pull requests to ignore. For example, to retrieve results 101-150, set top to 50 and skip to 100.`
* `:param int top: The number of pull requests to retrieve.`
#### Example usage:
```
from azure.devops.v5_1.git.models import GitPullRequestSearchCriteria

connection.clients.get_git_client().get_pull_requests(repository_id, search_criteria, project=None, max_comment_length=None, skip=None, top=None)
```


#### Return Type:
`:rtype: [GitPullRequest]`
### GetPullRequestsByProject
#### Description:
Retrieve all pull requests matching a specified criteria.

* `:param str project: Project ID or project name`
* `:param :class:<GitPullRequestSearchCriteria> <azure.devops.v5_1.git.models.GitPullRequestSearchCriteria> search_criteria: Pull requests will be returned that match this search criteria.`
* `:param int max_comment_length: Not used.`
* `:param int skip: The number of pull requests to ignore. For example, to retrieve results 101-150, set top to 50 and skip to 100.`
* `:param int top: The number of pull requests to retrieve.`
#### Example usage:
```
from azure.devops.v5_1.git.models import GitPullRequestSearchCriteria

connection.clients.get_git_client().get_pull_requests_by_project(project, search_criteria, max_comment_length=None, skip=None, top=None)
```


#### Return Type:
`:rtype: [GitPullRequest]`
### GetPush
#### Description:
Retrieves a particular push.

* `:param str repository_id: The name or ID of the repository.`
* `:param int push_id: ID of the push.`
* `:param str project: Project ID or project name`
* `:param int include_commits: The number of commits to include in the result.`
* `:param bool include_ref_updates: If true, include the list of refs that were updated by the push.`
#### Example usage:
```
connection.clients.get_git_client().get_push(repository_id, push_id, project=None, include_commits=None, include_ref_updates=None)
```


#### Return Type:
`:rtype: :class:<GitPush> <azure.devops.v5_1.git.models.GitPush>`
### GetPushCommits
#### Description:
Retrieve a list of commits associated with a particular push.

* `:param str repository_id: The id or friendly name of the repository. To use the friendly name, projectId must also be specified.`
* `:param int push_id: The id of the push.`
* `:param str project: Project ID or project name`
* `:param int top: The maximum number of commits to return ("get the top x commits").`
* `:param int skip: The number of commits to skip.`
* `:param bool include_links: Set to false to avoid including REST Url links for resources. Defaults to true.`
#### Example usage:
```
connection.clients.get_git_client().get_push_commits(repository_id, push_id, project=None, top=None, skip=None, include_links=None)
```


#### Return Type:
`:rtype: [GitCommitRef]`
### GetPushes
#### Description:
Retrieves pushes associated with the specified repository.

* `:param str repository_id: The name or ID of the repository.`
* `:param str project: Project ID or project name`
* `:param int skip: Number of pushes to skip.`
* `:param int top: Number of pushes to return.`
* `:param :class:<GitPushSearchCriteria> <azure.devops.v5_1.git.models.GitPushSearchCriteria> search_criteria: Search criteria attributes: fromDate, toDate, pusherId, refName, includeRefUpdates or includeLinks. fromDate: Start date to search from. toDate: End date to search to. pusherId: Identity of the person who submitted the push. refName: Branch name to consider. includeRefUpdates: If true, include the list of refs that were updated by the push. includeLinks: Whether to include the _links field on the shallow references.`
#### Example usage:
```
from azure.devops.v5_1.git.models import GitPushSearchCriteria

connection.clients.get_git_client().get_pushes(repository_id, project=None, skip=None, top=None, search_criteria=None)
```


#### Return Type:
`:rtype: [GitPush]`
### GetRefs
#### Description:
Queries the provided repository for its refs and returns them.

* `:param str repository_id: The name or ID of the repository.`
* `:param str project: Project ID or project name`
* `:param str filter: [optional] A filter to apply to the refs (starts with).`
* `:param bool include_links: [optional] Specifies if referenceLinks should be included in the result. default is false.`
* `:param bool include_statuses: [optional] Includes up to the first 1000 commit statuses for each ref. The default value is false.`
* `:param bool include_my_branches: [optional] Includes only branches that the user owns, the branches the user favorites, and the default branch. The default value is false. Cannot be combined with the filter parameter.`
* `:param bool latest_statuses_only: [optional] True to include only the tip commit status for each ref. This option requires includeStatuses to be true. The default value is false.`
* `:param bool peel_tags: [optional] Annotated tags will populate the PeeledObjectId property. default is false.`
* `:param str filter_contains: [optional] A filter to apply to the refs (contains).`
* `:param int top: [optional] Maximum number of refs to return. It cannot be bigger than 1000. If it is not provided but continuationToken is, top will default to 100.`
* `:param str continuation_token: The continuation token used for pagination.`
#### Example usage:
```
connection.clients.get_git_client().get_refs(repository_id, project=None, filter=None, include_links=None, include_statuses=None, include_my_branches=None, latest_statuses_only=None, peel_tags=None, filter_contains=None, top=None, continuation_token=None)
```


#### Return Type:
`:rtype: :class:<GetRefsResponseValue>`
### GetRepositories
#### Description:
Retrieve git repositories.

* `:param str project: Project ID or project name`
* `:param bool include_links: [optional] True to include reference links. The default value is false.`
* `:param bool include_all_urls: [optional] True to include all remote URLs. The default value is false.`
* `:param bool include_hidden: [optional] True to include hidden repositories. The default value is false.`
#### Example usage:
```
connection.clients.get_git_client().get_repositories(project=None, include_links=None, include_all_urls=None, include_hidden=None)
```


#### Return Type:
`:rtype: [GitRepository]`
### GetRepository
#### Description:
Retrieve a git repository.

* `:param str repository_id: The name or ID of the repository.`
* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_git_client().get_repository(repository_id, project=None)
```


#### Return Type:
`:rtype: :class:<GitRepository> <azure.devops.v5_1.git.models.GitRepository>`
### GetRepositoryWithParent
#### Description:
Retrieve a git repository.

* `:param str repository_id: The name or ID of the repository.`
* `:param bool include_parent: True to include parent repository. Only available in authenticated calls.`
* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_git_client().get_repository_with_parent(repository_id, include_parent, project=None)
```


#### Return Type:
`:rtype: :class:<GitRepository> <azure.devops.v5_1.git.models.GitRepository>`
### GetStatuses
#### Description:
Get statuses associated with the Git commit.

* `:param str commit_id: ID of the Git commit.`
* `:param str repository_id: ID of the repository.`
* `:param str project: Project ID or project name`
* `:param int top: Optional. The number of statuses to retrieve. Default is 1000.`
* `:param int skip: Optional. The number of statuses to ignore. Default is 0. For example, to retrieve results 101-150, set top to 50 and skip to 100.`
* `:param bool latest_only: The flag indicates whether to get only latest statuses grouped by Context.Name and Context.Genre.`
#### Example usage:
```
connection.clients.get_git_client().get_statuses(commit_id, repository_id, project=None, top=None, skip=None, latest_only=None)
```


#### Return Type:
`:rtype: [GitStatus]`
### GetThreads
#### Description:
Retrieve all threads in a pull request.

* `:param str repository_id: The repository ID of the pull request's target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param str project: Project ID or project name`
* `:param int iteration: If specified, thread positions will be tracked using this iteration as the right side of the diff.`
* `:param int base_iteration: If specified, thread positions will be tracked using this iteration as the left side of the diff.`
#### Example usage:
```
connection.clients.get_git_client().get_threads(repository_id, pull_request_id, project=None, iteration=None, base_iteration=None)
```


#### Return Type:
`:rtype: [GitPullRequestCommentThread]`
### GetTree
#### Description:
The Tree endpoint returns the collection of objects underneath the specified tree. Trees are folders in a Git repository.

* `:param str repository_id: Repository Id.`
* `:param str sha1: SHA1 hash of the tree object.`
* `:param str project: Project ID or project name`
* `:param str project_id: Project Id.`
* `:param bool recursive: Search recursively. Include trees underneath this tree. Default is false.`
* `:param str file_name: Name to use if a .zip file is returned. Default is the object ID.`
#### Example usage:
```
connection.clients.get_git_client().get_tree(repository_id, sha1, project=None, project_id=None, recursive=None, file_name=None)
```


#### Return Type:
`:rtype: :class:<GitTreeRef> <azure.devops.v5_1.git.models.GitTreeRef>`
### GetTreeZip
#### Description:
The Tree endpoint returns the collection of objects underneath the specified tree. Trees are folders in a Git repository.

* `:param str repository_id: Repository Id.`
* `:param str sha1: SHA1 hash of the tree object.`
* `:param str project: Project ID or project name`
* `:param str project_id: Project Id.`
* `:param bool recursive: Search recursively. Include trees underneath this tree. Default is false.`
* `:param str file_name: Name to use if a .zip file is returned. Default is the object ID.`
#### Example usage:
```
connection.clients.get_git_client().get_tree_zip(repository_id, sha1, project=None, project_id=None, recursive=None, file_name=None, **kwargs)
```


#### Return Type:
`:rtype: object`
### UpdateComment
#### Description:
Update a comment associated with a specific thread in a pull request.

* `:param :class:<Comment> <azure.devops.v5_1.git.models.Comment> comment: The comment content that should be updated. Comments can be up to 150,000 characters.`
* `:param str repository_id: The repository ID of the pull request's target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param int thread_id: ID of the thread that the desired comment is in.`
* `:param int comment_id: ID of the comment to update.`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.git.models import Comment

connection.clients.get_git_client().update_comment(comment, repository_id, pull_request_id, thread_id, comment_id, project=None)
```


#### Return Type:
`:rtype: :class:<Comment> <azure.devops.v5_1.git.models.Comment>`
### UpdatePullRequest
#### Description:
Update a pull request

* `:param :class:<GitPullRequest> <azure.devops.v5_1.git.models.GitPullRequest> git_pull_request_to_update: The pull request content that should be updated.`
* `:param str repository_id: The repository ID of the pull request's target branch.`
* `:param int pull_request_id: ID of the pull request to update.`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.git.models import GitPullRequest

connection.clients.get_git_client().update_pull_request(git_pull_request_to_update, repository_id, pull_request_id, project=None)
```


#### Return Type:
`:rtype: :class:<GitPullRequest> <azure.devops.v5_1.git.models.GitPullRequest>`
### UpdatePullRequestReviewers
#### Description:
Reset the votes of multiple reviewers on a pull request.  NOTE: This endpoint only supports updating votes, but does not support updating required reviewers (use policy) or display names.

* `:param [IdentityRefWithVote] patch_votes: IDs of the reviewers whose votes will be reset to zero`
* `:param str repository_id: The repository ID of the pull request’s target branch.`
* `:param int pull_request_id: ID of the pull request`
* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_git_client().update_pull_request_reviewers(patch_votes, repository_id, pull_request_id, project=None)
```


#### Return Type:
`:rtype: :class:<GitPullRequest> <azure.devops.v5_1.git.models.GitPullRequest>`
### UpdateRef
#### Description:
Lock or Unlock a branch.

* `:param :class:<GitRefUpdate> <azure.devops.v5_1.git.models.GitRefUpdate> new_ref_info: The ref update action (lock/unlock) to perform`
* `:param str repository_id: The name or ID of the repository.`
* `:param str filter: The name of the branch to lock/unlock`
* `:param str project: Project ID or project name`
* `:param str project_id: ID or name of the team project. Optional if specifying an ID for repository.`
#### Example usage:
```
from azure.devops.v5_1.git.models import GitRefUpdate

connection.clients.get_git_client().update_ref(new_ref_info, repository_id, filter, project=None, project_id=None)
```


#### Return Type:
`:rtype: :class:<GitRef> <azure.devops.v5_1.git.models.GitRef>`
### UpdateRefs
#### Description:
Creating, updating, or deleting refs(branches).

* `:param [GitRefUpdate] ref_updates: List of ref updates to attempt to perform`
* `:param str repository_id: The name or ID of the repository.`
* `:param str project: Project ID or project name`
* `:param str project_id: ID or name of the team project. Optional if specifying an ID for repository.`
#### Example usage:
```
connection.clients.get_git_client().update_refs(ref_updates, repository_id, project=None, project_id=None)
```


#### Return Type:
`:rtype: [GitRefUpdateResult]`
### UpdateRepository
#### Description:
Updates the Git repository with either a new repo name or a new default branch.

* `:param :class:<GitRepository> <azure.devops.v5_1.git.models.GitRepository> new_repository_info: Specify a new repo name or a new default branch of the repository`
* `:param str repository_id: The name or ID of the repository.`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.git.models import GitRepository

connection.clients.get_git_client().update_repository(new_repository_info, repository_id, project=None)
```


#### Return Type:
`:rtype: :class:<GitRepository> <azure.devops.v5_1.git.models.GitRepository>`
### UpdateThread
#### Description:
Update a thread in a pull request.

* `:param :class:<GitPullRequestCommentThread> <azure.devops.v5_1.git.models.GitPullRequestCommentThread> comment_thread: The thread content that should be updated.`
* `:param str repository_id: The repository ID of the pull request's target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param int thread_id: ID of the thread to update.`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.git.models import GitPullRequestCommentThread

connection.clients.get_git_client().update_thread(comment_thread, repository_id, pull_request_id, thread_id, project=None)
```


#### Return Type:
`:rtype: :class:<GitPullRequestCommentThread> <azure.devops.v5_1.git.models.GitPullRequestCommentThread>`
## Get Identity Client
### CreateGroups
#### Description:
* `:param :class:<object> <azure.devops.v5_1.identity.models.object> container:`
#### Example usage:
```
from azure.devops.v5_1.identity.models import object

connection.clients.get_identity_client().create_groups(container)
```


#### Return Type:
`:rtype: [Identity]`
### CreateIdentity
#### Description:
* `:param :class:<FrameworkIdentityInfo> <azure.devops.v5_1.identity.models.FrameworkIdentityInfo> framework_identity_info:`
#### Example usage:
```
from azure.devops.v5_1.identity.models import FrameworkIdentityInfo

connection.clients.get_identity_client().create_identity(framework_identity_info)
```


#### Return Type:
`:rtype: :class:<Identity> <azure.devops.v5_1.identity.models.Identity>`
### DeleteGroup
#### Description:
* `:param str group_id:`
#### Example usage:
```
connection.clients.get_identity_client().delete_group(group_id)
```


#### Return Type:
`:rtype: :class:<Identity> <azure.devops.v5_1.identity.models.Identity>`
### GetIdentityChanges
#### Description:
* `:param int identity_sequence_id:`
* `:param int group_sequence_id:`
* `:param int organization_identity_sequence_id:`
* `:param int page_size:`
* `:param str scope_id:`
#### Example usage:
```
connection.clients.get_identity_client().get_identity_changes(identity_sequence_id, group_sequence_id, organization_identity_sequence_id=None, page_size=None, scope_id=None)
```


#### Return Type:
`:rtype: :class:<ChangedIdentities> <azure.devops.v5_1.identity.models.ChangedIdentities>`
### GetMaxSequenceId
#### Description:
Read the max sequence id of all the identities.

#### Example usage:
```
connection.clients.get_identity_client().get_max_sequence_id()
```


#### Return Type:
`:rtype: long`
### GetSelf
#### Description:
Read identity of the home tenant request user.

#### Example usage:
```
connection.clients.get_identity_client().get_self()
```


#### Return Type:
`:rtype: :class:<IdentitySelf> <azure.devops.v5_1.identity.models.IdentitySelf>`
### GetUserIdentityIdsByDomainId
#### Description:
* `:param str domain_id:`
#### Example usage:
```
connection.clients.get_identity_client().get_user_identity_ids_by_domain_id(domain_id)
```


#### Return Type:
`:rtype: [str]`
### ListGroups
#### Description:
* `:param str scope_ids:`
* `:param bool recurse:`
* `:param bool deleted:`
* `:param str properties:`
#### Example usage:
```
connection.clients.get_identity_client().list_groups(scope_ids=None, recurse=None, deleted=None, properties=None)
```


#### Return Type:
`:rtype: [Identity]`
### ReadIdentities
#### Description:
* `:param str descriptors:`
* `:param str identity_ids:`
* `:param str subject_descriptors:`
* `:param str social_descriptors:`
* `:param str search_filter:`
* `:param str filter_value:`
* `:param str query_membership:`
* `:param str properties:`
* `:param bool include_restricted_visibility:`
* `:param str options:`
#### Example usage:
```
connection.clients.get_identity_client().read_identities(descriptors=None, identity_ids=None, subject_descriptors=None, social_descriptors=None, search_filter=None, filter_value=None, query_membership=None, properties=None, include_restricted_visibility=None, options=None)
```


#### Return Type:
`:rtype: [Identity]`
### ReadIdentitiesByScope
#### Description:
* `:param str scope_id:`
* `:param str query_membership:`
* `:param str properties:`
#### Example usage:
```
connection.clients.get_identity_client().read_identities_by_scope(scope_id, query_membership=None, properties=None)
```


#### Return Type:
`:rtype: [Identity]`
### ReadIdentity
#### Description:
* `:param str identity_id:`
* `:param str query_membership:`
* `:param str properties:`
#### Example usage:
```
connection.clients.get_identity_client().read_identity(identity_id, query_membership=None, properties=None)
```


#### Return Type:
`:rtype: :class:<Identity> <azure.devops.v5_1.identity.models.Identity>`
### UpdateIdentities
#### Description:
* `:param :class:<VssJsonCollectionWrapper> <azure.devops.v5_1.identity.models.VssJsonCollectionWrapper> identities:`
#### Example usage:
```
from azure.devops.v5_1.identity.models import VssJsonCollectionWrapper

connection.clients.get_identity_client().update_identities(identities)
```


#### Return Type:
`:rtype: [IdentityUpdateData]`
### UpdateIdentity
#### Description:
* `:param :class:<Identity> <azure.devops.v5_1.identity.models.Identity> identity:`
* `:param str identity_id:`
#### Example usage:
```
from azure.devops.v5_1.identity.models import Identity

connection.clients.get_identity_client().update_identity(identity, identity_id)
```


#### Return Type:
`:rtype: [IdentityUpdateData]`
## Get Notification Client
### CreateSubscription
#### Description:
Create a new subscription.

* `:param :class:<NotificationSubscriptionCreateParameters> <azure.devops.v5_1.notification.models.NotificationSubscriptionCreateParameters> create_parameters:`
#### Example usage:
```
from azure.devops.v5_1.notification.models import NotificationSubscriptionCreateParameters

connection.clients.get_notification_client().create_subscription(create_parameters)
```


#### Return Type:
`:rtype: :class:<NotificationSubscription> <azure.devops.v5_1.notification.models.NotificationSubscription>`
### DeleteSubscription
#### Description:
Delete a subscription.

* `:param str subscription_id:`
#### Example usage:
```
connection.clients.get_notification_client().delete_subscription(subscription_id)
```


#### Return Type:
`:rtype: :class:<NotificationSubscription> <azure.devops.v5_1.notification.models.NotificationSubscription>`
### GetEventType
#### Description:
Get a specific event type.

* `:param str event_type: The ID of the event type.`
#### Example usage:
```
connection.clients.get_notification_client().get_event_type(event_type)
```


#### Return Type:
`:rtype: :class:<NotificationEventType> <azure.devops.v5_1.notification.models.NotificationEventType>`
### GetSettings
#### Description:
#### Example usage:
```
connection.clients.get_notification_client().get_settings()
```


#### Return Type:
`:rtype: :class:<NotificationAdminSettings> <azure.devops.v5_1.notification.models.NotificationAdminSettings>`
### GetSubscriber
#### Description:
Get delivery preferences of a notifications subscriber.

* `:param str subscriber_id: ID of the user or group.`
#### Example usage:
```
connection.clients.get_notification_client().get_subscriber(subscriber_id)
```


#### Return Type:
`:rtype: :class:<NotificationSubscriber> <azure.devops.v5_1.notification.models.NotificationSubscriber>`
### GetSubscription
#### Description:
Get a notification subscription by its ID.

* `:param str subscription_id:`
* `:param str query_flags:`
#### Example usage:
```
connection.clients.get_notification_client().get_subscription(subscription_id, query_flags=None)
```


#### Return Type:
`:rtype: :class:<NotificationSubscription> <azure.devops.v5_1.notification.models.NotificationSubscription>`
### GetSubscriptionDiagnostics
#### Description:
Get the diagnostics settings for a subscription.

* `:param str subscription_id: The id of the notifications subscription.`
#### Example usage:
```
connection.clients.get_notification_client().get_subscription_diagnostics(subscription_id)
```


#### Return Type:
`:rtype: :class:<SubscriptionDiagnostics> <azure.devops.v5_1.notification.models.SubscriptionDiagnostics>`
### GetSubscriptionTemplates
#### Description:
Get available subscription templates.

#### Example usage:
```
connection.clients.get_notification_client().get_subscription_templates()
```


#### Return Type:
`:rtype: [NotificationSubscriptionTemplate]`
### ListEventTypes
#### Description:
List available event types for this service. Optionally filter by only event types for the specified publisher.

* `:param str publisher_id: Limit to event types for this publisher`
#### Example usage:
```
connection.clients.get_notification_client().list_event_types(publisher_id=None)
```


#### Return Type:
`:rtype: [NotificationEventType]`
### ListLogs
#### Description:
Get a list of diagnostic logs for this service.

* `:param str source: ID specifying which type of logs to check diagnostics for.`
* `:param str entry_id: The ID of the specific log to query for.`
* `:param datetime start_time: Start time for the time range to query in.`
* `:param datetime end_time: End time for the time range to query in.`
#### Example usage:
```
connection.clients.get_notification_client().list_logs(source, entry_id=None, start_time=None, end_time=None)
```


#### Return Type:
`:rtype: [INotificationDiagnosticLog]`
### ListSubscriptions
#### Description:
Get a list of notification subscriptions, either by subscription IDs or by all subscriptions for a given user or group.

* `:param str target_id: User or Group ID`
* `:param [str] ids: List of subscription IDs`
* `:param str query_flags:`
#### Example usage:
```
connection.clients.get_notification_client().list_subscriptions(target_id=None, ids=None, query_flags=None)
```


#### Return Type:
`:rtype: [NotificationSubscription]`
### QuerySubscriptions
#### Description:
Query for subscriptions. A subscription is returned if it matches one or more of the specified conditions.

* `:param :class:<SubscriptionQuery> <azure.devops.v5_1.notification.models.SubscriptionQuery> subscription_query:`
#### Example usage:
```
from azure.devops.v5_1.notification.models import SubscriptionQuery

connection.clients.get_notification_client().query_subscriptions(subscription_query)
```


#### Return Type:
`:rtype: [NotificationSubscription]`
### UpdateSettings
#### Description:
* `:param :class:<NotificationAdminSettingsUpdateParameters> <azure.devops.v5_1.notification.models.NotificationAdminSettingsUpdateParameters> update_parameters:`
#### Example usage:
```
from azure.devops.v5_1.notification.models import NotificationAdminSettingsUpdateParameters

connection.clients.get_notification_client().update_settings(update_parameters)
```


#### Return Type:
`:rtype: :class:<NotificationAdminSettings> <azure.devops.v5_1.notification.models.NotificationAdminSettings>`
### UpdateSubscriber
#### Description:
Update delivery preferences of a notifications subscriber.

* `:param :class:<NotificationSubscriberUpdateParameters> <azure.devops.v5_1.notification.models.NotificationSubscriberUpdateParameters> update_parameters:`
* `:param str subscriber_id: ID of the user or group.`
#### Example usage:
```
from azure.devops.v5_1.notification.models import NotificationSubscriberUpdateParameters

connection.clients.get_notification_client().update_subscriber(update_parameters, subscriber_id)
```


#### Return Type:
`:rtype: :class:<NotificationSubscriber> <azure.devops.v5_1.notification.models.NotificationSubscriber>`
### UpdateSubscription
#### Description:
Update an existing subscription. Depending on the type of subscription and permissions, the caller can update the description, filter settings, channel (delivery) settings and more.

* `:param :class:<NotificationSubscriptionUpdateParameters> <azure.devops.v5_1.notification.models.NotificationSubscriptionUpdateParameters> update_parameters:`
* `:param str subscription_id:`
#### Example usage:
```
from azure.devops.v5_1.notification.models import NotificationSubscriptionUpdateParameters

connection.clients.get_notification_client().update_subscription(update_parameters, subscription_id)
```


#### Return Type:
`:rtype: :class:<NotificationSubscription> <azure.devops.v5_1.notification.models.NotificationSubscription>`
### UpdateSubscriptionDiagnostics
#### Description:
Update the diagnostics settings for a subscription.

* `:param :class:<UpdateSubscripitonDiagnosticsParameters> <azure.devops.v5_1.notification.models.UpdateSubscripitonDiagnosticsParameters> update_parameters:`
* `:param str subscription_id: The id of the notifications subscription.`
#### Example usage:
```
from azure.devops.v5_1.notification.models import UpdateSubscripitonDiagnosticsParameters

connection.clients.get_notification_client().update_subscription_diagnostics(update_parameters, subscription_id)
```


#### Return Type:
`:rtype: :class:<SubscriptionDiagnostics> <azure.devops.v5_1.notification.models.SubscriptionDiagnostics>`
### UpdateSubscriptionUserSettings
#### Description:
Update the specified user's settings for the specified subscription. This API is typically used to opt in or out of a shared subscription. User settings can only be applied to shared subscriptions, like team subscriptions or default subscriptions.

* `:param :class:<SubscriptionUserSettings> <azure.devops.v5_1.notification.models.SubscriptionUserSettings> user_settings:`
* `:param str subscription_id:`
* `:param str user_id: ID of the user`
#### Example usage:
```
from azure.devops.v5_1.notification.models import SubscriptionUserSettings

connection.clients.get_notification_client().update_subscription_user_settings(user_settings, subscription_id, user_id)
```


#### Return Type:
`:rtype: :class:<SubscriptionUserSettings> <azure.devops.v5_1.notification.models.SubscriptionUserSettings>`
## Get Operations Client
### GetOperation
#### Description:
Gets an operation from the the operationId using the given pluginId.

* `:param str operation_id: The ID for the operation.`
* `:param str plugin_id: The ID for the plugin.`
#### Example usage:
```
connection.clients.get_operations_client().get_operation(operation_id, plugin_id=None)
```


#### Return Type:
`:rtype: :class:<Operation> <azure.devops.v5_1.operations.models.Operation>`
## Get Policy Client
### CreatePolicyConfiguration
#### Description:
Create a policy configuration of a given policy type.

* `:param :class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration> configuration: The policy configuration to create.`
* `:param str project: Project ID or project name`
* `:param int configuration_id:`
#### Example usage:
```
from azure.devops.v5_1.policy.models import PolicyConfiguration

connection.clients.get_policy_client().create_policy_configuration(configuration, project, configuration_id=None)
```


#### Return Type:
`:rtype: :class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>`
### DeletePolicyConfiguration
#### Description:
Delete a policy configuration by its ID.

* `:param str project: Project ID or project name`
* `:param int configuration_id: ID of the policy configuration to delete.`
#### Example usage:
```
connection.clients.get_policy_client().delete_policy_configuration(project, configuration_id)
```


#### Return Type:
`:rtype: :class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>`
### GetPolicyConfiguration
#### Description:
Get a policy configuration by its ID.

* `:param str project: Project ID or project name`
* `:param int configuration_id: ID of the policy configuration`
#### Example usage:
```
connection.clients.get_policy_client().get_policy_configuration(project, configuration_id)
```


#### Return Type:
`:rtype: :class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>`
### GetPolicyConfigurationRevision
#### Description:
Retrieve a specific revision of a given policy by ID.

* `:param str project: Project ID or project name`
* `:param int configuration_id: The policy configuration ID.`
* `:param int revision_id: The revision ID.`
#### Example usage:
```
connection.clients.get_policy_client().get_policy_configuration_revision(project, configuration_id, revision_id)
```


#### Return Type:
`:rtype: :class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>`
### GetPolicyConfigurationRevisions
#### Description:
Retrieve all revisions for a given policy.

* `:param str project: Project ID or project name`
* `:param int configuration_id: The policy configuration ID.`
* `:param int top: The number of revisions to retrieve.`
* `:param int skip: The number of revisions to ignore. For example, to retrieve results 101-150, set top to 50 and skip to 100.`
#### Example usage:
```
connection.clients.get_policy_client().get_policy_configuration_revisions(project, configuration_id, top=None, skip=None)
```


#### Return Type:
`:rtype: [PolicyConfiguration]`
### GetPolicyConfigurations
#### Description:
Get a list of policy configurations in a project.

* `:param str project: Project ID or project name`
* `:param str scope: [Provided for legacy reasons] The scope on which a subset of policies is defined.`
* `:param int top: Maximum number of policies to return.`
* `:param str continuation_token: The continuation token used for pagination.`
* `:param str policy_type: Filter returned policies to only this type`
#### Example usage:
```
connection.clients.get_policy_client().get_policy_configurations(project, scope=None, top=None, continuation_token=None, policy_type=None)
```


#### Return Type:
`:rtype: :class:<GetPolicyConfigurationsResponseValue>`
### GetPolicyType
#### Description:
Retrieve a specific policy type by ID.

* `:param str project: Project ID or project name`
* `:param str type_id: The policy ID.`
#### Example usage:
```
connection.clients.get_policy_client().get_policy_type(project, type_id)
```


#### Return Type:
`:rtype: :class:<PolicyType> <azure.devops.v5_1.policy.models.PolicyType>`
### GetPolicyTypes
#### Description:
Retrieve all available policy types.

* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_policy_client().get_policy_types(project)
```


#### Return Type:
`:rtype: [PolicyType]`
### UpdatePolicyConfiguration
#### Description:
Update a policy configuration by its ID.

* `:param :class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration> configuration: The policy configuration to update.`
* `:param str project: Project ID or project name`
* `:param int configuration_id: ID of the existing policy configuration to be updated.`
#### Example usage:
```
from azure.devops.v5_1.policy.models import PolicyConfiguration

connection.clients.get_policy_client().update_policy_configuration(configuration, project, configuration_id)
```


#### Return Type:
`:rtype: :class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>`
## Get Profile Client
### CreatePolicyConfiguration
#### Description:
Create a policy configuration of a given policy type.

* `:param :class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration> configuration: The policy configuration to create.`
* `:param str project: Project ID or project name`
* `:param int configuration_id:`
#### Example usage:
```
from azure.devops.v5_1.policy.models import PolicyConfiguration

connection.clients.get_profile_client().create_policy_configuration(configuration, project, configuration_id=None)
```


#### Return Type:
`:rtype: :class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>`
### DeletePolicyConfiguration
#### Description:
Delete a policy configuration by its ID.

* `:param str project: Project ID or project name`
* `:param int configuration_id: ID of the policy configuration to delete.`
#### Example usage:
```
connection.clients.get_profile_client().delete_policy_configuration(project, configuration_id)
```


#### Return Type:
`:rtype: :class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>`
### GetPolicyConfiguration
#### Description:
Get a policy configuration by its ID.

* `:param str project: Project ID or project name`
* `:param int configuration_id: ID of the policy configuration`
#### Example usage:
```
connection.clients.get_profile_client().get_policy_configuration(project, configuration_id)
```


#### Return Type:
`:rtype: :class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>`
### GetPolicyConfigurationRevision
#### Description:
Retrieve a specific revision of a given policy by ID.

* `:param str project: Project ID or project name`
* `:param int configuration_id: The policy configuration ID.`
* `:param int revision_id: The revision ID.`
#### Example usage:
```
connection.clients.get_profile_client().get_policy_configuration_revision(project, configuration_id, revision_id)
```


#### Return Type:
`:rtype: :class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>`
### GetPolicyConfigurationRevisions
#### Description:
Retrieve all revisions for a given policy.

* `:param str project: Project ID or project name`
* `:param int configuration_id: The policy configuration ID.`
* `:param int top: The number of revisions to retrieve.`
* `:param int skip: The number of revisions to ignore. For example, to retrieve results 101-150, set top to 50 and skip to 100.`
#### Example usage:
```
connection.clients.get_profile_client().get_policy_configuration_revisions(project, configuration_id, top=None, skip=None)
```


#### Return Type:
`:rtype: [PolicyConfiguration]`
### GetPolicyConfigurations
#### Description:
Get a list of policy configurations in a project.

* `:param str project: Project ID or project name`
* `:param str scope: [Provided for legacy reasons] The scope on which a subset of policies is defined.`
* `:param int top: Maximum number of policies to return.`
* `:param str continuation_token: The continuation token used for pagination.`
* `:param str policy_type: Filter returned policies to only this type`
#### Example usage:
```
connection.clients.get_profile_client().get_policy_configurations(project, scope=None, top=None, continuation_token=None, policy_type=None)
```


#### Return Type:
`:rtype: :class:<GetPolicyConfigurationsResponseValue>`
### GetPolicyType
#### Description:
Retrieve a specific policy type by ID.

* `:param str project: Project ID or project name`
* `:param str type_id: The policy ID.`
#### Example usage:
```
connection.clients.get_profile_client().get_policy_type(project, type_id)
```


#### Return Type:
`:rtype: :class:<PolicyType> <azure.devops.v5_1.policy.models.PolicyType>`
### GetPolicyTypes
#### Description:
Retrieve all available policy types.

* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_profile_client().get_policy_types(project)
```


#### Return Type:
`:rtype: [PolicyType]`
### UpdatePolicyConfiguration
#### Description:
Update a policy configuration by its ID.

* `:param :class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration> configuration: The policy configuration to update.`
* `:param str project: Project ID or project name`
* `:param int configuration_id: ID of the existing policy configuration to be updated.`
#### Example usage:
```
from azure.devops.v5_1.policy.models import PolicyConfiguration

connection.clients.get_profile_client().update_policy_configuration(configuration, project, configuration_id)
```


#### Return Type:
`:rtype: :class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>`
## Get Release Client
### CreateRelease
#### Description:
Create a release.

* `:param :class:<ReleaseStartMetadata> <azure.devops.v5_1.release.models.ReleaseStartMetadata> release_start_metadata: Metadata to create a release.`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.release.models import ReleaseStartMetadata

connection.clients.get_release_client().create_release(release_start_metadata, project)
```


#### Return Type:
`:rtype: :class:<Release> <azure.devops.v5_1.release.models.Release>`
### CreateReleaseDefinition
#### Description:
Create a release definition

* `:param :class:<ReleaseDefinition> <azure.devops.v5_1.release.models.ReleaseDefinition> release_definition: release definition object to create.`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.release.models import ReleaseDefinition

connection.clients.get_release_client().create_release_definition(release_definition, project)
```


#### Return Type:
`:rtype: :class:<ReleaseDefinition> <azure.devops.v5_1.release.models.ReleaseDefinition>`
### DeleteReleaseDefinition
#### Description:
Delete a release definition.

* `:param str project: Project ID or project name`
* `:param int definition_id: Id of the release definition.`
* `:param str comment: Comment for deleting a release definition.`
* `:param bool force_delete: 'true' to automatically cancel any in-progress release deployments and proceed with release definition deletion . Default is 'false'.`
#### Example usage:
```
connection.clients.get_release_client().delete_release_definition(project, definition_id, comment=None, force_delete=None)
```


#### Return Type:
`:rtype: :class:<ReleaseDefinition> <azure.devops.v5_1.release.models.ReleaseDefinition>`
### GetApprovals
#### Description:
Get a list of approvals

* `:param str project: Project ID or project name`
* `:param str assigned_to_filter: Approvals assigned to this user.`
* `:param str status_filter: Approvals with this status. Default is 'pending'.`
* `:param [int] release_ids_filter: Approvals for release id(s) mentioned in the filter. Multiple releases can be mentioned by separating them with ',' e.g. releaseIdsFilter=1,2,3,4.`
* `:param str type_filter: Approval with this type.`
* `:param int top: Number of approvals to get. Default is 50.`
* `:param int continuation_token: Gets the approvals after the continuation token provided.`
* `:param str query_order: Gets the results in the defined order of created approvals. Default is 'descending'.`
* `:param bool include_my_group_approvals: 'true' to include my group approvals. Default is 'false'.`
#### Example usage:
```
connection.clients.get_release_client().get_approvals(project, assigned_to_filter=None, status_filter=None, release_ids_filter=None, type_filter=None, top=None, continuation_token=None, query_order=None, include_my_group_approvals=None)
```


#### Return Type:
`:rtype: :class:<GetApprovalsResponseValue>`
### GetDeployments
#### Description:
* `:param str project: Project ID or project name`
* `:param int definition_id:`
* `:param int definition_environment_id:`
* `:param str created_by:`
* `:param datetime min_modified_time:`
* `:param datetime max_modified_time:`
* `:param str deployment_status:`
* `:param str operation_status:`
* `:param bool latest_attempts_only:`
* `:param str query_order:`
* `:param int top:`
* `:param int continuation_token:`
* `:param str created_for:`
* `:param datetime min_started_time:`
* `:param datetime max_started_time:`
* `:param str source_branch:`
#### Example usage:
```
connection.clients.get_release_client().get_deployments(project, definition_id=None, definition_environment_id=None, created_by=None, min_modified_time=None, max_modified_time=None, deployment_status=None, operation_status=None, latest_attempts_only=None, query_order=None, top=None, continuation_token=None, created_for=None, min_started_time=None, max_started_time=None, source_branch=None)
```


#### Return Type:
`:rtype: :class:<GetDeploymentsResponseValue>`
### GetManualIntervention
#### Description:
Get manual intervention for a given release and manual intervention id.

* `:param str project: Project ID or project name`
* `:param int release_id: Id of the release.`
* `:param int manual_intervention_id: Id of the manual intervention.`
#### Example usage:
```
connection.clients.get_release_client().get_manual_intervention(project, release_id, manual_intervention_id)
```


#### Return Type:
`:rtype: :class:<ManualIntervention> <azure.devops.v5_1.release.models.ManualIntervention>`
### GetManualInterventions
#### Description:
List all manual interventions for a given release.

* `:param str project: Project ID or project name`
* `:param int release_id: Id of the release.`
#### Example usage:
```
connection.clients.get_release_client().get_manual_interventions(project, release_id)
```


#### Return Type:
`:rtype: [ManualIntervention]`
### GetRelease
#### Description:
Get a Release

* `:param str project: Project ID or project name`
* `:param int release_id: Id of the release.`
* `:param str approval_filters: A filter which would allow fetching approval steps selectively based on whether it is automated, or manual. This would also decide whether we should fetch pre and post approval snapshots. Assumes All by default`
* `:param [str] property_filters: A comma-delimited list of extended properties to be retrieved. If set, the returned Release will contain values for the specified property Ids (if they exist). If not set, properties will not be included.`
* `:param str expand: A property that should be expanded in the release.`
* `:param int top_gate_records: Number of release gate records to get. Default is 5.`
#### Example usage:
```
connection.clients.get_release_client().get_release(project, release_id, approval_filters=None, property_filters=None, expand=None, top_gate_records=None)
```


#### Return Type:
`:rtype: :class:<Release> <azure.devops.v5_1.release.models.Release>`
### GetReleaseDefinition
#### Description:
Get a release definition.

* `:param str project: Project ID or project name`
* `:param int definition_id: Id of the release definition.`
* `:param [str] property_filters: A comma-delimited list of extended properties to be retrieved. If set, the returned Release Definition will contain values for the specified property Ids (if they exist). If not set, properties will not be included.`
#### Example usage:
```
connection.clients.get_release_client().get_release_definition(project, definition_id, property_filters=None)
```


#### Return Type:
`:rtype: :class:<ReleaseDefinition> <azure.devops.v5_1.release.models.ReleaseDefinition>`
### GetReleaseDefinitions
#### Description:
Get a list of release definitions.

* `:param str project: Project ID or project name`
* `:param str search_text: Get release definitions with names containing searchText.`
* `:param str expand: The properties that should be expanded in the list of Release definitions.`
* `:param str artifact_type: Release definitions with given artifactType will be returned. Values can be Build, Jenkins, GitHub, Nuget, Team Build (external), ExternalTFSBuild, Git, TFVC, ExternalTfsXamlBuild.`
* `:param str artifact_source_id: Release definitions with given artifactSourceId will be returned. e.g. For build it would be {projectGuid}:{BuildDefinitionId}, for Jenkins it would be {JenkinsConnectionId}:{JenkinsDefinitionId}, for TfsOnPrem it would be {TfsOnPremConnectionId}:{ProjectName}:{TfsOnPremDefinitionId}. For third-party artifacts e.g. TeamCity, BitBucket you may refer 'uniqueSourceIdentifier' inside vss-extension.json at https://github.com/Microsoft/vsts-rm-extensions/blob/master/Extensions.`
* `:param int top: Number of release definitions to get.`
* `:param str continuation_token: Gets the release definitions after the continuation token provided.`
* `:param str query_order: Gets the results in the defined order. Default is 'IdAscending'.`
* `:param str path: Gets the release definitions under the specified path.`
* `:param bool is_exact_name_match: 'true'to gets the release definitions with exact match as specified in searchText. Default is 'false'.`
* `:param [str] tag_filter: A comma-delimited list of tags. Only release definitions with these tags will be returned.`
* `:param [str] property_filters: A comma-delimited list of extended properties to be retrieved. If set, the returned Release Definitions will contain values for the specified property Ids (if they exist). If not set, properties will not be included. Note that this will not filter out any Release Definition from results irrespective of whether it has property set or not.`
* `:param [str] definition_id_filter: A comma-delimited list of release definitions to retrieve.`
* `:param bool is_deleted: 'true' to get release definitions that has been deleted. Default is 'false'`
* `:param bool search_text_contains_folder_name: 'true' to get the release definitions under the folder with name as specified in searchText. Default is 'false'.`
#### Example usage:
```
connection.clients.get_release_client().get_release_definitions(project, search_text=None, expand=None, artifact_type=None, artifact_source_id=None, top=None, continuation_token=None, query_order=None, path=None, is_exact_name_match=None, tag_filter=None, property_filters=None, definition_id_filter=None, is_deleted=None, search_text_contains_folder_name=None)
```


#### Return Type:
`:rtype: :class:<GetReleaseDefinitionsResponseValue>`
### GetReleaseRevision
#### Description:
Get release for a given revision number.

* `:param str project: Project ID or project name`
* `:param int release_id: Id of the release.`
* `:param int definition_snapshot_revision: Definition snapshot revision number.`
#### Example usage:
```
connection.clients.get_release_client().get_release_revision(project, release_id, definition_snapshot_revision, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetReleases
#### Description:
Get a list of releases

* `:param str project: Project ID or project name`
* `:param int definition_id: Releases from this release definition Id.`
* `:param int definition_environment_id:`
* `:param str search_text: Releases with names containing searchText.`
* `:param str created_by: Releases created by this user.`
* `:param str status_filter: Releases that have this status.`
* `:param int environment_status_filter:`
* `:param datetime min_created_time: Releases that were created after this time.`
* `:param datetime max_created_time: Releases that were created before this time.`
* `:param str query_order: Gets the results in the defined order of created date for releases. Default is descending.`
* `:param int top: Number of releases to get. Default is 50.`
* `:param int continuation_token: Gets the releases after the continuation token provided.`
* `:param str expand: The property that should be expanded in the list of releases.`
* `:param str artifact_type_id: Releases with given artifactTypeId will be returned. Values can be Build, Jenkins, GitHub, Nuget, Team Build (external), ExternalTFSBuild, Git, TFVC, ExternalTfsXamlBuild.`
* `:param str source_id: Unique identifier of the artifact used. e.g. For build it would be {projectGuid}:{BuildDefinitionId}, for Jenkins it would be {JenkinsConnectionId}:{JenkinsDefinitionId}, for TfsOnPrem it would be {TfsOnPremConnectionId}:{ProjectName}:{TfsOnPremDefinitionId}. For third-party artifacts e.g. TeamCity, BitBucket you may refer 'uniqueSourceIdentifier' inside vss-extension.json https://github.com/Microsoft/vsts-rm-extensions/blob/master/Extensions.`
* `:param str artifact_version_id: Releases with given artifactVersionId will be returned. E.g. in case of Build artifactType, it is buildId.`
* `:param str source_branch_filter: Releases with given sourceBranchFilter will be returned.`
* `:param bool is_deleted: Gets the soft deleted releases, if true.`
* `:param [str] tag_filter: A comma-delimited list of tags. Only releases with these tags will be returned.`
* `:param [str] property_filters: A comma-delimited list of extended properties to be retrieved. If set, the returned Releases will contain values for the specified property Ids (if they exist). If not set, properties will not be included. Note that this will not filter out any Release from results irrespective of whether it has property set or not.`
* `:param [int] release_id_filter: A comma-delimited list of releases Ids. Only releases with these Ids will be returned.`
* `:param str path: Releases under this folder path will be returned`
#### Example usage:
```
connection.clients.get_release_client().get_releases(project=None, definition_id=None, definition_environment_id=None, search_text=None, created_by=None, status_filter=None, environment_status_filter=None, min_created_time=None, max_created_time=None, query_order=None, top=None, continuation_token=None, expand=None, artifact_type_id=None, source_id=None, artifact_version_id=None, source_branch_filter=None, is_deleted=None, tag_filter=None, property_filters=None, release_id_filter=None, path=None)
```


#### Return Type:
`:rtype: :class:<GetReleasesResponseValue>`
### UpdateManualIntervention
#### Description:
Update manual intervention.

* `:param :class:<ManualInterventionUpdateMetadata> <azure.devops.v5_1.release.models.ManualInterventionUpdateMetadata> manual_intervention_update_metadata: Meta data to update manual intervention.`
* `:param str project: Project ID or project name`
* `:param int release_id: Id of the release.`
* `:param int manual_intervention_id: Id of the manual intervention.`
#### Example usage:
```
from azure.devops.v5_1.release.models import ManualInterventionUpdateMetadata

connection.clients.get_release_client().update_manual_intervention(manual_intervention_update_metadata, project, release_id, manual_intervention_id)
```


#### Return Type:
`:rtype: :class:<ManualIntervention> <azure.devops.v5_1.release.models.ManualIntervention>`
### UpdateRelease
#### Description:
Update a complete release object.

* `:param :class:<Release> <azure.devops.v5_1.release.models.Release> release: Release object for update.`
* `:param str project: Project ID or project name`
* `:param int release_id: Id of the release to update.`
#### Example usage:
```
from azure.devops.v5_1.release.models import Release

connection.clients.get_release_client().update_release(release, project, release_id)
```


#### Return Type:
`:rtype: :class:<Release> <azure.devops.v5_1.release.models.Release>`
### UpdateReleaseApproval
#### Description:
Update status of an approval

* `:param :class:<ReleaseApproval> <azure.devops.v5_1.release.models.ReleaseApproval> approval: ReleaseApproval object having status, approver and comments.`
* `:param str project: Project ID or project name`
* `:param int approval_id: Id of the approval.`
#### Example usage:
```
from azure.devops.v5_1.release.models import ReleaseApproval

connection.clients.get_release_client().update_release_approval(approval, project, approval_id)
```


#### Return Type:
`:rtype: :class:<ReleaseApproval> <azure.devops.v5_1.release.models.ReleaseApproval>`
### UpdateReleaseDefinition
#### Description:
Update a release definition.

* `:param :class:<ReleaseDefinition> <azure.devops.v5_1.release.models.ReleaseDefinition> release_definition: Release definition object to update.`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.release.models import ReleaseDefinition

connection.clients.get_release_client().update_release_definition(release_definition, project)
```


#### Return Type:
`:rtype: :class:<ReleaseDefinition> <azure.devops.v5_1.release.models.ReleaseDefinition>`
### UpdateReleaseResource
#### Description:
Update few properties of a release.

* `:param :class:<ReleaseUpdateMetadata> <azure.devops.v5_1.release.models.ReleaseUpdateMetadata> release_update_metadata: Properties of release to update.`
* `:param str project: Project ID or project name`
* `:param int release_id: Id of the release to update.`
#### Example usage:
```
from azure.devops.v5_1.release.models import ReleaseUpdateMetadata

connection.clients.get_release_client().update_release_resource(release_update_metadata, project, release_id)
```


#### Return Type:
`:rtype: :class:<Release> <azure.devops.v5_1.release.models.Release>`
## Get Security Client
### HasPermissions
#### Description:
Evaluates whether the caller has the specified permissions on the specified set of security tokens.

* `:param str security_namespace_id: Security namespace identifier.`
* `:param int permissions: Permissions to evaluate.`
* `:param str tokens: One or more security tokens to evaluate.`
* `:param bool always_allow_administrators: If true and if the caller is an administrator, always return true.`
* `:param str delimiter: Optional security token separator. Defaults to ",".`
#### Example usage:
```
connection.clients.get_security_client().has_permissions(security_namespace_id, permissions=None, tokens=None, always_allow_administrators=None, delimiter=None)
```


#### Return Type:
`:rtype: [bool]`
### HasPermissionsBatch
#### Description:
Evaluates multiple permissions for the calling user.  Note: This method does not aggregate the results, nor does it short-circuit if one of the permissions evaluates to false.

* `:param :class:<PermissionEvaluationBatch> <azure.devops.v5_1.security.models.PermissionEvaluationBatch> eval_batch: The set of evaluation requests.`
#### Example usage:
```
from azure.devops.v5_1.security.models import PermissionEvaluationBatch

connection.clients.get_security_client().has_permissions_batch(eval_batch)
```


#### Return Type:
`:rtype: :class:<PermissionEvaluationBatch> <azure.devops.v5_1.security.models.PermissionEvaluationBatch>`
### QueryAccessControlLists
#### Description:
Return a list of access control lists for the specified security namespace and token. All ACLs in the security namespace will be retrieved if no optional parameters are provided.

* `:param str security_namespace_id: Security namespace identifier.`
* `:param str token: Security token`
* `:param str descriptors: An optional filter string containing a list of identity descriptors separated by ',' whose ACEs should be retrieved. If this is left null, entire ACLs will be returned.`
* `:param bool include_extended_info: If true, populate the extended information properties for the access control entries contained in the returned lists.`
* `:param bool recurse: If true and this is a hierarchical namespace, return child ACLs of the specified token.`
#### Example usage:
```
connection.clients.get_security_client().query_access_control_lists(security_namespace_id, token=None, descriptors=None, include_extended_info=None, recurse=None)
```


#### Return Type:
`:rtype: [AccessControlList]`
### QuerySecurityNamespaces
#### Description:
List all security namespaces or just the specified namespace.

* `:param str security_namespace_id: Security namespace identifier.`
* `:param bool local_only: If true, retrieve only local security namespaces.`
#### Example usage:
```
connection.clients.get_security_client().query_security_namespaces(security_namespace_id=None, local_only=None)
```


#### Return Type:
`:rtype: [SecurityNamespaceDescription]`
### RemoveAccessControlEntries
#### Description:
Remove the specified ACEs from the ACL belonging to the specified token.

* `:param str security_namespace_id: Security namespace identifier.`
* `:param str token: The token whose ACL should be modified.`
* `:param str descriptors: String containing a list of identity descriptors separated by ',' whose entries should be removed.`
#### Example usage:
```
connection.clients.get_security_client().remove_access_control_entries(security_namespace_id, token=None, descriptors=None)
```


#### Return Type:
`:rtype: bool`
### RemoveAccessControlLists
#### Description:
Remove access control lists under the specfied security namespace.

* `:param str security_namespace_id: Security namespace identifier.`
* `:param str tokens: One or more comma-separated security tokens`
* `:param bool recurse: If true and this is a hierarchical namespace, also remove child ACLs of the specified tokens.`
#### Example usage:
```
connection.clients.get_security_client().remove_access_control_lists(security_namespace_id, tokens=None, recurse=None)
```


#### Return Type:
`:rtype: bool`
### RemovePermission
#### Description:
Removes the specified permissions on a security token for a user or group.

* `:param str security_namespace_id: Security namespace identifier.`
* `:param str descriptor: Identity descriptor of the user to remove permissions for.`
* `:param int permissions: Permissions to remove.`
* `:param str token: Security token to remove permissions for.`
#### Example usage:
```
connection.clients.get_security_client().remove_permission(security_namespace_id, descriptor, permissions=None, token=None)
```


#### Return Type:
`:rtype: :class:<AccessControlEntry> <azure.devops.v5_1.security.models.AccessControlEntry>`
### SetAccessControlEntries
#### Description:
Add or update ACEs in the ACL for the provided token. The request body contains the target token, a list of [ACEs](https://docs.microsoft.com/en-us/rest/api/azure/devops/security/access%20control%20entries/set%20access%20control%20entries?#accesscontrolentry) and a optional merge parameter. In the case of a collision (by identity descriptor) with an existing ACE in the ACL, the "merge" parameter determines the behavior. If set, the existing ACE has its allow and deny merged with the incoming ACE's allow and deny. If unset, the existing ACE is displaced.

* `:param :class:<object> <azure.devops.v5_1.security.models.object> container:`
* `:param str security_namespace_id: Security namespace identifier.`
#### Example usage:
```
from azure.devops.v5_1.security.models import object

connection.clients.get_security_client().set_access_control_entries(container, security_namespace_id)
```


#### Return Type:
`:rtype: [AccessControlEntry]`
### SetAccessControlLists
#### Description:
Create or update one or more access control lists. All data that currently exists for the ACLs supplied will be overwritten.

* `:param :class:<VssJsonCollectionWrapper> <azure.devops.v5_1.security.models.VssJsonCollectionWrapper> access_control_lists: A list of ACLs to create or update.`
* `:param str security_namespace_id: Security namespace identifier.`
#### Example usage:
```
from azure.devops.v5_1.security.models import VssJsonCollectionWrapper

connection.clients.get_security_client().set_access_control_lists(access_control_lists, security_namespace_id)
```


#### Return Type:
`:rtype: [AccessControlEntry]`
## Get Service Hooks Client
### CreateSubscription
#### Description:
Create a subscription.

* `:param :class:<Subscription> <azure.devops.v5_1.service_hooks.models.Subscription> subscription: Subscription to be created.`
#### Example usage:
```
from azure.devops.v5_1.service_hooks.models import Subscription

connection.clients.get_service_hooks_client().create_subscription(subscription)
```


#### Return Type:
`:rtype: :class:<Subscription> <azure.devops.v5_1.service_hooks.models.Subscription>`
### CreateSubscriptionsQuery
#### Description:
Query for service hook subscriptions.

* `:param :class:<SubscriptionsQuery> <azure.devops.v5_1.service_hooks.models.SubscriptionsQuery> query:`
#### Example usage:
```
from azure.devops.v5_1.service_hooks.models import SubscriptionsQuery

connection.clients.get_service_hooks_client().create_subscriptions_query(query)
```


#### Return Type:
`:rtype: :class:<SubscriptionsQuery> <azure.devops.v5_1.service_hooks.models.SubscriptionsQuery>`
### CreateTestNotification
#### Description:
Sends a test notification. This is useful for verifying the configuration of an updated or new service hooks subscription.

* `:param :class:<Notification> <azure.devops.v5_1.service_hooks.models.Notification> test_notification:`
* `:param bool use_real_data: Only allow testing with real data in existing subscriptions.`
#### Example usage:
```
from azure.devops.v5_1.service_hooks.models import Notification

connection.clients.get_service_hooks_client().create_test_notification(test_notification, use_real_data=None)
```


#### Return Type:
`:rtype: :class:<Notification> <azure.devops.v5_1.service_hooks.models.Notification>`
### DeleteSubscription
#### Description:
Delete a specific service hooks subscription.

* `:param str subscription_id: ID for a subscription.`
#### Example usage:
```
connection.clients.get_service_hooks_client().delete_subscription(subscription_id)
```


#### Return Type:
`:rtype: :class:<Notification> <azure.devops.v5_1.service_hooks.models.Notification>`
### GetConsumer
#### Description:
Get a specific consumer service. Optionally filter out consumer actions that do not support any event types for the specified publisher.

* `:param str consumer_id: ID for a consumer.`
* `:param str publisher_id:`
#### Example usage:
```
connection.clients.get_service_hooks_client().get_consumer(consumer_id, publisher_id=None)
```


#### Return Type:
`:rtype: :class:<Consumer> <azure.devops.v5_1.service_hooks.models.Consumer>`
### GetConsumerAction
#### Description:
Get details about a specific consumer action.

* `:param str consumer_id: ID for a consumer.`
* `:param str consumer_action_id: ID for a consumerActionId.`
* `:param str publisher_id:`
#### Example usage:
```
connection.clients.get_service_hooks_client().get_consumer_action(consumer_id, consumer_action_id, publisher_id=None)
```


#### Return Type:
`:rtype: :class:<ConsumerAction> <azure.devops.v5_1.service_hooks.models.ConsumerAction>`
### GetEventType
#### Description:
Get a specific event type.

* `:param str publisher_id: ID for a publisher.`
* `:param str event_type_id:`
#### Example usage:
```
connection.clients.get_service_hooks_client().get_event_type(publisher_id, event_type_id)
```


#### Return Type:
`:rtype: :class:<EventTypeDescriptor> <azure.devops.v5_1.service_hooks.models.EventTypeDescriptor>`
### GetNotification
#### Description:
Get a specific notification for a subscription.

* `:param str subscription_id: ID for a subscription.`
* `:param int notification_id:`
#### Example usage:
```
connection.clients.get_service_hooks_client().get_notification(subscription_id, notification_id)
```


#### Return Type:
`:rtype: :class:<Notification> <azure.devops.v5_1.service_hooks.models.Notification>`
### GetNotifications
#### Description:
Get a list of notifications for a specific subscription. A notification includes details about the event, the request to and the response from the consumer service.

* `:param str subscription_id: ID for a subscription.`
* `:param int max_results: Maximum number of notifications to return. Default is **100**.`
* `:param str status: Get only notifications with this status.`
* `:param str result: Get only notifications with this result type.`
#### Example usage:
```
connection.clients.get_service_hooks_client().get_notifications(subscription_id, max_results=None, status=None, result=None)
```


#### Return Type:
`:rtype: [Notification]`
### GetPublisher
#### Description:
Get a specific service hooks publisher.

* `:param str publisher_id: ID for a publisher.`
#### Example usage:
```
connection.clients.get_service_hooks_client().get_publisher(publisher_id)
```


#### Return Type:
`:rtype: :class:<Publisher> <azure.devops.v5_1.service_hooks.models.Publisher>`
### GetSubscription
#### Description:
Get a specific service hooks subscription.

* `:param str subscription_id: ID for a subscription.`
#### Example usage:
```
connection.clients.get_service_hooks_client().get_subscription(subscription_id)
```


#### Return Type:
`:rtype: :class:<Subscription> <azure.devops.v5_1.service_hooks.models.Subscription>`
### ListConsumerActions
#### Description:
Get a list of consumer actions for a specific consumer.

* `:param str consumer_id: ID for a consumer.`
* `:param str publisher_id:`
#### Example usage:
```
connection.clients.get_service_hooks_client().list_consumer_actions(consumer_id, publisher_id=None)
```


#### Return Type:
`:rtype: [ConsumerAction]`
### ListConsumers
#### Description:
Get a list of available service hook consumer services. Optionally filter by consumers that support at least one event type from the specific publisher.

* `:param str publisher_id:`
#### Example usage:
```
connection.clients.get_service_hooks_client().list_consumers(publisher_id=None)
```


#### Return Type:
`:rtype: [Consumer]`
### ListEventTypes
#### Description:
Get the event types for a specific publisher.

* `:param str publisher_id: ID for a publisher.`
#### Example usage:
```
connection.clients.get_service_hooks_client().list_event_types(publisher_id)
```


#### Return Type:
`:rtype: [EventTypeDescriptor]`
### ListPublishers
#### Description:
Get a list of publishers.

#### Example usage:
```
connection.clients.get_service_hooks_client().list_publishers()
```


#### Return Type:
`:rtype: [Publisher]`
### ListSubscriptions
#### Description:
Get a list of subscriptions.

* `:param str publisher_id: ID for a subscription.`
* `:param str event_type: The event type to filter on (if any).`
* `:param str consumer_id: ID for a consumer.`
* `:param str consumer_action_id: ID for a consumerActionId.`
#### Example usage:
```
connection.clients.get_service_hooks_client().list_subscriptions(publisher_id=None, event_type=None, consumer_id=None, consumer_action_id=None)
```


#### Return Type:
`:rtype: [Subscription]`
### QueryInputValues
#### Description:
* `:param :class:<InputValuesQuery> <azure.devops.v5_1.service_hooks.models.InputValuesQuery> input_values_query:`
* `:param str publisher_id:`
#### Example usage:
```
from azure.devops.v5_1.service_hooks.models import InputValuesQuery

connection.clients.get_service_hooks_client().query_input_values(input_values_query, publisher_id)
```


#### Return Type:
`:rtype: :class:<InputValuesQuery> <azure.devops.v5_1.service_hooks.models.InputValuesQuery>`
### QueryNotifications
#### Description:
Query for notifications. A notification includes details about the event, the request to and the response from the consumer service.

* `:param :class:<NotificationsQuery> <azure.devops.v5_1.service_hooks.models.NotificationsQuery> query:`
#### Example usage:
```
from azure.devops.v5_1.service_hooks.models import NotificationsQuery

connection.clients.get_service_hooks_client().query_notifications(query)
```


#### Return Type:
`:rtype: :class:<NotificationsQuery> <azure.devops.v5_1.service_hooks.models.NotificationsQuery>`
### QueryPublishers
#### Description:
Query for service hook publishers.

* `:param :class:<PublishersQuery> <azure.devops.v5_1.service_hooks.models.PublishersQuery> query:`
#### Example usage:
```
from azure.devops.v5_1.service_hooks.models import PublishersQuery

connection.clients.get_service_hooks_client().query_publishers(query)
```


#### Return Type:
`:rtype: :class:<PublishersQuery> <azure.devops.v5_1.service_hooks.models.PublishersQuery>`
### ReplaceSubscription
#### Description:
Update a subscription. <param name="subscriptionId">ID for a subscription that you wish to update.</param>

* `:param :class:<Subscription> <azure.devops.v5_1.service_hooks.models.Subscription> subscription:`
* `:param str subscription_id:`
#### Example usage:
```
from azure.devops.v5_1.service_hooks.models import Subscription

connection.clients.get_service_hooks_client().replace_subscription(subscription, subscription_id=None)
```


#### Return Type:
`:rtype: :class:<Subscription> <azure.devops.v5_1.service_hooks.models.Subscription>`
## Get Task Agent Client
### AddAgent
#### Description:
Adds an agent to a pool.  You probably don't want to call this endpoint directly. Instead, [configure an agent](https://docs.microsoft.com/azure/devops/pipelines/agents/agents) using the agent download package.

* `:param :class:<TaskAgent> <azure.devops.v5_1.task_agent.models.TaskAgent> agent: Details about the agent being added`
* `:param int pool_id: The agent pool in which to add the agent`
#### Example usage:
```
from azure.devops.v5_1.task_agent.models import TaskAgent

connection.clients.get_task_agent_client().add_agent(agent, pool_id)
```


#### Return Type:
`:rtype: :class:<TaskAgent> <azure.devops.v5_1.task_agent.models.TaskAgent>`
### AddAgentPool
#### Description:
Create an agent pool.

* `:param :class:<TaskAgentPool> <azure.devops.v5_1.task_agent.models.TaskAgentPool> pool: Details about the new agent pool`
#### Example usage:
```
from azure.devops.v5_1.task_agent.models import TaskAgentPool

connection.clients.get_task_agent_client().add_agent_pool(pool)
```


#### Return Type:
`:rtype: :class:<TaskAgentPool> <azure.devops.v5_1.task_agent.models.TaskAgentPool>`
### DeleteAgent
#### Description:
Delete an agent.  You probably don't want to call this endpoint directly. Instead, [use the agent configuration script](https://docs.microsoft.com/azure/devops/pipelines/agents/agents) to remove an agent from your organization.

* `:param int pool_id: The pool ID to remove the agent from`
* `:param int agent_id: The agent ID to remove`
#### Example usage:
```
connection.clients.get_task_agent_client().delete_agent(pool_id, agent_id)
```


#### Return Type:
`:rtype: :class:<TaskAgentPool> <azure.devops.v5_1.task_agent.models.TaskAgentPool>`
### DeleteAgentPool
#### Description:
Delete an agent pool.

* `:param int pool_id: ID of the agent pool to delete`
#### Example usage:
```
connection.clients.get_task_agent_client().delete_agent_pool(pool_id)
```


#### Return Type:
`:rtype: :class:<TaskAgentPool> <azure.devops.v5_1.task_agent.models.TaskAgentPool>`
### GetAgent
#### Description:
Get information about an agent.

* `:param int pool_id: The agent pool containing the agent`
* `:param int agent_id: The agent ID to get information about`
* `:param bool include_capabilities: Whether to include the agent's capabilities in the response`
* `:param bool include_assigned_request: Whether to include details about the agent's current work`
* `:param bool include_last_completed_request: Whether to include details about the agents' most recent completed work`
* `:param [str] property_filters: Filter which custom properties will be returned`
#### Example usage:
```
connection.clients.get_task_agent_client().get_agent(pool_id, agent_id, include_capabilities=None, include_assigned_request=None, include_last_completed_request=None, property_filters=None)
```


#### Return Type:
`:rtype: :class:<TaskAgent> <azure.devops.v5_1.task_agent.models.TaskAgent>`
### GetAgentPool
#### Description:
Get information about an agent pool.

* `:param int pool_id: An agent pool ID`
* `:param [str] properties: Agent pool properties (comma-separated)`
* `:param str action_filter: Filter by whether the calling user has use or manage permissions`
#### Example usage:
```
connection.clients.get_task_agent_client().get_agent_pool(pool_id, properties=None, action_filter=None)
```


#### Return Type:
`:rtype: :class:<TaskAgentPool> <azure.devops.v5_1.task_agent.models.TaskAgentPool>`
### GetAgentPools
#### Description:
Get a list of agent pools.

* `:param str pool_name: Filter by name`
* `:param [str] properties: Filter by agent pool properties (comma-separated)`
* `:param str pool_type: Filter by pool type`
* `:param str action_filter: Filter by whether the calling user has use or manage permissions`
#### Example usage:
```
connection.clients.get_task_agent_client().get_agent_pools(pool_name=None, properties=None, pool_type=None, action_filter=None)
```


#### Return Type:
`:rtype: [TaskAgentPool]`
### GetAgentPoolsByIds
#### Description:
Get a list of agent pools.

* `:param [int] pool_ids: pool Ids to fetch`
* `:param str action_filter: Filter by whether the calling user has use or manage permissions`
#### Example usage:
```
connection.clients.get_task_agent_client().get_agent_pools_by_ids(pool_ids, action_filter=None)
```


#### Return Type:
`:rtype: [TaskAgentPool]`
### GetAgents
#### Description:
Get a list of agents.

* `:param int pool_id: The agent pool containing the agents`
* `:param str agent_name: Filter on agent name`
* `:param bool include_capabilities: Whether to include the agents' capabilities in the response`
* `:param bool include_assigned_request: Whether to include details about the agents' current work`
* `:param bool include_last_completed_request: Whether to include details about the agents' most recent completed work`
* `:param [str] property_filters: Filter which custom properties will be returned`
* `:param [str] demands: Filter by demands the agents can satisfy`
#### Example usage:
```
connection.clients.get_task_agent_client().get_agents(pool_id, agent_name=None, include_capabilities=None, include_assigned_request=None, include_last_completed_request=None, property_filters=None, demands=None)
```


#### Return Type:
`:rtype: [TaskAgent]`
### GetYamlSchema
#### Description:
#### Example usage:
```
connection.clients.get_task_agent_client().get_yaml_schema()
```


#### Return Type:
`:rtype: object`
### ReplaceAgent
#### Description:
Replace an agent.  You probably don't want to call this endpoint directly. Instead, [use the agent configuration script](https://docs.microsoft.com/azure/devops/pipelines/agents/agents) to remove and reconfigure an agent from your organization.

* `:param :class:<TaskAgent> <azure.devops.v5_1.task_agent.models.TaskAgent> agent: Updated details about the replacing agent`
* `:param int pool_id: The agent pool to use`
* `:param int agent_id: The agent to replace`
#### Example usage:
```
from azure.devops.v5_1.task_agent.models import TaskAgent

connection.clients.get_task_agent_client().replace_agent(agent, pool_id, agent_id)
```


#### Return Type:
`:rtype: :class:<TaskAgent> <azure.devops.v5_1.task_agent.models.TaskAgent>`
### UpdateAgent
#### Description:
Update agent details.

* `:param :class:<TaskAgent> <azure.devops.v5_1.task_agent.models.TaskAgent> agent: Updated details about the agent`
* `:param int pool_id: The agent pool to use`
* `:param int agent_id: The agent to update`
#### Example usage:
```
from azure.devops.v5_1.task_agent.models import TaskAgent

connection.clients.get_task_agent_client().update_agent(agent, pool_id, agent_id)
```


#### Return Type:
`:rtype: :class:<TaskAgent> <azure.devops.v5_1.task_agent.models.TaskAgent>`
### UpdateAgentPool
#### Description:
Update properties on an agent pool

* `:param :class:<TaskAgentPool> <azure.devops.v5_1.task_agent.models.TaskAgentPool> pool: Updated agent pool details`
* `:param int pool_id: The agent pool to update`
#### Example usage:
```
from azure.devops.v5_1.task_agent.models import TaskAgentPool

connection.clients.get_task_agent_client().update_agent_pool(pool, pool_id)
```


#### Return Type:
`:rtype: :class:<TaskAgentPool> <azure.devops.v5_1.task_agent.models.TaskAgentPool>`
## Get Task Client
### AppendLogContent
#### Description:
* `:param object upload_stream: Stream to upload`
* `:param str scope_identifier: The project GUID to scope the request`
* `:param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server`
* `:param str plan_id:`
* `:param int log_id:`
#### Example usage:
```
connection.clients.get_task_client().append_log_content(upload_stream, scope_identifier, hub_name, plan_id, log_id, **kwargs)
```


#### Return Type:
`:rtype: :class:<TaskLog> <azure.devops.v5_1.task.models.TaskLog>`
### CreateLog
#### Description:
* `:param :class:<TaskLog> <azure.devops.v5_1.task.models.TaskLog> log:`
* `:param str scope_identifier: The project GUID to scope the request`
* `:param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server`
* `:param str plan_id:`
#### Example usage:
```
from azure.devops.v5_1.task.models import TaskLog

connection.clients.get_task_client().create_log(log, scope_identifier, hub_name, plan_id)
```


#### Return Type:
`:rtype: :class:<TaskLog> <azure.devops.v5_1.task.models.TaskLog>`
### CreateTimeline
#### Description:
* `:param :class:<Timeline> <azure.devops.v5_1.task.models.Timeline> timeline:`
* `:param str scope_identifier: The project GUID to scope the request`
* `:param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server`
* `:param str plan_id:`
#### Example usage:
```
from azure.devops.v5_1.task.models import Timeline

connection.clients.get_task_client().create_timeline(timeline, scope_identifier, hub_name, plan_id)
```


#### Return Type:
`:rtype: :class:<Timeline> <azure.devops.v5_1.task.models.Timeline>`
### DeleteTimeline
#### Description:
* `:param str scope_identifier: The project GUID to scope the request`
* `:param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server`
* `:param str plan_id:`
* `:param str timeline_id:`
#### Example usage:
```
connection.clients.get_task_client().delete_timeline(scope_identifier, hub_name, plan_id, timeline_id)
```


#### Return Type:
`:rtype: :class:<Timeline> <azure.devops.v5_1.task.models.Timeline>`
### GetLog
#### Description:
* `:param str scope_identifier: The project GUID to scope the request`
* `:param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server`
* `:param str plan_id:`
* `:param int log_id:`
* `:param long start_line:`
* `:param long end_line:`
#### Example usage:
```
connection.clients.get_task_client().get_log(scope_identifier, hub_name, plan_id, log_id, start_line=None, end_line=None)
```


#### Return Type:
`:rtype: [str]`
### GetLogs
#### Description:
* `:param str scope_identifier: The project GUID to scope the request`
* `:param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server`
* `:param str plan_id:`
#### Example usage:
```
connection.clients.get_task_client().get_logs(scope_identifier, hub_name, plan_id)
```


#### Return Type:
`:rtype: [TaskLog]`
### GetRecords
#### Description:
* `:param str scope_identifier: The project GUID to scope the request`
* `:param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server`
* `:param str plan_id:`
* `:param str timeline_id:`
* `:param int change_id:`
#### Example usage:
```
connection.clients.get_task_client().get_records(scope_identifier, hub_name, plan_id, timeline_id, change_id=None)
```


#### Return Type:
`:rtype: [TimelineRecord]`
### GetTimeline
#### Description:
* `:param str scope_identifier: The project GUID to scope the request`
* `:param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server`
* `:param str plan_id:`
* `:param str timeline_id:`
* `:param int change_id:`
* `:param bool include_records:`
#### Example usage:
```
connection.clients.get_task_client().get_timeline(scope_identifier, hub_name, plan_id, timeline_id, change_id=None, include_records=None)
```


#### Return Type:
`:rtype: :class:<Timeline> <azure.devops.v5_1.task.models.Timeline>`
### GetTimelines
#### Description:
* `:param str scope_identifier: The project GUID to scope the request`
* `:param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server`
* `:param str plan_id:`
#### Example usage:
```
connection.clients.get_task_client().get_timelines(scope_identifier, hub_name, plan_id)
```


#### Return Type:
`:rtype: [Timeline]`
### UpdateRecords
#### Description:
* `:param :class:<VssJsonCollectionWrapper> <azure.devops.v5_1.task.models.VssJsonCollectionWrapper> records:`
* `:param str scope_identifier: The project GUID to scope the request`
* `:param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server`
* `:param str plan_id:`
* `:param str timeline_id:`
#### Example usage:
```
from azure.devops.v5_1.task.models import VssJsonCollectionWrapper

connection.clients.get_task_client().update_records(records, scope_identifier, hub_name, plan_id, timeline_id)
```


#### Return Type:
`:rtype: [TimelineRecord]`
## Get Test Client
### AddTestCasesToSuite
#### Description:
Add test cases to suite.

* `:param str project: Project ID or project name`
* `:param int plan_id: ID of the test plan that contains the suite.`
* `:param int suite_id: ID of the test suite to which the test cases must be added.`
* `:param str test_case_ids: IDs of the test cases to add to the suite. Ids are specified in comma separated format.`
#### Example usage:
```
connection.clients.get_test_client().add_test_cases_to_suite(project, plan_id, suite_id, test_case_ids)
```


#### Return Type:
`:rtype: [SuiteTestCase]`
### AddTestResultsToTestRun
#### Description:
Add test results to a test run.

* `:param [TestCaseResult] results: List of test results to add.`
* `:param str project: Project ID or project name`
* `:param int run_id: Test run ID into which test results to add.`
#### Example usage:
```
connection.clients.get_test_client().add_test_results_to_test_run(results, project, run_id)
```


#### Return Type:
`:rtype: [TestCaseResult]`
### CreateTestRun
#### Description:
Create new test run.

* `:param :class:<RunCreateModel> <azure.devops.v5_1.test.models.RunCreateModel> test_run: Run details RunCreateModel`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.test.models import RunCreateModel

connection.clients.get_test_client().create_test_run(test_run, project)
```


#### Return Type:
`:rtype: :class:<TestRun> <azure.devops.v5_1.test.models.TestRun>`
### DeleteTestRun
#### Description:
Delete a test run by its ID.

* `:param str project: Project ID or project name`
* `:param int run_id: ID of the run to delete.`
#### Example usage:
```
connection.clients.get_test_client().delete_test_run(project, run_id)
```


#### Return Type:
`:rtype: :class:<TestRun> <azure.devops.v5_1.test.models.TestRun>`
### GetActionResults
#### Description:
Gets the action results for an iteration in a test result.

* `:param str project: Project ID or project name`
* `:param int run_id: ID of the test run that contains the result.`
* `:param int test_case_result_id: ID of the test result that contains the iterations.`
* `:param int iteration_id: ID of the iteration that contains the actions.`
* `:param str action_path: Path of a specific action, used to get just that action.`
#### Example usage:
```
connection.clients.get_test_client().get_action_results(project, run_id, test_case_result_id, iteration_id, action_path=None)
```


#### Return Type:
`:rtype: [TestActionResultModel]`
### GetPoint
#### Description:
Get a test point.

* `:param str project: Project ID or project name`
* `:param int plan_id: ID of the test plan.`
* `:param int suite_id: ID of the suite that contains the point.`
* `:param int point_ids: ID of the test point to get.`
* `:param str wit_fields: Comma-separated list of work item field names.`
#### Example usage:
```
connection.clients.get_test_client().get_point(project, plan_id, suite_id, point_ids, wit_fields=None)
```


#### Return Type:
`:rtype: :class:<TestPoint> <azure.devops.v5_1.test.models.TestPoint>`
### GetPoints
#### Description:
Get a list of test points.

* `:param str project: Project ID or project name`
* `:param int plan_id: ID of the test plan.`
* `:param int suite_id: ID of the suite that contains the points.`
* `:param str wit_fields: Comma-separated list of work item field names.`
* `:param str configuration_id: Get test points for specific configuration.`
* `:param str test_case_id: Get test points for a specific test case, valid when configurationId is not set.`
* `:param str test_point_ids: Get test points for comma-separated list of test point IDs, valid only when configurationId and testCaseId are not set.`
* `:param bool include_point_details: Include all properties for the test point.`
* `:param int skip: Number of test points to skip..`
* `:param int top: Number of test points to return.`
#### Example usage:
```
connection.clients.get_test_client().get_points(project, plan_id, suite_id, wit_fields=None, configuration_id=None, test_case_id=None, test_point_ids=None, include_point_details=None, skip=None, top=None)
```


#### Return Type:
`:rtype: [TestPoint]`
### GetResultParameters
#### Description:
Get a list of parameterized results

* `:param str project: Project ID or project name`
* `:param int run_id: ID of the test run that contains the result.`
* `:param int test_case_result_id: ID of the test result that contains the iterations.`
* `:param int iteration_id: ID of the iteration that contains the parameterized results.`
* `:param str param_name: Name of the parameter.`
#### Example usage:
```
connection.clients.get_test_client().get_result_parameters(project, run_id, test_case_result_id, iteration_id, param_name=None)
```


#### Return Type:
`:rtype: [TestResultParameterModel]`
### GetTestCaseById
#### Description:
Get a specific test case in a test suite with test case id.

* `:param str project: Project ID or project name`
* `:param int plan_id: ID of the test plan that contains the suites.`
* `:param int suite_id: ID of the suite that contains the test case.`
* `:param int test_case_ids: ID of the test case to get.`
#### Example usage:
```
connection.clients.get_test_client().get_test_case_by_id(project, plan_id, suite_id, test_case_ids)
```


#### Return Type:
`:rtype: :class:<SuiteTestCase> <azure.devops.v5_1.test.models.SuiteTestCase>`
### GetTestCases
#### Description:
Get all test cases in a suite.

* `:param str project: Project ID or project name`
* `:param int plan_id: ID of the test plan that contains the suites.`
* `:param int suite_id: ID of the suite to get.`
#### Example usage:
```
connection.clients.get_test_client().get_test_cases(project, plan_id, suite_id)
```


#### Return Type:
`:rtype: [SuiteTestCase]`
### GetTestIteration
#### Description:
Get iteration for a result

* `:param str project: Project ID or project name`
* `:param int run_id: ID of the test run that contains the result.`
* `:param int test_case_result_id: ID of the test result that contains the iterations.`
* `:param int iteration_id: Id of the test results Iteration.`
* `:param bool include_action_results: Include result details for each action performed in the test iteration. ActionResults refer to outcome (pass/fail) of test steps that are executed as part of a running a manual test. Including the ActionResults flag gets the outcome of test steps in the actionResults section and test parameters in the parameters section for each test iteration.`
#### Example usage:
```
connection.clients.get_test_client().get_test_iteration(project, run_id, test_case_result_id, iteration_id, include_action_results=None)
```


#### Return Type:
`:rtype: :class:<TestIterationDetailsModel> <azure.devops.v5_1.test.models.TestIterationDetailsModel>`
### GetTestIterations
#### Description:
Get iterations for a result

* `:param str project: Project ID or project name`
* `:param int run_id: ID of the test run that contains the result.`
* `:param int test_case_result_id: ID of the test result that contains the iterations.`
* `:param bool include_action_results: Include result details for each action performed in the test iteration. ActionResults refer to outcome (pass/fail) of test steps that are executed as part of a running a manual test. Including the ActionResults flag gets the outcome of test steps in the actionResults section and test parameters in the parameters section for each test iteration.`
#### Example usage:
```
connection.clients.get_test_client().get_test_iterations(project, run_id, test_case_result_id, include_action_results=None)
```


#### Return Type:
`:rtype: [TestIterationDetailsModel]`
### GetTestResultById
#### Description:
Get a test result for a test run.

* `:param str project: Project ID or project name`
* `:param int run_id: Test run ID of a test result to fetch.`
* `:param int test_case_result_id: Test result ID.`
* `:param str details_to_include: Details to include with test results. Default is None. Other values are Iterations, WorkItems and SubResults.`
#### Example usage:
```
connection.clients.get_test_client().get_test_result_by_id(project, run_id, test_case_result_id, details_to_include=None)
```


#### Return Type:
`:rtype: :class:<TestCaseResult> <azure.devops.v5_1.test.models.TestCaseResult>`
### GetTestResults
#### Description:
Get test results for a test run.

* `:param str project: Project ID or project name`
* `:param int run_id: Test run ID of test results to fetch.`
* `:param str details_to_include: Details to include with test results. Default is None. Other values are Iterations and WorkItems.`
* `:param int skip: Number of test results to skip from beginning.`
* `:param int top: Number of test results to return. Maximum is 1000 when detailsToInclude is None and 200 otherwise.`
* `:param [TestOutcome] outcomes: Comma separated list of test outcomes to filter test results.`
#### Example usage:
```
connection.clients.get_test_client().get_test_results(project, run_id, details_to_include=None, skip=None, top=None, outcomes=None)
```


#### Return Type:
`:rtype: [TestCaseResult]`
### GetTestRunById
#### Description:
Get a test run by its ID.

* `:param str project: Project ID or project name`
* `:param int run_id: ID of the run to get.`
* `:param bool include_details: Default value is true. It includes details like run statistics, release, build, test environment, post process state, and more.`
#### Example usage:
```
connection.clients.get_test_client().get_test_run_by_id(project, run_id, include_details=None)
```


#### Return Type:
`:rtype: :class:<TestRun> <azure.devops.v5_1.test.models.TestRun>`
### GetTestRunStatistics
#### Description:
Get test run statistics , used when we want to get summary of a run by outcome.

* `:param str project: Project ID or project name`
* `:param int run_id: ID of the run to get.`
#### Example usage:
```
connection.clients.get_test_client().get_test_run_statistics(project, run_id)
```


#### Return Type:
`:rtype: :class:<TestRunStatistic> <azure.devops.v5_1.test.models.TestRunStatistic>`
### GetTestRuns
#### Description:
Get a list of test runs.

* `:param str project: Project ID or project name`
* `:param str build_uri: URI of the build that the runs used.`
* `:param str owner: Team foundation ID of the owner of the runs.`
* `:param str tmi_run_id:`
* `:param int plan_id: ID of the test plan that the runs are a part of.`
* `:param bool include_run_details: If true, include all the properties of the runs.`
* `:param bool automated: If true, only returns automated runs.`
* `:param int skip: Number of test runs to skip.`
* `:param int top: Number of test runs to return.`
#### Example usage:
```
connection.clients.get_test_client().get_test_runs(project, build_uri=None, owner=None, tmi_run_id=None, plan_id=None, include_run_details=None, automated=None, skip=None, top=None)
```


#### Return Type:
`:rtype: [TestRun]`
### QueryTestRuns
#### Description:
Query Test Runs based on filters. Mandatory fields are minLastUpdatedDate and maxLastUpdatedDate.

* `:param str project: Project ID or project name`
* `:param datetime min_last_updated_date: Minimum Last Modified Date of run to be queried (Mandatory).`
* `:param datetime max_last_updated_date: Maximum Last Modified Date of run to be queried (Mandatory, difference between min and max date can be atmost 7 days).`
* `:param str state: Current state of the Runs to be queried.`
* `:param [int] plan_ids: Plan Ids of the Runs to be queried, comma separated list of valid ids (limit no. of ids 10).`
* `:param bool is_automated: Automation type of the Runs to be queried.`
* `:param str publish_context: PublishContext of the Runs to be queried.`
* `:param [int] build_ids: Build Ids of the Runs to be queried, comma separated list of valid ids (limit no. of ids 10).`
* `:param [int] build_def_ids: Build Definition Ids of the Runs to be queried, comma separated list of valid ids (limit no. of ids 10).`
* `:param str branch_name: Source Branch name of the Runs to be queried.`
* `:param [int] release_ids: Release Ids of the Runs to be queried, comma separated list of valid ids (limit no. of ids 10).`
* `:param [int] release_def_ids: Release Definition Ids of the Runs to be queried, comma separated list of valid ids (limit no. of ids 10).`
* `:param [int] release_env_ids: Release Environment Ids of the Runs to be queried, comma separated list of valid ids (limit no. of ids 10).`
* `:param [int] release_env_def_ids: Release Environment Definition Ids of the Runs to be queried, comma separated list of valid ids (limit no. of ids 10).`
* `:param str run_title: Run Title of the Runs to be queried.`
* `:param int top: Number of runs to be queried. Limit is 100`
* `:param str continuation_token: continuationToken received from previous batch or null for first batch. It is not supposed to be created (or altered, if received from last batch) by user.`
#### Example usage:
```
connection.clients.get_test_client().query_test_runs(project, min_last_updated_date, max_last_updated_date, state=None, plan_ids=None, is_automated=None, publish_context=None, build_ids=None, build_def_ids=None, branch_name=None, release_ids=None, release_def_ids=None, release_env_ids=None, release_env_def_ids=None, run_title=None, top=None, continuation_token=None)
```


#### Return Type:
`:rtype: :class:<QueryTestRunsResponseValue>`
### RemoveTestCasesFromSuiteUrl
#### Description:
The test points associated with the test cases are removed from the test suite. The test case work item is not deleted from the system. See test cases resource to delete a test case permanently.

* `:param str project: Project ID or project name`
* `:param int plan_id: ID of the test plan that contains the suite.`
* `:param int suite_id: ID of the suite to get.`
* `:param str test_case_ids: IDs of the test cases to remove from the suite.`
#### Example usage:
```
connection.clients.get_test_client().remove_test_cases_from_suite_url(project, plan_id, suite_id, test_case_ids)
```


#### Return Type:
`:rtype: :class:<QueryTestRunsResponseValue>`
### UpdateSuiteTestCases
#### Description:
Updates the properties of the test case association in a suite.

* `:param :class:<SuiteTestCaseUpdateModel> <azure.devops.v5_1.test.models.SuiteTestCaseUpdateModel> suite_test_case_update_model: Model for updation of the properties of test case suite association.`
* `:param str project: Project ID or project name`
* `:param int plan_id: ID of the test plan that contains the suite.`
* `:param int suite_id: ID of the test suite to which the test cases must be added.`
* `:param str test_case_ids: IDs of the test cases to add to the suite. Ids are specified in comma separated format.`
#### Example usage:
```
from azure.devops.v5_1.test.models import SuiteTestCaseUpdateModel

connection.clients.get_test_client().update_suite_test_cases(suite_test_case_update_model, project, plan_id, suite_id, test_case_ids)
```


#### Return Type:
`:rtype: [SuiteTestCase]`
### UpdateTestPoints
#### Description:
Update test points.

* `:param :class:<PointUpdateModel> <azure.devops.v5_1.test.models.PointUpdateModel> point_update_model: Data to update.`
* `:param str project: Project ID or project name`
* `:param int plan_id: ID of the test plan.`
* `:param int suite_id: ID of the suite that contains the points.`
* `:param str point_ids: ID of the test point to get. Use a comma-separated list of IDs to update multiple test points.`
#### Example usage:
```
from azure.devops.v5_1.test.models import PointUpdateModel

connection.clients.get_test_client().update_test_points(point_update_model, project, plan_id, suite_id, point_ids)
```


#### Return Type:
`:rtype: [TestPoint]`
### UpdateTestResults
#### Description:
Update test results in a test run.

* `:param [TestCaseResult] results: List of test results to update.`
* `:param str project: Project ID or project name`
* `:param int run_id: Test run ID whose test results to update.`
#### Example usage:
```
connection.clients.get_test_client().update_test_results(results, project, run_id)
```


#### Return Type:
`:rtype: [TestCaseResult]`
### UpdateTestRun
#### Description:
Update test run by its ID.

* `:param :class:<RunUpdateModel> <azure.devops.v5_1.test.models.RunUpdateModel> run_update_model: Run details RunUpdateModel`
* `:param str project: Project ID or project name`
* `:param int run_id: ID of the run to update.`
#### Example usage:
```
from azure.devops.v5_1.test.models import RunUpdateModel

connection.clients.get_test_client().update_test_run(run_update_model, project, run_id)
```


#### Return Type:
`:rtype: :class:<TestRun> <azure.devops.v5_1.test.models.TestRun>`
## Get Test Plan Client
### GetSuitesByTestCaseId
#### Description:
Find the list of all test suites in which a given test case is present. This is helpful if you need to find out which test suites are using a test case, when you need to make changes to a test case.

* `:param int test_case_id: ID of the test case for which suites need to be fetched.`
#### Example usage:
```
connection.clients.get_test_plan_client().get_suites_by_test_case_id(test_case_id)
```


#### Return Type:
`:rtype: [TestSuite]`
## Get Test Results Client
### GetTestRunStatistics
#### Description:
Get test run statistics , used when we want to get summary of a run by outcome.

* `:param str project: Project ID or project name`
* `:param int run_id: ID of the run to get.`
#### Example usage:
```
connection.clients.get_test_results_client().get_test_run_statistics(project, run_id)
```


#### Return Type:
`:rtype: :class:<TestRunStatistic> <azure.devops.v5_1.test_results.models.TestRunStatistic>`
## Get Tfvc Client
### CreateChangeset
#### Description:
Create a new changeset.

* `:param :class:<TfvcChangeset> <azure.devops.v5_1.tfvc.models.TfvcChangeset> changeset:`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.tfvc.models import TfvcChangeset

connection.clients.get_tfvc_client().create_changeset(changeset, project=None)
```


#### Return Type:
`:rtype: :class:<TfvcChangesetRef> <azure.devops.v5_1.tfvc.models.TfvcChangesetRef>`
### GetBatchedChangesets
#### Description:
Returns changesets for a given list of changeset Ids.

* `:param :class:<TfvcChangesetsRequestData> <azure.devops.v5_1.tfvc.models.TfvcChangesetsRequestData> changesets_request_data: List of changeset IDs.`
#### Example usage:
```
from azure.devops.v5_1.tfvc.models import TfvcChangesetsRequestData

connection.clients.get_tfvc_client().get_batched_changesets(changesets_request_data)
```


#### Return Type:
`:rtype: [TfvcChangesetRef]`
### GetBranch
#### Description:
Get a single branch hierarchy at the given path with parents or children as specified.

* `:param str path: Full path to the branch.  Default: $/ Examples: $/, $/MyProject, $/MyProject/SomeFolder.`
* `:param str project: Project ID or project name`
* `:param bool include_parent: Return the parent branch, if there is one. Default: False`
* `:param bool include_children: Return child branches, if there are any. Default: False`
#### Example usage:
```
connection.clients.get_tfvc_client().get_branch(path, project=None, include_parent=None, include_children=None)
```


#### Return Type:
`:rtype: :class:<TfvcBranch> <azure.devops.v5_1.tfvc.models.TfvcBranch>`
### GetBranchRefs
#### Description:
Get branch hierarchies below the specified scopePath

* `:param str scope_path: Full path to the branch.  Default: $/ Examples: $/, $/MyProject, $/MyProject/SomeFolder.`
* `:param str project: Project ID or project name`
* `:param bool include_deleted: Return deleted branches. Default: False`
* `:param bool include_links: Return links. Default: False`
#### Example usage:
```
connection.clients.get_tfvc_client().get_branch_refs(scope_path, project=None, include_deleted=None, include_links=None)
```


#### Return Type:
`:rtype: [TfvcBranchRef]`
### GetBranches
#### Description:
Get a collection of branch roots -- first-level children, branches with no parents.

* `:param str project: Project ID or project name`
* `:param bool include_parent: Return the parent branch, if there is one. Default: False`
* `:param bool include_children: Return the child branches for each root branch. Default: False`
* `:param bool include_deleted: Return deleted branches. Default: False`
* `:param bool include_links: Return links. Default: False`
#### Example usage:
```
connection.clients.get_tfvc_client().get_branches(project=None, include_parent=None, include_children=None, include_deleted=None, include_links=None)
```


#### Return Type:
`:rtype: [TfvcBranch]`
### GetChangeset
#### Description:
Retrieve a Tfvc Changeset

* `:param int id: Changeset Id to retrieve.`
* `:param str project: Project ID or project name`
* `:param int max_change_count: Number of changes to return (maximum 100 changes) Default: 0`
* `:param bool include_details: Include policy details and check-in notes in the response. Default: false`
* `:param bool include_work_items: Include workitems. Default: false`
* `:param int max_comment_length: Include details about associated work items in the response. Default: null`
* `:param bool include_source_rename: Include renames.  Default: false`
* `:param int skip: Number of results to skip. Default: null`
* `:param int top: The maximum number of results to return. Default: null`
* `:param str orderby: Results are sorted by ID in descending order by default. Use id asc to sort by ID in ascending order.`
* `:param :class:<TfvcChangesetSearchCriteria> <azure.devops.v5_1.tfvc.models.TfvcChangesetSearchCriteria> search_criteria: Following criteria available (.itemPath, .version, .versionType, .versionOption, .author, .fromId, .toId, .fromDate, .toDate) Default: null`
#### Example usage:
```
from azure.devops.v5_1.tfvc.models import TfvcChangesetSearchCriteria

connection.clients.get_tfvc_client().get_changeset(id, project=None, max_change_count=None, include_details=None, include_work_items=None, max_comment_length=None, include_source_rename=None, skip=None, top=None, orderby=None, search_criteria=None)
```


#### Return Type:
`:rtype: :class:<TfvcChangeset> <azure.devops.v5_1.tfvc.models.TfvcChangeset>`
### GetChangesetChanges
#### Description:
Retrieve Tfvc changes for a given changeset.

* `:param int id: ID of the changeset. Default: null`
* `:param int skip: Number of results to skip. Default: null`
* `:param int top: The maximum number of results to return. Default: null`
* `:param str continuation_token: Return the next page of results. Default: null`
#### Example usage:
```
connection.clients.get_tfvc_client().get_changeset_changes(id=None, skip=None, top=None, continuation_token=None)
```


#### Return Type:
`:rtype: :class:<GetChangesetChangesResponseValue>`
### GetChangesetWorkItems
#### Description:
Retrieves the work items associated with a particular changeset.

* `:param int id: ID of the changeset. Default: null`
#### Example usage:
```
connection.clients.get_tfvc_client().get_changeset_work_items(id=None)
```


#### Return Type:
`:rtype: [AssociatedWorkItem]`
### GetChangesets
#### Description:
Retrieve Tfvc Changesets

* `:param str project: Project ID or project name`
* `:param int max_comment_length: Include details about associated work items in the response. Default: null`
* `:param int skip: Number of results to skip. Default: null`
* `:param int top: The maximum number of results to return. Default: null`
* `:param str orderby: Results are sorted by ID in descending order by default. Use id asc to sort by ID in ascending order.`
* `:param :class:<TfvcChangesetSearchCriteria> <azure.devops.v5_1.tfvc.models.TfvcChangesetSearchCriteria> search_criteria: Following criteria available (.itemPath, .version, .versionType, .versionOption, .author, .fromId, .toId, .fromDate, .toDate) Default: null`
#### Example usage:
```
from azure.devops.v5_1.tfvc.models import TfvcChangesetSearchCriteria

connection.clients.get_tfvc_client().get_changesets(project=None, max_comment_length=None, skip=None, top=None, orderby=None, search_criteria=None)
```


#### Return Type:
`:rtype: [TfvcChangesetRef]`
### GetItem
#### Description:
Get Item Metadata and/or Content for a single item. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content which is always returned as a download.

* `:param str path: Version control path of an individual item to return.`
* `:param str project: Project ID or project name`
* `:param str file_name: file name of item returned.`
* `:param bool download: If true, create a downloadable attachment.`
* `:param str scope_path: Version control path of a folder to return multiple items.`
* `:param str recursion_level: None (just the item), or OneLevel (contents of a folder).`
* `:param :class:<TfvcVersionDescriptor> <azure.devops.v5_1.tfvc.models.TfvcVersionDescriptor> version_descriptor: Version descriptor.  Default is null.`
* `:param bool include_content: Set to true to include item content when requesting json.  Default is false.`
#### Example usage:
```
from azure.devops.v5_1.tfvc.models import TfvcVersionDescriptor

connection.clients.get_tfvc_client().get_item(path, project=None, file_name=None, download=None, scope_path=None, recursion_level=None, version_descriptor=None, include_content=None)
```


#### Return Type:
`:rtype: :class:<TfvcItem> <azure.devops.v5_1.tfvc.models.TfvcItem>`
### GetItemContent
#### Description:
Get Item Metadata and/or Content for a single item. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content which is always returned as a download.

* `:param str path: Version control path of an individual item to return.`
* `:param str project: Project ID or project name`
* `:param str file_name: file name of item returned.`
* `:param bool download: If true, create a downloadable attachment.`
* `:param str scope_path: Version control path of a folder to return multiple items.`
* `:param str recursion_level: None (just the item), or OneLevel (contents of a folder).`
* `:param :class:<TfvcVersionDescriptor> <azure.devops.v5_1.tfvc.models.TfvcVersionDescriptor> version_descriptor: Version descriptor.  Default is null.`
* `:param bool include_content: Set to true to include item content when requesting json.  Default is false.`
#### Example usage:
```
from azure.devops.v5_1.tfvc.models import TfvcVersionDescriptor

connection.clients.get_tfvc_client().get_item_content(path, project=None, file_name=None, download=None, scope_path=None, recursion_level=None, version_descriptor=None, include_content=None, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetItemText
#### Description:
Get Item Metadata and/or Content for a single item. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content which is always returned as a download.

* `:param str path: Version control path of an individual item to return.`
* `:param str project: Project ID or project name`
* `:param str file_name: file name of item returned.`
* `:param bool download: If true, create a downloadable attachment.`
* `:param str scope_path: Version control path of a folder to return multiple items.`
* `:param str recursion_level: None (just the item), or OneLevel (contents of a folder).`
* `:param :class:<TfvcVersionDescriptor> <azure.devops.v5_1.tfvc.models.TfvcVersionDescriptor> version_descriptor: Version descriptor.  Default is null.`
* `:param bool include_content: Set to true to include item content when requesting json.  Default is false.`
#### Example usage:
```
from azure.devops.v5_1.tfvc.models import TfvcVersionDescriptor

connection.clients.get_tfvc_client().get_item_text(path, project=None, file_name=None, download=None, scope_path=None, recursion_level=None, version_descriptor=None, include_content=None, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetItemZip
#### Description:
Get Item Metadata and/or Content for a single item. The download parameter is to indicate whether the content should be available as a download or just sent as a stream in the response. Doesn't apply to zipped content which is always returned as a download.

* `:param str path: Version control path of an individual item to return.`
* `:param str project: Project ID or project name`
* `:param str file_name: file name of item returned.`
* `:param bool download: If true, create a downloadable attachment.`
* `:param str scope_path: Version control path of a folder to return multiple items.`
* `:param str recursion_level: None (just the item), or OneLevel (contents of a folder).`
* `:param :class:<TfvcVersionDescriptor> <azure.devops.v5_1.tfvc.models.TfvcVersionDescriptor> version_descriptor: Version descriptor.  Default is null.`
* `:param bool include_content: Set to true to include item content when requesting json.  Default is false.`
#### Example usage:
```
from azure.devops.v5_1.tfvc.models import TfvcVersionDescriptor

connection.clients.get_tfvc_client().get_item_zip(path, project=None, file_name=None, download=None, scope_path=None, recursion_level=None, version_descriptor=None, include_content=None, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetItems
#### Description:
Get a list of Tfvc items

* `:param str project: Project ID or project name`
* `:param str scope_path: Version control path of a folder to return multiple items.`
* `:param str recursion_level: None (just the item), or OneLevel (contents of a folder).`
* `:param bool include_links: True to include links.`
* `:param :class:<TfvcVersionDescriptor> <azure.devops.v5_1.tfvc.models.TfvcVersionDescriptor> version_descriptor:`
#### Example usage:
```
from azure.devops.v5_1.tfvc.models import TfvcVersionDescriptor

connection.clients.get_tfvc_client().get_items(project=None, scope_path=None, recursion_level=None, include_links=None, version_descriptor=None)
```


#### Return Type:
`:rtype: [TfvcItem]`
### GetItemsBatch
#### Description:
Post for retrieving a set of items given a list of paths or a long path. Allows for specifying the recursionLevel and version descriptors for each path.

* `:param :class:<TfvcItemRequestData> <azure.devops.v5_1.tfvc.models.TfvcItemRequestData> item_request_data:`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.tfvc.models import TfvcItemRequestData

connection.clients.get_tfvc_client().get_items_batch(item_request_data, project=None)
```


#### Return Type:
`:rtype: [[TfvcItem]]`
### GetItemsBatchZip
#### Description:
Post for retrieving a set of items given a list of paths or a long path. Allows for specifying the recursionLevel and version descriptors for each path.

* `:param :class:<TfvcItemRequestData> <azure.devops.v5_1.tfvc.models.TfvcItemRequestData> item_request_data:`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.tfvc.models import TfvcItemRequestData

connection.clients.get_tfvc_client().get_items_batch_zip(item_request_data, project=None, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetLabel
#### Description:
Get a single deep label.

* `:param str label_id: Unique identifier of label`
* `:param :class:<TfvcLabelRequestData> <azure.devops.v5_1.tfvc.models.TfvcLabelRequestData> request_data: maxItemCount`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.tfvc.models import TfvcLabelRequestData

connection.clients.get_tfvc_client().get_label(label_id, request_data, project=None)
```


#### Return Type:
`:rtype: :class:<TfvcLabel> <azure.devops.v5_1.tfvc.models.TfvcLabel>`
### GetLabelItems
#### Description:
Get items under a label.

* `:param str label_id: Unique identifier of label`
* `:param int top: Max number of items to return`
* `:param int skip: Number of items to skip`
#### Example usage:
```
connection.clients.get_tfvc_client().get_label_items(label_id, top=None, skip=None)
```


#### Return Type:
`:rtype: [TfvcItem]`
### GetLabels
#### Description:
Get a collection of shallow label references.

* `:param :class:<TfvcLabelRequestData> <azure.devops.v5_1.tfvc.models.TfvcLabelRequestData> request_data: labelScope, name, owner, and itemLabelFilter`
* `:param str project: Project ID or project name`
* `:param int top: Max number of labels to return, defaults to 100 when undefined`
* `:param int skip: Number of labels to skip`
#### Example usage:
```
from azure.devops.v5_1.tfvc.models import TfvcLabelRequestData

connection.clients.get_tfvc_client().get_labels(request_data, project=None, top=None, skip=None)
```


#### Return Type:
`:rtype: [TfvcLabelRef]`
### GetShelveset
#### Description:
Get a single deep shelveset.

* `:param str shelveset_id: Shelveset's unique ID`
* `:param :class:<TfvcShelvesetRequestData> <azure.devops.v5_1.tfvc.models.TfvcShelvesetRequestData> request_data: includeDetails, includeWorkItems, maxChangeCount, and maxCommentLength`
#### Example usage:
```
from azure.devops.v5_1.tfvc.models import TfvcShelvesetRequestData

connection.clients.get_tfvc_client().get_shelveset(shelveset_id, request_data=None)
```


#### Return Type:
`:rtype: :class:<TfvcShelveset> <azure.devops.v5_1.tfvc.models.TfvcShelveset>`
### GetShelvesetChanges
#### Description:
Get changes included in a shelveset.

* `:param str shelveset_id: Shelveset's unique ID`
* `:param int top: Max number of changes to return`
* `:param int skip: Number of changes to skip`
#### Example usage:
```
connection.clients.get_tfvc_client().get_shelveset_changes(shelveset_id, top=None, skip=None)
```


#### Return Type:
`:rtype: [TfvcChange]`
### GetShelvesetWorkItems
#### Description:
Get work items associated with a shelveset.

* `:param str shelveset_id: Shelveset's unique ID`
#### Example usage:
```
connection.clients.get_tfvc_client().get_shelveset_work_items(shelveset_id)
```


#### Return Type:
`:rtype: [AssociatedWorkItem]`
### GetShelvesets
#### Description:
Return a collection of shallow shelveset references.

* `:param :class:<TfvcShelvesetRequestData> <azure.devops.v5_1.tfvc.models.TfvcShelvesetRequestData> request_data: name, owner, and maxCommentLength`
* `:param int top: Max number of shelvesets to return`
* `:param int skip: Number of shelvesets to skip`
#### Example usage:
```
from azure.devops.v5_1.tfvc.models import TfvcShelvesetRequestData

connection.clients.get_tfvc_client().get_shelvesets(request_data=None, top=None, skip=None)
```


#### Return Type:
`:rtype: [TfvcShelvesetRef]`
## Get Wiki Client
### CreateAttachment
#### Description:
Creates an attachment in the wiki.

* `:param object upload_stream: Stream to upload`
* `:param str project: Project ID or project name`
* `:param str wiki_identifier: Wiki Id or name.`
* `:param str name: Wiki attachment name.`
* `:param :class:<GitVersionDescriptor> <azure.devops.v5_1.wiki.models.GitVersionDescriptor> version_descriptor: GitVersionDescriptor for the page. (Optional in case of ProjectWiki).`
#### Example usage:
```
from azure.devops.v5_1.wiki.models import GitVersionDescriptor

connection.clients.get_wiki_client().create_attachment(upload_stream, project, wiki_identifier, name, version_descriptor=None, **kwargs)
```


#### Return Type:
`:rtype: :class:<WikiAttachmentResponse> <azure.devops.v5_1.wiki.models.WikiAttachmentResponse>`
### CreateOrUpdatePage
#### Description:
Creates or edits a wiki page.

* `:param :class:<WikiPageCreateOrUpdateParameters> <azure.devops.v5_1.wiki.models.WikiPageCreateOrUpdateParameters> parameters: Wiki create or update operation parameters.`
* `:param str project: Project ID or project name`
* `:param str wiki_identifier: Wiki Id or name.`
* `:param str path: Wiki page path.`
* `:param String version: Version of the page on which the change is to be made. Mandatory for Edit scenario. To be populated in the If-Match header of the request.`
* `:param str comment: Comment to be associated with the page operation.`
* `:param :class:<GitVersionDescriptor> <azure.devops.v5_1.wiki.models.GitVersionDescriptor> version_descriptor: GitVersionDescriptor for the page. (Optional in case of ProjectWiki).`
#### Example usage:
```
from azure.devops.v5_1.wiki.models import WikiPageCreateOrUpdateParameters
from azure.devops.v5_1.wiki.models import GitVersionDescriptor

connection.clients.get_wiki_client().create_or_update_page(parameters, project, wiki_identifier, path, version, comment=None, version_descriptor=None)
```


#### Return Type:
`:rtype: :class:<WikiPageResponse> <azure.devops.v5_1.wiki.models.WikiPageResponse>`
### CreatePageMove
#### Description:
Creates a page move operation that updates the path and order of the page as provided in the parameters.

* `:param :class:<WikiPageMoveParameters> <azure.devops.v5_1.wiki.models.WikiPageMoveParameters> page_move_parameters: Page more operation parameters.`
* `:param str project: Project ID or project name`
* `:param str wiki_identifier: Wiki Id or name.`
* `:param str comment: Comment that is to be associated with this page move.`
* `:param :class:<GitVersionDescriptor> <azure.devops.v5_1.wiki.models.GitVersionDescriptor> version_descriptor: GitVersionDescriptor for the page. (Optional in case of ProjectWiki).`
#### Example usage:
```
from azure.devops.v5_1.wiki.models import WikiPageMoveParameters
from azure.devops.v5_1.wiki.models import GitVersionDescriptor

connection.clients.get_wiki_client().create_page_move(page_move_parameters, project, wiki_identifier, comment=None, version_descriptor=None)
```


#### Return Type:
`:rtype: :class:<WikiPageMoveResponse> <azure.devops.v5_1.wiki.models.WikiPageMoveResponse>`
### CreateWiki
#### Description:
Creates the wiki resource.

* `:param :class:<WikiCreateParametersV2> <azure.devops.v5_1.wiki.models.WikiCreateParametersV2> wiki_create_params: Parameters for the wiki creation.`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.wiki.models import WikiCreateParametersV2

connection.clients.get_wiki_client().create_wiki(wiki_create_params, project=None)
```


#### Return Type:
`:rtype: :class:<WikiV2> <azure.devops.v5_1.wiki.models.WikiV2>`
### DeletePage
#### Description:
Deletes a wiki page.

* `:param str project: Project ID or project name`
* `:param str wiki_identifier: Wiki Id or name.`
* `:param str path: Wiki page path.`
* `:param str comment: Comment to be associated with this page delete.`
* `:param :class:<GitVersionDescriptor> <azure.devops.v5_1.wiki.models.GitVersionDescriptor> version_descriptor: GitVersionDescriptor for the page. (Optional in case of ProjectWiki).`
#### Example usage:
```
from azure.devops.v5_1.wiki.models import GitVersionDescriptor

connection.clients.get_wiki_client().delete_page(project, wiki_identifier, path, comment=None, version_descriptor=None)
```


#### Return Type:
`:rtype: :class:<WikiPageResponse> <azure.devops.v5_1.wiki.models.WikiPageResponse>`
### DeleteWiki
#### Description:
Deletes the wiki corresponding to the wiki name or Id provided.

* `:param str wiki_identifier: Wiki name or Id.`
* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_wiki_client().delete_wiki(wiki_identifier, project=None)
```


#### Return Type:
`:rtype: :class:<WikiV2> <azure.devops.v5_1.wiki.models.WikiV2>`
### GetAllWikis
#### Description:
Gets all wikis in a project or collection.

* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_wiki_client().get_all_wikis(project=None)
```


#### Return Type:
`:rtype: [WikiV2]`
### GetPage
#### Description:
Gets metadata or content of the wiki page for the provided path. Content negotiation is done based on the `Accept` header sent in the request.

* `:param str project: Project ID or project name`
* `:param str wiki_identifier: Wiki Id or name.`
* `:param str path: Wiki page path.`
* `:param str recursion_level: Recursion level for subpages retrieval. Defaults to None (Optional).`
* `:param :class:<GitVersionDescriptor> <azure.devops.v5_1.wiki.models.GitVersionDescriptor> version_descriptor: GitVersionDescriptor for the page. Defaults to the default branch (Optional).`
* `:param bool include_content: True to include the content of the page in the response for Json content type. Defaults to false (Optional)`
#### Example usage:
```
from azure.devops.v5_1.wiki.models import GitVersionDescriptor

connection.clients.get_wiki_client().get_page(project, wiki_identifier, path=None, recursion_level=None, version_descriptor=None, include_content=None)
```


#### Return Type:
`:rtype: :class:<WikiPageResponse> <azure.devops.v5_1.wiki.models.WikiPageResponse>`
### GetPageText
#### Description:
Gets metadata or content of the wiki page for the provided path. Content negotiation is done based on the `Accept` header sent in the request.

* `:param str project: Project ID or project name`
* `:param str wiki_identifier: Wiki Id or name.`
* `:param str path: Wiki page path.`
* `:param str recursion_level: Recursion level for subpages retrieval. Defaults to None (Optional).`
* `:param :class:<GitVersionDescriptor> <azure.devops.v5_1.wiki.models.GitVersionDescriptor> version_descriptor: GitVersionDescriptor for the page. Defaults to the default branch (Optional).`
* `:param bool include_content: True to include the content of the page in the response for Json content type. Defaults to false (Optional)`
#### Example usage:
```
from azure.devops.v5_1.wiki.models import GitVersionDescriptor

connection.clients.get_wiki_client().get_page_text(project, wiki_identifier, path=None, recursion_level=None, version_descriptor=None, include_content=None, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetPageZip
#### Description:
Gets metadata or content of the wiki page for the provided path. Content negotiation is done based on the `Accept` header sent in the request.

* `:param str project: Project ID or project name`
* `:param str wiki_identifier: Wiki Id or name.`
* `:param str path: Wiki page path.`
* `:param str recursion_level: Recursion level for subpages retrieval. Defaults to None (Optional).`
* `:param :class:<GitVersionDescriptor> <azure.devops.v5_1.wiki.models.GitVersionDescriptor> version_descriptor: GitVersionDescriptor for the page. Defaults to the default branch (Optional).`
* `:param bool include_content: True to include the content of the page in the response for Json content type. Defaults to false (Optional)`
#### Example usage:
```
from azure.devops.v5_1.wiki.models import GitVersionDescriptor

connection.clients.get_wiki_client().get_page_zip(project, wiki_identifier, path=None, recursion_level=None, version_descriptor=None, include_content=None, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetWiki
#### Description:
Gets the wiki corresponding to the wiki name or Id provided.

* `:param str wiki_identifier: Wiki name or id.`
* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_wiki_client().get_wiki(wiki_identifier, project=None)
```


#### Return Type:
`:rtype: :class:<WikiV2> <azure.devops.v5_1.wiki.models.WikiV2>`
### UpdateWiki
#### Description:
Updates the wiki corresponding to the wiki Id or name provided using the update parameters.

* `:param :class:<WikiUpdateParameters> <azure.devops.v5_1.wiki.models.WikiUpdateParameters> update_parameters: Update parameters.`
* `:param str wiki_identifier: Wiki name or Id.`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.wiki.models import WikiUpdateParameters

connection.clients.get_wiki_client().update_wiki(update_parameters, wiki_identifier, project=None)
```


#### Return Type:
`:rtype: :class:<WikiV2> <azure.devops.v5_1.wiki.models.WikiV2>`
## Get Work Client
### CreatePlan
#### Description:
Add a new plan for the team

* `:param :class:<CreatePlan> <azure.devops.v5_1.work.models.CreatePlan> posted_plan: Plan definition`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.work.models import CreatePlan

connection.clients.get_work_client().create_plan(posted_plan, project)
```


#### Return Type:
`:rtype: :class:<Plan> <azure.devops.v5_1.work.models.Plan>`
### DeletePlan
#### Description:
Delete the specified plan

* `:param str project: Project ID or project name`
* `:param str id: Identifier of the plan`
#### Example usage:
```
connection.clients.get_work_client().delete_plan(project, id)
```


#### Return Type:
`:rtype: :class:<Plan> <azure.devops.v5_1.work.models.Plan>`
### DeleteTeamIteration
#### Description:
Delete a team's iteration by iterationId

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str id: ID of the iteration`
#### Example usage:
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().delete_team_iteration(team_context, id)
```


#### Return Type:
`:rtype: :class:<Plan> <azure.devops.v5_1.work.models.Plan>`
### GetBacklogConfigurations
#### Description:
Gets backlog configuration for a team

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
#### Example usage:
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_backlog_configurations(team_context)
```


#### Return Type:
`:rtype: :class:<BacklogConfiguration> <azure.devops.v5_1.work.models.BacklogConfiguration>`
### GetBoard
#### Description:
Get board

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str id: identifier for board, either board's backlog level name (Eg:"Stories") or Id`
#### Example usage:
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_board(team_context, id)
```


#### Return Type:
`:rtype: :class:<Board> <azure.devops.v5_1.work.models.Board>`
### GetBoardCardRuleSettings
#### Description:
Get board card Rule settings for the board id or board by name

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str board:`
#### Example usage:
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_board_card_rule_settings(team_context, board)
```


#### Return Type:
`:rtype: :class:<BoardCardRuleSettings> <azure.devops.v5_1.work.models.BoardCardRuleSettings>`
### GetBoardCardSettings
#### Description:
Get board card settings for the board id or board by name

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str board:`
#### Example usage:
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_board_card_settings(team_context, board)
```


#### Return Type:
`:rtype: :class:<BoardCardSettings> <azure.devops.v5_1.work.models.BoardCardSettings>`
### GetBoardChart
#### Description:
Get a board chart

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str board: Identifier for board, either board's backlog level name (Eg:"Stories") or Id`
* `:param str name: The chart name`
#### Example usage:
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_board_chart(team_context, board, name)
```


#### Return Type:
`:rtype: :class:<BoardChart> <azure.devops.v5_1.work.models.BoardChart>`
### GetBoardCharts
#### Description:
Get board charts

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str board: Identifier for board, either board's backlog level name (Eg:"Stories") or Id`
#### Example usage:
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_board_charts(team_context, board)
```


#### Return Type:
`:rtype: [BoardChartReference]`
### GetBoardColumns
#### Description:
Get columns on a board

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str board: Name or ID of the specific board`
#### Example usage:
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_board_columns(team_context, board)
```


#### Return Type:
`:rtype: [BoardColumn]`
### GetBoardRows
#### Description:
Get rows on a board

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str board: Name or ID of the specific board`
#### Example usage:
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_board_rows(team_context, board)
```


#### Return Type:
`:rtype: [BoardRow]`
### GetBoards
#### Description:
Get boards

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
#### Example usage:
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_boards(team_context)
```


#### Return Type:
`:rtype: [BoardReference]`
### GetCapacitiesWithIdentityRef
#### Description:
Get a team's capacity

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str iteration_id: ID of the iteration`
#### Example usage:
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_capacities_with_identity_ref(team_context, iteration_id)
```


#### Return Type:
`:rtype: [TeamMemberCapacityIdentityRef]`
### GetCapacityWithIdentityRef
#### Description:
Get a team member's capacity

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str iteration_id: ID of the iteration`
* `:param str team_member_id: ID of the team member`
#### Example usage:
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_capacity_with_identity_ref(team_context, iteration_id, team_member_id)
```


#### Return Type:
`:rtype: :class:<TeamMemberCapacityIdentityRef> <azure.devops.v5_1.work.models.TeamMemberCapacityIdentityRef>`
### GetColumnSuggestedValues
#### Description:
Get available board columns in a project

* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_work_client().get_column_suggested_values(project=None)
```


#### Return Type:
`:rtype: [BoardSuggestedValue]`
### GetDeliveryTimelineData
#### Description:
Get Delivery View Data

* `:param str project: Project ID or project name`
* `:param str id: Identifier for delivery view`
* `:param int revision: Revision of the plan for which you want data. If the current plan is a different revision you will get an ViewRevisionMismatchException exception. If you do not supply a revision you will get data for the latest revision.`
* `:param datetime start_date: The start date of timeline`
* `:param datetime end_date: The end date of timeline`
#### Example usage:
```
connection.clients.get_work_client().get_delivery_timeline_data(project, id, revision=None, start_date=None, end_date=None)
```


#### Return Type:
`:rtype: :class:<DeliveryViewData> <azure.devops.v5_1.work.models.DeliveryViewData>`
### GetPlan
#### Description:
Get the information for the specified plan

* `:param str project: Project ID or project name`
* `:param str id: Identifier of the plan`
#### Example usage:
```
connection.clients.get_work_client().get_plan(project, id)
```


#### Return Type:
`:rtype: :class:<Plan> <azure.devops.v5_1.work.models.Plan>`
### GetPlans
#### Description:
Get the information for all the plans configured for the given team

* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_work_client().get_plans(project)
```


#### Return Type:
`:rtype: [Plan]`
### GetRowSuggestedValues
#### Description:
Get available board rows in a project

* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_work_client().get_row_suggested_values(project=None)
```


#### Return Type:
`:rtype: [BoardSuggestedValue]`
### GetTeamDaysOff
#### Description:
Get team's days off for an iteration

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str iteration_id: ID of the iteration`
#### Example usage:
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_team_days_off(team_context, iteration_id)
```


#### Return Type:
`:rtype: :class:<TeamSettingsDaysOff> <azure.devops.v5_1.work.models.TeamSettingsDaysOff>`
### GetTeamFieldValues
#### Description:
Get a collection of team field values

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
#### Example usage:
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_team_field_values(team_context)
```


#### Return Type:
`:rtype: :class:<TeamFieldValues> <azure.devops.v5_1.work.models.TeamFieldValues>`
### GetTeamIteration
#### Description:
Get team's iteration by iterationId

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str id: ID of the iteration`
#### Example usage:
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_team_iteration(team_context, id)
```


#### Return Type:
`:rtype: :class:<TeamSettingsIteration> <azure.devops.v5_1.work.models.TeamSettingsIteration>`
### GetTeamIterations
#### Description:
Get a team's iterations using timeframe filter

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str timeframe: A filter for which iterations are returned based on relative time. Only Current is supported currently.`
#### Example usage:
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_team_iterations(team_context, timeframe=None)
```


#### Return Type:
`:rtype: [TeamSettingsIteration]`
### GetTeamSettings
#### Description:
Get a team's settings

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
#### Example usage:
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().get_team_settings(team_context)
```


#### Return Type:
`:rtype: :class:<TeamSetting> <azure.devops.v5_1.work.models.TeamSetting>`
### PostTeamIteration
#### Description:
Add an iteration to the team

* `:param :class:<TeamSettingsIteration> <azure.devops.v5_1.work.models.TeamSettingsIteration> iteration: Iteration to add`
* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
#### Example usage:
```
from azure.devops.v5_1.work.models import TeamSettingsIteration
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().post_team_iteration(iteration, team_context)
```


#### Return Type:
`:rtype: :class:<TeamSettingsIteration> <azure.devops.v5_1.work.models.TeamSettingsIteration>`
### ReplaceCapacitiesWithIdentityRef
#### Description:
Replace a team's capacity

* `:param [TeamMemberCapacityIdentityRef] capacities: Team capacity to replace`
* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str iteration_id: ID of the iteration`
#### Example usage:
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().replace_capacities_with_identity_ref(capacities, team_context, iteration_id)
```


#### Return Type:
`:rtype: [TeamMemberCapacityIdentityRef]`
### SetBoardOptions
#### Description:
Update board options

* `:param {str} options: options to updated`
* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str id: identifier for board, either category plural name (Eg:"Stories") or guid`
#### Example usage:
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().set_board_options(options, team_context, id)
```


#### Return Type:
`:rtype: {str}`
### UpdateBoardCardRuleSettings
#### Description:
Update board card Rule settings for the board id or board by name

* `:param :class:<BoardCardRuleSettings> <azure.devops.v5_1.work.models.BoardCardRuleSettings> board_card_rule_settings:`
* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str board:`
#### Example usage:
```
from azure.devops.v5_1.work.models import BoardCardRuleSettings
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().update_board_card_rule_settings(board_card_rule_settings, team_context, board)
```


#### Return Type:
`:rtype: :class:<BoardCardRuleSettings> <azure.devops.v5_1.work.models.BoardCardRuleSettings>`
### UpdateBoardCardSettings
#### Description:
Update board card settings for the board id or board by name

* `:param :class:<BoardCardSettings> <azure.devops.v5_1.work.models.BoardCardSettings> board_card_settings_to_save:`
* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str board:`
#### Example usage:
```
from azure.devops.v5_1.work.models import BoardCardSettings
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().update_board_card_settings(board_card_settings_to_save, team_context, board)
```


#### Return Type:
`:rtype: :class:<BoardCardSettings> <azure.devops.v5_1.work.models.BoardCardSettings>`
### UpdateBoardChart
#### Description:
Update a board chart

* `:param :class:<BoardChart> <azure.devops.v5_1.work.models.BoardChart> chart:`
* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str board: Identifier for board, either board's backlog level name (Eg:"Stories") or Id`
* `:param str name: The chart name`
#### Example usage:
```
from azure.devops.v5_1.work.models import BoardChart
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().update_board_chart(chart, team_context, board, name)
```


#### Return Type:
`:rtype: :class:<BoardChart> <azure.devops.v5_1.work.models.BoardChart>`
### UpdateBoardColumns
#### Description:
Update columns on a board

* `:param [BoardColumn] board_columns: List of board columns to update`
* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str board: Name or ID of the specific board`
#### Example usage:
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().update_board_columns(board_columns, team_context, board)
```


#### Return Type:
`:rtype: [BoardColumn]`
### UpdateBoardRows
#### Description:
Update rows on a board

* `:param [BoardRow] board_rows: List of board rows to update`
* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str board: Name or ID of the specific board`
#### Example usage:
```
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().update_board_rows(board_rows, team_context, board)
```


#### Return Type:
`:rtype: [BoardRow]`
### UpdateCapacityWithIdentityRef
#### Description:
Update a team member's capacity

* `:param :class:<CapacityPatch> <azure.devops.v5_1.work.models.CapacityPatch> patch: Updated capacity`
* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str iteration_id: ID of the iteration`
* `:param str team_member_id: ID of the team member`
#### Example usage:
```
from azure.devops.v5_1.work.models import CapacityPatch
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().update_capacity_with_identity_ref(patch, team_context, iteration_id, team_member_id)
```


#### Return Type:
`:rtype: :class:<TeamMemberCapacityIdentityRef> <azure.devops.v5_1.work.models.TeamMemberCapacityIdentityRef>`
### UpdatePlan
#### Description:
Update the information for the specified plan

* `:param :class:<UpdatePlan> <azure.devops.v5_1.work.models.UpdatePlan> updated_plan: Plan definition to be updated`
* `:param str project: Project ID or project name`
* `:param str id: Identifier of the plan`
#### Example usage:
```
from azure.devops.v5_1.work.models import UpdatePlan

connection.clients.get_work_client().update_plan(updated_plan, project, id)
```


#### Return Type:
`:rtype: :class:<Plan> <azure.devops.v5_1.work.models.Plan>`
### UpdateTeamDaysOff
#### Description:
Set a team's days off for an iteration

* `:param :class:<TeamSettingsDaysOffPatch> <azure.devops.v5_1.work.models.TeamSettingsDaysOffPatch> days_off_patch: Team's days off patch containing a list of start and end dates`
* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str iteration_id: ID of the iteration`
#### Example usage:
```
from azure.devops.v5_1.work.models import TeamSettingsDaysOffPatch
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().update_team_days_off(days_off_patch, team_context, iteration_id)
```


#### Return Type:
`:rtype: :class:<TeamSettingsDaysOff> <azure.devops.v5_1.work.models.TeamSettingsDaysOff>`
### UpdateTeamFieldValues
#### Description:
Update team field values

* `:param :class:<TeamFieldValuesPatch> <azure.devops.v5_1.work.models.TeamFieldValuesPatch> patch:`
* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
#### Example usage:
```
from azure.devops.v5_1.work.models import TeamFieldValuesPatch
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().update_team_field_values(patch, team_context)
```


#### Return Type:
`:rtype: :class:<TeamFieldValues> <azure.devops.v5_1.work.models.TeamFieldValues>`
### UpdateTeamSettings
#### Description:
Update a team's settings

* `:param :class:<TeamSettingsPatch> <azure.devops.v5_1.work.models.TeamSettingsPatch> team_settings_patch: TeamSettings changes`
* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
#### Example usage:
```
from azure.devops.v5_1.work.models import TeamSettingsPatch
from azure.devops.v5_1.work.models import TeamContext

connection.clients.get_work_client().update_team_settings(team_settings_patch, team_context)
```


#### Return Type:
`:rtype: :class:<TeamSetting> <azure.devops.v5_1.work.models.TeamSetting>`
## Get Work Item Tracking Client
### CreateAttachment
#### Description:
Uploads an attachment.

* `:param object upload_stream: Stream to upload`
* `:param str project: Project ID or project name`
* `:param str file_name: The name of the file`
* `:param str upload_type: Attachment upload type: Simple or Chunked`
* `:param str area_path: Target project Area Path`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().create_attachment(upload_stream, project=None, file_name=None, upload_type=None, area_path=None, **kwargs)
```


#### Return Type:
`:rtype: :class:<AttachmentReference> <azure.devops.v5_1.work_item_tracking.models.AttachmentReference>`
### CreateField
#### Description:
Create a new field.

* `:param :class:<WorkItemField> <azure.devops.v5_1.work_item_tracking.models.WorkItemField> work_item_field: New field definition`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.work_item_tracking.models import WorkItemField

connection.clients.get_work_item_tracking_client().create_field(work_item_field, project=None)
```


#### Return Type:
`:rtype: :class:<WorkItemField> <azure.devops.v5_1.work_item_tracking.models.WorkItemField>`
### CreateOrUpdateClassificationNode
#### Description:
Create new or update an existing classification node.

* `:param :class:<WorkItemClassificationNode> <azure.devops.v5_1.work_item_tracking.models.WorkItemClassificationNode> posted_node: Node to create or update.`
* `:param str project: Project ID or project name`
* `:param TreeStructureGroup structure_group: Structure group of the classification node, area or iteration.`
* `:param str path: Path of the classification node.`
#### Example usage:
```
from azure.devops.v5_1.work_item_tracking.models import WorkItemClassificationNode

connection.clients.get_work_item_tracking_client().create_or_update_classification_node(posted_node, project, structure_group, path=None)
```


#### Return Type:
`:rtype: :class:<WorkItemClassificationNode> <azure.devops.v5_1.work_item_tracking.models.WorkItemClassificationNode>`
### CreateQuery
#### Description:
Creates a query, or moves a query.

* `:param :class:<QueryHierarchyItem> <azure.devops.v5_1.work_item_tracking.models.QueryHierarchyItem> posted_query: The query to create.`
* `:param str project: Project ID or project name`
* `:param str query: The parent id or path under which the query is to be created.`
* `:param bool validate_wiql_only: If you only want to validate your WIQL query without actually creating one, set it to true. Default is false.`
#### Example usage:
```
from azure.devops.v5_1.work_item_tracking.models import QueryHierarchyItem

connection.clients.get_work_item_tracking_client().create_query(posted_query, project, query, validate_wiql_only=None)
```


#### Return Type:
`:rtype: :class:<QueryHierarchyItem> <azure.devops.v5_1.work_item_tracking.models.QueryHierarchyItem>`
### CreateWorkItem
#### Description:
Creates a single work item.

* `:param :class:<[JsonPatchOperation]> <azure.devops.v5_1.work_item_tracking.models.[JsonPatchOperation]> document: The JSON Patch document representing the work item`
* `:param str project: Project ID or project name`
* `:param str type: The work item type of the work item to create`
* `:param bool validate_only: Indicate if you only want to validate the changes without saving the work item`
* `:param bool bypass_rules: Do not enforce the work item type rules on this update`
* `:param bool suppress_notifications: Do not fire any notifications for this change`
* `:param str expand: The expand parameters for work item attributes. Possible options are { None, Relations, Fields, Links, All }.`
#### Example usage:
```
from azure.devops.v5_1.work_item_tracking.models import [JsonPatchOperation]

connection.clients.get_work_item_tracking_client().create_work_item(document, project, type, validate_only=None, bypass_rules=None, suppress_notifications=None, expand=None)
```


#### Return Type:
`:rtype: :class:<WorkItem> <azure.devops.v5_1.work_item_tracking.models.WorkItem>`
### DeleteClassificationNode
#### Description:
Delete an existing classification node.

* `:param str project: Project ID or project name`
* `:param TreeStructureGroup structure_group: Structure group of the classification node, area or iteration.`
* `:param str path: Path of the classification node.`
* `:param int reclassify_id: Id of the target classification node for reclassification.`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().delete_classification_node(project, structure_group, path=None, reclassify_id=None)
```


#### Return Type:
`:rtype: :class:<WorkItem> <azure.devops.v5_1.work_item_tracking.models.WorkItem>`
### DeleteField
#### Description:
Deletes the field.

* `:param str field_name_or_ref_name: Field simple name or reference name`
* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().delete_field(field_name_or_ref_name, project=None)
```


#### Return Type:
`:rtype: :class:<WorkItem> <azure.devops.v5_1.work_item_tracking.models.WorkItem>`
### DeleteQuery
#### Description:
Delete a query or a folder. This deletes any permission change on the deleted query or folder and any of its descendants if it is a folder. It is important to note that the deleted permission changes cannot be recovered upon undeleting the query or folder.

* `:param str project: Project ID or project name`
* `:param str query: ID or path of the query or folder to delete.`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().delete_query(project, query)
```


#### Return Type:
`:rtype: :class:<WorkItem> <azure.devops.v5_1.work_item_tracking.models.WorkItem>`
### DeleteWorkItem
#### Description:
Deletes the specified work item and sends it to the Recycle Bin, so that it can be restored back, if required. Optionally, if the destroy parameter has been set to true, it destroys the work item permanently. WARNING: If the destroy parameter is set to true, work items deleted by this command will NOT go to recycle-bin and there is no way to restore/recover them after deletion. It is recommended NOT to use this parameter. If you do, please use this parameter with extreme caution.

* `:param int id: ID of the work item to be deleted`
* `:param str project: Project ID or project name`
* `:param bool destroy: Optional parameter, if set to true, the work item is deleted permanently. Please note: the destroy action is PERMANENT and cannot be undone.`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().delete_work_item(id, project=None, destroy=None)
```


#### Return Type:
`:rtype: :class:<WorkItemDelete> <azure.devops.v5_1.work_item_tracking.models.WorkItemDelete>`
### DestroyWorkItem
#### Description:
Destroys the specified work item permanently from the Recycle Bin. This action can not be undone.

* `:param int id: ID of the work item to be destroyed permanently`
* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().destroy_work_item(id, project=None)
```


#### Return Type:
`:rtype: :class:<WorkItemDelete> <azure.devops.v5_1.work_item_tracking.models.WorkItemDelete>`
### GetAttachmentContent
#### Description:
Downloads an attachment.

* `:param str id: Attachment ID`
* `:param str project: Project ID or project name`
* `:param str file_name: Name of the file`
* `:param bool download: If set to <c>true</c> always download attachment`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_attachment_content(id, project=None, file_name=None, download=None, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetAttachmentZip
#### Description:
Downloads an attachment.

* `:param str id: Attachment ID`
* `:param str project: Project ID or project name`
* `:param str file_name: Name of the file`
* `:param bool download: If set to <c>true</c> always download attachment`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_attachment_zip(id, project=None, file_name=None, download=None, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetClassificationNode
#### Description:
Gets the classification node for a given node path.

* `:param str project: Project ID or project name`
* `:param TreeStructureGroup structure_group: Structure group of the classification node, area or iteration.`
* `:param str path: Path of the classification node.`
* `:param int depth: Depth of children to fetch.`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_classification_node(project, structure_group, path=None, depth=None)
```


#### Return Type:
`:rtype: :class:<WorkItemClassificationNode> <azure.devops.v5_1.work_item_tracking.models.WorkItemClassificationNode>`
### GetClassificationNodes
#### Description:
Gets root classification nodes or list of classification nodes for a given list of nodes ids, for a given project. In case ids parameter is supplied you will  get list of classification nodes for those ids. Otherwise you will get root classification nodes for this project.

* `:param str project: Project ID or project name`
* `:param [int] ids: Comma separated integer classification nodes ids. It's not required, if you want root nodes.`
* `:param int depth: Depth of children to fetch.`
* `:param str error_policy: Flag to handle errors in getting some nodes. Possible options are Fail and Omit.`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_classification_nodes(project, ids, depth=None, error_policy=None)
```


#### Return Type:
`:rtype: [WorkItemClassificationNode]`
### GetDeletedWorkItem
#### Description:
Gets a deleted work item from Recycle Bin.

* `:param int id: ID of the work item to be returned`
* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_deleted_work_item(id, project=None)
```


#### Return Type:
`:rtype: :class:<WorkItemDelete> <azure.devops.v5_1.work_item_tracking.models.WorkItemDelete>`
### GetDeletedWorkItemShallowReferences
#### Description:
Gets a list of the IDs and the URLs of the deleted the work items in the Recycle Bin.

* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_deleted_work_item_shallow_references(project=None)
```


#### Return Type:
`:rtype: [WorkItemDeleteShallowReference]`
### GetDeletedWorkItems
#### Description:
Gets the work items from the recycle bin, whose IDs have been specified in the parameters

* `:param [int] ids: Comma separated list of IDs of the deleted work items to be returned`
* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_deleted_work_items(ids, project=None)
```


#### Return Type:
`:rtype: [WorkItemDeleteReference]`
### GetField
#### Description:
Gets information on a specific field.

* `:param str field_name_or_ref_name: Field simple name or reference name`
* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_field(field_name_or_ref_name, project=None)
```


#### Return Type:
`:rtype: :class:<WorkItemField> <azure.devops.v5_1.work_item_tracking.models.WorkItemField>`
### GetFields
#### Description:
Returns information for all fields.

* `:param str project: Project ID or project name`
* `:param str expand: Use ExtensionFields to include extension fields, otherwise exclude them. Unless the feature flag for this parameter is enabled, extension fields are always included.`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_fields(project=None, expand=None)
```


#### Return Type:
`:rtype: [WorkItemField]`
### GetQueries
#### Description:
Gets the root queries and their children

* `:param str project: Project ID or project name`
* `:param str expand: Include the query string (wiql), clauses, query result columns, and sort options in the results.`
* `:param int depth: In the folder of queries, return child queries and folders to this depth.`
* `:param bool include_deleted: Include deleted queries and folders`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_queries(project, expand=None, depth=None, include_deleted=None)
```


#### Return Type:
`:rtype: [QueryHierarchyItem]`
### GetQueriesBatch
#### Description:
Gets a list of queries by ids (Maximum 1000)

* `:param :class:<QueryBatchGetRequest> <azure.devops.v5_1.work_item_tracking.models.QueryBatchGetRequest> query_get_request:`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.work_item_tracking.models import QueryBatchGetRequest

connection.clients.get_work_item_tracking_client().get_queries_batch(query_get_request, project)
```


#### Return Type:
`:rtype: [QueryHierarchyItem]`
### GetQuery
#### Description:
Retrieves an individual query and its children

* `:param str project: Project ID or project name`
* `:param str query: ID or path of the query.`
* `:param str expand: Include the query string (wiql), clauses, query result columns, and sort options in the results.`
* `:param int depth: In the folder of queries, return child queries and folders to this depth.`
* `:param bool include_deleted: Include deleted queries and folders`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_query(project, query, expand=None, depth=None, include_deleted=None)
```


#### Return Type:
`:rtype: :class:<QueryHierarchyItem> <azure.devops.v5_1.work_item_tracking.models.QueryHierarchyItem>`
### GetQueryResultCount
#### Description:
Gets the results of the query given the query ID.

* `:param str id: The query ID.`
* `:param :class:<TeamContext> <azure.devops.v5_1.work_item_tracking.models.TeamContext> team_context: The team context for the operation`
* `:param bool time_precision: Whether or not to use time precision.`
* `:param int top: The max number of results to return.`
#### Example usage:
```
from azure.devops.v5_1.work_item_tracking.models import TeamContext

connection.clients.get_work_item_tracking_client().get_query_result_count(id, team_context=None, time_precision=None, top=None)
```


#### Return Type:
`:rtype: int`
### GetRelationType
#### Description:
Gets the work item relation type definition.

* `:param str relation: The relation name`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_relation_type(relation)
```


#### Return Type:
`:rtype: :class:<WorkItemRelationType> <azure.devops.v5_1.work_item_tracking.models.WorkItemRelationType>`
### GetRelationTypes
#### Description:
Gets the work item relation types.

#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_relation_types()
```


#### Return Type:
`:rtype: [WorkItemRelationType]`
### GetReportingLinksByLinkType
#### Description:
Get a batch of work item links

* `:param str project: Project ID or project name`
* `:param [str] link_types: A list of types to filter the results to specific link types. Omit this parameter to get work item links of all link types.`
* `:param [str] types: A list of types to filter the results to specific work item types. Omit this parameter to get work item links of all work item types.`
* `:param str continuation_token: Specifies the continuationToken to start the batch from. Omit this parameter to get the first batch of links.`
* `:param datetime start_date_time: Date/time to use as a starting point for link changes. Only link changes that occurred after that date/time will be returned. Cannot be used in conjunction with 'watermark' parameter.`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_reporting_links_by_link_type(project=None, link_types=None, types=None, continuation_token=None, start_date_time=None)
```


#### Return Type:
`:rtype: :class:<ReportingWorkItemLinksBatch> <azure.devops.v5_1.work_item_tracking.models.ReportingWorkItemLinksBatch>`
### GetRevision
#### Description:
Returns a fully hydrated work item for the requested revision

* `:param int id:`
* `:param int revision_number:`
* `:param str project: Project ID or project name`
* `:param str expand:`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_revision(id, revision_number, project=None, expand=None)
```


#### Return Type:
`:rtype: :class:<WorkItem> <azure.devops.v5_1.work_item_tracking.models.WorkItem>`
### GetRevisions
#### Description:
Returns the list of fully hydrated work item revisions, paged.

* `:param int id:`
* `:param str project: Project ID or project name`
* `:param int top:`
* `:param int skip:`
* `:param str expand:`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_revisions(id, project=None, top=None, skip=None, expand=None)
```


#### Return Type:
`:rtype: [WorkItem]`
### GetRootNodes
#### Description:
Gets root classification nodes under the project.

* `:param str project: Project ID or project name`
* `:param int depth: Depth of children to fetch.`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_root_nodes(project, depth=None)
```


#### Return Type:
`:rtype: [WorkItemClassificationNode]`
### GetUpdate
#### Description:
Returns a single update for a work item

* `:param int id:`
* `:param int update_number:`
* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_update(id, update_number, project=None)
```


#### Return Type:
`:rtype: :class:<WorkItemUpdate> <azure.devops.v5_1.work_item_tracking.models.WorkItemUpdate>`
### GetUpdates
#### Description:
Returns a the deltas between work item revisions

* `:param int id:`
* `:param str project: Project ID or project name`
* `:param int top:`
* `:param int skip:`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_updates(id, project=None, top=None, skip=None)
```


#### Return Type:
`:rtype: [WorkItemUpdate]`
### GetWorkItem
#### Description:
Returns a single work item.

* `:param int id: The work item id`
* `:param str project: Project ID or project name`
* `:param [str] fields: Comma-separated list of requested fields`
* `:param datetime as_of: AsOf UTC date time string`
* `:param str expand: The expand parameters for work item attributes. Possible options are { None, Relations, Fields, Links, All }.`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_work_item(id, project=None, fields=None, as_of=None, expand=None)
```


#### Return Type:
`:rtype: :class:<WorkItem> <azure.devops.v5_1.work_item_tracking.models.WorkItem>`
### GetWorkItemIconJson
#### Description:
Get a work item icon given the friendly name and icon color.

* `:param str icon: The name of the icon`
* `:param str color: The 6-digit hex color for the icon`
* `:param int v: The version of the icon (used only for cache invalidation)`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_work_item_icon_json(icon, color=None, v=None)
```


#### Return Type:
`:rtype: :class:<WorkItemIcon> <azure.devops.v5_1.work_item_tracking.models.WorkItemIcon>`
### GetWorkItemIconSvg
#### Description:
Get a work item icon given the friendly name and icon color.

* `:param str icon: The name of the icon`
* `:param str color: The 6-digit hex color for the icon`
* `:param int v: The version of the icon (used only for cache invalidation)`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_work_item_icon_svg(icon, color=None, v=None, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetWorkItemIconXaml
#### Description:
Get a work item icon given the friendly name and icon color.

* `:param str icon: The name of the icon`
* `:param str color: The 6-digit hex color for the icon`
* `:param int v: The version of the icon (used only for cache invalidation)`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_work_item_icon_xaml(icon, color=None, v=None, **kwargs)
```


#### Return Type:
`:rtype: object`
### GetWorkItemIcons
#### Description:
Get a list of all work item icons.

#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_work_item_icons()
```


#### Return Type:
`:rtype: [WorkItemIcon]`
### GetWorkItemTemplate
#### Description:
Returns a single work item from a template.

* `:param str project: Project ID or project name`
* `:param str type: The work item type name`
* `:param str fields: Comma-separated list of requested fields`
* `:param datetime as_of: AsOf UTC date time string`
* `:param str expand: The expand parameters for work item attributes. Possible options are { None, Relations, Fields, Links, All }.`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_work_item_template(project, type, fields=None, as_of=None, expand=None)
```


#### Return Type:
`:rtype: :class:<WorkItem> <azure.devops.v5_1.work_item_tracking.models.WorkItem>`
### GetWorkItemType
#### Description:
Returns a work item type definition.

* `:param str project: Project ID or project name`
* `:param str type: Work item type name`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_work_item_type(project, type)
```


#### Return Type:
`:rtype: :class:<WorkItemType> <azure.devops.v5_1.work_item_tracking.models.WorkItemType>`
### GetWorkItemTypeCategories
#### Description:
Get all work item type categories.

* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_work_item_type_categories(project)
```


#### Return Type:
`:rtype: [WorkItemTypeCategory]`
### GetWorkItemTypeCategory
#### Description:
Get specific work item type category by name.

* `:param str project: Project ID or project name`
* `:param str category: The category name`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_work_item_type_category(project, category)
```


#### Return Type:
`:rtype: :class:<WorkItemTypeCategory> <azure.devops.v5_1.work_item_tracking.models.WorkItemTypeCategory>`
### GetWorkItemTypeFieldWithReferences
#### Description:
Get a field for a work item type with detailed references.

* `:param str project: Project ID or project name`
* `:param str type: Work item type.`
* `:param str field:`
* `:param str expand: Expand level for the API response. Properties: to include allowedvalues, default value, isRequired etc. as a part of response; None: to skip these properties.`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_work_item_type_field_with_references(project, type, field, expand=None)
```


#### Return Type:
`:rtype: :class:<WorkItemTypeFieldWithReferences> <azure.devops.v5_1.work_item_tracking.models.WorkItemTypeFieldWithReferences>`
### GetWorkItemTypeFieldsWithReferences
#### Description:
Get a list of fields for a work item type with detailed references.

* `:param str project: Project ID or project name`
* `:param str type: Work item type.`
* `:param str expand: Expand level for the API response. Properties: to include allowedvalues, default value, isRequired etc. as a part of response; None: to skip these properties.`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_work_item_type_fields_with_references(project, type, expand=None)
```


#### Return Type:
`:rtype: [WorkItemTypeFieldWithReferences]`
### GetWorkItemTypes
#### Description:
Returns the list of work item types

* `:param str project: Project ID or project name`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_work_item_types(project)
```


#### Return Type:
`:rtype: [WorkItemType]`
### GetWorkItems
#### Description:
Returns a list of work items (Maximum 200)

* `:param [int] ids: The comma-separated list of requested work item ids. (Maximum 200 ids allowed).`
* `:param str project: Project ID or project name`
* `:param [str] fields: Comma-separated list of requested fields`
* `:param datetime as_of: AsOf UTC date time string`
* `:param str expand: The expand parameters for work item attributes. Possible options are { None, Relations, Fields, Links, All }.`
* `:param str error_policy: The flag to control error policy in a bulk get work items request. Possible options are {Fail, Omit}.`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().get_work_items(ids, project=None, fields=None, as_of=None, expand=None, error_policy=None)
```


#### Return Type:
`:rtype: [WorkItem]`
### GetWorkItemsBatch
#### Description:
Gets work items for a list of work item ids (Maximum 200)

* `:param :class:<WorkItemBatchGetRequest> <azure.devops.v5_1.work_item_tracking.models.WorkItemBatchGetRequest> work_item_get_request:`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.work_item_tracking.models import WorkItemBatchGetRequest

connection.clients.get_work_item_tracking_client().get_work_items_batch(work_item_get_request, project=None)
```


#### Return Type:
`:rtype: [WorkItem]`
### QueryById
#### Description:
Gets the results of the query given the query ID.

* `:param str id: The query ID.`
* `:param :class:<TeamContext> <azure.devops.v5_1.work_item_tracking.models.TeamContext> team_context: The team context for the operation`
* `:param bool time_precision: Whether or not to use time precision.`
* `:param int top: The max number of results to return.`
#### Example usage:
```
from azure.devops.v5_1.work_item_tracking.models import TeamContext

connection.clients.get_work_item_tracking_client().query_by_id(id, team_context=None, time_precision=None, top=None)
```


#### Return Type:
`:rtype: :class:<WorkItemQueryResult> <azure.devops.v5_1.work_item_tracking.models.WorkItemQueryResult>`
### QueryByWiql
#### Description:
Gets the results of the query given its WIQL.

* `:param :class:<Wiql> <azure.devops.v5_1.work_item_tracking.models.Wiql> wiql: The query containing the WIQL.`
* `:param :class:<TeamContext> <azure.devops.v5_1.work_item_tracking.models.TeamContext> team_context: The team context for the operation`
* `:param bool time_precision: Whether or not to use time precision.`
* `:param int top: The max number of results to return.`
#### Example usage:
```
from azure.devops.v5_1.work_item_tracking.models import Wiql
from azure.devops.v5_1.work_item_tracking.models import TeamContext

connection.clients.get_work_item_tracking_client().query_by_wiql(wiql, team_context=None, time_precision=None, top=None)
```


#### Return Type:
`:rtype: :class:<WorkItemQueryResult> <azure.devops.v5_1.work_item_tracking.models.WorkItemQueryResult>`
### ReadReportingRevisionsGet
#### Description:
Get a batch of work item revisions with the option of including deleted items

* `:param str project: Project ID or project name`
* `:param [str] fields: A list of fields to return in work item revisions. Omit this parameter to get all reportable fields.`
* `:param [str] types: A list of types to filter the results to specific work item types. Omit this parameter to get work item revisions of all work item types.`
* `:param str continuation_token: Specifies the watermark to start the batch from. Omit this parameter to get the first batch of revisions.`
* `:param datetime start_date_time: Date/time to use as a starting point for revisions, all revisions will occur after this date/time. Cannot be used in conjunction with 'watermark' parameter.`
* `:param bool include_identity_ref: Return an identity reference instead of a string value for identity fields.`
* `:param bool include_deleted: Specify if the deleted item should be returned.`
* `:param bool include_tag_ref: Specify if the tag objects should be returned for System.Tags field.`
* `:param bool include_latest_only: Return only the latest revisions of work items, skipping all historical revisions`
* `:param str expand: Return all the fields in work item revisions, including long text fields which are not returned by default`
* `:param bool include_discussion_changes_only: Return only the those revisions of work items, where only history field was changed`
* `:param int max_page_size: The maximum number of results to return in this batch`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().read_reporting_revisions_get(project=None, fields=None, types=None, continuation_token=None, start_date_time=None, include_identity_ref=None, include_deleted=None, include_tag_ref=None, include_latest_only=None, expand=None, include_discussion_changes_only=None, max_page_size=None)
```


#### Return Type:
`:rtype: :class:<ReportingWorkItemRevisionsBatch> <azure.devops.v5_1.work_item_tracking.models.ReportingWorkItemRevisionsBatch>`
### ReadReportingRevisionsPost
#### Description:
Get a batch of work item revisions. This request may be used if your list of fields is large enough that it may run the URL over the length limit.

* `:param :class:<ReportingWorkItemRevisionsFilter> <azure.devops.v5_1.work_item_tracking.models.ReportingWorkItemRevisionsFilter> filter: An object that contains request settings: field filter, type filter, identity format`
* `:param str project: Project ID or project name`
* `:param str continuation_token: Specifies the watermark to start the batch from. Omit this parameter to get the first batch of revisions.`
* `:param datetime start_date_time: Date/time to use as a starting point for revisions, all revisions will occur after this date/time. Cannot be used in conjunction with 'watermark' parameter.`
* `:param str expand:`
#### Example usage:
```
from azure.devops.v5_1.work_item_tracking.models import ReportingWorkItemRevisionsFilter

connection.clients.get_work_item_tracking_client().read_reporting_revisions_post(filter, project=None, continuation_token=None, start_date_time=None, expand=None)
```


#### Return Type:
`:rtype: :class:<ReportingWorkItemRevisionsBatch> <azure.devops.v5_1.work_item_tracking.models.ReportingWorkItemRevisionsBatch>`
### RestoreWorkItem
#### Description:
Restores the deleted work item from Recycle Bin.

* `:param :class:<WorkItemDeleteUpdate> <azure.devops.v5_1.work_item_tracking.models.WorkItemDeleteUpdate> payload: Paylod with instructions to update the IsDeleted flag to false`
* `:param int id: ID of the work item to be restored`
* `:param str project: Project ID or project name`
#### Example usage:
```
from azure.devops.v5_1.work_item_tracking.models import WorkItemDeleteUpdate

connection.clients.get_work_item_tracking_client().restore_work_item(payload, id, project=None)
```


#### Return Type:
`:rtype: :class:<WorkItemDelete> <azure.devops.v5_1.work_item_tracking.models.WorkItemDelete>`
### SearchQueries
#### Description:
Searches all queries the user has access to in the current project

* `:param str project: Project ID or project name`
* `:param str filter: The text to filter the queries with.`
* `:param int top: The number of queries to return (Default is 50 and maximum is 200).`
* `:param str expand:`
* `:param bool include_deleted: Include deleted queries and folders`
#### Example usage:
```
connection.clients.get_work_item_tracking_client().search_queries(project, filter, top=None, expand=None, include_deleted=None)
```


#### Return Type:
`:rtype: :class:<QueryHierarchyItemsResult> <azure.devops.v5_1.work_item_tracking.models.QueryHierarchyItemsResult>`
### UpdateClassificationNode
#### Description:
Update an existing classification node.

* `:param :class:<WorkItemClassificationNode> <azure.devops.v5_1.work_item_tracking.models.WorkItemClassificationNode> posted_node: Node to create or update.`
* `:param str project: Project ID or project name`
* `:param TreeStructureGroup structure_group: Structure group of the classification node, area or iteration.`
* `:param str path: Path of the classification node.`
#### Example usage:
```
from azure.devops.v5_1.work_item_tracking.models import WorkItemClassificationNode

connection.clients.get_work_item_tracking_client().update_classification_node(posted_node, project, structure_group, path=None)
```


#### Return Type:
`:rtype: :class:<WorkItemClassificationNode> <azure.devops.v5_1.work_item_tracking.models.WorkItemClassificationNode>`
### UpdateQuery
#### Description:
Update a query or a folder. This allows you to update, rename and move queries and folders.

* `:param :class:<QueryHierarchyItem> <azure.devops.v5_1.work_item_tracking.models.QueryHierarchyItem> query_update: The query to update.`
* `:param str project: Project ID or project name`
* `:param str query: The ID or path for the query to update.`
* `:param bool undelete_descendants: Undelete the children of this folder. It is important to note that this will not bring back the permission changes that were previously applied to the descendants.`
#### Example usage:
```
from azure.devops.v5_1.work_item_tracking.models import QueryHierarchyItem

connection.clients.get_work_item_tracking_client().update_query(query_update, project, query, undelete_descendants=None)
```


#### Return Type:
`:rtype: :class:<QueryHierarchyItem> <azure.devops.v5_1.work_item_tracking.models.QueryHierarchyItem>`
### UpdateWorkItem
#### Description:
Updates a single work item.

* `:param :class:<[JsonPatchOperation]> <azure.devops.v5_1.work_item_tracking.models.[JsonPatchOperation]> document: The JSON Patch document representing the update`
* `:param int id: The id of the work item to update`
* `:param str project: Project ID or project name`
* `:param bool validate_only: Indicate if you only want to validate the changes without saving the work item`
* `:param bool bypass_rules: Do not enforce the work item type rules on this update`
* `:param bool suppress_notifications: Do not fire any notifications for this change`
* `:param str expand: The expand parameters for work item attributes. Possible options are { None, Relations, Fields, Links, All }.`
#### Example usage:
```
from azure.devops.v5_1.work_item_tracking.models import [JsonPatchOperation]

connection.clients.get_work_item_tracking_client().update_work_item(document, id, project=None, validate_only=None, bypass_rules=None, suppress_notifications=None, expand=None)
```


#### Return Type:
`:rtype: :class:<WorkItem> <azure.devops.v5_1.work_item_tracking.models.WorkItem>`