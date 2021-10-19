---
title: API Reference

language_tabs: # must be one of https://git.io/vQNgJ
  - shell
  - python

toc_footers:
  - <a href='#'>Sign Up for a Developer Key</a>
  - <a href='https://github.com/slatedocs/slate'>Documentation Powered by Slate</a>

includes:
  - errors

search: true

code_clipboard: true

meta:
  - name: description
    content: Documentation for the Kittn API
---

# Introduction

Welcome to the Sieve API! You can use our API to access Sieve API endpoints, which can help you submit images to Sieve to get tagged and later query by ids, timestamps, or subsets.

Our API is currently in Beta, so please reach out to us if you're interested in the API and getting onboarded. We're trying to handle as many customers as possible right now.

> API Endpoint

```python
https://api.sievedata.com/v1/
```

```shell
https://api.sievedata.com/v1/
```
# Authentication

> To authorize, use this code:

```python
import sieve

client = sieve.client.Client('YOUR_API_KEY')
```

```shell
# With shell, you can just pass the correct header with each request
curl "api_endpoint_here" \
  -H "X-API-Key: YOUR_API_KEY"
```

> Make sure to replace `YOUR_API_KEY` with your API key.

Sieve uses API keys to allow access to the API. You can access / manage your API keys via your Sieve dasbhoard after you get access.

Sieve expects for the API key to be included in all API requests to the server in a header that looks like the following:

`X-API-Key: YOUR_API_KEY`

# Projects

## Initialize a New Project

```python
from sieve.client import Client

client = Client('YOUR_API_KEY')
client.init_project(project_name = "amazing_sieve_project")
```

```shell
curl "https://api.sievedata.com/v1/init_project" \
  -H "X-API-Key: YOUR_API_KEY" \
  -D "name: amazing_sieve_project"
```

This endpoint creates a new Sieve project. A new project might be per general problem, per dataset, or however else you want to divide projects. Functionally, all querying will happen within a specific project.

### HTTP Request

`POST https://api.sievedata.com/v1/init_project`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project

<aside class="notice">
A project name is used to access images and tags for that project
</aside>

## Get All Projects

```python
from sieve.client import Client

client = Client('YOUR_API_KEY')
print(client.get_projects())
```

```shell
curl "https://api.sievedata.com/v1/get_projects" \
  -H "X-API-Key: YOUR_API_KEY"
```

> The above command returns JSON structured like this:

```json
{
  "id": "placeholder"
}
```

This endpoint retrieves the names of all projects you've created within your organization.

### HTTP Request

`GET https://api.sievedata.com/v1/get_projects`

## Add Metadata Tags

```python
from sieve.client import Client

client = Client('YOUR_API_KEY')
client.add_tags(
    project_name = "amazing_sieve_project",
    tags = [
        "glare": "1-5 scale of how glary the image is",
        "weather": "is the image foggy, sunny, rainy, or none?"
        "angle": "1 (floor) - 5 (ceiling) classification of how the camera is angled"
    ]
)
```

```shell
PLACEHOLDER
```

This endpoint allows you to specify which types of metadata you want tagged in this project and precisely define them.

### HTTP Request

`POST https://api.sievedata.com/v1/add_tags`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```tags``` | list | list of tags and their descriptions

# Submitting Data and Searching

## Create Training / Tagging Job

```python
PLACEHOLDER
```

```shell
PLACEHOLDER
```

This endpoint is for submitting data to Sieve. You might do this for one of two purposes. Either you're submitting data to us so we can train our models and deploy them to then be able to tag your data or you're submitting the data to actually get it tagged.

### HTTP Request

`POST https://api.sievedata.com/v1/push_data`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```urls``` | list | list of input urls (images) you want to submit
```type``` | string | either ```train``` or ```query``` depending on whether the data is for Sieve's team to use to build models or if it's data you want to submit to get tags back. By default, this is ```query```.

## Query by Job ID

```python
PLACEHOLDER
```

```shell
PLACEHOLDER
```

This endpoint is for retreiving a batch of images image and their metadata by the ```job_id```. The ```job_id``` is something that was returned to you when you initially submitted data which is unique to the batch you submitted during that one request.

### HTTP Request

`POST https://api.sievedata.com/v1/get_metadata_from_job_id`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```job_id``` | string | the job id

## Query by Image ID

```python
PLACEHOLDER
```

```shell
PLACEHOLDER
```

This endpoint is for retreiving an image and its metadata by the ```image_id```. The ```image_id``` is something that was returned to you when you initially submitted data which is unique to each image you submitted.

### HTTP Request

`POST https://api.sievedata.com/v1/get_metadata_from_image_ids`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```image_ids``` | list | a list of image ids

## Query by Metadata

```python
PLACEHOLDER
```

```shell
PLACEHOLDER
```

This endpoint is for retreiving a set of images and their metadata, matching the query parameters.

### HTTP Request

`POST https://api.sievedata.com/v1/get_metadata_subset`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```tags``` | dict | a dictionary of form ```query_dict```
