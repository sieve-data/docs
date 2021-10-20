---
title: API Reference

language_tabs: # must be one of https://git.io/vQNgJ
  - shell
  - python

toc_footers:
  - <a target='_blank' href='https://sievedata.com/'>Sign Up for a Sieve Account</a>

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

Our API is currently in Beta, so please [reach out to us](https://sievedata.com/) if you're interested in the API and getting onboarded. We're trying to handle as many customers as possible right now.

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
from sieve.client import SieveClient

client = SieveClient(api_key="YOUR_API_KEY")
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
from sieve.client import SieveClient

client = SieveClient(api_key="YOUR_API_KEY")
client.init_project(project_name="amazing_project_1")
```

```shell
curl https://api.sievedata.com/v1/init_project \
    -X POST \
    -H "X-API-Key: YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
        "project_name": "amazing_project_1"
    }'
```

> A sample response would look as follows:

```json
{
    "description": "Created project amazing_project_1",
    "project_id": "18ff75d5-8f7d-4c7b-b3ed-7c66615d9808"
}
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
from sieve.client import SieveClient

client = SieveClient(api_key="YOUR_API_KEY")
print(client.get_all_projects()) # this prints project names in a list
```

```shell
curl https://api.sievedata.com/v1/get_all_projects \
    -H "X-API-Key: YOUR_API_KEY"
```

> A sample response would look as follows:

```json
{
    "description": "successful",
    "projects": [
        "amazing_project_1",
        "amazing_project_2",
        "amazing_project_x"
    ]
}
```

This endpoint retrieves the names of all projects you've created within your organization.

### HTTP Request

`GET https://api.sievedata.com/v1/get_projects`

## Add Metadata Tags

```python
from sieve.client import SieveClient

client = SieveClient('YOUR_API_KEY')
my_proj = client.get_project("amazing_project_1")

my_proj.add_tags(
    tags = [
        {"name": "glare", "description": "1-5 scale of how glary the image is"},
        {"name": "weather", "description": "is the image foggy, sunny, rainy, or none?"},
        {"name": "angle", "description": "1 (floor) - 5 (ceiling) classification of how the camera is angled"}
    ]
)
```

```shell
curl https://api.sievedata.com/v1/add_tags \
    -X POST \
    -H "X-API-Key: YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
        "project_name": "amazing_project_1",
        "tags": [
            {"name": "glare", "description": "1-5 scale of how glary the image is"},
            {"name": "weather", "description": "is the image foggy, sunny, rainy, or none?"},
            {"name": "angle", "description": "1 (floor) - 5 (ceiling) classification of how the camera is angled"}
        ]
    }'
```

> A sample response would look as follows:

```json
{
    "description": "pushed tags"
}
```

This endpoint allows you to specify which types of metadata you want tagged in this project.

### HTTP Request

`POST https://api.sievedata.com/v1/add_tags`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```tags``` | list | list of tags and their descriptions

## Delete Metadata Tags

```python
from sieve.client import SieveClient

client = SieveClient('YOUR_API_KEY')
my_proj = client.get_project("amazing_project_1")

my_proj.delete_tags(
    tags=["glare", "weather"]
)
```

```shell
curl https://api.sievedata.com/v1/delete_tags \
    -X POST \
    -H "X-API-Key: YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
        "project_name": "amazing_project_1",
        "tags": ["glare", "weather"]
    }'
```

> A sample response would look as follows:

```json
{
    "description": "successful",
    "tags": [
        {"name": "glare", "description": "1-5 scale of how glary the image is"},
        {"name": "weather", "description": "is the image foggy, sunny, rainy, or none?"}
    ]
}
```

This endpoint allows you to specify which metadata tags you want to delete from the project.

### HTTP Request

`POST https://api.sievedata.com/v1/add_tags`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```tags``` | dict | list of tag names to delete

## Get Metadata Tag Status

```python
from sieve.client import SieveClient

client = SieveClient('YOUR_API_KEY')
my_proj = client.get_project("amazing_project_1")

print(project.get_tag_status() # prints status of all tags in the project
```

```shell
curl https://api.sievedata.com/v1/get_tag_status \
    -X POST \
    -H "X-API-Key: YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
        "project_name": "amazing_project_1"
    }'

```

> A sample response would look as follows:

```json
{
    "description": "successful",
    "tag_status": [
        {"name": "glare", "status": "live"},
        {"name": "weather", "status": "training"},
        {"name": "angle", "status": "queued"}
    ]
}
```

This endpoint allows you to get the status of the tagging models for each type of metadata tag added to the project.

### HTTP Request

`POST https://api.sievedata.com/v1/add_tags`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```tags``` | dict | list of tag names to delete

# Submitting Data

## Create Training / Tagging Job

```python
from sieve.client import SieveClient

client = SieveClient('YOUR_API_KEY')
my_proj = client.get_project("amazing_project_1")

# send data for Sieve to use in model fine-tuning / training
my_image_urls = open('my_urls.txt', 'r')
project.push_data(urls, train=True)

# send data for Sieve to tag
test_url = 'https://cdn.cnn.com/cnnnext/dam/assets/200824175931-kobe-bryant-file-super-tease.jpg'
test_url1 = 'https://api.time.com/wp-content/uploads/2020/09/kobe-bryant-book-04.jpg'
project.push_data([test_url, test_url1])
```

```shell
curl https://api.sievedata.com/v1/push_data \
    -X POST \
    -H "X-API-Key: YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
        "project_name": amazing_project_1,
        "urls": [
            "https://example.com/image1.jpg",
            "https://example.com/image2.jpg"
        ],
        "train": true
    }'
```

> A sample response would look as follows:

```json
{
    "description": "successful",
    "image_ids": [
        "39a28821-aa81-4a69-9197-b519252a42c4",
        "e0ddbbdf-027c-4e3a-bd6d-4e9ba9fb35f1"
    ],
    "job_id": "42077167-c11a-404c-b538-a5d5f057365b"
}
```

This endpoint is for submitting data to Sieve. You might do this for one of two purposes. Either you're submitting data to us so we can train our models and deploy them to then be able to tag your data or you're submitting the data to actually get it tagged.

### HTTP Request

`POST https://api.sievedata.com/v1/push_data`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```urls``` | list | list of input urls (images) you want to submit
```train``` | bool | By default, this is set to false. Set to true if data is meant to be used by Sieve to train tagging models, false otherwise.

# Querying Data

## Query by Job ID

```python
from sieve.client import SieveClient

client = SieveClient('YOUR_API_KEY')
my_proj = client.get_project("amazing_project_1")

my_proj.get_metadata_by_job_id("42077167-c11a-404c-b538-a5d5f057365b")
```

```shell
curl https://api.sievedata.com/v1/get_metadata_by_job_id \
    -X POST \
    -H "X-API-Key: YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
        "project_name": "amazing_project_1",
        "job_id": "42077167-c11a-404c-b538-a5d5f057365b"
    }’
```

> A sample response would look as follows:

```json
{
    "description": "successful",
    "metadata": [
        {
            "image_id": "39a28821-aa81-4a69-9197-b519252a42c4",
            "job_id": "42077167-c11a-404c-b538-a5d5f057365b",
            "url": "https://cdn.cnn.com/cnnnext/dam/assets/200824175931-kobe-bryant-file-super-tease.jpg",
            "glare": "1",
            "angle": "3",
            "weather": "other"
        },
        {
            "image_id": "e0ddbbdf-027c-4e3a-bd6d-4e9ba9fb35f1",
            "job_id": "42077167-c11a-404c-b538-a5d5f057365b",
            "url": "https://api.time.com/wp-content/uploads/2020/09/kobe-bryant-book-04.jpg",
            "glare": "2",
            "angle": "3",
            "weather": "other"
        }
    ]
}
```

This endpoint is for retreiving a batch of images image and their metadata by the ```job_id```. The ```job_id``` is something that was returned to you when you initially submitted data which is unique to the batch you submitted during that one request.

### HTTP Request

`POST https://api.sievedata.com/v1/get_metadata_from_job_id`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```job_id``` | string | the job id

## Query by Image ID

```python
from sieve.client import SieveClient

client = SieveClient('YOUR_API_KEY')
my_proj = client.get_project("amazing_project_1")

project.get_metadata_by_image_ids(["39a28821-aa81-4a69-9197-b519252a42c4"])
```

```shell
curl https://api.sievedata.com/v1/get_metadata_by_image_ids \
    -X POST \
    -H "X-API-Key: YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
        "project_name": "amazing_project_1",
        "image_ids": ["39a28821-aa81-4a69-9197-b519252a42c4"]
    }’
```

> A sample response would look as follows:

```json
{
    "description": "successful",
    "metadata": [
        {
            "image_id": "39a28821-aa81-4a69-9197-b519252a42c4",
            "job_id": "42077167-c11a-404c-b538-a5d5f057365b",
            "url": "https://cdn.cnn.com/cnnnext/dam/assets/200824175931-kobe-bryant-file-super-tease.jpg",
            "glare": "1",
            "angle": "3",
            "weather": "other"
        }
    ]
}
```

This endpoint is for retreiving an image and its metadata by the ```image_id```. The ```image_id``` is something that was returned to you when you initially submitted data which is unique to each image you submitted.

### HTTP Request

`POST https://api.sievedata.com/v1/get_metadata_from_image_ids`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```image_ids``` | list | a list of image ids

## Query by Metadata

```python
from sieve.client import SieveClient

client = SieveClient('YOUR_API_KEY')
my_proj = client.get_project("amazing_project_1")

my_proj.get_by_metadata(
    {
        "glare": [2],
        "weather": ["rainy", "other"]
    }
)
```

```shell
curl https://api.sievedata.com/v1/get_metadata_by_subset \
    -X POST \
    -H "X-API-Key: YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
        "project_name": "amazing_project_1",
        "tags": {
            "glare": [2],
            "weather": ["rainy", "other"]
        }
    }
```

> A sample response would look as follows:

```json
{
    "description": "successful",
    "metadata": [
        {
            "image_id": "e0ddbbdf-027c-4e3a-bd6d-4e9ba9fb35f1",
            "job_id": "42077167-c11a-404c-b538-a5d5f057365b",
            "url": "https://api.time.com/wp-content/uploads/2020/09/kobe-bryant-book-04.jpg",
            "glare": "2",
            "angle": "3",
            "weather": "other"
        }
    ]
}
```

This endpoint is for retreiving a set of images and their metadata, matching the query parameters. Each tag can be specified in the query along with a list of possible outputs that would count as a valid match (treated as an OR).

### HTTP Request

`POST https://api.sievedata.com/v1/get_metadata_subset`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```tags``` | dict | a dictionary of form seen in the example
