---
title: API Reference

language_tabs: # must be one of https://git.io/vQNgJ
  - shell
#   - python

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

Welcome to the Sieve API! You can use our API to access Sieve API endpoints, which can help you submit visual data to Sieve and then query that data by many visual attributes that are relevant to your data.

Our API is currently in Beta, so please [reach out to us](https://sievedata.com/) if you're interested in the API and getting onboarded. We're trying to handle as many customers as possible right now.

> API Endpoint

<!-- ```python
https://api.sievedata.com/v1/
``` -->

```shell
https://api.sievedata.com/v1/
```
# Authentication

> To authorize, use this code:

<!-- ```python
from sieve.client import SieveClient

client = SieveClient(api_key="YOUR_API_KEY")
``` -->

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

<!-- ```python
from sieve.client import SieveClient

client = SieveClient(api_key="YOUR_API_KEY")
client.init_project(project_name="amazing_project_1")
``` -->

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
A project name needs to be specified on every API request having to do with project data.
</aside>

## Get All Projects

<!-- ```python
from sieve.client import SieveClient

client = SieveClient(api_key="YOUR_API_KEY")
print(client.get_all_projects()) # this prints project names in a list
``` -->

```shell
curl https://api.sievedata.com/v1/get_projects \
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

<!-- ```python
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
``` -->

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
    "description": "Pushed tags"
}
```

This endpoint allows you to specify which types of metadata you want tagged in this project. Typically, you'll work with the Sieve team so they can decide which of their internal models will work best for your use-case.

### HTTP Request

`POST https://api.sievedata.com/v1/add_tags`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```tags``` | list | list of tags and their descriptions

## Delete Metadata Tags

<!-- ```python
from sieve.client import SieveClient

client = SieveClient('YOUR_API_KEY')
my_proj = client.get_project("amazing_project_1")

my_proj.delete_tags(
    tags=["glare", "weather"]
)
``` -->

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

`POST https://api.sievedata.com/v1/delete_tags`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```tags``` | dict | list of tag names to delete

# Submitting Data

## Push Video Data

<!-- ```python
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

# send video for Sieve to tag
test_url1 = 'https://example.com/video/video.mp4'
project.push_data([test_url, test_url1])
``` -->

```shell
curl https://api.sievedata.com/v1/push_video \
    -X POST \
    -H "X-API-Key: YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
        "project_name": amazing_project_1,
        "video_url": "https://storage.googleapis.com/sieve-data-video-test-bucket/PRG1.avi"
    }'
```

> A sample response would look as follows:

```json
{
    "description": "Published video to batching",
    "job_id":"add3978a-94ac-4585-ab52-8bc5c2295c6f"
}
```

This endpoint allows you to submit video data to Sieve. Every video you submit to Sieve either needs to have a URL that is signed (secure) or public. Learn more about signed URLs for [AWS](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-signed-urls.html) or [GCP](https://cloud.google.com/storage/docs/access-control/signed-urls) at the respective links. Sieve processes cuts videos into their individual frames and uses a set of filters to process them efficiently.

### HTTP Request

`POST https://api.sievedata.com/v1/push_video`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```video_url``` | string | valid URL to video

# Querying and Exporting Data

## Query by Metadata

<!-- ```python
from sieve.client import SieveClient

client = SieveClient('YOUR_API_KEY')
my_proj = client.get_project("amazing_project_1")

my_proj.get_by_metadata(
    {
        "glare": [2],
        "weather": ["rainy", "other"]
    }
)
``` -->

```shell
curl 'https://api.sievedata.com/v1/get_metadata?project_name=demo_project&blur=slightly_blurry&lighting=dim&person_detected=True&noise=clear' \
    -X GET \
    -H "X-API-Key: YOUR_API_KEY"
```

> A sample response would look as follows (truncated):

```json
[
    {
        "project_name":"demo_project",
        "aspect_ratio":"22:15",
        "blur":"slightly_blurry",
        "contrast":"normal",
        "frame_number":21260,
        "group_id":"267fb3eb-90e2-400a-a8db-7b48e48583e5",
        "image_height":480,
        "image_width":704,
        "lighting":"dim",
        "motion_detected":true,
        "noise":"clear",
        "person_detected":true,
        "sharpness":"not_sharp",
        "train":false,
        "storage_path":"gs://sieve-data-frames-api_test_org/PRG1/PRG1-21260.jpg",
        "video_url":"https://storage.googleapis.com/sieve-data-video-test-bucket/PRG1.avi",
        "signed_url":"PLACEHOLDER_SIGNED_URL",
        "video_name":"PRG1"
    },
    thousands of more samples...
]
```

This endpoint is for retreiving a set of frames / images based on their defining metadata. Each tag can be specified as a part of the URL along with the matching output class. You'll be returned a list of matching samples along with all their metadata. Keep in mind that, the response to this call is truncated due to large
payload sizes so if you're interested in exporting an entire query, you should use then next listed API call.

### HTTP Request

`POST https://api.sievedata.com/v1/get_metadata`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```tags``` | list | a list passed in as URL parameters


## Export Query by Metadata

<!-- ```python
from sieve.client import SieveClient

client = SieveClient('YOUR_API_KEY')
my_proj = client.get_project("amazing_project_1")

my_proj.get_by_metadata(
    {
        "glare": [2],
        "weather": ["rainy", "other"]
    }
)
``` -->

```shell
curl 'https://api.sievedata.com/v1/export_metadata?export_name=some_name&project_name=demo_project&blur=slightly_blurry&lighting=dim&person_detected=True&noise=clear' \
    -X GET \
    -H "X-API-Key: YOUR_API_KEY"
```

> A sample response would look as follows (truncated):

```json
{
    "description":"queued for tarring",
    "metadata_json_url": "PLACEHOLDER_JSON_URL",
    "num_samples": 49210
}
```

This endpoint is for retreiving and exporting a set of frames / images based on their defining metadata. Each tag can be specified as a part of the URL along with the matching output class. You'll be returned a list of matching samples along with all their metadata. You'll be returned a signed URL to a JSON containing a non-truncated version of the metadata for the query. You can either choose to process this yourself or wait for Sieve to automatically process and compress the raw data for you in the backend for a faster download. Use the `get_exports_status` to get information about all your exports, including status, and links to download.

### HTTP Request

`POST https://api.sievedata.com/v1/export_metadata`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```export_name``` | string | the name of the export
```tags``` | list | a list passed in as URL parameters

## Get Exports

<!-- ```python
from sieve.client import SieveClient

client = SieveClient('YOUR_API_KEY')
my_proj = client.get_project("amazing_project_1")

my_proj.get_by_metadata(
    {
        "glare": [2],
        "weather": ["rainy", "other"]
    }
)
``` -->

```shell
curl 'https://api.sievedata.com/v1/get_exports_status?project_name=CamNet' \
    -X GET \
    -H "X-API-Key: YOUR_API_KEY"
```

> A sample response would look as follows (truncated):

```json
{
    "description":"Successful",
    "exports":[
        {
            "name": "people_with_greenery",
            "json_path":"SIGNED_URL_TO_METADATA_JSON",
            "status": "failed",
            "time_created": "12/07/2021, 03:57:59"
        },
        {
            "name":"dim_lighting_and_people",
            "json_path":"SIGNED_URL_TO_METADATA_JSON",
            "status":"complete",
            "tar_path":"SIGNED_URL_TO_ZIPPED_IMAGES",
            "time_created":"12/07/2021, 01:13:17"
        }
    ]
}
```

This endpoint is for retreiving information you can use to download your exported query data.

Use `curl sample_tar_path | tar -xz` to download and uncompress your query raw data.

Use `curl sample_metadata_json_path --output sieve-metadata.json` to download the metadata json.

### HTTP Request

`POST https://api.sievedata.com/v1/export_metadata`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project