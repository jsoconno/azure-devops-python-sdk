# Azure DevOps SDK for Python
This repo is documents all of python-sdk clients as well as their methods and attributes.  It was created to help those looking to get started with this development kit by providing more information about each client to a new user and real world examples to help you get started.

For more information, check out the original repo here:
https://github.com/microsoft/azure-devops-python-api

# Table of Contents
* [Getting Started](#getting-started)
  * [Installing the SDK](#installing)
  * [Authenticating with an Azure DevOps PAT Token](#authenticating)
  * [Using a Client](#using)
* [Clients](#clients)
  * [Get Accounts Client](#get-accounts)
  * [Get Build Client](#get-build)
  * [Get Cloud Load Test Client](#get-cloud-load-test)
  * [Get Core Client](#get-core)
  * [Get Git Client](#get-git)
  * [Get Identity Client](#get-identity)
  * [Get Notification Client](#get-notification)
  * [Get Operations Client](#get-operations)
  * [Get Policy Client](#get-policy)
  * [Get Profile Client](#get-profile)
  * [Get Release Client](#get-release)
  * [Get Security Client](#get-security)
  * [Get Service Hooks Client](#get-service-hooks)
  * [Get Task Agent Client](#get-task-agent)
  * [Get Task Client](#get-task)
  * [Get Test Client](#get-test)
  * [Get Test Plan Client](#get-test-plan)
  * [Get Test Results Client](#get-test-results)
  * [Get Tfvc Client](#get-tfvc)
  * [Get Wiki Client](#get-wiki)
  * [Get Work Client](#get-work)
  * [Get Work Item Tracking Client](#get-work-item-tracking)

# Getting Started
## Installing the SDK
Open the terminal and type the following command:

`pip install azure-devops`

## Authenticating with an Azure DevOps PAT Token
To use the API, establish a connection using a personal access token and the URL to your Azure DevOps organization. Then get a client from the connection and make API calls.

```
from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import inspect

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
* `:rtype: [Account]`
#### Example usage:
`connection.clients.get_accounts_client().get_accounts(owner_id,member_id,properties)`


## Get Build Client
### AddBuildTag
#### Description:
Adds a tag to a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param str tag: The tag to add.`
* `:rtype: [str]`
#### Example usage:
`connection.clients.get_build_client().add_build_tag(project,build_id,tag)`


### AddBuildTags
#### Description:
Adds tags to a build.

* `:param [str] tags: The tags to add.`
* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:rtype: [str]`
#### Example usage:
`connection.clients.get_build_client().add_build_tags(tags,project,build_id)`


### CreateArtifact
#### Description:
Associates an artifact with a build.

* `:param :class:<BuildArtifact> <azure.devops.v5_1.build.models.BuildArtifact> artifact: The artifact.`
* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:rtype: :class:<BuildArtifact> <azure.devops.v5_1.build.models.BuildArtifact>`
#### Example usage:
`connection.clients.get_build_client().create_artifact(artifact,project,build_id)`


### CreateDefinition
#### Description:
Creates a new definition.

* `:param :class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition> definition: The definition.`
* `:param str project: Project ID or project name`
* `:param int definition_to_clone_id:`
* `:param int definition_to_clone_revision:`
* `:rtype: :class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition>`
#### Example usage:
`connection.clients.get_build_client().create_definition(definition,project,definition_to_clone_id,definition_to_clone_revision)`


### DeleteBuild
#### Description:
Deletes a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
#### Example usage:
`connection.clients.get_build_client().delete_build(project,build_id)`


### DeleteBuildTag
#### Description:
Removes a tag from a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param str tag: The tag to remove.`
* `:rtype: [str]`
#### Example usage:
`connection.clients.get_build_client().delete_build_tag(project,build_id,tag)`


### DeleteDefinition
#### Description:
Deletes a definition and all associated builds.

* `:param str project: Project ID or project name`
* `:param int definition_id: The ID of the definition.`
#### Example usage:
`connection.clients.get_build_client().delete_definition(project,definition_id)`


### DeleteTemplate
#### Description:
Deletes a build definition template.

* `:param str project: Project ID or project name`
* `:param str template_id: The ID of the template.`
#### Example usage:
`connection.clients.get_build_client().delete_template(project,template_id)`


### GetArtifact
#### Description:
Gets a specific artifact for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param str artifact_name: The name of the artifact.`
* `:rtype: :class:<BuildArtifact> <azure.devops.v5_1.build.models.BuildArtifact>`
#### Example usage:
`connection.clients.get_build_client().get_artifact(project,build_id,artifact_name)`


### GetArtifactContentZip
#### Description:
Gets a specific artifact for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param str artifact_name: The name of the artifact.`
* `:rtype: object`
#### Example usage:
`connection.clients.get_build_client().get_artifact_content_zip(project,build_id,artifact_name)`


### GetArtifacts
#### Description:
Gets all artifacts for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:rtype: [BuildArtifact]`
#### Example usage:
`connection.clients.get_build_client().get_artifacts(project,build_id)`


### GetBuild
#### Description:
Gets a build

* `:param str project: Project ID or project name`
* `:param int build_id:`
* `:param str property_filters:`
* `:rtype: :class:<Build> <azure.devops.v5_1.build.models.Build>`
#### Example usage:
`connection.clients.get_build_client().get_build(project,build_id,property_filters)`


### GetBuildChanges
#### Description:
Gets the changes associated with a build

* `:param str project: Project ID or project name`
* `:param int build_id:`
* `:param str continuation_token:`
* `:param int top: The maximum number of changes to return`
* `:param bool include_source_change:`
* `:rtype: :class:<GetBuildChangesResponseValue>`
#### Example usage:
`connection.clients.get_build_client().get_build_changes(project,build_id,continuation_token,top,include_source_change)`


### GetBuildController
#### Description:
Gets a controller

* `:param int controller_id:`
* `:rtype: :class:<BuildController> <azure.devops.v5_1.build.models.BuildController>`
#### Example usage:
`connection.clients.get_build_client().get_build_controller(controller_id)`


### GetBuildControllers
#### Description:
Gets controller, optionally filtered by name

* `:param str name:`
* `:rtype: [BuildController]`
#### Example usage:
`connection.clients.get_build_client().get_build_controllers(name)`


### GetBuildLog
#### Description:
Gets an individual log file for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param int log_id: The ID of the log file.`
* `:param long start_line: The start line.`
* `:param long end_line: The end line.`
* `:rtype: object`
#### Example usage:
`connection.clients.get_build_client().get_build_log(project,build_id,log_id,start_line,end_line)`


### GetBuildLogLines
#### Description:
Gets an individual log file for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param int log_id: The ID of the log file.`
* `:param long start_line: The start line.`
* `:param long end_line: The end line.`
* `:rtype: [str]`
#### Example usage:
`connection.clients.get_build_client().get_build_log_lines(project,build_id,log_id,start_line,end_line)`


### GetBuildLogZip
#### Description:
Gets an individual log file for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param int log_id: The ID of the log file.`
* `:param long start_line: The start line.`
* `:param long end_line: The end line.`
* `:rtype: object`
#### Example usage:
`connection.clients.get_build_client().get_build_log_zip(project,build_id,log_id,start_line,end_line)`


### GetBuildLogs
#### Description:
Gets the logs for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:rtype: [BuildLog]`
#### Example usage:
`connection.clients.get_build_client().get_build_logs(project,build_id)`


### GetBuildLogsZip
#### Description:
Gets the logs for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:rtype: object`
#### Example usage:
`connection.clients.get_build_client().get_build_logs_zip(project,build_id)`


### GetBuildOptionDefinitions
#### Description:
Gets all build definition options supported by the system.

* `:param str project: Project ID or project name`
* `:rtype: [BuildOptionDefinition]`
#### Example usage:
`connection.clients.get_build_client().get_build_option_definitions(project)`


### GetBuildSettings
#### Description:
Gets the build settings.

* `:param str project: Project ID or project name`
* `:rtype: :class:<BuildSettings> <azure.devops.v5_1.build.models.BuildSettings>`
#### Example usage:
`connection.clients.get_build_client().get_build_settings(project)`


### GetBuildTags
#### Description:
Gets the tags for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:rtype: [str]`
#### Example usage:
`connection.clients.get_build_client().get_build_tags(project,build_id)`


### GetBuildTimeline
#### Description:
Gets details for a build

* `:param str project: Project ID or project name`
* `:param int build_id:`
* `:param str timeline_id:`
* `:param int change_id:`
* `:param str plan_id:`
* `:rtype: :class:<Timeline> <azure.devops.v5_1.build.models.Timeline>`
#### Example usage:
`connection.clients.get_build_client().get_build_timeline(project,build_id,timeline_id,change_id,plan_id)`


### GetBuildWorkItemsRefs
#### Description:
Gets the work items associated with a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param int top: The maximum number of work items to return.`
* `:rtype: [ResourceRef]`
#### Example usage:
`connection.clients.get_build_client().get_build_work_items_refs(project,build_id,top)`


### GetBuildWorkItemsRefsFromCommits
#### Description:
Gets the work items associated with a build, filtered to specific commits.

* `:param [str] commit_ids: A comma-delimited list of commit IDs.`
* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param int top: The maximum number of work items to return, or the number of commits to consider if no commit IDs are specified.`
* `:rtype: [ResourceRef]`
#### Example usage:
`connection.clients.get_build_client().get_build_work_items_refs_from_commits(commit_ids,project,build_id,top)`


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
* `:rtype: :class:<GetBuildsResponseValue>`
#### Example usage:
`connection.clients.get_build_client().get_builds(project,definitions,queues,build_number,min_time,max_time,requested_for,reason_filter,status_filter,result_filter,tag_filters,properties,top,continuation_token,max_builds_per_definition,deleted_filter,query_order,branch_name,build_ids,repository_id,repository_type)`


### GetDefinition
#### Description:
Gets a definition, optionally at a specific revision.

* `:param str project: Project ID or project name`
* `:param int definition_id: The ID of the definition.`
* `:param int revision: The revision number to retrieve. If this is not specified, the latest version will be returned.`
* `:param datetime min_metrics_time: If specified, indicates the date from which metrics should be included.`
* `:param [str] property_filters: A comma-delimited list of properties to include in the results.`
* `:param bool include_latest_builds:`
* `:rtype: :class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition>`
#### Example usage:
`connection.clients.get_build_client().get_definition(project,definition_id,revision,min_metrics_time,property_filters,include_latest_builds)`


### GetDefinitionRevisions
#### Description:
Gets all revisions of a definition.

* `:param str project: Project ID or project name`
* `:param int definition_id: The ID of the definition.`
* `:rtype: [BuildDefinitionRevision]`
#### Example usage:
`connection.clients.get_build_client().get_definition_revisions(project,definition_id)`


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
* `:rtype: :class:<GetDefinitionsResponseValue>`
#### Example usage:
`connection.clients.get_build_client().get_definitions(project,name,repository_id,repository_type,query_order,top,continuation_token,min_metrics_time,definition_ids,path,built_after,not_built_after,include_all_properties,include_latest_builds,task_id_filter,process_type,yaml_filename)`


### GetFile
#### Description:
Gets a file from the build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param str artifact_name: The name of the artifact.`
* `:param str file_id: The primary key for the file.`
* `:param str file_name: The name that the file will be set to.`
* `:rtype: object`
#### Example usage:
`connection.clients.get_build_client().get_file(project,build_id,artifact_name,file_id,file_name)`


### GetTags
#### Description:
Gets a list of all build and definition tags in the project.

* `:param str project: Project ID or project name`
* `:rtype: [str]`
#### Example usage:
`connection.clients.get_build_client().get_tags(project)`


### GetTemplate
#### Description:
Gets a specific build definition template.

* `:param str project: Project ID or project name`
* `:param str template_id: The ID of the requested template.`
* `:rtype: :class:<BuildDefinitionTemplate> <azure.devops.v5_1.build.models.BuildDefinitionTemplate>`
#### Example usage:
`connection.clients.get_build_client().get_template(project,template_id)`


### GetTemplates
#### Description:
Gets all definition templates.

* `:param str project: Project ID or project name`
* `:rtype: [BuildDefinitionTemplate]`
#### Example usage:
`connection.clients.get_build_client().get_templates(project)`


### QueueBuild
#### Description:
Queues a build

* `:param :class:<Build> <azure.devops.v5_1.build.models.Build> build:`
* `:param str project: Project ID or project name`
* `:param bool ignore_warnings:`
* `:param str check_in_ticket:`
* `:param int source_build_id:`
* `:rtype: :class:<Build> <azure.devops.v5_1.build.models.Build>`
#### Example usage:
`connection.clients.get_build_client().queue_build(build,project,ignore_warnings,check_in_ticket,source_build_id)`


### RestoreDefinition
#### Description:
Restores a deleted definition

* `:param str project: Project ID or project name`
* `:param int definition_id: The identifier of the definition to restore.`
* `:param bool deleted: When false, restores a deleted definition.`
* `:rtype: :class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition>`
#### Example usage:
`connection.clients.get_build_client().restore_definition(project,definition_id,deleted)`


### SaveTemplate
#### Description:
Updates an existing build definition template.

* `:param :class:<BuildDefinitionTemplate> <azure.devops.v5_1.build.models.BuildDefinitionTemplate> template: The new version of the template.`
* `:param str project: Project ID or project name`
* `:param str template_id: The ID of the template.`
* `:rtype: :class:<BuildDefinitionTemplate> <azure.devops.v5_1.build.models.BuildDefinitionTemplate>`
#### Example usage:
`connection.clients.get_build_client().save_template(template,project,template_id)`


### UpdateBuild
#### Description:
Updates a build.

* `:param :class:<Build> <azure.devops.v5_1.build.models.Build> build: The build.`
* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param bool retry:`
* `:rtype: :class:<Build> <azure.devops.v5_1.build.models.Build>`
#### Example usage:
`connection.clients.get_build_client().update_build(build,project,build_id,retry)`


### UpdateBuildSettings
#### Description:
Updates the build settings.

* `:param :class:<BuildSettings> <azure.devops.v5_1.build.models.BuildSettings> settings: The new settings.`
* `:param str project: Project ID or project name`
* `:rtype: :class:<BuildSettings> <azure.devops.v5_1.build.models.BuildSettings>`
#### Example usage:
`connection.clients.get_build_client().update_build_settings(settings,project)`


### UpdateBuilds
#### Description:
Updates multiple builds.

* `:param [Build] builds: The builds to update.`
* `:param str project: Project ID or project name`
* `:rtype: [Build]`
#### Example usage:
`connection.clients.get_build_client().update_builds(builds,project)`


### UpdateDefinition
#### Description:
Updates an existing definition.

* `:param :class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition> definition: The new version of the definition.`
* `:param str project: Project ID or project name`
* `:param int definition_id: The ID of the definition.`
* `:param int secrets_source_definition_id:`
* `:param int secrets_source_definition_revision:`
* `:rtype: :class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition>`
#### Example usage:
`connection.clients.get_build_client().update_definition(definition,project,definition_id,secrets_source_definition_id,secrets_source_definition_revision)`


## Get Cloud Load Test Client
### AddBuildTag
#### Description:
Adds a tag to a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param str tag: The tag to add.`
* `:rtype: [str]`
#### Example usage:
`connection.clients.get_cloud_load_test_client().add_build_tag(project,build_id,tag)`


### AddBuildTags
#### Description:
Adds tags to a build.

* `:param [str] tags: The tags to add.`
* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:rtype: [str]`
#### Example usage:
`connection.clients.get_cloud_load_test_client().add_build_tags(tags,project,build_id)`


### CreateArtifact
#### Description:
Associates an artifact with a build.

* `:param :class:<BuildArtifact> <azure.devops.v5_1.build.models.BuildArtifact> artifact: The artifact.`
* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:rtype: :class:<BuildArtifact> <azure.devops.v5_1.build.models.BuildArtifact>`
#### Example usage:
`connection.clients.get_cloud_load_test_client().create_artifact(artifact,project,build_id)`


### CreateDefinition
#### Description:
Creates a new definition.

* `:param :class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition> definition: The definition.`
* `:param str project: Project ID or project name`
* `:param int definition_to_clone_id:`
* `:param int definition_to_clone_revision:`
* `:rtype: :class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition>`
#### Example usage:
`connection.clients.get_cloud_load_test_client().create_definition(definition,project,definition_to_clone_id,definition_to_clone_revision)`


### DeleteBuild
#### Description:
Deletes a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
#### Example usage:
`connection.clients.get_cloud_load_test_client().delete_build(project,build_id)`


### DeleteBuildTag
#### Description:
Removes a tag from a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param str tag: The tag to remove.`
* `:rtype: [str]`
#### Example usage:
`connection.clients.get_cloud_load_test_client().delete_build_tag(project,build_id,tag)`


### DeleteDefinition
#### Description:
Deletes a definition and all associated builds.

* `:param str project: Project ID or project name`
* `:param int definition_id: The ID of the definition.`
#### Example usage:
`connection.clients.get_cloud_load_test_client().delete_definition(project,definition_id)`


### DeleteTemplate
#### Description:
Deletes a build definition template.

* `:param str project: Project ID or project name`
* `:param str template_id: The ID of the template.`
#### Example usage:
`connection.clients.get_cloud_load_test_client().delete_template(project,template_id)`


### GetArtifact
#### Description:
Gets a specific artifact for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param str artifact_name: The name of the artifact.`
* `:rtype: :class:<BuildArtifact> <azure.devops.v5_1.build.models.BuildArtifact>`
#### Example usage:
`connection.clients.get_cloud_load_test_client().get_artifact(project,build_id,artifact_name)`


### GetArtifactContentZip
#### Description:
Gets a specific artifact for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param str artifact_name: The name of the artifact.`
* `:rtype: object`
#### Example usage:
`connection.clients.get_cloud_load_test_client().get_artifact_content_zip(project,build_id,artifact_name)`


### GetArtifacts
#### Description:
Gets all artifacts for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:rtype: [BuildArtifact]`
#### Example usage:
`connection.clients.get_cloud_load_test_client().get_artifacts(project,build_id)`


### GetBuild
#### Description:
Gets a build

* `:param str project: Project ID or project name`
* `:param int build_id:`
* `:param str property_filters:`
* `:rtype: :class:<Build> <azure.devops.v5_1.build.models.Build>`
#### Example usage:
`connection.clients.get_cloud_load_test_client().get_build(project,build_id,property_filters)`


### GetBuildChanges
#### Description:
Gets the changes associated with a build

* `:param str project: Project ID or project name`
* `:param int build_id:`
* `:param str continuation_token:`
* `:param int top: The maximum number of changes to return`
* `:param bool include_source_change:`
* `:rtype: :class:<GetBuildChangesResponseValue>`
#### Example usage:
`connection.clients.get_cloud_load_test_client().get_build_changes(project,build_id,continuation_token,top,include_source_change)`


### GetBuildController
#### Description:
Gets a controller

* `:param int controller_id:`
* `:rtype: :class:<BuildController> <azure.devops.v5_1.build.models.BuildController>`
#### Example usage:
`connection.clients.get_cloud_load_test_client().get_build_controller(controller_id)`


### GetBuildControllers
#### Description:
Gets controller, optionally filtered by name

* `:param str name:`
* `:rtype: [BuildController]`
#### Example usage:
`connection.clients.get_cloud_load_test_client().get_build_controllers(name)`


### GetBuildLog
#### Description:
Gets an individual log file for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param int log_id: The ID of the log file.`
* `:param long start_line: The start line.`
* `:param long end_line: The end line.`
* `:rtype: object`
#### Example usage:
`connection.clients.get_cloud_load_test_client().get_build_log(project,build_id,log_id,start_line,end_line)`


### GetBuildLogLines
#### Description:
Gets an individual log file for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param int log_id: The ID of the log file.`
* `:param long start_line: The start line.`
* `:param long end_line: The end line.`
* `:rtype: [str]`
#### Example usage:
`connection.clients.get_cloud_load_test_client().get_build_log_lines(project,build_id,log_id,start_line,end_line)`


### GetBuildLogZip
#### Description:
Gets an individual log file for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param int log_id: The ID of the log file.`
* `:param long start_line: The start line.`
* `:param long end_line: The end line.`
* `:rtype: object`
#### Example usage:
`connection.clients.get_cloud_load_test_client().get_build_log_zip(project,build_id,log_id,start_line,end_line)`


### GetBuildLogs
#### Description:
Gets the logs for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:rtype: [BuildLog]`
#### Example usage:
`connection.clients.get_cloud_load_test_client().get_build_logs(project,build_id)`


### GetBuildLogsZip
#### Description:
Gets the logs for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:rtype: object`
#### Example usage:
`connection.clients.get_cloud_load_test_client().get_build_logs_zip(project,build_id)`


### GetBuildOptionDefinitions
#### Description:
Gets all build definition options supported by the system.

* `:param str project: Project ID or project name`
* `:rtype: [BuildOptionDefinition]`
#### Example usage:
`connection.clients.get_cloud_load_test_client().get_build_option_definitions(project)`


### GetBuildSettings
#### Description:
Gets the build settings.

* `:param str project: Project ID or project name`
* `:rtype: :class:<BuildSettings> <azure.devops.v5_1.build.models.BuildSettings>`
#### Example usage:
`connection.clients.get_cloud_load_test_client().get_build_settings(project)`


### GetBuildTags
#### Description:
Gets the tags for a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:rtype: [str]`
#### Example usage:
`connection.clients.get_cloud_load_test_client().get_build_tags(project,build_id)`


### GetBuildTimeline
#### Description:
Gets details for a build

* `:param str project: Project ID or project name`
* `:param int build_id:`
* `:param str timeline_id:`
* `:param int change_id:`
* `:param str plan_id:`
* `:rtype: :class:<Timeline> <azure.devops.v5_1.build.models.Timeline>`
#### Example usage:
`connection.clients.get_cloud_load_test_client().get_build_timeline(project,build_id,timeline_id,change_id,plan_id)`


### GetBuildWorkItemsRefs
#### Description:
Gets the work items associated with a build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param int top: The maximum number of work items to return.`
* `:rtype: [ResourceRef]`
#### Example usage:
`connection.clients.get_cloud_load_test_client().get_build_work_items_refs(project,build_id,top)`


### GetBuildWorkItemsRefsFromCommits
#### Description:
Gets the work items associated with a build, filtered to specific commits.

* `:param [str] commit_ids: A comma-delimited list of commit IDs.`
* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param int top: The maximum number of work items to return, or the number of commits to consider if no commit IDs are specified.`
* `:rtype: [ResourceRef]`
#### Example usage:
`connection.clients.get_cloud_load_test_client().get_build_work_items_refs_from_commits(commit_ids,project,build_id,top)`


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
* `:rtype: :class:<GetBuildsResponseValue>`
#### Example usage:
`connection.clients.get_cloud_load_test_client().get_builds(project,definitions,queues,build_number,min_time,max_time,requested_for,reason_filter,status_filter,result_filter,tag_filters,properties,top,continuation_token,max_builds_per_definition,deleted_filter,query_order,branch_name,build_ids,repository_id,repository_type)`


### GetDefinition
#### Description:
Gets a definition, optionally at a specific revision.

* `:param str project: Project ID or project name`
* `:param int definition_id: The ID of the definition.`
* `:param int revision: The revision number to retrieve. If this is not specified, the latest version will be returned.`
* `:param datetime min_metrics_time: If specified, indicates the date from which metrics should be included.`
* `:param [str] property_filters: A comma-delimited list of properties to include in the results.`
* `:param bool include_latest_builds:`
* `:rtype: :class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition>`
#### Example usage:
`connection.clients.get_cloud_load_test_client().get_definition(project,definition_id,revision,min_metrics_time,property_filters,include_latest_builds)`


### GetDefinitionRevisions
#### Description:
Gets all revisions of a definition.

* `:param str project: Project ID or project name`
* `:param int definition_id: The ID of the definition.`
* `:rtype: [BuildDefinitionRevision]`
#### Example usage:
`connection.clients.get_cloud_load_test_client().get_definition_revisions(project,definition_id)`


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
* `:rtype: :class:<GetDefinitionsResponseValue>`
#### Example usage:
`connection.clients.get_cloud_load_test_client().get_definitions(project,name,repository_id,repository_type,query_order,top,continuation_token,min_metrics_time,definition_ids,path,built_after,not_built_after,include_all_properties,include_latest_builds,task_id_filter,process_type,yaml_filename)`


### GetFile
#### Description:
Gets a file from the build.

* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param str artifact_name: The name of the artifact.`
* `:param str file_id: The primary key for the file.`
* `:param str file_name: The name that the file will be set to.`
* `:rtype: object`
#### Example usage:
`connection.clients.get_cloud_load_test_client().get_file(project,build_id,artifact_name,file_id,file_name)`


### GetTags
#### Description:
Gets a list of all build and definition tags in the project.

* `:param str project: Project ID or project name`
* `:rtype: [str]`
#### Example usage:
`connection.clients.get_cloud_load_test_client().get_tags(project)`


### GetTemplate
#### Description:
Gets a specific build definition template.

* `:param str project: Project ID or project name`
* `:param str template_id: The ID of the requested template.`
* `:rtype: :class:<BuildDefinitionTemplate> <azure.devops.v5_1.build.models.BuildDefinitionTemplate>`
#### Example usage:
`connection.clients.get_cloud_load_test_client().get_template(project,template_id)`


### GetTemplates
#### Description:
Gets all definition templates.

* `:param str project: Project ID or project name`
* `:rtype: [BuildDefinitionTemplate]`
#### Example usage:
`connection.clients.get_cloud_load_test_client().get_templates(project)`


### QueueBuild
#### Description:
Queues a build

* `:param :class:<Build> <azure.devops.v5_1.build.models.Build> build:`
* `:param str project: Project ID or project name`
* `:param bool ignore_warnings:`
* `:param str check_in_ticket:`
* `:param int source_build_id:`
* `:rtype: :class:<Build> <azure.devops.v5_1.build.models.Build>`
#### Example usage:
`connection.clients.get_cloud_load_test_client().queue_build(build,project,ignore_warnings,check_in_ticket,source_build_id)`


### RestoreDefinition
#### Description:
Restores a deleted definition

* `:param str project: Project ID or project name`
* `:param int definition_id: The identifier of the definition to restore.`
* `:param bool deleted: When false, restores a deleted definition.`
* `:rtype: :class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition>`
#### Example usage:
`connection.clients.get_cloud_load_test_client().restore_definition(project,definition_id,deleted)`


### SaveTemplate
#### Description:
Updates an existing build definition template.

* `:param :class:<BuildDefinitionTemplate> <azure.devops.v5_1.build.models.BuildDefinitionTemplate> template: The new version of the template.`
* `:param str project: Project ID or project name`
* `:param str template_id: The ID of the template.`
* `:rtype: :class:<BuildDefinitionTemplate> <azure.devops.v5_1.build.models.BuildDefinitionTemplate>`
#### Example usage:
`connection.clients.get_cloud_load_test_client().save_template(template,project,template_id)`


### UpdateBuild
#### Description:
Updates a build.

* `:param :class:<Build> <azure.devops.v5_1.build.models.Build> build: The build.`
* `:param str project: Project ID or project name`
* `:param int build_id: The ID of the build.`
* `:param bool retry:`
* `:rtype: :class:<Build> <azure.devops.v5_1.build.models.Build>`
#### Example usage:
`connection.clients.get_cloud_load_test_client().update_build(build,project,build_id,retry)`


### UpdateBuildSettings
#### Description:
Updates the build settings.

* `:param :class:<BuildSettings> <azure.devops.v5_1.build.models.BuildSettings> settings: The new settings.`
* `:param str project: Project ID or project name`
* `:rtype: :class:<BuildSettings> <azure.devops.v5_1.build.models.BuildSettings>`
#### Example usage:
`connection.clients.get_cloud_load_test_client().update_build_settings(settings,project)`


### UpdateBuilds
#### Description:
Updates multiple builds.

* `:param [Build] builds: The builds to update.`
* `:param str project: Project ID or project name`
* `:rtype: [Build]`
#### Example usage:
`connection.clients.get_cloud_load_test_client().update_builds(builds,project)`


### UpdateDefinition
#### Description:
Updates an existing definition.

* `:param :class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition> definition: The new version of the definition.`
* `:param str project: Project ID or project name`
* `:param int definition_id: The ID of the definition.`
* `:param int secrets_source_definition_id:`
* `:param int secrets_source_definition_revision:`
* `:rtype: :class:<BuildDefinition> <azure.devops.v5_1.build.models.BuildDefinition>`
#### Example usage:
`connection.clients.get_cloud_load_test_client().update_definition(definition,project,definition_id,secrets_source_definition_id,secrets_source_definition_revision)`


## Get Core Client
### CreateTeam
#### Description:
Create a team in a team project.

* `:param :class:<WebApiTeam> <azure.devops.v5_1.core.models.WebApiTeam> team: The team data used to create the team.`
* `:param str project_id: The name or ID (GUID) of the team project in which to create the team.`
* `:rtype: :class:<WebApiTeam> <azure.devops.v5_1.core.models.WebApiTeam>`
#### Example usage:
`connection.clients.get_core_client().create_team(team,project_id)`


### DeleteTeam
#### Description:
Delete a team.

* `:param str project_id: The name or ID (GUID) of the team project containing the team to delete.`
* `:param str team_id: The name or ID of the team to delete.`
#### Example usage:
`connection.clients.get_core_client().delete_team(project_id,team_id)`


### GetProcessById
#### Description:
Get a process by ID.

* `:param str process_id: ID for a process.`
* `:rtype: :class:<Process> <azure.devops.v5_1.core.models.Process>`
#### Example usage:
`connection.clients.get_core_client().get_process_by_id(process_id)`


### GetProcesses
#### Description:
Get a list of processes.

* `:rtype: [Process]`
#### Example usage:
`connection.clients.get_core_client().get_processes()`


### GetProject
#### Description:
Get project with the specified id or name, optionally including capabilities.

* `:param str project_id:`
* `:param bool include_capabilities: Include capabilities (such as source control) in the team project result (default: false).`
* `:param bool include_history: Search within renamed projects (that had such name in the past).`
* `:rtype: :class:<TeamProject> <azure.devops.v5_1.core.models.TeamProject>`
#### Example usage:
`connection.clients.get_core_client().get_project(project_id,include_capabilities,include_history)`


### GetProjectCollection
#### Description:
Get project collection with the specified id or name.

* `:param str collection_id:`
* `:rtype: :class:<TeamProjectCollection> <azure.devops.v5_1.core.models.TeamProjectCollection>`
#### Example usage:
`connection.clients.get_core_client().get_project_collection(collection_id)`


### GetProjectCollections
#### Description:
Get project collection references for this application.

* `:param int top:`
* `:param int skip:`
* `:rtype: [TeamProjectCollectionReference]`
#### Example usage:
`connection.clients.get_core_client().get_project_collections(top,skip)`


### GetProjects
#### Description:
Get all projects in the organization that the authenticated user has access to.

* `:param str state_filter: Filter on team projects in a specific team project state (default: WellFormed).`
* `:param int top:`
* `:param int skip:`
* `:param str continuation_token:`
* `:param bool get_default_team_image_url:`
* `:rtype: :class:<GetProjectsResponseValue>`
#### Example usage:
`connection.clients.get_core_client().get_projects(state_filter,top,skip,continuation_token,get_default_team_image_url)`


### GetTeam
#### Description:
Get a specific team.

* `:param str project_id: The name or ID (GUID) of the team project containing the team.`
* `:param str team_id: The name or ID (GUID) of the team.`
* `:param bool expand_identity: A value indicating whether or not to expand Identity information in the result WebApiTeam object.`
* `:rtype: :class:<WebApiTeam> <azure.devops.v5_1.core.models.WebApiTeam>`
#### Example usage:
`connection.clients.get_core_client().get_team(project_id,team_id,expand_identity)`


### GetTeamMembersWithExtendedProperties
#### Description:
Get a list of members for a specific team.

* `:param str project_id: The name or ID (GUID) of the team project the team belongs to.`
* `:param str team_id: The name or ID (GUID) of the team .`
* `:param int top:`
* `:param int skip:`
* `:rtype: [TeamMember]`
#### Example usage:
`connection.clients.get_core_client().get_team_members_with_extended_properties(project_id,team_id,top,skip)`


### GetTeams
#### Description:
Get a list of teams.

* `:param str project_id:`
* `:param bool mine: If true return all the teams requesting user is member, otherwise return all the teams user has read access.`
* `:param int top: Maximum number of teams to return.`
* `:param int skip: Number of teams to skip.`
* `:param bool expand_identity: A value indicating whether or not to expand Identity information in the result WebApiTeam object.`
* `:rtype: [WebApiTeam]`
#### Example usage:
`connection.clients.get_core_client().get_teams(project_id,mine,top,skip,expand_identity)`


### QueueCreateProject
#### Description:
Queues a project to be created. Use the [GetOperation](../../operations/operations/get) to periodically check for create project status.

* `:param :class:<TeamProject> <azure.devops.v5_1.core.models.TeamProject> project_to_create: The project to create.`
* `:rtype: :class:<OperationReference> <azure.devops.v5_1.core.models.OperationReference>`
#### Example usage:
`connection.clients.get_core_client().queue_create_project(project_to_create)`


### QueueDeleteProject
#### Description:
Queues a project to be deleted. Use the [GetOperation](../../operations/operations/get) to periodically check for delete project status.

* `:param str project_id: The project id of the project to delete.`
* `:rtype: :class:<OperationReference> <azure.devops.v5_1.core.models.OperationReference>`
#### Example usage:
`connection.clients.get_core_client().queue_delete_project(project_id)`


### UpdateProject
#### Description:
Update an existing project's name, abbreviation, description, or restore a project.

* `:param :class:<TeamProject> <azure.devops.v5_1.core.models.TeamProject> project_update: The updates for the project. The state must be set to wellFormed to restore the project.`
* `:param str project_id: The project id of the project to update.`
* `:rtype: :class:<OperationReference> <azure.devops.v5_1.core.models.OperationReference>`
#### Example usage:
`connection.clients.get_core_client().update_project(project_update,project_id)`


### UpdateTeam
#### Description:
Update a team's name and/or description.

* `:param :class:<WebApiTeam> <azure.devops.v5_1.core.models.WebApiTeam> team_data:`
* `:param str project_id: The name or ID (GUID) of the team project containing the team to update.`
* `:param str team_id: The name of ID of the team to update.`
* `:rtype: :class:<WebApiTeam> <azure.devops.v5_1.core.models.WebApiTeam>`
#### Example usage:
`connection.clients.get_core_client().update_team(team_data,project_id,team_id)`


## Get Git Client
### CreateComment
#### Description:
Create a comment on a specific thread in a pull request (up to 500 comments can be created per thread).

* `:param :class:<Comment> <azure.devops.v5_1.git.models.Comment> comment: The comment to create. Comments can be up to 150,000 characters.`
* `:param str repository_id: The repository ID of the pull request's target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param int thread_id: ID of the thread that the desired comment is in.`
* `:param str project: Project ID or project name`
* `:rtype: :class:<Comment> <azure.devops.v5_1.git.models.Comment>`
#### Example usage:
`connection.clients.get_git_client().create_comment(comment,repository_id,pull_request_id,thread_id,project)`


### CreateCommitStatus
#### Description:
Create Git commit status.

* `:param :class:<GitStatus> <azure.devops.v5_1.git.models.GitStatus> git_commit_status_to_create: Git commit status object to create.`
* `:param str commit_id: ID of the Git commit.`
* `:param str repository_id: ID of the repository.`
* `:param str project: Project ID or project name`
* `:rtype: :class:<GitStatus> <azure.devops.v5_1.git.models.GitStatus>`
#### Example usage:
`connection.clients.get_git_client().create_commit_status(git_commit_status_to_create,commit_id,repository_id,project)`


### CreatePullRequest
#### Description:
Create a pull request.

* `:param :class:<GitPullRequest> <azure.devops.v5_1.git.models.GitPullRequest> git_pull_request_to_create: The pull request to create.`
* `:param str repository_id: The repository ID of the pull request's target branch.`
* `:param str project: Project ID or project name`
* `:param bool supports_iterations: If true, subsequent pushes to the pull request will be individually reviewable. Set this to false for large pull requests for performance reasons if this functionality is not needed.`
* `:rtype: :class:<GitPullRequest> <azure.devops.v5_1.git.models.GitPullRequest>`
#### Example usage:
`connection.clients.get_git_client().create_pull_request(git_pull_request_to_create,repository_id,project,supports_iterations)`


### CreatePullRequestReviewer
#### Description:
Add a reviewer to a pull request or cast a vote.

* `:param :class:<IdentityRefWithVote> <azure.devops.v5_1.git.models.IdentityRefWithVote> reviewer: Reviewer's vote.<br />If the reviewer's ID is included here, it must match the reviewerID parameter.<br />Reviewers can set their own vote with this method.  When adding other reviewers, vote must be set to zero.`
* `:param str repository_id: The repository ID of the pull request’s target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param str reviewer_id: ID of the reviewer.`
* `:param str project: Project ID or project name`
* `:rtype: :class:<IdentityRefWithVote> <azure.devops.v5_1.git.models.IdentityRefWithVote>`
#### Example usage:
`connection.clients.get_git_client().create_pull_request_reviewer(reviewer,repository_id,pull_request_id,reviewer_id,project)`


### CreatePullRequestReviewers
#### Description:
Add reviewers to a pull request.

* `:param [IdentityRef] reviewers: Reviewers to add to the pull request.`
* `:param str repository_id: The repository ID of the pull request’s target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param str project: Project ID or project name`
* `:rtype: [IdentityRefWithVote]`
#### Example usage:
`connection.clients.get_git_client().create_pull_request_reviewers(reviewers,repository_id,pull_request_id,project)`


### CreatePush
#### Description:
Push changes to the repository.

* `:param :class:<GitPush> <azure.devops.v5_1.git.models.GitPush> push:`
* `:param str repository_id: The name or ID of the repository.`
* `:param str project: Project ID or project name`
* `:rtype: :class:<GitPush> <azure.devops.v5_1.git.models.GitPush>`
#### Example usage:
`connection.clients.get_git_client().create_push(push,repository_id,project)`


### CreateRepository
#### Description:
Create a git repository in a team project.

* `:param :class:<GitRepositoryCreateOptions> <azure.devops.v5_1.git.models.GitRepositoryCreateOptions> git_repository_to_create: Specify the repo name, team project and/or parent repository. Team project information can be omitted from gitRepositoryToCreate if the request is project-scoped (i.e., includes project Id).`
* `:param str project: Project ID or project name`
* `:param str source_ref: [optional] Specify the source refs to use while creating a fork repo`
* `:rtype: :class:<GitRepository> <azure.devops.v5_1.git.models.GitRepository>`
#### Example usage:
`connection.clients.get_git_client().create_repository(git_repository_to_create,project,source_ref)`


### CreateThread
#### Description:
Create a thread in a pull request.

* `:param :class:<GitPullRequestCommentThread> <azure.devops.v5_1.git.models.GitPullRequestCommentThread> comment_thread: The thread to create. Thread must contain at least one comment.`
* `:param str repository_id: Repository ID of the pull request's target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param str project: Project ID or project name`
* `:rtype: :class:<GitPullRequestCommentThread> <azure.devops.v5_1.git.models.GitPullRequestCommentThread>`
#### Example usage:
`connection.clients.get_git_client().create_thread(comment_thread,repository_id,pull_request_id,project)`


### DeleteComment
#### Description:
Delete a comment associated with a specific thread in a pull request.

* `:param str repository_id: The repository ID of the pull request's target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param int thread_id: ID of the thread that the desired comment is in.`
* `:param int comment_id: ID of the comment.`
* `:param str project: Project ID or project name`
#### Example usage:
`connection.clients.get_git_client().delete_comment(repository_id,pull_request_id,thread_id,comment_id,project)`


### DeletePullRequestReviewer
#### Description:
Remove a reviewer from a pull request.

* `:param str repository_id: The repository ID of the pull request’s target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param str reviewer_id: ID of the reviewer to remove.`
* `:param str project: Project ID or project name`
#### Example usage:
`connection.clients.get_git_client().delete_pull_request_reviewer(repository_id,pull_request_id,reviewer_id,project)`


### DeleteRepository
#### Description:
Delete a git repository

* `:param str repository_id: The name or ID of the repository.`
* `:param str project: Project ID or project name`
#### Example usage:
`connection.clients.get_git_client().delete_repository(repository_id,project)`


### GetBlob
#### Description:
Get a single blob.

* `:param str repository_id: The name or ID of the repository.`
* `:param str sha1: SHA1 hash of the file. You can get the SHA1 of a file using the "Git/Items/Get Item" endpoint.`
* `:param str project: Project ID or project name`
* `:param bool download: If true, prompt for a download rather than rendering in a browser. Note: this value defaults to true if $format is zip`
* `:param str file_name: Provide a fileName to use for a download.`
* `:param bool resolve_lfs: If true, try to resolve a blob to its LFS contents, if it's an LFS pointer file. Only compatible with octet-stream Accept headers or $format types`
* `:rtype: :class:<GitBlobRef> <azure.devops.v5_1.git.models.GitBlobRef>`
#### Example usage:
`connection.clients.get_git_client().get_blob(repository_id,sha1,project,download,file_name,resolve_lfs)`


### GetBlobContent
#### Description:
Get a single blob.

* `:param str repository_id: The name or ID of the repository.`
* `:param str sha1: SHA1 hash of the file. You can get the SHA1 of a file using the "Git/Items/Get Item" endpoint.`
* `:param str project: Project ID or project name`
* `:param bool download: If true, prompt for a download rather than rendering in a browser. Note: this value defaults to true if $format is zip`
* `:param str file_name: Provide a fileName to use for a download.`
* `:param bool resolve_lfs: If true, try to resolve a blob to its LFS contents, if it's an LFS pointer file. Only compatible with octet-stream Accept headers or $format types`
* `:rtype: object`
#### Example usage:
`connection.clients.get_git_client().get_blob_content(repository_id,sha1,project,download,file_name,resolve_lfs)`


### GetBlobZip
#### Description:
Get a single blob.

* `:param str repository_id: The name or ID of the repository.`
* `:param str sha1: SHA1 hash of the file. You can get the SHA1 of a file using the "Git/Items/Get Item" endpoint.`
* `:param str project: Project ID or project name`
* `:param bool download: If true, prompt for a download rather than rendering in a browser. Note: this value defaults to true if $format is zip`
* `:param str file_name: Provide a fileName to use for a download.`
* `:param bool resolve_lfs: If true, try to resolve a blob to its LFS contents, if it's an LFS pointer file. Only compatible with octet-stream Accept headers or $format types`
* `:rtype: object`
#### Example usage:
`connection.clients.get_git_client().get_blob_zip(repository_id,sha1,project,download,file_name,resolve_lfs)`


### GetBlobsZip
#### Description:
Gets one or more blobs in a zip file download.

* `:param [str] blob_ids: Blob IDs (SHA1 hashes) to be returned in the zip file.`
* `:param str repository_id: The name or ID of the repository.`
* `:param str project: Project ID or project name`
* `:param str filename:`
* `:rtype: object`
#### Example usage:
`connection.clients.get_git_client().get_blobs_zip(blob_ids,repository_id,project,filename)`


### GetBranch
#### Description:
Retrieve statistics about a single branch.

* `:param str repository_id: The name or ID of the repository.`
* `:param str name: Name of the branch.`
* `:param str project: Project ID or project name`
* `:param :class:<GitVersionDescriptor> <azure.devops.v5_1.git.models.GitVersionDescriptor> base_version_descriptor: Identifies the commit or branch to use as the base.`
* `:rtype: :class:<GitBranchStats> <azure.devops.v5_1.git.models.GitBranchStats>`
#### Example usage:
`connection.clients.get_git_client().get_branch(repository_id,name,project,base_version_descriptor)`


### GetBranches
#### Description:
Retrieve statistics about all branches within a repository.

* `:param str repository_id: The name or ID of the repository.`
* `:param str project: Project ID or project name`
* `:param :class:<GitVersionDescriptor> <azure.devops.v5_1.git.models.GitVersionDescriptor> base_version_descriptor: Identifies the commit or branch to use as the base.`
* `:rtype: [GitBranchStats]`
#### Example usage:
`connection.clients.get_git_client().get_branches(repository_id,project,base_version_descriptor)`


### GetChanges
#### Description:
Retrieve changes for a particular commit.

* `:param str commit_id: The id of the commit.`
* `:param str repository_id: The id or friendly name of the repository. To use the friendly name, projectId must also be specified.`
* `:param str project: Project ID or project name`
* `:param int top: The maximum number of changes to return.`
* `:param int skip: The number of changes to skip.`
* `:rtype: :class:<GitCommitChanges> <azure.devops.v5_1.git.models.GitCommitChanges>`
#### Example usage:
`connection.clients.get_git_client().get_changes(commit_id,repository_id,project,top,skip)`


### GetComment
#### Description:
Retrieve a comment associated with a specific thread in a pull request.

* `:param str repository_id: The repository ID of the pull request's target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param int thread_id: ID of the thread that the desired comment is in.`
* `:param int comment_id: ID of the comment.`
* `:param str project: Project ID or project name`
* `:rtype: :class:<Comment> <azure.devops.v5_1.git.models.Comment>`
#### Example usage:
`connection.clients.get_git_client().get_comment(repository_id,pull_request_id,thread_id,comment_id,project)`


### GetComments
#### Description:
Retrieve all comments associated with a specific thread in a pull request.

* `:param str repository_id: The repository ID of the pull request's target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param int thread_id: ID of the thread.`
* `:param str project: Project ID or project name`
* `:rtype: [Comment]`
#### Example usage:
`connection.clients.get_git_client().get_comments(repository_id,pull_request_id,thread_id,project)`


### GetCommit
#### Description:
Retrieve a particular commit.

* `:param str commit_id: The id of the commit.`
* `:param str repository_id: The id or friendly name of the repository. To use the friendly name, projectId must also be specified.`
* `:param str project: Project ID or project name`
* `:param int change_count: The number of changes to include in the result.`
* `:rtype: :class:<GitCommit> <azure.devops.v5_1.git.models.GitCommit>`
#### Example usage:
`connection.clients.get_git_client().get_commit(commit_id,repository_id,project,change_count)`


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
* `:rtype: :class:<GitCommitDiffs> <azure.devops.v5_1.git.models.GitCommitDiffs>`
#### Example usage:
`connection.clients.get_git_client().get_commit_diffs(repository_id,project,diff_common_commit,top,skip,base_version_descriptor,target_version_descriptor)`


### GetCommits
#### Description:
Retrieve git commits for a project

* `:param str repository_id: The id or friendly name of the repository. To use the friendly name, projectId must also be specified.`
* `:param :class:<GitQueryCommitsCriteria> <azure.devops.v5_1.git.models.GitQueryCommitsCriteria> search_criteria:`
* `:param str project: Project ID or project name`
* `:param int skip:`
* `:param int top:`
* `:rtype: [GitCommitRef]`
#### Example usage:
`connection.clients.get_git_client().get_commits(repository_id,search_criteria,project,skip,top)`


### GetCommitsBatch
#### Description:
Retrieve git commits for a project matching the search criteria

* `:param :class:<GitQueryCommitsCriteria> <azure.devops.v5_1.git.models.GitQueryCommitsCriteria> search_criteria: Search options`
* `:param str repository_id: The name or ID of the repository.`
* `:param str project: Project ID or project name`
* `:param int skip: Number of commits to skip.`
* `:param int top: Maximum number of commits to return.`
* `:param bool include_statuses: True to include additional commit status information.`
* `:rtype: [GitCommitRef]`
#### Example usage:
`connection.clients.get_git_client().get_commits_batch(search_criteria,repository_id,project,skip,top,include_statuses)`


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
* `:rtype: :class:<GitItem> <azure.devops.v5_1.git.models.GitItem>`
#### Example usage:
`connection.clients.get_git_client().get_item(repository_id,path,project,scope_path,recursion_level,include_content_metadata,latest_processed_change,download,version_descriptor,include_content,resolve_lfs)`


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
* `:rtype: object`
#### Example usage:
`connection.clients.get_git_client().get_item_content(repository_id,path,project,scope_path,recursion_level,include_content_metadata,latest_processed_change,download,version_descriptor,include_content,resolve_lfs)`


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
* `:rtype: object`
#### Example usage:
`connection.clients.get_git_client().get_item_text(repository_id,path,project,scope_path,recursion_level,include_content_metadata,latest_processed_change,download,version_descriptor,include_content,resolve_lfs)`


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
* `:rtype: object`
#### Example usage:
`connection.clients.get_git_client().get_item_zip(repository_id,path,project,scope_path,recursion_level,include_content_metadata,latest_processed_change,download,version_descriptor,include_content,resolve_lfs)`


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
* `:rtype: [GitItem]`
#### Example usage:
`connection.clients.get_git_client().get_items(repository_id,project,scope_path,recursion_level,include_content_metadata,latest_processed_change,download,include_links,version_descriptor)`


### GetItemsBatch
#### Description:
Post for retrieving a creating a batch out of a set of items in a repo / project given a list of paths or a long path

* `:param :class:<GitItemRequestData> <azure.devops.v5_1.git.models.GitItemRequestData> request_data: Request data attributes: ItemDescriptors, IncludeContentMetadata, LatestProcessedChange, IncludeLinks. ItemDescriptors: Collection of items to fetch, including path, version, and recursion level. IncludeContentMetadata: Whether to include metadata for all items LatestProcessedChange: Whether to include shallow ref to commit that last changed each item. IncludeLinks: Whether to include the _links field on the shallow references.`
* `:param str repository_id: The name or ID of the repository`
* `:param str project: Project ID or project name`
* `:rtype: [[GitItem]]`
#### Example usage:
`connection.clients.get_git_client().get_items_batch(request_data,repository_id,project)`


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
* `:rtype: :class:<GitPullRequest> <azure.devops.v5_1.git.models.GitPullRequest>`
#### Example usage:
`connection.clients.get_git_client().get_pull_request(repository_id,pull_request_id,project,max_comment_length,skip,top,include_commits,include_work_item_refs)`


### GetPullRequestById
#### Description:
Retrieve a pull request.

* `:param int pull_request_id: The ID of the pull request to retrieve.`
* `:param str project: Project ID or project name`
* `:rtype: :class:<GitPullRequest> <azure.devops.v5_1.git.models.GitPullRequest>`
#### Example usage:
`connection.clients.get_git_client().get_pull_request_by_id(pull_request_id,project)`


### GetPullRequestCommits
#### Description:
Get the commits for the specified pull request.

* `:param str repository_id: ID or name of the repository.`
* `:param int pull_request_id: ID of the pull request.`
* `:param str project: Project ID or project name`
* `:param int top: Maximum number of commits to return.`
* `:param str continuation_token: The continuation token used for pagination.`
* `:rtype: :class:<GetPullRequestCommitsResponseValue>`
#### Example usage:
`connection.clients.get_git_client().get_pull_request_commits(repository_id,pull_request_id,project,top,continuation_token)`


### GetPullRequestIteration
#### Description:
Get the specified iteration for a pull request.

* `:param str repository_id: ID or name of the repository.`
* `:param int pull_request_id: ID of the pull request.`
* `:param int iteration_id: ID of the pull request iteration to return.`
* `:param str project: Project ID or project name`
* `:rtype: :class:<GitPullRequestIteration> <azure.devops.v5_1.git.models.GitPullRequestIteration>`
#### Example usage:
`connection.clients.get_git_client().get_pull_request_iteration(repository_id,pull_request_id,iteration_id,project)`


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
* `:rtype: :class:<GitPullRequestIterationChanges> <azure.devops.v5_1.git.models.GitPullRequestIterationChanges>`
#### Example usage:
`connection.clients.get_git_client().get_pull_request_iteration_changes(repository_id,pull_request_id,iteration_id,project,top,skip,compare_to)`


### GetPullRequestIterationCommits
#### Description:
Get the commits for the specified iteration of a pull request.

* `:param str repository_id: ID or name of the repository.`
* `:param int pull_request_id: ID of the pull request.`
* `:param int iteration_id: ID of the iteration from which to get the commits.`
* `:param str project: Project ID or project name`
* `:param int top: Maximum number of commits to return. The maximum number of commits that can be returned per batch is 500.`
* `:param int skip: Number of commits to skip.`
* `:rtype: [GitCommitRef]`
#### Example usage:
`connection.clients.get_git_client().get_pull_request_iteration_commits(repository_id,pull_request_id,iteration_id,project,top,skip)`


### GetPullRequestIterations
#### Description:
Get the list of iterations for the specified pull request.

* `:param str repository_id: ID or name of the repository.`
* `:param int pull_request_id: ID of the pull request.`
* `:param str project: Project ID or project name`
* `:param bool include_commits: If true, include the commits associated with each iteration in the response.`
* `:rtype: [GitPullRequestIteration]`
#### Example usage:
`connection.clients.get_git_client().get_pull_request_iterations(repository_id,pull_request_id,project,include_commits)`


### GetPullRequestQuery
#### Description:
This API is used to find what pull requests are related to a given commit.  It can be used to either find the pull request that created a particular merge commit or it can be used to find all pull requests that have ever merged a particular commit.  The input is a list of queries which each contain a list of commits. For each commit that you search against, you will get back a dictionary of commit -> pull requests.

* `:param :class:<GitPullRequestQuery> <azure.devops.v5_1.git.models.GitPullRequestQuery> queries: The list of queries to perform.`
* `:param str repository_id: ID of the repository.`
* `:param str project: Project ID or project name`
* `:rtype: :class:<GitPullRequestQuery> <azure.devops.v5_1.git.models.GitPullRequestQuery>`
#### Example usage:
`connection.clients.get_git_client().get_pull_request_query(queries,repository_id,project)`


### GetPullRequestReviewer
#### Description:
Retrieve information about a particular reviewer on a pull request

* `:param str repository_id: The repository ID of the pull request’s target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param str reviewer_id: ID of the reviewer.`
* `:param str project: Project ID or project name`
* `:rtype: :class:<IdentityRefWithVote> <azure.devops.v5_1.git.models.IdentityRefWithVote>`
#### Example usage:
`connection.clients.get_git_client().get_pull_request_reviewer(repository_id,pull_request_id,reviewer_id,project)`


### GetPullRequestReviewers
#### Description:
Retrieve the reviewers for a pull request

* `:param str repository_id: The repository ID of the pull request’s target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param str project: Project ID or project name`
* `:rtype: [IdentityRefWithVote]`
#### Example usage:
`connection.clients.get_git_client().get_pull_request_reviewers(repository_id,pull_request_id,project)`


### GetPullRequestThread
#### Description:
Retrieve a thread in a pull request.

* `:param str repository_id: The repository ID of the pull request's target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param int thread_id: ID of the thread.`
* `:param str project: Project ID or project name`
* `:param int iteration: If specified, thread position will be tracked using this iteration as the right side of the diff.`
* `:param int base_iteration: If specified, thread position will be tracked using this iteration as the left side of the diff.`
* `:rtype: :class:<GitPullRequestCommentThread> <azure.devops.v5_1.git.models.GitPullRequestCommentThread>`
#### Example usage:
`connection.clients.get_git_client().get_pull_request_thread(repository_id,pull_request_id,thread_id,project,iteration,base_iteration)`


### GetPullRequestWorkItemRefs
#### Description:
Retrieve a list of work items associated with a pull request.

* `:param str repository_id: ID or name of the repository.`
* `:param int pull_request_id: ID of the pull request.`
* `:param str project: Project ID or project name`
* `:rtype: [ResourceRef]`
#### Example usage:
`connection.clients.get_git_client().get_pull_request_work_item_refs(repository_id,pull_request_id,project)`


### GetPullRequests
#### Description:
Retrieve all pull requests matching a specified criteria.

* `:param str repository_id: The repository ID of the pull request's target branch.`
* `:param :class:<GitPullRequestSearchCriteria> <azure.devops.v5_1.git.models.GitPullRequestSearchCriteria> search_criteria: Pull requests will be returned that match this search criteria.`
* `:param str project: Project ID or project name`
* `:param int max_comment_length: Not used.`
* `:param int skip: The number of pull requests to ignore. For example, to retrieve results 101-150, set top to 50 and skip to 100.`
* `:param int top: The number of pull requests to retrieve.`
* `:rtype: [GitPullRequest]`
#### Example usage:
`connection.clients.get_git_client().get_pull_requests(repository_id,search_criteria,project,max_comment_length,skip,top)`


### GetPullRequestsByProject
#### Description:
Retrieve all pull requests matching a specified criteria.

* `:param str project: Project ID or project name`
* `:param :class:<GitPullRequestSearchCriteria> <azure.devops.v5_1.git.models.GitPullRequestSearchCriteria> search_criteria: Pull requests will be returned that match this search criteria.`
* `:param int max_comment_length: Not used.`
* `:param int skip: The number of pull requests to ignore. For example, to retrieve results 101-150, set top to 50 and skip to 100.`
* `:param int top: The number of pull requests to retrieve.`
* `:rtype: [GitPullRequest]`
#### Example usage:
`connection.clients.get_git_client().get_pull_requests_by_project(project,search_criteria,max_comment_length,skip,top)`


### GetPush
#### Description:
Retrieves a particular push.

* `:param str repository_id: The name or ID of the repository.`
* `:param int push_id: ID of the push.`
* `:param str project: Project ID or project name`
* `:param int include_commits: The number of commits to include in the result.`
* `:param bool include_ref_updates: If true, include the list of refs that were updated by the push.`
* `:rtype: :class:<GitPush> <azure.devops.v5_1.git.models.GitPush>`
#### Example usage:
`connection.clients.get_git_client().get_push(repository_id,push_id,project,include_commits,include_ref_updates)`


### GetPushCommits
#### Description:
Retrieve a list of commits associated with a particular push.

* `:param str repository_id: The id or friendly name of the repository. To use the friendly name, projectId must also be specified.`
* `:param int push_id: The id of the push.`
* `:param str project: Project ID or project name`
* `:param int top: The maximum number of commits to return ("get the top x commits").`
* `:param int skip: The number of commits to skip.`
* `:param bool include_links: Set to false to avoid including REST Url links for resources. Defaults to true.`
* `:rtype: [GitCommitRef]`
#### Example usage:
`connection.clients.get_git_client().get_push_commits(repository_id,push_id,project,top,skip,include_links)`


### GetPushes
#### Description:
Retrieves pushes associated with the specified repository.

* `:param str repository_id: The name or ID of the repository.`
* `:param str project: Project ID or project name`
* `:param int skip: Number of pushes to skip.`
* `:param int top: Number of pushes to return.`
* `:param :class:<GitPushSearchCriteria> <azure.devops.v5_1.git.models.GitPushSearchCriteria> search_criteria: Search criteria attributes: fromDate, toDate, pusherId, refName, includeRefUpdates or includeLinks. fromDate: Start date to search from. toDate: End date to search to. pusherId: Identity of the person who submitted the push. refName: Branch name to consider. includeRefUpdates: If true, include the list of refs that were updated by the push. includeLinks: Whether to include the _links field on the shallow references.`
* `:rtype: [GitPush]`
#### Example usage:
`connection.clients.get_git_client().get_pushes(repository_id,project,skip,top,search_criteria)`


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
* `:rtype: :class:<GetRefsResponseValue>`
#### Example usage:
`connection.clients.get_git_client().get_refs(repository_id,project,filter,include_links,include_statuses,include_my_branches,latest_statuses_only,peel_tags,filter_contains,top,continuation_token)`


### GetRepositories
#### Description:
Retrieve git repositories.

* `:param str project: Project ID or project name`
* `:param bool include_links: [optional] True to include reference links. The default value is false.`
* `:param bool include_all_urls: [optional] True to include all remote URLs. The default value is false.`
* `:param bool include_hidden: [optional] True to include hidden repositories. The default value is false.`
* `:rtype: [GitRepository]`
#### Example usage:
`connection.clients.get_git_client().get_repositories(project,include_links,include_all_urls,include_hidden)`


### GetRepository
#### Description:
Retrieve a git repository.

* `:param str repository_id: The name or ID of the repository.`
* `:param str project: Project ID or project name`
* `:rtype: :class:<GitRepository> <azure.devops.v5_1.git.models.GitRepository>`
#### Example usage:
`connection.clients.get_git_client().get_repository(repository_id,project)`


### GetRepositoryWithParent
#### Description:
Retrieve a git repository.

* `:param str repository_id: The name or ID of the repository.`
* `:param bool include_parent: True to include parent repository. Only available in authenticated calls.`
* `:param str project: Project ID or project name`
* `:rtype: :class:<GitRepository> <azure.devops.v5_1.git.models.GitRepository>`
#### Example usage:
`connection.clients.get_git_client().get_repository_with_parent(repository_id,include_parent,project)`


### GetStatuses
#### Description:
Get statuses associated with the Git commit.

* `:param str commit_id: ID of the Git commit.`
* `:param str repository_id: ID of the repository.`
* `:param str project: Project ID or project name`
* `:param int top: Optional. The number of statuses to retrieve. Default is 1000.`
* `:param int skip: Optional. The number of statuses to ignore. Default is 0. For example, to retrieve results 101-150, set top to 50 and skip to 100.`
* `:param bool latest_only: The flag indicates whether to get only latest statuses grouped by Context.Name and Context.Genre.`
* `:rtype: [GitStatus]`
#### Example usage:
`connection.clients.get_git_client().get_statuses(commit_id,repository_id,project,top,skip,latest_only)`


### GetThreads
#### Description:
Retrieve all threads in a pull request.

* `:param str repository_id: The repository ID of the pull request's target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param str project: Project ID or project name`
* `:param int iteration: If specified, thread positions will be tracked using this iteration as the right side of the diff.`
* `:param int base_iteration: If specified, thread positions will be tracked using this iteration as the left side of the diff.`
* `:rtype: [GitPullRequestCommentThread]`
#### Example usage:
`connection.clients.get_git_client().get_threads(repository_id,pull_request_id,project,iteration,base_iteration)`


### GetTree
#### Description:
The Tree endpoint returns the collection of objects underneath the specified tree. Trees are folders in a Git repository.

* `:param str repository_id: Repository Id.`
* `:param str sha1: SHA1 hash of the tree object.`
* `:param str project: Project ID or project name`
* `:param str project_id: Project Id.`
* `:param bool recursive: Search recursively. Include trees underneath this tree. Default is false.`
* `:param str file_name: Name to use if a .zip file is returned. Default is the object ID.`
* `:rtype: :class:<GitTreeRef> <azure.devops.v5_1.git.models.GitTreeRef>`
#### Example usage:
`connection.clients.get_git_client().get_tree(repository_id,sha1,project,project_id,recursive,file_name)`


### GetTreeZip
#### Description:
The Tree endpoint returns the collection of objects underneath the specified tree. Trees are folders in a Git repository.

* `:param str repository_id: Repository Id.`
* `:param str sha1: SHA1 hash of the tree object.`
* `:param str project: Project ID or project name`
* `:param str project_id: Project Id.`
* `:param bool recursive: Search recursively. Include trees underneath this tree. Default is false.`
* `:param str file_name: Name to use if a .zip file is returned. Default is the object ID.`
* `:rtype: object`
#### Example usage:
`connection.clients.get_git_client().get_tree_zip(repository_id,sha1,project,project_id,recursive,file_name)`


### UpdateComment
#### Description:
Update a comment associated with a specific thread in a pull request.

* `:param :class:<Comment> <azure.devops.v5_1.git.models.Comment> comment: The comment content that should be updated. Comments can be up to 150,000 characters.`
* `:param str repository_id: The repository ID of the pull request's target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param int thread_id: ID of the thread that the desired comment is in.`
* `:param int comment_id: ID of the comment to update.`
* `:param str project: Project ID or project name`
* `:rtype: :class:<Comment> <azure.devops.v5_1.git.models.Comment>`
#### Example usage:
`connection.clients.get_git_client().update_comment(comment,repository_id,pull_request_id,thread_id,comment_id,project)`


### UpdatePullRequest
#### Description:
Update a pull request

* `:param :class:<GitPullRequest> <azure.devops.v5_1.git.models.GitPullRequest> git_pull_request_to_update: The pull request content that should be updated.`
* `:param str repository_id: The repository ID of the pull request's target branch.`
* `:param int pull_request_id: ID of the pull request to update.`
* `:param str project: Project ID or project name`
* `:rtype: :class:<GitPullRequest> <azure.devops.v5_1.git.models.GitPullRequest>`
#### Example usage:
`connection.clients.get_git_client().update_pull_request(git_pull_request_to_update,repository_id,pull_request_id,project)`


### UpdatePullRequestReviewers
#### Description:
Reset the votes of multiple reviewers on a pull request.  NOTE: This endpoint only supports updating votes, but does not support updating required reviewers (use policy) or display names.

* `:param [IdentityRefWithVote] patch_votes: IDs of the reviewers whose votes will be reset to zero`
* `:param str repository_id: The repository ID of the pull request’s target branch.`
* `:param int pull_request_id: ID of the pull request`
* `:param str project: Project ID or project name`
#### Example usage:
`connection.clients.get_git_client().update_pull_request_reviewers(patch_votes,repository_id,pull_request_id,project)`


### UpdateRef
#### Description:
Lock or Unlock a branch.

* `:param :class:<GitRefUpdate> <azure.devops.v5_1.git.models.GitRefUpdate> new_ref_info: The ref update action (lock/unlock) to perform`
* `:param str repository_id: The name or ID of the repository.`
* `:param str filter: The name of the branch to lock/unlock`
* `:param str project: Project ID or project name`
* `:param str project_id: ID or name of the team project. Optional if specifying an ID for repository.`
* `:rtype: :class:<GitRef> <azure.devops.v5_1.git.models.GitRef>`
#### Example usage:
`connection.clients.get_git_client().update_ref(new_ref_info,repository_id,filter,project,project_id)`


### UpdateRefs
#### Description:
Creating, updating, or deleting refs(branches).

* `:param [GitRefUpdate] ref_updates: List of ref updates to attempt to perform`
* `:param str repository_id: The name or ID of the repository.`
* `:param str project: Project ID or project name`
* `:param str project_id: ID or name of the team project. Optional if specifying an ID for repository.`
* `:rtype: [GitRefUpdateResult]`
#### Example usage:
`connection.clients.get_git_client().update_refs(ref_updates,repository_id,project,project_id)`


### UpdateRepository
#### Description:
Updates the Git repository with either a new repo name or a new default branch.

* `:param :class:<GitRepository> <azure.devops.v5_1.git.models.GitRepository> new_repository_info: Specify a new repo name or a new default branch of the repository`
* `:param str repository_id: The name or ID of the repository.`
* `:param str project: Project ID or project name`
* `:rtype: :class:<GitRepository> <azure.devops.v5_1.git.models.GitRepository>`
#### Example usage:
`connection.clients.get_git_client().update_repository(new_repository_info,repository_id,project)`


### UpdateThread
#### Description:
Update a thread in a pull request.

* `:param :class:<GitPullRequestCommentThread> <azure.devops.v5_1.git.models.GitPullRequestCommentThread> comment_thread: The thread content that should be updated.`
* `:param str repository_id: The repository ID of the pull request's target branch.`
* `:param int pull_request_id: ID of the pull request.`
* `:param int thread_id: ID of the thread to update.`
* `:param str project: Project ID or project name`
* `:rtype: :class:<GitPullRequestCommentThread> <azure.devops.v5_1.git.models.GitPullRequestCommentThread>`
#### Example usage:
`connection.clients.get_git_client().update_thread(comment_thread,repository_id,pull_request_id,thread_id,project)`


## Get Identity Client
### CreateGroups
#### Description:
* `:param :class:<object> <azure.devops.v5_1.identity.models.object> container:`
* `:rtype: [Identity]`
#### Example usage:
`connection.clients.get_identity_client().create_groups(container)`


### CreateIdentity
#### Description:
* `:param :class:<FrameworkIdentityInfo> <azure.devops.v5_1.identity.models.FrameworkIdentityInfo> framework_identity_info:`
* `:rtype: :class:<Identity> <azure.devops.v5_1.identity.models.Identity>`
#### Example usage:
`connection.clients.get_identity_client().create_identity(framework_identity_info)`


### DeleteGroup
#### Description:
* `:param str group_id:`
#### Example usage:
`connection.clients.get_identity_client().delete_group(group_id)`


### GetIdentityChanges
#### Description:
* `:param int identity_sequence_id:`
* `:param int group_sequence_id:`
* `:param int organization_identity_sequence_id:`
* `:param int page_size:`
* `:param str scope_id:`
* `:rtype: :class:<ChangedIdentities> <azure.devops.v5_1.identity.models.ChangedIdentities>`
#### Example usage:
`connection.clients.get_identity_client().get_identity_changes(identity_sequence_id,group_sequence_id,organization_identity_sequence_id,page_size,scope_id)`


### GetMaxSequenceId
#### Description:
Read the max sequence id of all the identities.

* `:rtype: long`
#### Example usage:
`connection.clients.get_identity_client().get_max_sequence_id()`


### GetSelf
#### Description:
Read identity of the home tenant request user.

* `:rtype: :class:<IdentitySelf> <azure.devops.v5_1.identity.models.IdentitySelf>`
#### Example usage:
`connection.clients.get_identity_client().get_self()`


### GetUserIdentityIdsByDomainId
#### Description:
* `:param str domain_id:`
* `:rtype: [str]`
#### Example usage:
`connection.clients.get_identity_client().get_user_identity_ids_by_domain_id(domain_id)`


### ListGroups
#### Description:
* `:param str scope_ids:`
* `:param bool recurse:`
* `:param bool deleted:`
* `:param str properties:`
* `:rtype: [Identity]`
#### Example usage:
`connection.clients.get_identity_client().list_groups(scope_ids,recurse,deleted,properties)`


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
* `:rtype: [Identity]`
#### Example usage:
`connection.clients.get_identity_client().read_identities(descriptors,identity_ids,subject_descriptors,social_descriptors,search_filter,filter_value,query_membership,properties,include_restricted_visibility,options)`


### ReadIdentitiesByScope
#### Description:
* `:param str scope_id:`
* `:param str query_membership:`
* `:param str properties:`
* `:rtype: [Identity]`
#### Example usage:
`connection.clients.get_identity_client().read_identities_by_scope(scope_id,query_membership,properties)`


### ReadIdentity
#### Description:
* `:param str identity_id:`
* `:param str query_membership:`
* `:param str properties:`
* `:rtype: :class:<Identity> <azure.devops.v5_1.identity.models.Identity>`
#### Example usage:
`connection.clients.get_identity_client().read_identity(identity_id,query_membership,properties)`


### UpdateIdentities
#### Description:
* `:param :class:<VssJsonCollectionWrapper> <azure.devops.v5_1.identity.models.VssJsonCollectionWrapper> identities:`
* `:rtype: [IdentityUpdateData]`
#### Example usage:
`connection.clients.get_identity_client().update_identities(identities)`


### UpdateIdentity
#### Description:
* `:param :class:<Identity> <azure.devops.v5_1.identity.models.Identity> identity:`
* `:param str identity_id:`
#### Example usage:
`connection.clients.get_identity_client().update_identity(identity,identity_id)`


## Get Notification Client
### CreateSubscription
#### Description:
Create a new subscription.

* `:param :class:<NotificationSubscriptionCreateParameters> <azure.devops.v5_1.notification.models.NotificationSubscriptionCreateParameters> create_parameters:`
* `:rtype: :class:<NotificationSubscription> <azure.devops.v5_1.notification.models.NotificationSubscription>`
#### Example usage:
`connection.clients.get_notification_client().create_subscription(create_parameters)`


### DeleteSubscription
#### Description:
Delete a subscription.

* `:param str subscription_id:`
#### Example usage:
`connection.clients.get_notification_client().delete_subscription(subscription_id)`


### GetEventType
#### Description:
Get a specific event type.

* `:param str event_type: The ID of the event type.`
* `:rtype: :class:<NotificationEventType> <azure.devops.v5_1.notification.models.NotificationEventType>`
#### Example usage:
`connection.clients.get_notification_client().get_event_type(event_type)`


### GetSettings
#### Description:
* `:rtype: :class:<NotificationAdminSettings> <azure.devops.v5_1.notification.models.NotificationAdminSettings>`
#### Example usage:
`connection.clients.get_notification_client().get_settings()`


### GetSubscriber
#### Description:
Get delivery preferences of a notifications subscriber.

* `:param str subscriber_id: ID of the user or group.`
* `:rtype: :class:<NotificationSubscriber> <azure.devops.v5_1.notification.models.NotificationSubscriber>`
#### Example usage:
`connection.clients.get_notification_client().get_subscriber(subscriber_id)`


### GetSubscription
#### Description:
Get a notification subscription by its ID.

* `:param str subscription_id:`
* `:param str query_flags:`
* `:rtype: :class:<NotificationSubscription> <azure.devops.v5_1.notification.models.NotificationSubscription>`
#### Example usage:
`connection.clients.get_notification_client().get_subscription(subscription_id,query_flags)`


### GetSubscriptionDiagnostics
#### Description:
Get the diagnostics settings for a subscription.

* `:param str subscription_id: The id of the notifications subscription.`
* `:rtype: :class:<SubscriptionDiagnostics> <azure.devops.v5_1.notification.models.SubscriptionDiagnostics>`
#### Example usage:
`connection.clients.get_notification_client().get_subscription_diagnostics(subscription_id)`


### GetSubscriptionTemplates
#### Description:
Get available subscription templates.

* `:rtype: [NotificationSubscriptionTemplate]`
#### Example usage:
`connection.clients.get_notification_client().get_subscription_templates()`


### ListEventTypes
#### Description:
List available event types for this service. Optionally filter by only event types for the specified publisher.

* `:param str publisher_id: Limit to event types for this publisher`
* `:rtype: [NotificationEventType]`
#### Example usage:
`connection.clients.get_notification_client().list_event_types(publisher_id)`


### ListLogs
#### Description:
Get a list of diagnostic logs for this service.

* `:param str source: ID specifying which type of logs to check diagnostics for.`
* `:param str entry_id: The ID of the specific log to query for.`
* `:param datetime start_time: Start time for the time range to query in.`
* `:param datetime end_time: End time for the time range to query in.`
* `:rtype: [INotificationDiagnosticLog]`
#### Example usage:
`connection.clients.get_notification_client().list_logs(source,entry_id,start_time,end_time)`


### ListSubscriptions
#### Description:
Get a list of notification subscriptions, either by subscription IDs or by all subscriptions for a given user or group.

* `:param str target_id: User or Group ID`
* `:param [str] ids: List of subscription IDs`
* `:param str query_flags:`
* `:rtype: [NotificationSubscription]`
#### Example usage:
`connection.clients.get_notification_client().list_subscriptions(target_id,ids,query_flags)`


### QuerySubscriptions
#### Description:
Query for subscriptions. A subscription is returned if it matches one or more of the specified conditions.

* `:param :class:<SubscriptionQuery> <azure.devops.v5_1.notification.models.SubscriptionQuery> subscription_query:`
* `:rtype: [NotificationSubscription]`
#### Example usage:
`connection.clients.get_notification_client().query_subscriptions(subscription_query)`


### UpdateSettings
#### Description:
* `:param :class:<NotificationAdminSettingsUpdateParameters> <azure.devops.v5_1.notification.models.NotificationAdminSettingsUpdateParameters> update_parameters:`
* `:rtype: :class:<NotificationAdminSettings> <azure.devops.v5_1.notification.models.NotificationAdminSettings>`
#### Example usage:
`connection.clients.get_notification_client().update_settings(update_parameters)`


### UpdateSubscriber
#### Description:
Update delivery preferences of a notifications subscriber.

* `:param :class:<NotificationSubscriberUpdateParameters> <azure.devops.v5_1.notification.models.NotificationSubscriberUpdateParameters> update_parameters:`
* `:param str subscriber_id: ID of the user or group.`
* `:rtype: :class:<NotificationSubscriber> <azure.devops.v5_1.notification.models.NotificationSubscriber>`
#### Example usage:
`connection.clients.get_notification_client().update_subscriber(update_parameters,subscriber_id)`


### UpdateSubscription
#### Description:
Update an existing subscription. Depending on the type of subscription and permissions, the caller can update the description, filter settings, channel (delivery) settings and more.

* `:param :class:<NotificationSubscriptionUpdateParameters> <azure.devops.v5_1.notification.models.NotificationSubscriptionUpdateParameters> update_parameters:`
* `:param str subscription_id:`
* `:rtype: :class:<NotificationSubscription> <azure.devops.v5_1.notification.models.NotificationSubscription>`
#### Example usage:
`connection.clients.get_notification_client().update_subscription(update_parameters,subscription_id)`


### UpdateSubscriptionDiagnostics
#### Description:
Update the diagnostics settings for a subscription.

* `:param :class:<UpdateSubscripitonDiagnosticsParameters> <azure.devops.v5_1.notification.models.UpdateSubscripitonDiagnosticsParameters> update_parameters:`
* `:param str subscription_id: The id of the notifications subscription.`
* `:rtype: :class:<SubscriptionDiagnostics> <azure.devops.v5_1.notification.models.SubscriptionDiagnostics>`
#### Example usage:
`connection.clients.get_notification_client().update_subscription_diagnostics(update_parameters,subscription_id)`


### UpdateSubscriptionUserSettings
#### Description:
Update the specified user's settings for the specified subscription. This API is typically used to opt in or out of a shared subscription. User settings can only be applied to shared subscriptions, like team subscriptions or default subscriptions.

* `:param :class:<SubscriptionUserSettings> <azure.devops.v5_1.notification.models.SubscriptionUserSettings> user_settings:`
* `:param str subscription_id:`
* `:param str user_id: ID of the user`
* `:rtype: :class:<SubscriptionUserSettings> <azure.devops.v5_1.notification.models.SubscriptionUserSettings>`
#### Example usage:
`connection.clients.get_notification_client().update_subscription_user_settings(user_settings,subscription_id,user_id)`


## Get Operations Client
### GetOperation
#### Description:
Gets an operation from the the operationId using the given pluginId.

* `:param str operation_id: The ID for the operation.`
* `:param str plugin_id: The ID for the plugin.`
* `:rtype: :class:<Operation> <azure.devops.v5_1.operations.models.Operation>`
#### Example usage:
`connection.clients.get_operations_client().get_operation(operation_id,plugin_id)`


## Get Policy Client
### CreatePolicyConfiguration
#### Description:
Create a policy configuration of a given policy type.

* `:param :class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration> configuration: The policy configuration to create.`
* `:param str project: Project ID or project name`
* `:param int configuration_id:`
* `:rtype: :class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>`
#### Example usage:
`connection.clients.get_policy_client().create_policy_configuration(configuration,project,configuration_id)`


### DeletePolicyConfiguration
#### Description:
Delete a policy configuration by its ID.

* `:param str project: Project ID or project name`
* `:param int configuration_id: ID of the policy configuration to delete.`
#### Example usage:
`connection.clients.get_policy_client().delete_policy_configuration(project,configuration_id)`


### GetPolicyConfiguration
#### Description:
Get a policy configuration by its ID.

* `:param str project: Project ID or project name`
* `:param int configuration_id: ID of the policy configuration`
* `:rtype: :class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>`
#### Example usage:
`connection.clients.get_policy_client().get_policy_configuration(project,configuration_id)`


### GetPolicyConfigurationRevision
#### Description:
Retrieve a specific revision of a given policy by ID.

* `:param str project: Project ID or project name`
* `:param int configuration_id: The policy configuration ID.`
* `:param int revision_id: The revision ID.`
* `:rtype: :class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>`
#### Example usage:
`connection.clients.get_policy_client().get_policy_configuration_revision(project,configuration_id,revision_id)`


### GetPolicyConfigurationRevisions
#### Description:
Retrieve all revisions for a given policy.

* `:param str project: Project ID or project name`
* `:param int configuration_id: The policy configuration ID.`
* `:param int top: The number of revisions to retrieve.`
* `:param int skip: The number of revisions to ignore. For example, to retrieve results 101-150, set top to 50 and skip to 100.`
* `:rtype: [PolicyConfiguration]`
#### Example usage:
`connection.clients.get_policy_client().get_policy_configuration_revisions(project,configuration_id,top,skip)`


### GetPolicyConfigurations
#### Description:
Get a list of policy configurations in a project.

* `:param str project: Project ID or project name`
* `:param str scope: [Provided for legacy reasons] The scope on which a subset of policies is defined.`
* `:param int top: Maximum number of policies to return.`
* `:param str continuation_token: The continuation token used for pagination.`
* `:param str policy_type: Filter returned policies to only this type`
* `:rtype: :class:<GetPolicyConfigurationsResponseValue>`
#### Example usage:
`connection.clients.get_policy_client().get_policy_configurations(project,scope,top,continuation_token,policy_type)`


### GetPolicyType
#### Description:
Retrieve a specific policy type by ID.

* `:param str project: Project ID or project name`
* `:param str type_id: The policy ID.`
* `:rtype: :class:<PolicyType> <azure.devops.v5_1.policy.models.PolicyType>`
#### Example usage:
`connection.clients.get_policy_client().get_policy_type(project,type_id)`


### GetPolicyTypes
#### Description:
Retrieve all available policy types.

* `:param str project: Project ID or project name`
* `:rtype: [PolicyType]`
#### Example usage:
`connection.clients.get_policy_client().get_policy_types(project)`


### UpdatePolicyConfiguration
#### Description:
Update a policy configuration by its ID.

* `:param :class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration> configuration: The policy configuration to update.`
* `:param str project: Project ID or project name`
* `:param int configuration_id: ID of the existing policy configuration to be updated.`
* `:rtype: :class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>`
#### Example usage:
`connection.clients.get_policy_client().update_policy_configuration(configuration,project,configuration_id)`


## Get Profile Client
### CreatePolicyConfiguration
#### Description:
Create a policy configuration of a given policy type.

* `:param :class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration> configuration: The policy configuration to create.`
* `:param str project: Project ID or project name`
* `:param int configuration_id:`
* `:rtype: :class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>`
#### Example usage:
`connection.clients.get_profile_client().create_policy_configuration(configuration,project,configuration_id)`


### DeletePolicyConfiguration
#### Description:
Delete a policy configuration by its ID.

* `:param str project: Project ID or project name`
* `:param int configuration_id: ID of the policy configuration to delete.`
#### Example usage:
`connection.clients.get_profile_client().delete_policy_configuration(project,configuration_id)`


### GetPolicyConfiguration
#### Description:
Get a policy configuration by its ID.

* `:param str project: Project ID or project name`
* `:param int configuration_id: ID of the policy configuration`
* `:rtype: :class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>`
#### Example usage:
`connection.clients.get_profile_client().get_policy_configuration(project,configuration_id)`


### GetPolicyConfigurationRevision
#### Description:
Retrieve a specific revision of a given policy by ID.

* `:param str project: Project ID or project name`
* `:param int configuration_id: The policy configuration ID.`
* `:param int revision_id: The revision ID.`
* `:rtype: :class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>`
#### Example usage:
`connection.clients.get_profile_client().get_policy_configuration_revision(project,configuration_id,revision_id)`


### GetPolicyConfigurationRevisions
#### Description:
Retrieve all revisions for a given policy.

* `:param str project: Project ID or project name`
* `:param int configuration_id: The policy configuration ID.`
* `:param int top: The number of revisions to retrieve.`
* `:param int skip: The number of revisions to ignore. For example, to retrieve results 101-150, set top to 50 and skip to 100.`
* `:rtype: [PolicyConfiguration]`
#### Example usage:
`connection.clients.get_profile_client().get_policy_configuration_revisions(project,configuration_id,top,skip)`


### GetPolicyConfigurations
#### Description:
Get a list of policy configurations in a project.

* `:param str project: Project ID or project name`
* `:param str scope: [Provided for legacy reasons] The scope on which a subset of policies is defined.`
* `:param int top: Maximum number of policies to return.`
* `:param str continuation_token: The continuation token used for pagination.`
* `:param str policy_type: Filter returned policies to only this type`
* `:rtype: :class:<GetPolicyConfigurationsResponseValue>`
#### Example usage:
`connection.clients.get_profile_client().get_policy_configurations(project,scope,top,continuation_token,policy_type)`


### GetPolicyType
#### Description:
Retrieve a specific policy type by ID.

* `:param str project: Project ID or project name`
* `:param str type_id: The policy ID.`
* `:rtype: :class:<PolicyType> <azure.devops.v5_1.policy.models.PolicyType>`
#### Example usage:
`connection.clients.get_profile_client().get_policy_type(project,type_id)`


### GetPolicyTypes
#### Description:
Retrieve all available policy types.

* `:param str project: Project ID or project name`
* `:rtype: [PolicyType]`
#### Example usage:
`connection.clients.get_profile_client().get_policy_types(project)`


### UpdatePolicyConfiguration
#### Description:
Update a policy configuration by its ID.

* `:param :class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration> configuration: The policy configuration to update.`
* `:param str project: Project ID or project name`
* `:param int configuration_id: ID of the existing policy configuration to be updated.`
* `:rtype: :class:<PolicyConfiguration> <azure.devops.v5_1.policy.models.PolicyConfiguration>`
#### Example usage:
`connection.clients.get_profile_client().update_policy_configuration(configuration,project,configuration_id)`


## Get Release Client
### CreateRelease
#### Description:
Create a release.

* `:param :class:<ReleaseStartMetadata> <azure.devops.v5_1.release.models.ReleaseStartMetadata> release_start_metadata: Metadata to create a release.`
* `:param str project: Project ID or project name`
* `:rtype: :class:<Release> <azure.devops.v5_1.release.models.Release>`
#### Example usage:
`connection.clients.get_release_client().create_release(release_start_metadata,project)`


### CreateReleaseDefinition
#### Description:
Create a release definition

* `:param :class:<ReleaseDefinition> <azure.devops.v5_1.release.models.ReleaseDefinition> release_definition: release definition object to create.`
* `:param str project: Project ID or project name`
* `:rtype: :class:<ReleaseDefinition> <azure.devops.v5_1.release.models.ReleaseDefinition>`
#### Example usage:
`connection.clients.get_release_client().create_release_definition(release_definition,project)`


### DeleteReleaseDefinition
#### Description:
Delete a release definition.

* `:param str project: Project ID or project name`
* `:param int definition_id: Id of the release definition.`
* `:param str comment: Comment for deleting a release definition.`
* `:param bool force_delete: 'true' to automatically cancel any in-progress release deployments and proceed with release definition deletion . Default is 'false'.`
#### Example usage:
`connection.clients.get_release_client().delete_release_definition(project,definition_id,comment,force_delete)`


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
* `:rtype: :class:<GetApprovalsResponseValue>`
#### Example usage:
`connection.clients.get_release_client().get_approvals(project,assigned_to_filter,status_filter,release_ids_filter,type_filter,top,continuation_token,query_order,include_my_group_approvals)`


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
* `:rtype: :class:<GetDeploymentsResponseValue>`
#### Example usage:
`connection.clients.get_release_client().get_deployments(project,definition_id,definition_environment_id,created_by,min_modified_time,max_modified_time,deployment_status,operation_status,latest_attempts_only,query_order,top,continuation_token,created_for,min_started_time,max_started_time,source_branch)`


### GetManualIntervention
#### Description:
Get manual intervention for a given release and manual intervention id.

* `:param str project: Project ID or project name`
* `:param int release_id: Id of the release.`
* `:param int manual_intervention_id: Id of the manual intervention.`
* `:rtype: :class:<ManualIntervention> <azure.devops.v5_1.release.models.ManualIntervention>`
#### Example usage:
`connection.clients.get_release_client().get_manual_intervention(project,release_id,manual_intervention_id)`


### GetManualInterventions
#### Description:
List all manual interventions for a given release.

* `:param str project: Project ID or project name`
* `:param int release_id: Id of the release.`
* `:rtype: [ManualIntervention]`
#### Example usage:
`connection.clients.get_release_client().get_manual_interventions(project,release_id)`


### GetRelease
#### Description:
Get a Release

* `:param str project: Project ID or project name`
* `:param int release_id: Id of the release.`
* `:param str approval_filters: A filter which would allow fetching approval steps selectively based on whether it is automated, or manual. This would also decide whether we should fetch pre and post approval snapshots. Assumes All by default`
* `:param [str] property_filters: A comma-delimited list of extended properties to be retrieved. If set, the returned Release will contain values for the specified property Ids (if they exist). If not set, properties will not be included.`
* `:param str expand: A property that should be expanded in the release.`
* `:param int top_gate_records: Number of release gate records to get. Default is 5.`
* `:rtype: :class:<Release> <azure.devops.v5_1.release.models.Release>`
#### Example usage:
`connection.clients.get_release_client().get_release(project,release_id,approval_filters,property_filters,expand,top_gate_records)`


### GetReleaseDefinition
#### Description:
Get a release definition.

* `:param str project: Project ID or project name`
* `:param int definition_id: Id of the release definition.`
* `:param [str] property_filters: A comma-delimited list of extended properties to be retrieved. If set, the returned Release Definition will contain values for the specified property Ids (if they exist). If not set, properties will not be included.`
* `:rtype: :class:<ReleaseDefinition> <azure.devops.v5_1.release.models.ReleaseDefinition>`
#### Example usage:
`connection.clients.get_release_client().get_release_definition(project,definition_id,property_filters)`


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
* `:rtype: :class:<GetReleaseDefinitionsResponseValue>`
#### Example usage:
`connection.clients.get_release_client().get_release_definitions(project,search_text,expand,artifact_type,artifact_source_id,top,continuation_token,query_order,path,is_exact_name_match,tag_filter,property_filters,definition_id_filter,is_deleted,search_text_contains_folder_name)`


### GetReleaseRevision
#### Description:
Get release for a given revision number.

* `:param str project: Project ID or project name`
* `:param int release_id: Id of the release.`
* `:param int definition_snapshot_revision: Definition snapshot revision number.`
* `:rtype: object`
#### Example usage:
`connection.clients.get_release_client().get_release_revision(project,release_id,definition_snapshot_revision)`


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
* `:rtype: :class:<GetReleasesResponseValue>`
#### Example usage:
`connection.clients.get_release_client().get_releases(project,definition_id,definition_environment_id,search_text,created_by,status_filter,environment_status_filter,min_created_time,max_created_time,query_order,top,continuation_token,expand,artifact_type_id,source_id,artifact_version_id,source_branch_filter,is_deleted,tag_filter,property_filters,release_id_filter,path)`


### UpdateManualIntervention
#### Description:
Update manual intervention.

* `:param :class:<ManualInterventionUpdateMetadata> <azure.devops.v5_1.release.models.ManualInterventionUpdateMetadata> manual_intervention_update_metadata: Meta data to update manual intervention.`
* `:param str project: Project ID or project name`
* `:param int release_id: Id of the release.`
* `:param int manual_intervention_id: Id of the manual intervention.`
* `:rtype: :class:<ManualIntervention> <azure.devops.v5_1.release.models.ManualIntervention>`
#### Example usage:
`connection.clients.get_release_client().update_manual_intervention(manual_intervention_update_metadata,project,release_id,manual_intervention_id)`


### UpdateRelease
#### Description:
Update a complete release object.

* `:param :class:<Release> <azure.devops.v5_1.release.models.Release> release: Release object for update.`
* `:param str project: Project ID or project name`
* `:param int release_id: Id of the release to update.`
* `:rtype: :class:<Release> <azure.devops.v5_1.release.models.Release>`
#### Example usage:
`connection.clients.get_release_client().update_release(release,project,release_id)`


### UpdateReleaseApproval
#### Description:
Update status of an approval

* `:param :class:<ReleaseApproval> <azure.devops.v5_1.release.models.ReleaseApproval> approval: ReleaseApproval object having status, approver and comments.`
* `:param str project: Project ID or project name`
* `:param int approval_id: Id of the approval.`
* `:rtype: :class:<ReleaseApproval> <azure.devops.v5_1.release.models.ReleaseApproval>`
#### Example usage:
`connection.clients.get_release_client().update_release_approval(approval,project,approval_id)`


### UpdateReleaseDefinition
#### Description:
Update a release definition.

* `:param :class:<ReleaseDefinition> <azure.devops.v5_1.release.models.ReleaseDefinition> release_definition: Release definition object to update.`
* `:param str project: Project ID or project name`
* `:rtype: :class:<ReleaseDefinition> <azure.devops.v5_1.release.models.ReleaseDefinition>`
#### Example usage:
`connection.clients.get_release_client().update_release_definition(release_definition,project)`


### UpdateReleaseResource
#### Description:
Update few properties of a release.

* `:param :class:<ReleaseUpdateMetadata> <azure.devops.v5_1.release.models.ReleaseUpdateMetadata> release_update_metadata: Properties of release to update.`
* `:param str project: Project ID or project name`
* `:param int release_id: Id of the release to update.`
* `:rtype: :class:<Release> <azure.devops.v5_1.release.models.Release>`
#### Example usage:
`connection.clients.get_release_client().update_release_resource(release_update_metadata,project,release_id)`


## Get Security Client
### HasPermissions
#### Description:
Evaluates whether the caller has the specified permissions on the specified set of security tokens.

* `:param str security_namespace_id: Security namespace identifier.`
* `:param int permissions: Permissions to evaluate.`
* `:param str tokens: One or more security tokens to evaluate.`
* `:param bool always_allow_administrators: If true and if the caller is an administrator, always return true.`
* `:param str delimiter: Optional security token separator. Defaults to ",".`
* `:rtype: [bool]`
#### Example usage:
`connection.clients.get_security_client().has_permissions(security_namespace_id,permissions,tokens,always_allow_administrators,delimiter)`


### HasPermissionsBatch
#### Description:
Evaluates multiple permissions for the calling user.  Note: This method does not aggregate the results, nor does it short-circuit if one of the permissions evaluates to false.

* `:param :class:<PermissionEvaluationBatch> <azure.devops.v5_1.security.models.PermissionEvaluationBatch> eval_batch: The set of evaluation requests.`
* `:rtype: :class:<PermissionEvaluationBatch> <azure.devops.v5_1.security.models.PermissionEvaluationBatch>`
#### Example usage:
`connection.clients.get_security_client().has_permissions_batch(eval_batch)`


### QueryAccessControlLists
#### Description:
Return a list of access control lists for the specified security namespace and token. All ACLs in the security namespace will be retrieved if no optional parameters are provided.

* `:param str security_namespace_id: Security namespace identifier.`
* `:param str token: Security token`
* `:param str descriptors: An optional filter string containing a list of identity descriptors separated by ',' whose ACEs should be retrieved. If this is left null, entire ACLs will be returned.`
* `:param bool include_extended_info: If true, populate the extended information properties for the access control entries contained in the returned lists.`
* `:param bool recurse: If true and this is a hierarchical namespace, return child ACLs of the specified token.`
* `:rtype: [AccessControlList]`
#### Example usage:
`connection.clients.get_security_client().query_access_control_lists(security_namespace_id,token,descriptors,include_extended_info,recurse)`


### QuerySecurityNamespaces
#### Description:
List all security namespaces or just the specified namespace.

* `:param str security_namespace_id: Security namespace identifier.`
* `:param bool local_only: If true, retrieve only local security namespaces.`
* `:rtype: [SecurityNamespaceDescription]`
#### Example usage:
`connection.clients.get_security_client().query_security_namespaces(security_namespace_id,local_only)`


### RemoveAccessControlEntries
#### Description:
Remove the specified ACEs from the ACL belonging to the specified token.

* `:param str security_namespace_id: Security namespace identifier.`
* `:param str token: The token whose ACL should be modified.`
* `:param str descriptors: String containing a list of identity descriptors separated by ',' whose entries should be removed.`
* `:rtype: bool`
#### Example usage:
`connection.clients.get_security_client().remove_access_control_entries(security_namespace_id,token,descriptors)`


### RemoveAccessControlLists
#### Description:
Remove access control lists under the specfied security namespace.

* `:param str security_namespace_id: Security namespace identifier.`
* `:param str tokens: One or more comma-separated security tokens`
* `:param bool recurse: If true and this is a hierarchical namespace, also remove child ACLs of the specified tokens.`
* `:rtype: bool`
#### Example usage:
`connection.clients.get_security_client().remove_access_control_lists(security_namespace_id,tokens,recurse)`


### RemovePermission
#### Description:
Removes the specified permissions on a security token for a user or group.

* `:param str security_namespace_id: Security namespace identifier.`
* `:param str descriptor: Identity descriptor of the user to remove permissions for.`
* `:param int permissions: Permissions to remove.`
* `:param str token: Security token to remove permissions for.`
* `:rtype: :class:<AccessControlEntry> <azure.devops.v5_1.security.models.AccessControlEntry>`
#### Example usage:
`connection.clients.get_security_client().remove_permission(security_namespace_id,descriptor,permissions,token)`


### SetAccessControlEntries
#### Description:
Add or update ACEs in the ACL for the provided token. The request body contains the target token, a list of [ACEs](https://docs.microsoft.com/en-us/rest/api/azure/devops/security/access%20control%20entries/set%20access%20control%20entries?#accesscontrolentry) and a optional merge parameter. In the case of a collision (by identity descriptor) with an existing ACE in the ACL, the "merge" parameter determines the behavior. If set, the existing ACE has its allow and deny merged with the incoming ACE's allow and deny. If unset, the existing ACE is displaced.

* `:param :class:<object> <azure.devops.v5_1.security.models.object> container:`
* `:param str security_namespace_id: Security namespace identifier.`
* `:rtype: [AccessControlEntry]`
#### Example usage:
`connection.clients.get_security_client().set_access_control_entries(container,security_namespace_id)`


### SetAccessControlLists
#### Description:
Create or update one or more access control lists. All data that currently exists for the ACLs supplied will be overwritten.

* `:param :class:<VssJsonCollectionWrapper> <azure.devops.v5_1.security.models.VssJsonCollectionWrapper> access_control_lists: A list of ACLs to create or update.`
* `:param str security_namespace_id: Security namespace identifier.`
#### Example usage:
`connection.clients.get_security_client().set_access_control_lists(access_control_lists,security_namespace_id)`


## Get Service Hooks Client
### CreateSubscription
#### Description:
Create a subscription.

* `:param :class:<Subscription> <azure.devops.v5_1.service_hooks.models.Subscription> subscription: Subscription to be created.`
* `:rtype: :class:<Subscription> <azure.devops.v5_1.service_hooks.models.Subscription>`
#### Example usage:
`connection.clients.get_service_hooks_client().create_subscription(subscription)`


### CreateSubscriptionsQuery
#### Description:
Query for service hook subscriptions.

* `:param :class:<SubscriptionsQuery> <azure.devops.v5_1.service_hooks.models.SubscriptionsQuery> query:`
* `:rtype: :class:<SubscriptionsQuery> <azure.devops.v5_1.service_hooks.models.SubscriptionsQuery>`
#### Example usage:
`connection.clients.get_service_hooks_client().create_subscriptions_query(query)`


### CreateTestNotification
#### Description:
Sends a test notification. This is useful for verifying the configuration of an updated or new service hooks subscription.

* `:param :class:<Notification> <azure.devops.v5_1.service_hooks.models.Notification> test_notification:`
* `:param bool use_real_data: Only allow testing with real data in existing subscriptions.`
* `:rtype: :class:<Notification> <azure.devops.v5_1.service_hooks.models.Notification>`
#### Example usage:
`connection.clients.get_service_hooks_client().create_test_notification(test_notification,use_real_data)`


### DeleteSubscription
#### Description:
Delete a specific service hooks subscription.

* `:param str subscription_id: ID for a subscription.`
#### Example usage:
`connection.clients.get_service_hooks_client().delete_subscription(subscription_id)`


### GetConsumer
#### Description:
Get a specific consumer service. Optionally filter out consumer actions that do not support any event types for the specified publisher.

* `:param str consumer_id: ID for a consumer.`
* `:param str publisher_id:`
* `:rtype: :class:<Consumer> <azure.devops.v5_1.service_hooks.models.Consumer>`
#### Example usage:
`connection.clients.get_service_hooks_client().get_consumer(consumer_id,publisher_id)`


### GetConsumerAction
#### Description:
Get details about a specific consumer action.

* `:param str consumer_id: ID for a consumer.`
* `:param str consumer_action_id: ID for a consumerActionId.`
* `:param str publisher_id:`
* `:rtype: :class:<ConsumerAction> <azure.devops.v5_1.service_hooks.models.ConsumerAction>`
#### Example usage:
`connection.clients.get_service_hooks_client().get_consumer_action(consumer_id,consumer_action_id,publisher_id)`


### GetEventType
#### Description:
Get a specific event type.

* `:param str publisher_id: ID for a publisher.`
* `:param str event_type_id:`
* `:rtype: :class:<EventTypeDescriptor> <azure.devops.v5_1.service_hooks.models.EventTypeDescriptor>`
#### Example usage:
`connection.clients.get_service_hooks_client().get_event_type(publisher_id,event_type_id)`


### GetNotification
#### Description:
Get a specific notification for a subscription.

* `:param str subscription_id: ID for a subscription.`
* `:param int notification_id:`
* `:rtype: :class:<Notification> <azure.devops.v5_1.service_hooks.models.Notification>`
#### Example usage:
`connection.clients.get_service_hooks_client().get_notification(subscription_id,notification_id)`


### GetNotifications
#### Description:
Get a list of notifications for a specific subscription. A notification includes details about the event, the request to and the response from the consumer service.

* `:param str subscription_id: ID for a subscription.`
* `:param int max_results: Maximum number of notifications to return. Default is **100**.`
* `:param str status: Get only notifications with this status.`
* `:param str result: Get only notifications with this result type.`
* `:rtype: [Notification]`
#### Example usage:
`connection.clients.get_service_hooks_client().get_notifications(subscription_id,max_results,status,result)`


### GetPublisher
#### Description:
Get a specific service hooks publisher.

* `:param str publisher_id: ID for a publisher.`
* `:rtype: :class:<Publisher> <azure.devops.v5_1.service_hooks.models.Publisher>`
#### Example usage:
`connection.clients.get_service_hooks_client().get_publisher(publisher_id)`


### GetSubscription
#### Description:
Get a specific service hooks subscription.

* `:param str subscription_id: ID for a subscription.`
* `:rtype: :class:<Subscription> <azure.devops.v5_1.service_hooks.models.Subscription>`
#### Example usage:
`connection.clients.get_service_hooks_client().get_subscription(subscription_id)`


### ListConsumerActions
#### Description:
Get a list of consumer actions for a specific consumer.

* `:param str consumer_id: ID for a consumer.`
* `:param str publisher_id:`
* `:rtype: [ConsumerAction]`
#### Example usage:
`connection.clients.get_service_hooks_client().list_consumer_actions(consumer_id,publisher_id)`


### ListConsumers
#### Description:
Get a list of available service hook consumer services. Optionally filter by consumers that support at least one event type from the specific publisher.

* `:param str publisher_id:`
* `:rtype: [Consumer]`
#### Example usage:
`connection.clients.get_service_hooks_client().list_consumers(publisher_id)`


### ListEventTypes
#### Description:
Get the event types for a specific publisher.

* `:param str publisher_id: ID for a publisher.`
* `:rtype: [EventTypeDescriptor]`
#### Example usage:
`connection.clients.get_service_hooks_client().list_event_types(publisher_id)`


### ListPublishers
#### Description:
Get a list of publishers.

* `:rtype: [Publisher]`
#### Example usage:
`connection.clients.get_service_hooks_client().list_publishers()`


### ListSubscriptions
#### Description:
Get a list of subscriptions.

* `:param str publisher_id: ID for a subscription.`
* `:param str event_type: The event type to filter on (if any).`
* `:param str consumer_id: ID for a consumer.`
* `:param str consumer_action_id: ID for a consumerActionId.`
* `:rtype: [Subscription]`
#### Example usage:
`connection.clients.get_service_hooks_client().list_subscriptions(publisher_id,event_type,consumer_id,consumer_action_id)`


### QueryInputValues
#### Description:
* `:param :class:<InputValuesQuery> <azure.devops.v5_1.service_hooks.models.InputValuesQuery> input_values_query:`
* `:param str publisher_id:`
* `:rtype: :class:<InputValuesQuery> <azure.devops.v5_1.service_hooks.models.InputValuesQuery>`
#### Example usage:
`connection.clients.get_service_hooks_client().query_input_values(input_values_query,publisher_id)`


### QueryNotifications
#### Description:
Query for notifications. A notification includes details about the event, the request to and the response from the consumer service.

* `:param :class:<NotificationsQuery> <azure.devops.v5_1.service_hooks.models.NotificationsQuery> query:`
* `:rtype: :class:<NotificationsQuery> <azure.devops.v5_1.service_hooks.models.NotificationsQuery>`
#### Example usage:
`connection.clients.get_service_hooks_client().query_notifications(query)`


### QueryPublishers
#### Description:
Query for service hook publishers.

* `:param :class:<PublishersQuery> <azure.devops.v5_1.service_hooks.models.PublishersQuery> query:`
* `:rtype: :class:<PublishersQuery> <azure.devops.v5_1.service_hooks.models.PublishersQuery>`
#### Example usage:
`connection.clients.get_service_hooks_client().query_publishers(query)`


### ReplaceSubscription
#### Description:
Update a subscription. <param name="subscriptionId">ID for a subscription that you wish to update.</param>

* `:param :class:<Subscription> <azure.devops.v5_1.service_hooks.models.Subscription> subscription:`
* `:param str subscription_id:`
* `:rtype: :class:<Subscription> <azure.devops.v5_1.service_hooks.models.Subscription>`
#### Example usage:
`connection.clients.get_service_hooks_client().replace_subscription(subscription,subscription_id)`


## Get Task Agent Client
### AddAgent
#### Description:
Adds an agent to a pool.  You probably don't want to call this endpoint directly. Instead, [configure an agent](https://docs.microsoft.com/azure/devops/pipelines/agents/agents) using the agent download package.

* `:param :class:<TaskAgent> <azure.devops.v5_1.task_agent.models.TaskAgent> agent: Details about the agent being added`
* `:param int pool_id: The agent pool in which to add the agent`
* `:rtype: :class:<TaskAgent> <azure.devops.v5_1.task_agent.models.TaskAgent>`
#### Example usage:
`connection.clients.get_task_agent_client().add_agent(agent,pool_id)`


### AddAgentPool
#### Description:
Create an agent pool.

* `:param :class:<TaskAgentPool> <azure.devops.v5_1.task_agent.models.TaskAgentPool> pool: Details about the new agent pool`
* `:rtype: :class:<TaskAgentPool> <azure.devops.v5_1.task_agent.models.TaskAgentPool>`
#### Example usage:
`connection.clients.get_task_agent_client().add_agent_pool(pool)`


### DeleteAgent
#### Description:
Delete an agent.  You probably don't want to call this endpoint directly. Instead, [use the agent configuration script](https://docs.microsoft.com/azure/devops/pipelines/agents/agents) to remove an agent from your organization.

* `:param int pool_id: The pool ID to remove the agent from`
* `:param int agent_id: The agent ID to remove`
#### Example usage:
`connection.clients.get_task_agent_client().delete_agent(pool_id,agent_id)`


### DeleteAgentPool
#### Description:
Delete an agent pool.

* `:param int pool_id: ID of the agent pool to delete`
#### Example usage:
`connection.clients.get_task_agent_client().delete_agent_pool(pool_id)`


### GetAgent
#### Description:
Get information about an agent.

* `:param int pool_id: The agent pool containing the agent`
* `:param int agent_id: The agent ID to get information about`
* `:param bool include_capabilities: Whether to include the agent's capabilities in the response`
* `:param bool include_assigned_request: Whether to include details about the agent's current work`
* `:param bool include_last_completed_request: Whether to include details about the agents' most recent completed work`
* `:param [str] property_filters: Filter which custom properties will be returned`
* `:rtype: :class:<TaskAgent> <azure.devops.v5_1.task_agent.models.TaskAgent>`
#### Example usage:
`connection.clients.get_task_agent_client().get_agent(pool_id,agent_id,include_capabilities,include_assigned_request,include_last_completed_request,property_filters)`


### GetAgentPool
#### Description:
Get information about an agent pool.

* `:param int pool_id: An agent pool ID`
* `:param [str] properties: Agent pool properties (comma-separated)`
* `:param str action_filter: Filter by whether the calling user has use or manage permissions`
* `:rtype: :class:<TaskAgentPool> <azure.devops.v5_1.task_agent.models.TaskAgentPool>`
#### Example usage:
`connection.clients.get_task_agent_client().get_agent_pool(pool_id,properties,action_filter)`


### GetAgentPools
#### Description:
Get a list of agent pools.

* `:param str pool_name: Filter by name`
* `:param [str] properties: Filter by agent pool properties (comma-separated)`
* `:param str pool_type: Filter by pool type`
* `:param str action_filter: Filter by whether the calling user has use or manage permissions`
* `:rtype: [TaskAgentPool]`
#### Example usage:
`connection.clients.get_task_agent_client().get_agent_pools(pool_name,properties,pool_type,action_filter)`


### GetAgentPoolsByIds
#### Description:
Get a list of agent pools.

* `:param [int] pool_ids: pool Ids to fetch`
* `:param str action_filter: Filter by whether the calling user has use or manage permissions`
* `:rtype: [TaskAgentPool]`
#### Example usage:
`connection.clients.get_task_agent_client().get_agent_pools_by_ids(pool_ids,action_filter)`


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
* `:rtype: [TaskAgent]`
#### Example usage:
`connection.clients.get_task_agent_client().get_agents(pool_id,agent_name,include_capabilities,include_assigned_request,include_last_completed_request,property_filters,demands)`


### GetYamlSchema
#### Description:
* `:rtype: object`
#### Example usage:
`connection.clients.get_task_agent_client().get_yaml_schema()`


### ReplaceAgent
#### Description:
Replace an agent.  You probably don't want to call this endpoint directly. Instead, [use the agent configuration script](https://docs.microsoft.com/azure/devops/pipelines/agents/agents) to remove and reconfigure an agent from your organization.

* `:param :class:<TaskAgent> <azure.devops.v5_1.task_agent.models.TaskAgent> agent: Updated details about the replacing agent`
* `:param int pool_id: The agent pool to use`
* `:param int agent_id: The agent to replace`
* `:rtype: :class:<TaskAgent> <azure.devops.v5_1.task_agent.models.TaskAgent>`
#### Example usage:
`connection.clients.get_task_agent_client().replace_agent(agent,pool_id,agent_id)`


### UpdateAgent
#### Description:
Update agent details.

* `:param :class:<TaskAgent> <azure.devops.v5_1.task_agent.models.TaskAgent> agent: Updated details about the agent`
* `:param int pool_id: The agent pool to use`
* `:param int agent_id: The agent to update`
* `:rtype: :class:<TaskAgent> <azure.devops.v5_1.task_agent.models.TaskAgent>`
#### Example usage:
`connection.clients.get_task_agent_client().update_agent(agent,pool_id,agent_id)`


### UpdateAgentPool
#### Description:
Update properties on an agent pool

* `:param :class:<TaskAgentPool> <azure.devops.v5_1.task_agent.models.TaskAgentPool> pool: Updated agent pool details`
* `:param int pool_id: The agent pool to update`
* `:rtype: :class:<TaskAgentPool> <azure.devops.v5_1.task_agent.models.TaskAgentPool>`
#### Example usage:
`connection.clients.get_task_agent_client().update_agent_pool(pool,pool_id)`


## Get Task Client
### AppendLogContent
#### Description:
* `:param object upload_stream: Stream to upload`
* `:param str scope_identifier: The project GUID to scope the request`
* `:param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server`
* `:param str plan_id:`
* `:param int log_id:`
* `:rtype: :class:<TaskLog> <azure.devops.v5_1.task.models.TaskLog>`
#### Example usage:
`connection.clients.get_task_client().append_log_content(upload_stream,scope_identifier,hub_name,plan_id,log_id)`


### CreateLog
#### Description:
* `:param :class:<TaskLog> <azure.devops.v5_1.task.models.TaskLog> log:`
* `:param str scope_identifier: The project GUID to scope the request`
* `:param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server`
* `:param str plan_id:`
* `:rtype: :class:<TaskLog> <azure.devops.v5_1.task.models.TaskLog>`
#### Example usage:
`connection.clients.get_task_client().create_log(log,scope_identifier,hub_name,plan_id)`


### CreateTimeline
#### Description:
* `:param :class:<Timeline> <azure.devops.v5_1.task.models.Timeline> timeline:`
* `:param str scope_identifier: The project GUID to scope the request`
* `:param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server`
* `:param str plan_id:`
* `:rtype: :class:<Timeline> <azure.devops.v5_1.task.models.Timeline>`
#### Example usage:
`connection.clients.get_task_client().create_timeline(timeline,scope_identifier,hub_name,plan_id)`


### DeleteTimeline
#### Description:
* `:param str scope_identifier: The project GUID to scope the request`
* `:param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server`
* `:param str plan_id:`
* `:param str timeline_id:`
#### Example usage:
`connection.clients.get_task_client().delete_timeline(scope_identifier,hub_name,plan_id,timeline_id)`


### GetLog
#### Description:
* `:param str scope_identifier: The project GUID to scope the request`
* `:param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server`
* `:param str plan_id:`
* `:param int log_id:`
* `:param long start_line:`
* `:param long end_line:`
* `:rtype: [str]`
#### Example usage:
`connection.clients.get_task_client().get_log(scope_identifier,hub_name,plan_id,log_id,start_line,end_line)`


### GetLogs
#### Description:
* `:param str scope_identifier: The project GUID to scope the request`
* `:param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server`
* `:param str plan_id:`
* `:rtype: [TaskLog]`
#### Example usage:
`connection.clients.get_task_client().get_logs(scope_identifier,hub_name,plan_id)`


### GetRecords
#### Description:
* `:param str scope_identifier: The project GUID to scope the request`
* `:param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server`
* `:param str plan_id:`
* `:param str timeline_id:`
* `:param int change_id:`
* `:rtype: [TimelineRecord]`
#### Example usage:
`connection.clients.get_task_client().get_records(scope_identifier,hub_name,plan_id,timeline_id,change_id)`


### GetTimeline
#### Description:
* `:param str scope_identifier: The project GUID to scope the request`
* `:param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server`
* `:param str plan_id:`
* `:param str timeline_id:`
* `:param int change_id:`
* `:param bool include_records:`
* `:rtype: :class:<Timeline> <azure.devops.v5_1.task.models.Timeline>`
#### Example usage:
`connection.clients.get_task_client().get_timeline(scope_identifier,hub_name,plan_id,timeline_id,change_id,include_records)`


### GetTimelines
#### Description:
* `:param str scope_identifier: The project GUID to scope the request`
* `:param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server`
* `:param str plan_id:`
* `:rtype: [Timeline]`
#### Example usage:
`connection.clients.get_task_client().get_timelines(scope_identifier,hub_name,plan_id)`


### UpdateRecords
#### Description:
* `:param :class:<VssJsonCollectionWrapper> <azure.devops.v5_1.task.models.VssJsonCollectionWrapper> records:`
* `:param str scope_identifier: The project GUID to scope the request`
* `:param str hub_name: The name of the server hub: "build" for the Build server or "rm" for the Release Management server`
* `:param str plan_id:`
* `:param str timeline_id:`
* `:rtype: [TimelineRecord]`
#### Example usage:
`connection.clients.get_task_client().update_records(records,scope_identifier,hub_name,plan_id,timeline_id)`


## Get Test Client
### AddTestCasesToSuite
#### Description:
Add test cases to suite.

* `:param str project: Project ID or project name`
* `:param int plan_id: ID of the test plan that contains the suite.`
* `:param int suite_id: ID of the test suite to which the test cases must be added.`
* `:param str test_case_ids: IDs of the test cases to add to the suite. Ids are specified in comma separated format.`
* `:rtype: [SuiteTestCase]`
#### Example usage:
`connection.clients.get_test_client().add_test_cases_to_suite(project,plan_id,suite_id,test_case_ids)`


### AddTestResultsToTestRun
#### Description:
Add test results to a test run.

* `:param [TestCaseResult] results: List of test results to add.`
* `:param str project: Project ID or project name`
* `:param int run_id: Test run ID into which test results to add.`
* `:rtype: [TestCaseResult]`
#### Example usage:
`connection.clients.get_test_client().add_test_results_to_test_run(results,project,run_id)`


### CreateTestRun
#### Description:
Create new test run.

* `:param :class:<RunCreateModel> <azure.devops.v5_1.test.models.RunCreateModel> test_run: Run details RunCreateModel`
* `:param str project: Project ID or project name`
* `:rtype: :class:<TestRun> <azure.devops.v5_1.test.models.TestRun>`
#### Example usage:
`connection.clients.get_test_client().create_test_run(test_run,project)`


### DeleteTestRun
#### Description:
Delete a test run by its ID.

* `:param str project: Project ID or project name`
* `:param int run_id: ID of the run to delete.`
#### Example usage:
`connection.clients.get_test_client().delete_test_run(project,run_id)`


### GetActionResults
#### Description:
Gets the action results for an iteration in a test result.

* `:param str project: Project ID or project name`
* `:param int run_id: ID of the test run that contains the result.`
* `:param int test_case_result_id: ID of the test result that contains the iterations.`
* `:param int iteration_id: ID of the iteration that contains the actions.`
* `:param str action_path: Path of a specific action, used to get just that action.`
* `:rtype: [TestActionResultModel]`
#### Example usage:
`connection.clients.get_test_client().get_action_results(project,run_id,test_case_result_id,iteration_id,action_path)`


### GetPoint
#### Description:
Get a test point.

* `:param str project: Project ID or project name`
* `:param int plan_id: ID of the test plan.`
* `:param int suite_id: ID of the suite that contains the point.`
* `:param int point_ids: ID of the test point to get.`
* `:param str wit_fields: Comma-separated list of work item field names.`
* `:rtype: :class:<TestPoint> <azure.devops.v5_1.test.models.TestPoint>`
#### Example usage:
`connection.clients.get_test_client().get_point(project,plan_id,suite_id,point_ids,wit_fields)`


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
* `:rtype: [TestPoint]`
#### Example usage:
`connection.clients.get_test_client().get_points(project,plan_id,suite_id,wit_fields,configuration_id,test_case_id,test_point_ids,include_point_details,skip,top)`


### GetResultParameters
#### Description:
Get a list of parameterized results

* `:param str project: Project ID or project name`
* `:param int run_id: ID of the test run that contains the result.`
* `:param int test_case_result_id: ID of the test result that contains the iterations.`
* `:param int iteration_id: ID of the iteration that contains the parameterized results.`
* `:param str param_name: Name of the parameter.`
* `:rtype: [TestResultParameterModel]`
#### Example usage:
`connection.clients.get_test_client().get_result_parameters(project,run_id,test_case_result_id,iteration_id,param_name)`


### GetTestCaseById
#### Description:
Get a specific test case in a test suite with test case id.

* `:param str project: Project ID or project name`
* `:param int plan_id: ID of the test plan that contains the suites.`
* `:param int suite_id: ID of the suite that contains the test case.`
* `:param int test_case_ids: ID of the test case to get.`
* `:rtype: :class:<SuiteTestCase> <azure.devops.v5_1.test.models.SuiteTestCase>`
#### Example usage:
`connection.clients.get_test_client().get_test_case_by_id(project,plan_id,suite_id,test_case_ids)`


### GetTestCases
#### Description:
Get all test cases in a suite.

* `:param str project: Project ID or project name`
* `:param int plan_id: ID of the test plan that contains the suites.`
* `:param int suite_id: ID of the suite to get.`
* `:rtype: [SuiteTestCase]`
#### Example usage:
`connection.clients.get_test_client().get_test_cases(project,plan_id,suite_id)`


### GetTestIteration
#### Description:
Get iteration for a result

* `:param str project: Project ID or project name`
* `:param int run_id: ID of the test run that contains the result.`
* `:param int test_case_result_id: ID of the test result that contains the iterations.`
* `:param int iteration_id: Id of the test results Iteration.`
* `:param bool include_action_results: Include result details for each action performed in the test iteration. ActionResults refer to outcome (pass/fail) of test steps that are executed as part of a running a manual test. Including the ActionResults flag gets the outcome of test steps in the actionResults section and test parameters in the parameters section for each test iteration.`
* `:rtype: :class:<TestIterationDetailsModel> <azure.devops.v5_1.test.models.TestIterationDetailsModel>`
#### Example usage:
`connection.clients.get_test_client().get_test_iteration(project,run_id,test_case_result_id,iteration_id,include_action_results)`


### GetTestIterations
#### Description:
Get iterations for a result

* `:param str project: Project ID or project name`
* `:param int run_id: ID of the test run that contains the result.`
* `:param int test_case_result_id: ID of the test result that contains the iterations.`
* `:param bool include_action_results: Include result details for each action performed in the test iteration. ActionResults refer to outcome (pass/fail) of test steps that are executed as part of a running a manual test. Including the ActionResults flag gets the outcome of test steps in the actionResults section and test parameters in the parameters section for each test iteration.`
* `:rtype: [TestIterationDetailsModel]`
#### Example usage:
`connection.clients.get_test_client().get_test_iterations(project,run_id,test_case_result_id,include_action_results)`


### GetTestResultById
#### Description:
Get a test result for a test run.

* `:param str project: Project ID or project name`
* `:param int run_id: Test run ID of a test result to fetch.`
* `:param int test_case_result_id: Test result ID.`
* `:param str details_to_include: Details to include with test results. Default is None. Other values are Iterations, WorkItems and SubResults.`
* `:rtype: :class:<TestCaseResult> <azure.devops.v5_1.test.models.TestCaseResult>`
#### Example usage:
`connection.clients.get_test_client().get_test_result_by_id(project,run_id,test_case_result_id,details_to_include)`


### GetTestResults
#### Description:
Get test results for a test run.

* `:param str project: Project ID or project name`
* `:param int run_id: Test run ID of test results to fetch.`
* `:param str details_to_include: Details to include with test results. Default is None. Other values are Iterations and WorkItems.`
* `:param int skip: Number of test results to skip from beginning.`
* `:param int top: Number of test results to return. Maximum is 1000 when detailsToInclude is None and 200 otherwise.`
* `:param [TestOutcome] outcomes: Comma separated list of test outcomes to filter test results.`
* `:rtype: [TestCaseResult]`
#### Example usage:
`connection.clients.get_test_client().get_test_results(project,run_id,details_to_include,skip,top,outcomes)`


### GetTestRunById
#### Description:
Get a test run by its ID.

* `:param str project: Project ID or project name`
* `:param int run_id: ID of the run to get.`
* `:param bool include_details: Default value is true. It includes details like run statistics, release, build, test environment, post process state, and more.`
* `:rtype: :class:<TestRun> <azure.devops.v5_1.test.models.TestRun>`
#### Example usage:
`connection.clients.get_test_client().get_test_run_by_id(project,run_id,include_details)`


### GetTestRunStatistics
#### Description:
Get test run statistics , used when we want to get summary of a run by outcome.

* `:param str project: Project ID or project name`
* `:param int run_id: ID of the run to get.`
* `:rtype: :class:<TestRunStatistic> <azure.devops.v5_1.test.models.TestRunStatistic>`
#### Example usage:
`connection.clients.get_test_client().get_test_run_statistics(project,run_id)`


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
* `:rtype: [TestRun]`
#### Example usage:
`connection.clients.get_test_client().get_test_runs(project,build_uri,owner,tmi_run_id,plan_id,include_run_details,automated,skip,top)`


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
* `:rtype: :class:<QueryTestRunsResponseValue>`
#### Example usage:
`connection.clients.get_test_client().query_test_runs(project,min_last_updated_date,max_last_updated_date,state,plan_ids,is_automated,publish_context,build_ids,build_def_ids,branch_name,release_ids,release_def_ids,release_env_ids,release_env_def_ids,run_title,top,continuation_token)`


### RemoveTestCasesFromSuiteUrl
#### Description:
The test points associated with the test cases are removed from the test suite. The test case work item is not deleted from the system. See test cases resource to delete a test case permanently.

* `:param str project: Project ID or project name`
* `:param int plan_id: ID of the test plan that contains the suite.`
* `:param int suite_id: ID of the suite to get.`
* `:param str test_case_ids: IDs of the test cases to remove from the suite.`
#### Example usage:
`connection.clients.get_test_client().remove_test_cases_from_suite_url(project,plan_id,suite_id,test_case_ids)`


### UpdateSuiteTestCases
#### Description:
Updates the properties of the test case association in a suite.

* `:param :class:<SuiteTestCaseUpdateModel> <azure.devops.v5_1.test.models.SuiteTestCaseUpdateModel> suite_test_case_update_model: Model for updation of the properties of test case suite association.`
* `:param str project: Project ID or project name`
* `:param int plan_id: ID of the test plan that contains the suite.`
* `:param int suite_id: ID of the test suite to which the test cases must be added.`
* `:param str test_case_ids: IDs of the test cases to add to the suite. Ids are specified in comma separated format.`
* `:rtype: [SuiteTestCase]`
#### Example usage:
`connection.clients.get_test_client().update_suite_test_cases(suite_test_case_update_model,project,plan_id,suite_id,test_case_ids)`


### UpdateTestPoints
#### Description:
Update test points.

* `:param :class:<PointUpdateModel> <azure.devops.v5_1.test.models.PointUpdateModel> point_update_model: Data to update.`
* `:param str project: Project ID or project name`
* `:param int plan_id: ID of the test plan.`
* `:param int suite_id: ID of the suite that contains the points.`
* `:param str point_ids: ID of the test point to get. Use a comma-separated list of IDs to update multiple test points.`
* `:rtype: [TestPoint]`
#### Example usage:
`connection.clients.get_test_client().update_test_points(point_update_model,project,plan_id,suite_id,point_ids)`


### UpdateTestResults
#### Description:
Update test results in a test run.

* `:param [TestCaseResult] results: List of test results to update.`
* `:param str project: Project ID or project name`
* `:param int run_id: Test run ID whose test results to update.`
* `:rtype: [TestCaseResult]`
#### Example usage:
`connection.clients.get_test_client().update_test_results(results,project,run_id)`


### UpdateTestRun
#### Description:
Update test run by its ID.

* `:param :class:<RunUpdateModel> <azure.devops.v5_1.test.models.RunUpdateModel> run_update_model: Run details RunUpdateModel`
* `:param str project: Project ID or project name`
* `:param int run_id: ID of the run to update.`
* `:rtype: :class:<TestRun> <azure.devops.v5_1.test.models.TestRun>`
#### Example usage:
`connection.clients.get_test_client().update_test_run(run_update_model,project,run_id)`


## Get Test Plan Client
### GetSuitesByTestCaseId
#### Description:
Find the list of all test suites in which a given test case is present. This is helpful if you need to find out which test suites are using a test case, when you need to make changes to a test case.

* `:param int test_case_id: ID of the test case for which suites need to be fetched.`
* `:rtype: [TestSuite]`
#### Example usage:
`connection.clients.get_test_plan_client().get_suites_by_test_case_id(test_case_id)`


## Get Test Results Client
### GetTestRunStatistics
#### Description:
Get test run statistics , used when we want to get summary of a run by outcome.

* `:param str project: Project ID or project name`
* `:param int run_id: ID of the run to get.`
* `:rtype: :class:<TestRunStatistic> <azure.devops.v5_1.test_results.models.TestRunStatistic>`
#### Example usage:
`connection.clients.get_test_results_client().get_test_run_statistics(project,run_id)`


## Get Tfvc Client
### CreateChangeset
#### Description:
Create a new changeset.

* `:param :class:<TfvcChangeset> <azure.devops.v5_1.tfvc.models.TfvcChangeset> changeset:`
* `:param str project: Project ID or project name`
* `:rtype: :class:<TfvcChangesetRef> <azure.devops.v5_1.tfvc.models.TfvcChangesetRef>`
#### Example usage:
`connection.clients.get_tfvc_client().create_changeset(changeset,project)`


### GetBatchedChangesets
#### Description:
Returns changesets for a given list of changeset Ids.

* `:param :class:<TfvcChangesetsRequestData> <azure.devops.v5_1.tfvc.models.TfvcChangesetsRequestData> changesets_request_data: List of changeset IDs.`
* `:rtype: [TfvcChangesetRef]`
#### Example usage:
`connection.clients.get_tfvc_client().get_batched_changesets(changesets_request_data)`


### GetBranch
#### Description:
Get a single branch hierarchy at the given path with parents or children as specified.

* `:param str path: Full path to the branch.  Default: $/ Examples: $/, $/MyProject, $/MyProject/SomeFolder.`
* `:param str project: Project ID or project name`
* `:param bool include_parent: Return the parent branch, if there is one. Default: False`
* `:param bool include_children: Return child branches, if there are any. Default: False`
* `:rtype: :class:<TfvcBranch> <azure.devops.v5_1.tfvc.models.TfvcBranch>`
#### Example usage:
`connection.clients.get_tfvc_client().get_branch(path,project,include_parent,include_children)`


### GetBranchRefs
#### Description:
Get branch hierarchies below the specified scopePath

* `:param str scope_path: Full path to the branch.  Default: $/ Examples: $/, $/MyProject, $/MyProject/SomeFolder.`
* `:param str project: Project ID or project name`
* `:param bool include_deleted: Return deleted branches. Default: False`
* `:param bool include_links: Return links. Default: False`
* `:rtype: [TfvcBranchRef]`
#### Example usage:
`connection.clients.get_tfvc_client().get_branch_refs(scope_path,project,include_deleted,include_links)`


### GetBranches
#### Description:
Get a collection of branch roots -- first-level children, branches with no parents.

* `:param str project: Project ID or project name`
* `:param bool include_parent: Return the parent branch, if there is one. Default: False`
* `:param bool include_children: Return the child branches for each root branch. Default: False`
* `:param bool include_deleted: Return deleted branches. Default: False`
* `:param bool include_links: Return links. Default: False`
* `:rtype: [TfvcBranch]`
#### Example usage:
`connection.clients.get_tfvc_client().get_branches(project,include_parent,include_children,include_deleted,include_links)`


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
* `:rtype: :class:<TfvcChangeset> <azure.devops.v5_1.tfvc.models.TfvcChangeset>`
#### Example usage:
`connection.clients.get_tfvc_client().get_changeset(id,project,max_change_count,include_details,include_work_items,max_comment_length,include_source_rename,skip,top,orderby,search_criteria)`


### GetChangesetChanges
#### Description:
Retrieve Tfvc changes for a given changeset.

* `:param int id: ID of the changeset. Default: null`
* `:param int skip: Number of results to skip. Default: null`
* `:param int top: The maximum number of results to return. Default: null`
* `:param str continuation_token: Return the next page of results. Default: null`
* `:rtype: :class:<GetChangesetChangesResponseValue>`
#### Example usage:
`connection.clients.get_tfvc_client().get_changeset_changes(id,skip,top,continuation_token)`


### GetChangesetWorkItems
#### Description:
Retrieves the work items associated with a particular changeset.

* `:param int id: ID of the changeset. Default: null`
* `:rtype: [AssociatedWorkItem]`
#### Example usage:
`connection.clients.get_tfvc_client().get_changeset_work_items(id)`


### GetChangesets
#### Description:
Retrieve Tfvc Changesets

* `:param str project: Project ID or project name`
* `:param int max_comment_length: Include details about associated work items in the response. Default: null`
* `:param int skip: Number of results to skip. Default: null`
* `:param int top: The maximum number of results to return. Default: null`
* `:param str orderby: Results are sorted by ID in descending order by default. Use id asc to sort by ID in ascending order.`
* `:param :class:<TfvcChangesetSearchCriteria> <azure.devops.v5_1.tfvc.models.TfvcChangesetSearchCriteria> search_criteria: Following criteria available (.itemPath, .version, .versionType, .versionOption, .author, .fromId, .toId, .fromDate, .toDate) Default: null`
* `:rtype: [TfvcChangesetRef]`
#### Example usage:
`connection.clients.get_tfvc_client().get_changesets(project,max_comment_length,skip,top,orderby,search_criteria)`


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
* `:rtype: :class:<TfvcItem> <azure.devops.v5_1.tfvc.models.TfvcItem>`
#### Example usage:
`connection.clients.get_tfvc_client().get_item(path,project,file_name,download,scope_path,recursion_level,version_descriptor,include_content)`


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
* `:rtype: object`
#### Example usage:
`connection.clients.get_tfvc_client().get_item_content(path,project,file_name,download,scope_path,recursion_level,version_descriptor,include_content)`


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
* `:rtype: object`
#### Example usage:
`connection.clients.get_tfvc_client().get_item_text(path,project,file_name,download,scope_path,recursion_level,version_descriptor,include_content)`


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
* `:rtype: object`
#### Example usage:
`connection.clients.get_tfvc_client().get_item_zip(path,project,file_name,download,scope_path,recursion_level,version_descriptor,include_content)`


### GetItems
#### Description:
Get a list of Tfvc items

* `:param str project: Project ID or project name`
* `:param str scope_path: Version control path of a folder to return multiple items.`
* `:param str recursion_level: None (just the item), or OneLevel (contents of a folder).`
* `:param bool include_links: True to include links.`
* `:param :class:<TfvcVersionDescriptor> <azure.devops.v5_1.tfvc.models.TfvcVersionDescriptor> version_descriptor:`
* `:rtype: [TfvcItem]`
#### Example usage:
`connection.clients.get_tfvc_client().get_items(project,scope_path,recursion_level,include_links,version_descriptor)`


### GetItemsBatch
#### Description:
Post for retrieving a set of items given a list of paths or a long path. Allows for specifying the recursionLevel and version descriptors for each path.

* `:param :class:<TfvcItemRequestData> <azure.devops.v5_1.tfvc.models.TfvcItemRequestData> item_request_data:`
* `:param str project: Project ID or project name`
* `:rtype: [[TfvcItem]]`
#### Example usage:
`connection.clients.get_tfvc_client().get_items_batch(item_request_data,project)`


### GetItemsBatchZip
#### Description:
Post for retrieving a set of items given a list of paths or a long path. Allows for specifying the recursionLevel and version descriptors for each path.

* `:param :class:<TfvcItemRequestData> <azure.devops.v5_1.tfvc.models.TfvcItemRequestData> item_request_data:`
* `:param str project: Project ID or project name`
* `:rtype: object`
#### Example usage:
`connection.clients.get_tfvc_client().get_items_batch_zip(item_request_data,project)`


### GetLabel
#### Description:
Get a single deep label.

* `:param str label_id: Unique identifier of label`
* `:param :class:<TfvcLabelRequestData> <azure.devops.v5_1.tfvc.models.TfvcLabelRequestData> request_data: maxItemCount`
* `:param str project: Project ID or project name`
* `:rtype: :class:<TfvcLabel> <azure.devops.v5_1.tfvc.models.TfvcLabel>`
#### Example usage:
`connection.clients.get_tfvc_client().get_label(label_id,request_data,project)`


### GetLabelItems
#### Description:
Get items under a label.

* `:param str label_id: Unique identifier of label`
* `:param int top: Max number of items to return`
* `:param int skip: Number of items to skip`
* `:rtype: [TfvcItem]`
#### Example usage:
`connection.clients.get_tfvc_client().get_label_items(label_id,top,skip)`


### GetLabels
#### Description:
Get a collection of shallow label references.

* `:param :class:<TfvcLabelRequestData> <azure.devops.v5_1.tfvc.models.TfvcLabelRequestData> request_data: labelScope, name, owner, and itemLabelFilter`
* `:param str project: Project ID or project name`
* `:param int top: Max number of labels to return, defaults to 100 when undefined`
* `:param int skip: Number of labels to skip`
* `:rtype: [TfvcLabelRef]`
#### Example usage:
`connection.clients.get_tfvc_client().get_labels(request_data,project,top,skip)`


### GetShelveset
#### Description:
Get a single deep shelveset.

* `:param str shelveset_id: Shelveset's unique ID`
* `:param :class:<TfvcShelvesetRequestData> <azure.devops.v5_1.tfvc.models.TfvcShelvesetRequestData> request_data: includeDetails, includeWorkItems, maxChangeCount, and maxCommentLength`
* `:rtype: :class:<TfvcShelveset> <azure.devops.v5_1.tfvc.models.TfvcShelveset>`
#### Example usage:
`connection.clients.get_tfvc_client().get_shelveset(shelveset_id,request_data)`


### GetShelvesetChanges
#### Description:
Get changes included in a shelveset.

* `:param str shelveset_id: Shelveset's unique ID`
* `:param int top: Max number of changes to return`
* `:param int skip: Number of changes to skip`
* `:rtype: [TfvcChange]`
#### Example usage:
`connection.clients.get_tfvc_client().get_shelveset_changes(shelveset_id,top,skip)`


### GetShelvesetWorkItems
#### Description:
Get work items associated with a shelveset.

* `:param str shelveset_id: Shelveset's unique ID`
* `:rtype: [AssociatedWorkItem]`
#### Example usage:
`connection.clients.get_tfvc_client().get_shelveset_work_items(shelveset_id)`


### GetShelvesets
#### Description:
Return a collection of shallow shelveset references.

* `:param :class:<TfvcShelvesetRequestData> <azure.devops.v5_1.tfvc.models.TfvcShelvesetRequestData> request_data: name, owner, and maxCommentLength`
* `:param int top: Max number of shelvesets to return`
* `:param int skip: Number of shelvesets to skip`
* `:rtype: [TfvcShelvesetRef]`
#### Example usage:
`connection.clients.get_tfvc_client().get_shelvesets(request_data,top,skip)`


## Get Wiki Client
### CreateAttachment
#### Description:
Creates an attachment in the wiki.

* `:param object upload_stream: Stream to upload`
* `:param str project: Project ID or project name`
* `:param str wiki_identifier: Wiki Id or name.`
* `:param str name: Wiki attachment name.`
* `:param :class:<GitVersionDescriptor> <azure.devops.v5_1.wiki.models.GitVersionDescriptor> version_descriptor: GitVersionDescriptor for the page. (Optional in case of ProjectWiki).`
* `:rtype: :class:<WikiAttachmentResponse> <azure.devops.v5_1.wiki.models.WikiAttachmentResponse>`
#### Example usage:
`connection.clients.get_wiki_client().create_attachment(upload_stream,project,wiki_identifier,name,version_descriptor)`


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
* `:rtype: :class:<WikiPageResponse> <azure.devops.v5_1.wiki.models.WikiPageResponse>`
#### Example usage:
`connection.clients.get_wiki_client().create_or_update_page(parameters,project,wiki_identifier,path,version,comment,version_descriptor)`


### CreatePageMove
#### Description:
Creates a page move operation that updates the path and order of the page as provided in the parameters.

* `:param :class:<WikiPageMoveParameters> <azure.devops.v5_1.wiki.models.WikiPageMoveParameters> page_move_parameters: Page more operation parameters.`
* `:param str project: Project ID or project name`
* `:param str wiki_identifier: Wiki Id or name.`
* `:param str comment: Comment that is to be associated with this page move.`
* `:param :class:<GitVersionDescriptor> <azure.devops.v5_1.wiki.models.GitVersionDescriptor> version_descriptor: GitVersionDescriptor for the page. (Optional in case of ProjectWiki).`
* `:rtype: :class:<WikiPageMoveResponse> <azure.devops.v5_1.wiki.models.WikiPageMoveResponse>`
#### Example usage:
`connection.clients.get_wiki_client().create_page_move(page_move_parameters,project,wiki_identifier,comment,version_descriptor)`


### CreateWiki
#### Description:
Creates the wiki resource.

* `:param :class:<WikiCreateParametersV2> <azure.devops.v5_1.wiki.models.WikiCreateParametersV2> wiki_create_params: Parameters for the wiki creation.`
* `:param str project: Project ID or project name`
* `:rtype: :class:<WikiV2> <azure.devops.v5_1.wiki.models.WikiV2>`
#### Example usage:
`connection.clients.get_wiki_client().create_wiki(wiki_create_params,project)`


### DeletePage
#### Description:
Deletes a wiki page.

* `:param str project: Project ID or project name`
* `:param str wiki_identifier: Wiki Id or name.`
* `:param str path: Wiki page path.`
* `:param str comment: Comment to be associated with this page delete.`
* `:param :class:<GitVersionDescriptor> <azure.devops.v5_1.wiki.models.GitVersionDescriptor> version_descriptor: GitVersionDescriptor for the page. (Optional in case of ProjectWiki).`
* `:rtype: :class:<WikiPageResponse> <azure.devops.v5_1.wiki.models.WikiPageResponse>`
#### Example usage:
`connection.clients.get_wiki_client().delete_page(project,wiki_identifier,path,comment,version_descriptor)`


### DeleteWiki
#### Description:
Deletes the wiki corresponding to the wiki name or Id provided.

* `:param str wiki_identifier: Wiki name or Id.`
* `:param str project: Project ID or project name`
* `:rtype: :class:<WikiV2> <azure.devops.v5_1.wiki.models.WikiV2>`
#### Example usage:
`connection.clients.get_wiki_client().delete_wiki(wiki_identifier,project)`


### GetAllWikis
#### Description:
Gets all wikis in a project or collection.

* `:param str project: Project ID or project name`
* `:rtype: [WikiV2]`
#### Example usage:
`connection.clients.get_wiki_client().get_all_wikis(project)`


### GetPage
#### Description:
Gets metadata or content of the wiki page for the provided path. Content negotiation is done based on the `Accept` header sent in the request.

* `:param str project: Project ID or project name`
* `:param str wiki_identifier: Wiki Id or name.`
* `:param str path: Wiki page path.`
* `:param str recursion_level: Recursion level for subpages retrieval. Defaults to None (Optional).`
* `:param :class:<GitVersionDescriptor> <azure.devops.v5_1.wiki.models.GitVersionDescriptor> version_descriptor: GitVersionDescriptor for the page. Defaults to the default branch (Optional).`
* `:param bool include_content: True to include the content of the page in the response for Json content type. Defaults to false (Optional)`
* `:rtype: :class:<WikiPageResponse> <azure.devops.v5_1.wiki.models.WikiPageResponse>`
#### Example usage:
`connection.clients.get_wiki_client().get_page(project,wiki_identifier,path,recursion_level,version_descriptor,include_content)`


### GetPageText
#### Description:
Gets metadata or content of the wiki page for the provided path. Content negotiation is done based on the `Accept` header sent in the request.

* `:param str project: Project ID or project name`
* `:param str wiki_identifier: Wiki Id or name.`
* `:param str path: Wiki page path.`
* `:param str recursion_level: Recursion level for subpages retrieval. Defaults to None (Optional).`
* `:param :class:<GitVersionDescriptor> <azure.devops.v5_1.wiki.models.GitVersionDescriptor> version_descriptor: GitVersionDescriptor for the page. Defaults to the default branch (Optional).`
* `:param bool include_content: True to include the content of the page in the response for Json content type. Defaults to false (Optional)`
* `:rtype: object`
#### Example usage:
`connection.clients.get_wiki_client().get_page_text(project,wiki_identifier,path,recursion_level,version_descriptor,include_content)`


### GetPageZip
#### Description:
Gets metadata or content of the wiki page for the provided path. Content negotiation is done based on the `Accept` header sent in the request.

* `:param str project: Project ID or project name`
* `:param str wiki_identifier: Wiki Id or name.`
* `:param str path: Wiki page path.`
* `:param str recursion_level: Recursion level for subpages retrieval. Defaults to None (Optional).`
* `:param :class:<GitVersionDescriptor> <azure.devops.v5_1.wiki.models.GitVersionDescriptor> version_descriptor: GitVersionDescriptor for the page. Defaults to the default branch (Optional).`
* `:param bool include_content: True to include the content of the page in the response for Json content type. Defaults to false (Optional)`
* `:rtype: object`
#### Example usage:
`connection.clients.get_wiki_client().get_page_zip(project,wiki_identifier,path,recursion_level,version_descriptor,include_content)`


### GetWiki
#### Description:
Gets the wiki corresponding to the wiki name or Id provided.

* `:param str wiki_identifier: Wiki name or id.`
* `:param str project: Project ID or project name`
* `:rtype: :class:<WikiV2> <azure.devops.v5_1.wiki.models.WikiV2>`
#### Example usage:
`connection.clients.get_wiki_client().get_wiki(wiki_identifier,project)`


### UpdateWiki
#### Description:
Updates the wiki corresponding to the wiki Id or name provided using the update parameters.

* `:param :class:<WikiUpdateParameters> <azure.devops.v5_1.wiki.models.WikiUpdateParameters> update_parameters: Update parameters.`
* `:param str wiki_identifier: Wiki name or Id.`
* `:param str project: Project ID or project name`
* `:rtype: :class:<WikiV2> <azure.devops.v5_1.wiki.models.WikiV2>`
#### Example usage:
`connection.clients.get_wiki_client().update_wiki(update_parameters,wiki_identifier,project)`


## Get Work Client
### CreatePlan
#### Description:
Add a new plan for the team

* `:param :class:<CreatePlan> <azure.devops.v5_1.work.models.CreatePlan> posted_plan: Plan definition`
* `:param str project: Project ID or project name`
* `:rtype: :class:<Plan> <azure.devops.v5_1.work.models.Plan>`
#### Example usage:
`connection.clients.get_work_client().create_plan(posted_plan,project)`


### DeletePlan
#### Description:
Delete the specified plan

* `:param str project: Project ID or project name`
* `:param str id: Identifier of the plan`
#### Example usage:
`connection.clients.get_work_client().delete_plan(project,id)`


### DeleteTeamIteration
#### Description:
Delete a team's iteration by iterationId

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str id: ID of the iteration`
#### Example usage:
`connection.clients.get_work_client().delete_team_iteration(team_context,id)`


### GetBacklogConfigurations
#### Description:
Gets backlog configuration for a team

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:rtype: :class:<BacklogConfiguration> <azure.devops.v5_1.work.models.BacklogConfiguration>`
#### Example usage:
`connection.clients.get_work_client().get_backlog_configurations(team_context)`


### GetBoard
#### Description:
Get board

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str id: identifier for board, either board's backlog level name (Eg:"Stories") or Id`
* `:rtype: :class:<Board> <azure.devops.v5_1.work.models.Board>`
#### Example usage:
`connection.clients.get_work_client().get_board(team_context,id)`


### GetBoardCardRuleSettings
#### Description:
Get board card Rule settings for the board id or board by name

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str board:`
* `:rtype: :class:<BoardCardRuleSettings> <azure.devops.v5_1.work.models.BoardCardRuleSettings>`
#### Example usage:
`connection.clients.get_work_client().get_board_card_rule_settings(team_context,board)`


### GetBoardCardSettings
#### Description:
Get board card settings for the board id or board by name

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str board:`
* `:rtype: :class:<BoardCardSettings> <azure.devops.v5_1.work.models.BoardCardSettings>`
#### Example usage:
`connection.clients.get_work_client().get_board_card_settings(team_context,board)`


### GetBoardChart
#### Description:
Get a board chart

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str board: Identifier for board, either board's backlog level name (Eg:"Stories") or Id`
* `:param str name: The chart name`
* `:rtype: :class:<BoardChart> <azure.devops.v5_1.work.models.BoardChart>`
#### Example usage:
`connection.clients.get_work_client().get_board_chart(team_context,board,name)`


### GetBoardCharts
#### Description:
Get board charts

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str board: Identifier for board, either board's backlog level name (Eg:"Stories") or Id`
* `:rtype: [BoardChartReference]`
#### Example usage:
`connection.clients.get_work_client().get_board_charts(team_context,board)`


### GetBoardColumns
#### Description:
Get columns on a board

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str board: Name or ID of the specific board`
* `:rtype: [BoardColumn]`
#### Example usage:
`connection.clients.get_work_client().get_board_columns(team_context,board)`


### GetBoardRows
#### Description:
Get rows on a board

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str board: Name or ID of the specific board`
* `:rtype: [BoardRow]`
#### Example usage:
`connection.clients.get_work_client().get_board_rows(team_context,board)`


### GetBoards
#### Description:
Get boards

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:rtype: [BoardReference]`
#### Example usage:
`connection.clients.get_work_client().get_boards(team_context)`


### GetCapacitiesWithIdentityRef
#### Description:
Get a team's capacity

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str iteration_id: ID of the iteration`
* `:rtype: [TeamMemberCapacityIdentityRef]`
#### Example usage:
`connection.clients.get_work_client().get_capacities_with_identity_ref(team_context,iteration_id)`


### GetCapacityWithIdentityRef
#### Description:
Get a team member's capacity

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str iteration_id: ID of the iteration`
* `:param str team_member_id: ID of the team member`
* `:rtype: :class:<TeamMemberCapacityIdentityRef> <azure.devops.v5_1.work.models.TeamMemberCapacityIdentityRef>`
#### Example usage:
`connection.clients.get_work_client().get_capacity_with_identity_ref(team_context,iteration_id,team_member_id)`


### GetColumnSuggestedValues
#### Description:
Get available board columns in a project

* `:param str project: Project ID or project name`
* `:rtype: [BoardSuggestedValue]`
#### Example usage:
`connection.clients.get_work_client().get_column_suggested_values(project)`


### GetDeliveryTimelineData
#### Description:
Get Delivery View Data

* `:param str project: Project ID or project name`
* `:param str id: Identifier for delivery view`
* `:param int revision: Revision of the plan for which you want data. If the current plan is a different revision you will get an ViewRevisionMismatchException exception. If you do not supply a revision you will get data for the latest revision.`
* `:param datetime start_date: The start date of timeline`
* `:param datetime end_date: The end date of timeline`
* `:rtype: :class:<DeliveryViewData> <azure.devops.v5_1.work.models.DeliveryViewData>`
#### Example usage:
`connection.clients.get_work_client().get_delivery_timeline_data(project,id,revision,start_date,end_date)`


### GetPlan
#### Description:
Get the information for the specified plan

* `:param str project: Project ID or project name`
* `:param str id: Identifier of the plan`
* `:rtype: :class:<Plan> <azure.devops.v5_1.work.models.Plan>`
#### Example usage:
`connection.clients.get_work_client().get_plan(project,id)`


### GetPlans
#### Description:
Get the information for all the plans configured for the given team

* `:param str project: Project ID or project name`
* `:rtype: [Plan]`
#### Example usage:
`connection.clients.get_work_client().get_plans(project)`


### GetRowSuggestedValues
#### Description:
Get available board rows in a project

* `:param str project: Project ID or project name`
* `:rtype: [BoardSuggestedValue]`
#### Example usage:
`connection.clients.get_work_client().get_row_suggested_values(project)`


### GetTeamDaysOff
#### Description:
Get team's days off for an iteration

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str iteration_id: ID of the iteration`
* `:rtype: :class:<TeamSettingsDaysOff> <azure.devops.v5_1.work.models.TeamSettingsDaysOff>`
#### Example usage:
`connection.clients.get_work_client().get_team_days_off(team_context,iteration_id)`


### GetTeamFieldValues
#### Description:
Get a collection of team field values

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:rtype: :class:<TeamFieldValues> <azure.devops.v5_1.work.models.TeamFieldValues>`
#### Example usage:
`connection.clients.get_work_client().get_team_field_values(team_context)`


### GetTeamIteration
#### Description:
Get team's iteration by iterationId

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str id: ID of the iteration`
* `:rtype: :class:<TeamSettingsIteration> <azure.devops.v5_1.work.models.TeamSettingsIteration>`
#### Example usage:
`connection.clients.get_work_client().get_team_iteration(team_context,id)`


### GetTeamIterations
#### Description:
Get a team's iterations using timeframe filter

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str timeframe: A filter for which iterations are returned based on relative time. Only Current is supported currently.`
* `:rtype: [TeamSettingsIteration]`
#### Example usage:
`connection.clients.get_work_client().get_team_iterations(team_context,timeframe)`


### GetTeamSettings
#### Description:
Get a team's settings

* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:rtype: :class:<TeamSetting> <azure.devops.v5_1.work.models.TeamSetting>`
#### Example usage:
`connection.clients.get_work_client().get_team_settings(team_context)`


### PostTeamIteration
#### Description:
Add an iteration to the team

* `:param :class:<TeamSettingsIteration> <azure.devops.v5_1.work.models.TeamSettingsIteration> iteration: Iteration to add`
* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:rtype: :class:<TeamSettingsIteration> <azure.devops.v5_1.work.models.TeamSettingsIteration>`
#### Example usage:
`connection.clients.get_work_client().post_team_iteration(iteration,team_context)`


### ReplaceCapacitiesWithIdentityRef
#### Description:
Replace a team's capacity

* `:param [TeamMemberCapacityIdentityRef] capacities: Team capacity to replace`
* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str iteration_id: ID of the iteration`
* `:rtype: [TeamMemberCapacityIdentityRef]`
#### Example usage:
`connection.clients.get_work_client().replace_capacities_with_identity_ref(capacities,team_context,iteration_id)`


### SetBoardOptions
#### Description:
Update board options

* `:param {str} options: options to updated`
* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str id: identifier for board, either category plural name (Eg:"Stories") or guid`
* `:rtype: {str}`
#### Example usage:
`connection.clients.get_work_client().set_board_options(options,team_context,id)`


### UpdateBoardCardRuleSettings
#### Description:
Update board card Rule settings for the board id or board by name

* `:param :class:<BoardCardRuleSettings> <azure.devops.v5_1.work.models.BoardCardRuleSettings> board_card_rule_settings:`
* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str board:`
* `:rtype: :class:<BoardCardRuleSettings> <azure.devops.v5_1.work.models.BoardCardRuleSettings>`
#### Example usage:
`connection.clients.get_work_client().update_board_card_rule_settings(board_card_rule_settings,team_context,board)`


### UpdateBoardCardSettings
#### Description:
Update board card settings for the board id or board by name

* `:param :class:<BoardCardSettings> <azure.devops.v5_1.work.models.BoardCardSettings> board_card_settings_to_save:`
* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str board:`
* `:rtype: :class:<BoardCardSettings> <azure.devops.v5_1.work.models.BoardCardSettings>`
#### Example usage:
`connection.clients.get_work_client().update_board_card_settings(board_card_settings_to_save,team_context,board)`


### UpdateBoardChart
#### Description:
Update a board chart

* `:param :class:<BoardChart> <azure.devops.v5_1.work.models.BoardChart> chart:`
* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str board: Identifier for board, either board's backlog level name (Eg:"Stories") or Id`
* `:param str name: The chart name`
* `:rtype: :class:<BoardChart> <azure.devops.v5_1.work.models.BoardChart>`
#### Example usage:
`connection.clients.get_work_client().update_board_chart(chart,team_context,board,name)`


### UpdateBoardColumns
#### Description:
Update columns on a board

* `:param [BoardColumn] board_columns: List of board columns to update`
* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str board: Name or ID of the specific board`
* `:rtype: [BoardColumn]`
#### Example usage:
`connection.clients.get_work_client().update_board_columns(board_columns,team_context,board)`


### UpdateBoardRows
#### Description:
Update rows on a board

* `:param [BoardRow] board_rows: List of board rows to update`
* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str board: Name or ID of the specific board`
* `:rtype: [BoardRow]`
#### Example usage:
`connection.clients.get_work_client().update_board_rows(board_rows,team_context,board)`


### UpdateCapacityWithIdentityRef
#### Description:
Update a team member's capacity

* `:param :class:<CapacityPatch> <azure.devops.v5_1.work.models.CapacityPatch> patch: Updated capacity`
* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str iteration_id: ID of the iteration`
* `:param str team_member_id: ID of the team member`
* `:rtype: :class:<TeamMemberCapacityIdentityRef> <azure.devops.v5_1.work.models.TeamMemberCapacityIdentityRef>`
#### Example usage:
`connection.clients.get_work_client().update_capacity_with_identity_ref(patch,team_context,iteration_id,team_member_id)`


### UpdatePlan
#### Description:
Update the information for the specified plan

* `:param :class:<UpdatePlan> <azure.devops.v5_1.work.models.UpdatePlan> updated_plan: Plan definition to be updated`
* `:param str project: Project ID or project name`
* `:param str id: Identifier of the plan`
* `:rtype: :class:<Plan> <azure.devops.v5_1.work.models.Plan>`
#### Example usage:
`connection.clients.get_work_client().update_plan(updated_plan,project,id)`


### UpdateTeamDaysOff
#### Description:
Set a team's days off for an iteration

* `:param :class:<TeamSettingsDaysOffPatch> <azure.devops.v5_1.work.models.TeamSettingsDaysOffPatch> days_off_patch: Team's days off patch containing a list of start and end dates`
* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:param str iteration_id: ID of the iteration`
* `:rtype: :class:<TeamSettingsDaysOff> <azure.devops.v5_1.work.models.TeamSettingsDaysOff>`
#### Example usage:
`connection.clients.get_work_client().update_team_days_off(days_off_patch,team_context,iteration_id)`


### UpdateTeamFieldValues
#### Description:
Update team field values

* `:param :class:<TeamFieldValuesPatch> <azure.devops.v5_1.work.models.TeamFieldValuesPatch> patch:`
* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:rtype: :class:<TeamFieldValues> <azure.devops.v5_1.work.models.TeamFieldValues>`
#### Example usage:
`connection.clients.get_work_client().update_team_field_values(patch,team_context)`


### UpdateTeamSettings
#### Description:
Update a team's settings

* `:param :class:<TeamSettingsPatch> <azure.devops.v5_1.work.models.TeamSettingsPatch> team_settings_patch: TeamSettings changes`
* `:param :class:<TeamContext> <azure.devops.v5_1.work.models.TeamContext> team_context: The team context for the operation`
* `:rtype: :class:<TeamSetting> <azure.devops.v5_1.work.models.TeamSetting>`
#### Example usage:
`connection.clients.get_work_client().update_team_settings(team_settings_patch,team_context)`


## Get Work Item Tracking Client
### CreateAttachment
#### Description:
Uploads an attachment.

* `:param object upload_stream: Stream to upload`
* `:param str project: Project ID or project name`
* `:param str file_name: The name of the file`
* `:param str upload_type: Attachment upload type: Simple or Chunked`
* `:param str area_path: Target project Area Path`
* `:rtype: :class:<AttachmentReference> <azure.devops.v5_1.work_item_tracking.models.AttachmentReference>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().create_attachment(upload_stream,project,file_name,upload_type,area_path)`


### CreateField
#### Description:
Create a new field.

* `:param :class:<WorkItemField> <azure.devops.v5_1.work_item_tracking.models.WorkItemField> work_item_field: New field definition`
* `:param str project: Project ID or project name`
* `:rtype: :class:<WorkItemField> <azure.devops.v5_1.work_item_tracking.models.WorkItemField>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().create_field(work_item_field,project)`


### CreateOrUpdateClassificationNode
#### Description:
Create new or update an existing classification node.

* `:param :class:<WorkItemClassificationNode> <azure.devops.v5_1.work_item_tracking.models.WorkItemClassificationNode> posted_node: Node to create or update.`
* `:param str project: Project ID or project name`
* `:param TreeStructureGroup structure_group: Structure group of the classification node, area or iteration.`
* `:param str path: Path of the classification node.`
* `:rtype: :class:<WorkItemClassificationNode> <azure.devops.v5_1.work_item_tracking.models.WorkItemClassificationNode>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().create_or_update_classification_node(posted_node,project,structure_group,path)`


### CreateQuery
#### Description:
Creates a query, or moves a query.

* `:param :class:<QueryHierarchyItem> <azure.devops.v5_1.work_item_tracking.models.QueryHierarchyItem> posted_query: The query to create.`
* `:param str project: Project ID or project name`
* `:param str query: The parent id or path under which the query is to be created.`
* `:param bool validate_wiql_only: If you only want to validate your WIQL query without actually creating one, set it to true. Default is false.`
* `:rtype: :class:<QueryHierarchyItem> <azure.devops.v5_1.work_item_tracking.models.QueryHierarchyItem>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().create_query(posted_query,project,query,validate_wiql_only)`


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
* `:rtype: :class:<WorkItem> <azure.devops.v5_1.work_item_tracking.models.WorkItem>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().create_work_item(document,project,type,validate_only,bypass_rules,suppress_notifications,expand)`


### DeleteClassificationNode
#### Description:
Delete an existing classification node.

* `:param str project: Project ID or project name`
* `:param TreeStructureGroup structure_group: Structure group of the classification node, area or iteration.`
* `:param str path: Path of the classification node.`
* `:param int reclassify_id: Id of the target classification node for reclassification.`
#### Example usage:
`connection.clients.get_work_item_tracking_client().delete_classification_node(project,structure_group,path,reclassify_id)`


### DeleteField
#### Description:
Deletes the field.

* `:param str field_name_or_ref_name: Field simple name or reference name`
* `:param str project: Project ID or project name`
#### Example usage:
`connection.clients.get_work_item_tracking_client().delete_field(field_name_or_ref_name,project)`


### DeleteQuery
#### Description:
Delete a query or a folder. This deletes any permission change on the deleted query or folder and any of its descendants if it is a folder. It is important to note that the deleted permission changes cannot be recovered upon undeleting the query or folder.

* `:param str project: Project ID or project name`
* `:param str query: ID or path of the query or folder to delete.`
#### Example usage:
`connection.clients.get_work_item_tracking_client().delete_query(project,query)`


### DeleteWorkItem
#### Description:
Deletes the specified work item and sends it to the Recycle Bin, so that it can be restored back, if required. Optionally, if the destroy parameter has been set to true, it destroys the work item permanently. WARNING: If the destroy parameter is set to true, work items deleted by this command will NOT go to recycle-bin and there is no way to restore/recover them after deletion. It is recommended NOT to use this parameter. If you do, please use this parameter with extreme caution.

* `:param int id: ID of the work item to be deleted`
* `:param str project: Project ID or project name`
* `:param bool destroy: Optional parameter, if set to true, the work item is deleted permanently. Please note: the destroy action is PERMANENT and cannot be undone.`
* `:rtype: :class:<WorkItemDelete> <azure.devops.v5_1.work_item_tracking.models.WorkItemDelete>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().delete_work_item(id,project,destroy)`


### DestroyWorkItem
#### Description:
Destroys the specified work item permanently from the Recycle Bin. This action can not be undone.

* `:param int id: ID of the work item to be destroyed permanently`
* `:param str project: Project ID or project name`
#### Example usage:
`connection.clients.get_work_item_tracking_client().destroy_work_item(id,project)`


### GetAttachmentContent
#### Description:
Downloads an attachment.

* `:param str id: Attachment ID`
* `:param str project: Project ID or project name`
* `:param str file_name: Name of the file`
* `:param bool download: If set to <c>true</c> always download attachment`
* `:rtype: object`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_attachment_content(id,project,file_name,download)`


### GetAttachmentZip
#### Description:
Downloads an attachment.

* `:param str id: Attachment ID`
* `:param str project: Project ID or project name`
* `:param str file_name: Name of the file`
* `:param bool download: If set to <c>true</c> always download attachment`
* `:rtype: object`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_attachment_zip(id,project,file_name,download)`


### GetClassificationNode
#### Description:
Gets the classification node for a given node path.

* `:param str project: Project ID or project name`
* `:param TreeStructureGroup structure_group: Structure group of the classification node, area or iteration.`
* `:param str path: Path of the classification node.`
* `:param int depth: Depth of children to fetch.`
* `:rtype: :class:<WorkItemClassificationNode> <azure.devops.v5_1.work_item_tracking.models.WorkItemClassificationNode>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_classification_node(project,structure_group,path,depth)`


### GetClassificationNodes
#### Description:
Gets root classification nodes or list of classification nodes for a given list of nodes ids, for a given project. In case ids parameter is supplied you will  get list of classification nodes for those ids. Otherwise you will get root classification nodes for this project.

* `:param str project: Project ID or project name`
* `:param [int] ids: Comma separated integer classification nodes ids. It's not required, if you want root nodes.`
* `:param int depth: Depth of children to fetch.`
* `:param str error_policy: Flag to handle errors in getting some nodes. Possible options are Fail and Omit.`
* `:rtype: [WorkItemClassificationNode]`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_classification_nodes(project,ids,depth,error_policy)`


### GetDeletedWorkItem
#### Description:
Gets a deleted work item from Recycle Bin.

* `:param int id: ID of the work item to be returned`
* `:param str project: Project ID or project name`
* `:rtype: :class:<WorkItemDelete> <azure.devops.v5_1.work_item_tracking.models.WorkItemDelete>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_deleted_work_item(id,project)`


### GetDeletedWorkItemShallowReferences
#### Description:
Gets a list of the IDs and the URLs of the deleted the work items in the Recycle Bin.

* `:param str project: Project ID or project name`
* `:rtype: [WorkItemDeleteShallowReference]`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_deleted_work_item_shallow_references(project)`


### GetDeletedWorkItems
#### Description:
Gets the work items from the recycle bin, whose IDs have been specified in the parameters

* `:param [int] ids: Comma separated list of IDs of the deleted work items to be returned`
* `:param str project: Project ID or project name`
* `:rtype: [WorkItemDeleteReference]`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_deleted_work_items(ids,project)`


### GetField
#### Description:
Gets information on a specific field.

* `:param str field_name_or_ref_name: Field simple name or reference name`
* `:param str project: Project ID or project name`
* `:rtype: :class:<WorkItemField> <azure.devops.v5_1.work_item_tracking.models.WorkItemField>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_field(field_name_or_ref_name,project)`


### GetFields
#### Description:
Returns information for all fields.

* `:param str project: Project ID or project name`
* `:param str expand: Use ExtensionFields to include extension fields, otherwise exclude them. Unless the feature flag for this parameter is enabled, extension fields are always included.`
* `:rtype: [WorkItemField]`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_fields(project,expand)`


### GetQueries
#### Description:
Gets the root queries and their children

* `:param str project: Project ID or project name`
* `:param str expand: Include the query string (wiql), clauses, query result columns, and sort options in the results.`
* `:param int depth: In the folder of queries, return child queries and folders to this depth.`
* `:param bool include_deleted: Include deleted queries and folders`
* `:rtype: [QueryHierarchyItem]`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_queries(project,expand,depth,include_deleted)`


### GetQueriesBatch
#### Description:
Gets a list of queries by ids (Maximum 1000)

* `:param :class:<QueryBatchGetRequest> <azure.devops.v5_1.work_item_tracking.models.QueryBatchGetRequest> query_get_request:`
* `:param str project: Project ID or project name`
* `:rtype: [QueryHierarchyItem]`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_queries_batch(query_get_request,project)`


### GetQuery
#### Description:
Retrieves an individual query and its children

* `:param str project: Project ID or project name`
* `:param str query: ID or path of the query.`
* `:param str expand: Include the query string (wiql), clauses, query result columns, and sort options in the results.`
* `:param int depth: In the folder of queries, return child queries and folders to this depth.`
* `:param bool include_deleted: Include deleted queries and folders`
* `:rtype: :class:<QueryHierarchyItem> <azure.devops.v5_1.work_item_tracking.models.QueryHierarchyItem>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_query(project,query,expand,depth,include_deleted)`


### GetQueryResultCount
#### Description:
Gets the results of the query given the query ID.

* `:param str id: The query ID.`
* `:param :class:<TeamContext> <azure.devops.v5_1.work_item_tracking.models.TeamContext> team_context: The team context for the operation`
* `:param bool time_precision: Whether or not to use time precision.`
* `:param int top: The max number of results to return.`
* `:rtype: int`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_query_result_count(id,team_context,time_precision,top)`


### GetRelationType
#### Description:
Gets the work item relation type definition.

* `:param str relation: The relation name`
* `:rtype: :class:<WorkItemRelationType> <azure.devops.v5_1.work_item_tracking.models.WorkItemRelationType>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_relation_type(relation)`


### GetRelationTypes
#### Description:
Gets the work item relation types.

* `:rtype: [WorkItemRelationType]`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_relation_types()`


### GetReportingLinksByLinkType
#### Description:
Get a batch of work item links

* `:param str project: Project ID or project name`
* `:param [str] link_types: A list of types to filter the results to specific link types. Omit this parameter to get work item links of all link types.`
* `:param [str] types: A list of types to filter the results to specific work item types. Omit this parameter to get work item links of all work item types.`
* `:param str continuation_token: Specifies the continuationToken to start the batch from. Omit this parameter to get the first batch of links.`
* `:param datetime start_date_time: Date/time to use as a starting point for link changes. Only link changes that occurred after that date/time will be returned. Cannot be used in conjunction with 'watermark' parameter.`
* `:rtype: :class:<ReportingWorkItemLinksBatch> <azure.devops.v5_1.work_item_tracking.models.ReportingWorkItemLinksBatch>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_reporting_links_by_link_type(project,link_types,types,continuation_token,start_date_time)`


### GetRevision
#### Description:
Returns a fully hydrated work item for the requested revision

* `:param int id:`
* `:param int revision_number:`
* `:param str project: Project ID or project name`
* `:param str expand:`
* `:rtype: :class:<WorkItem> <azure.devops.v5_1.work_item_tracking.models.WorkItem>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_revision(id,revision_number,project,expand)`


### GetRevisions
#### Description:
Returns the list of fully hydrated work item revisions, paged.

* `:param int id:`
* `:param str project: Project ID or project name`
* `:param int top:`
* `:param int skip:`
* `:param str expand:`
* `:rtype: [WorkItem]`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_revisions(id,project,top,skip,expand)`


### GetRootNodes
#### Description:
Gets root classification nodes under the project.

* `:param str project: Project ID or project name`
* `:param int depth: Depth of children to fetch.`
* `:rtype: [WorkItemClassificationNode]`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_root_nodes(project,depth)`


### GetUpdate
#### Description:
Returns a single update for a work item

* `:param int id:`
* `:param int update_number:`
* `:param str project: Project ID or project name`
* `:rtype: :class:<WorkItemUpdate> <azure.devops.v5_1.work_item_tracking.models.WorkItemUpdate>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_update(id,update_number,project)`


### GetUpdates
#### Description:
Returns a the deltas between work item revisions

* `:param int id:`
* `:param str project: Project ID or project name`
* `:param int top:`
* `:param int skip:`
* `:rtype: [WorkItemUpdate]`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_updates(id,project,top,skip)`


### GetWorkItem
#### Description:
Returns a single work item.

* `:param int id: The work item id`
* `:param str project: Project ID or project name`
* `:param [str] fields: Comma-separated list of requested fields`
* `:param datetime as_of: AsOf UTC date time string`
* `:param str expand: The expand parameters for work item attributes. Possible options are { None, Relations, Fields, Links, All }.`
* `:rtype: :class:<WorkItem> <azure.devops.v5_1.work_item_tracking.models.WorkItem>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_work_item(id,project,fields,as_of,expand)`


### GetWorkItemIconJson
#### Description:
Get a work item icon given the friendly name and icon color.

* `:param str icon: The name of the icon`
* `:param str color: The 6-digit hex color for the icon`
* `:param int v: The version of the icon (used only for cache invalidation)`
* `:rtype: :class:<WorkItemIcon> <azure.devops.v5_1.work_item_tracking.models.WorkItemIcon>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_work_item_icon_json(icon,color,v)`


### GetWorkItemIconSvg
#### Description:
Get a work item icon given the friendly name and icon color.

* `:param str icon: The name of the icon`
* `:param str color: The 6-digit hex color for the icon`
* `:param int v: The version of the icon (used only for cache invalidation)`
* `:rtype: object`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_work_item_icon_svg(icon,color,v)`


### GetWorkItemIconXaml
#### Description:
Get a work item icon given the friendly name and icon color.

* `:param str icon: The name of the icon`
* `:param str color: The 6-digit hex color for the icon`
* `:param int v: The version of the icon (used only for cache invalidation)`
* `:rtype: object`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_work_item_icon_xaml(icon,color,v)`


### GetWorkItemIcons
#### Description:
Get a list of all work item icons.

* `:rtype: [WorkItemIcon]`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_work_item_icons()`


### GetWorkItemTemplate
#### Description:
Returns a single work item from a template.

* `:param str project: Project ID or project name`
* `:param str type: The work item type name`
* `:param str fields: Comma-separated list of requested fields`
* `:param datetime as_of: AsOf UTC date time string`
* `:param str expand: The expand parameters for work item attributes. Possible options are { None, Relations, Fields, Links, All }.`
* `:rtype: :class:<WorkItem> <azure.devops.v5_1.work_item_tracking.models.WorkItem>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_work_item_template(project,type,fields,as_of,expand)`


### GetWorkItemType
#### Description:
Returns a work item type definition.

* `:param str project: Project ID or project name`
* `:param str type: Work item type name`
* `:rtype: :class:<WorkItemType> <azure.devops.v5_1.work_item_tracking.models.WorkItemType>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_work_item_type(project,type)`


### GetWorkItemTypeCategories
#### Description:
Get all work item type categories.

* `:param str project: Project ID or project name`
* `:rtype: [WorkItemTypeCategory]`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_work_item_type_categories(project)`


### GetWorkItemTypeCategory
#### Description:
Get specific work item type category by name.

* `:param str project: Project ID or project name`
* `:param str category: The category name`
* `:rtype: :class:<WorkItemTypeCategory> <azure.devops.v5_1.work_item_tracking.models.WorkItemTypeCategory>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_work_item_type_category(project,category)`


### GetWorkItemTypeFieldWithReferences
#### Description:
Get a field for a work item type with detailed references.

* `:param str project: Project ID or project name`
* `:param str type: Work item type.`
* `:param str field:`
* `:param str expand: Expand level for the API response. Properties: to include allowedvalues, default value, isRequired etc. as a part of response; None: to skip these properties.`
* `:rtype: :class:<WorkItemTypeFieldWithReferences> <azure.devops.v5_1.work_item_tracking.models.WorkItemTypeFieldWithReferences>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_work_item_type_field_with_references(project,type,field,expand)`


### GetWorkItemTypeFieldsWithReferences
#### Description:
Get a list of fields for a work item type with detailed references.

* `:param str project: Project ID or project name`
* `:param str type: Work item type.`
* `:param str expand: Expand level for the API response. Properties: to include allowedvalues, default value, isRequired etc. as a part of response; None: to skip these properties.`
* `:rtype: [WorkItemTypeFieldWithReferences]`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_work_item_type_fields_with_references(project,type,expand)`


### GetWorkItemTypes
#### Description:
Returns the list of work item types

* `:param str project: Project ID or project name`
* `:rtype: [WorkItemType]`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_work_item_types(project)`


### GetWorkItems
#### Description:
Returns a list of work items (Maximum 200)

* `:param [int] ids: The comma-separated list of requested work item ids. (Maximum 200 ids allowed).`
* `:param str project: Project ID or project name`
* `:param [str] fields: Comma-separated list of requested fields`
* `:param datetime as_of: AsOf UTC date time string`
* `:param str expand: The expand parameters for work item attributes. Possible options are { None, Relations, Fields, Links, All }.`
* `:param str error_policy: The flag to control error policy in a bulk get work items request. Possible options are {Fail, Omit}.`
* `:rtype: [WorkItem]`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_work_items(ids,project,fields,as_of,expand,error_policy)`


### GetWorkItemsBatch
#### Description:
Gets work items for a list of work item ids (Maximum 200)

* `:param :class:<WorkItemBatchGetRequest> <azure.devops.v5_1.work_item_tracking.models.WorkItemBatchGetRequest> work_item_get_request:`
* `:param str project: Project ID or project name`
* `:rtype: [WorkItem]`
#### Example usage:
`connection.clients.get_work_item_tracking_client().get_work_items_batch(work_item_get_request,project)`


### QueryById
#### Description:
Gets the results of the query given the query ID.

* `:param str id: The query ID.`
* `:param :class:<TeamContext> <azure.devops.v5_1.work_item_tracking.models.TeamContext> team_context: The team context for the operation`
* `:param bool time_precision: Whether or not to use time precision.`
* `:param int top: The max number of results to return.`
* `:rtype: :class:<WorkItemQueryResult> <azure.devops.v5_1.work_item_tracking.models.WorkItemQueryResult>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().query_by_id(id,team_context,time_precision,top)`


### QueryByWiql
#### Description:
Gets the results of the query given its WIQL.

* `:param :class:<Wiql> <azure.devops.v5_1.work_item_tracking.models.Wiql> wiql: The query containing the WIQL.`
* `:param :class:<TeamContext> <azure.devops.v5_1.work_item_tracking.models.TeamContext> team_context: The team context for the operation`
* `:param bool time_precision: Whether or not to use time precision.`
* `:param int top: The max number of results to return.`
* `:rtype: :class:<WorkItemQueryResult> <azure.devops.v5_1.work_item_tracking.models.WorkItemQueryResult>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().query_by_wiql(wiql,team_context,time_precision,top)`


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
* `:rtype: :class:<ReportingWorkItemRevisionsBatch> <azure.devops.v5_1.work_item_tracking.models.ReportingWorkItemRevisionsBatch>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().read_reporting_revisions_get(project,fields,types,continuation_token,start_date_time,include_identity_ref,include_deleted,include_tag_ref,include_latest_only,expand,include_discussion_changes_only,max_page_size)`


### ReadReportingRevisionsPost
#### Description:
Get a batch of work item revisions. This request may be used if your list of fields is large enough that it may run the URL over the length limit.

* `:param :class:<ReportingWorkItemRevisionsFilter> <azure.devops.v5_1.work_item_tracking.models.ReportingWorkItemRevisionsFilter> filter: An object that contains request settings: field filter, type filter, identity format`
* `:param str project: Project ID or project name`
* `:param str continuation_token: Specifies the watermark to start the batch from. Omit this parameter to get the first batch of revisions.`
* `:param datetime start_date_time: Date/time to use as a starting point for revisions, all revisions will occur after this date/time. Cannot be used in conjunction with 'watermark' parameter.`
* `:param str expand:`
* `:rtype: :class:<ReportingWorkItemRevisionsBatch> <azure.devops.v5_1.work_item_tracking.models.ReportingWorkItemRevisionsBatch>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().read_reporting_revisions_post(filter,project,continuation_token,start_date_time,expand)`


### RestoreWorkItem
#### Description:
Restores the deleted work item from Recycle Bin.

* `:param :class:<WorkItemDeleteUpdate> <azure.devops.v5_1.work_item_tracking.models.WorkItemDeleteUpdate> payload: Paylod with instructions to update the IsDeleted flag to false`
* `:param int id: ID of the work item to be restored`
* `:param str project: Project ID or project name`
* `:rtype: :class:<WorkItemDelete> <azure.devops.v5_1.work_item_tracking.models.WorkItemDelete>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().restore_work_item(payload,id,project)`


### SearchQueries
#### Description:
Searches all queries the user has access to in the current project

* `:param str project: Project ID or project name`
* `:param str filter: The text to filter the queries with.`
* `:param int top: The number of queries to return (Default is 50 and maximum is 200).`
* `:param str expand:`
* `:param bool include_deleted: Include deleted queries and folders`
* `:rtype: :class:<QueryHierarchyItemsResult> <azure.devops.v5_1.work_item_tracking.models.QueryHierarchyItemsResult>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().search_queries(project,filter,top,expand,include_deleted)`


### UpdateClassificationNode
#### Description:
Update an existing classification node.

* `:param :class:<WorkItemClassificationNode> <azure.devops.v5_1.work_item_tracking.models.WorkItemClassificationNode> posted_node: Node to create or update.`
* `:param str project: Project ID or project name`
* `:param TreeStructureGroup structure_group: Structure group of the classification node, area or iteration.`
* `:param str path: Path of the classification node.`
* `:rtype: :class:<WorkItemClassificationNode> <azure.devops.v5_1.work_item_tracking.models.WorkItemClassificationNode>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().update_classification_node(posted_node,project,structure_group,path)`


### UpdateQuery
#### Description:
Update a query or a folder. This allows you to update, rename and move queries and folders.

* `:param :class:<QueryHierarchyItem> <azure.devops.v5_1.work_item_tracking.models.QueryHierarchyItem> query_update: The query to update.`
* `:param str project: Project ID or project name`
* `:param str query: The ID or path for the query to update.`
* `:param bool undelete_descendants: Undelete the children of this folder. It is important to note that this will not bring back the permission changes that were previously applied to the descendants.`
* `:rtype: :class:<QueryHierarchyItem> <azure.devops.v5_1.work_item_tracking.models.QueryHierarchyItem>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().update_query(query_update,project,query,undelete_descendants)`


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
* `:rtype: :class:<WorkItem> <azure.devops.v5_1.work_item_tracking.models.WorkItem>`
#### Example usage:
`connection.clients.get_work_item_tracking_client().update_work_item(document,id,project,validate_only,bypass_rules,suppress_notifications,expand)