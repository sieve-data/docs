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

## Get All Projects and User Info

<!-- ```python
from sieve.client import SieveClient

client = SieveClient(api_key="YOUR_API_KEY")
print(client.get_projects()) # this prints project names in a list
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
    ],
    "customer_info": {
        "API-Key": "YOUR_API_KEY",
        "can_set": True,
        "can_store": True,
        "name": "YOUR_NAME",
        "videos_left": NUM_VIDEOS_LEFT,
        "hours_left": NUM_HOURS_LEFT
    }
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

## Get Metadata Tags

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
curl 'https://api.sievedata.com/v1/get_tags?project_name=amazing_project_1' \
    -X GET \
    -H "X-API-Key: YOUR_API_KEY" \
    -H "Content-Type: application/json"
```

> A sample response would look as follows:

```json
{
    "description": "Successful",
    "tag_status": {
        "project_name": "demo_project",
        "tags": [
            {
            "description": "contrast in image",
            "name": "contrast",
            "output_kind": "string",
            "outputs": ["low", "normal"],
            "status": "up",
            "type": "metadata"
            },
            ...
            {
            "description": "glare in image",
            "name": "glare",
            "output_kind": "string",
            "outputs": ["low", "normal", "high", "none"],
            "status": "received",
            "type": "metadata"
            }
        ]
    }
    
}
```

This endpoint allows you to view what tags you've submitted thus far, including status on if they're up, what the outputs for them are, name, and description.

### HTTP Request

`GET https://api.sievedata.com/v1/get_tags`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project

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
```tags``` | list | list of tag names to delete

## Add Custom Model Config

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
curl https://api.sievedata.com/v1/add_custom_model_config \
    -X POST \
    -H "X-API-Key: YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
        "project_name": "amazing_project_1",
        "model_name": "my_model_name",
        "version_name": "my_version_name",
        "file_urls": [
            "file_1",
            "file_2",
            "file_n"
        ]
    }'
```

> A sample response would look as follows:

```json
{
    "description": "Pushed custom model my_model_name with version my_version_name"
}
```

This endpoint allows you to configure a new version for a custom model within your project that is controlled by you, allowing you to attach your own config files to that version to be pulled when we run the model.

### HTTP Request

`POST https://api.sievedata.com/v1/add_custom_model_config`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```model_name``` | string | the name of the model you are modifying
```version_name``` | string | the version of the model you are setting
```file_urls``` | list | list of file_urls for your config for the model architecture

## Set Active Custom Model Configuration

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
curl https://api.sievedata.com/v1/set_active_custom_model \
    -X POST \
    -H "X-API-Key: YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
        "project_name": "amazing_project_1",
        "model_name": "my_model_name",
        "version_name": "my_version_name",
    }'
```

> A sample response would look as follows:

```json
{
    "description": "Set custom model my_model_name to active version my_version_name"
}
```

This endpoint allows you to set your active model version for custom models. These versions would've either been added by us or by you with the add_custom_model_config endpoint.

### HTTP Request

`POST https://api.sievedata.com/v1/set_active_custom_model`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```model_name``` | string | the name of the model you are setting
```version_name``` | string | the version of the model you are activating

## Get Custom Models 

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
curl 'https://api.sievedata.com/v1/get_custom_models?project_name=amazing_project_1' \
    -X GET \
    -H "X-API-Key: YOUR_API_KEY" \
    -H "Content-Type: application/json"
```

> A sample response would look as follows:

```json
{
    "description": "Successful",
    "tag_status": {
        "project_name": "demo_project",
        "custom_models": [
            {
            "custom_model_info": {
                "active_version": "version_1",
                "versions": {
                    "version_1": {
                        "files": [
                            "file_1",
                            "file_2.txt",
                            ...
                            "file_n.yaml"
                        ]
                    },
                    ...
                    "version_n": {
                        "files": [
                            "file_11",
                            "file_22.txt",
                            ...
                            "file_nn.yaml"
                        ]
                    }
                }
            },
            "model_name": "my_custom_model",
            "outputs": ["low", "normal"],
            "status": "up",
            },
            ...
        ]
    }
    
}
```

This endpoint allows you to view the statuses and active configs of all custom models controlled by you that you've shipped to your platform thus far.

### HTTP Request

`GET https://api.sievedata.com/v1/get_custom_models`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project

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
        "video_url": "https://storage.googleapis.com/sieve-data-video-test-bucket/PRG1.avi",
        "video_name": "YOUR_VIDEO_NAME"
        "user_metadata": {"per_video_metadata_1": "your_val", "per_video_metadata_2": "your_other_val"}
    }'
```

> A sample response would look as follows:

```json
{
    "description": "Published video to batching",
    "job_id":"add3978a-94ac-4585-ab52-8bc5c2295c6f"
}
```

This endpoint allows you to submit video data to Sieve. Every video you submit to Sieve either needs to have a URL that is signed (secure) or public. Learn more about signed URLs for [AWS](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-signed-urls.html) or [GCP](https://cloud.google.com/storage/docs/access-control/signed-urls) at the respective links. In addition, you need to supply a unique video name for each video. Optionally, you can also submit custom metadata for the video as a whole, alone with it's associated value. For example, if you have internal indexes or fields you want to track with our platform, this would be an easy way for you to port it into our platforrm. Sieve processes cuts videos into their individual frames and uses a set of filters to process them efficiently.

### HTTP Request

`POST https://api.sievedata.com/v1/push_video`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```video_url``` | string | valid URL to video
```video_name``` | string | valid name for video
```user_metadata``` | JSON object with string keys and values (optional) | all per_video user-specified metadata

## View Status of Pushed Jobs

```shell
curl 'https://api.sievedata.com/v1/get_all_jobs?project_name=amazing_project_1&start_index=0&end_index=1000' \
    -X GET \
    -H "X-API-Key: YOUR_API_KEY" \
    -H "Content-Type: application/json"
```

> A sample response would look as follows:

```json
{
    "description": "Successful",
    "jobs": [
        {
            "job_id": "add3978a-94ac-4585-ab52-8bc5c2295c6f",
            "size_bytes": 355877454,
            "status": "processing",
            "timestamp": "Tue, 18 Jan 2022 08:36:11 GMT",
            "user_metadata": {},
            "video_name": "PRG1"
        },
        {
            "job_id": "da3fa99c-54b7-43f0-bc70-24583bc60914",
            "size_bytes": 53135264,
            "status": "finished",
            "timestamp": "Tue, 18 Jan 2022 08:30:56 GMT",
            "user_metadata": {},
            "video_name": "PRG4"
        }
        ...
        {
            "job_id": "cf9529f8-7207-469e-8879-f315c3689a06",
            "size_bytes": 34523464,
            "status": "finished",
            "timestamp": "Tue, 18 Jan 2022 05:10:45 GMT",
            "user_metadata": {},
            "video_name": "PRG30"
        }
    ],
    "total_jobs": 24
}
```

This endpoint allows you to view the properties of all jobs/videos you have submitted in the past. You get the registered size of the video, the status of processing it, the timestamp it was submitted, any user metadata that was supplied, and of course, the video name and job_id. This is batched in the event that you have many jobs, so you can specify the start_index and end_index of the jobs you want returned. The max batch size possible is 7500 objects, and the default batch size is 5000 objects. The timestamps are ordered from most recent to least recent.

### HTTP Request

`GET https://api.sievedata.com/v1/get_all_jobs`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```start_index``` | (optional) string | the start index of objects to return from the query (defaults to 0)
```end_index``` | (optional) string | the end index (exclusive) of objects to return from the query (defaults to 5000)

## Get Status of Specific Job

```shell
curl 'https://api.sievedata.com/v1/get_job_status?project_name=amazing_project_1&job_id=add3978a-94ac-4585-ab52-8bc5c2295c6f' \
    -X GET \
    -H "X-API-Key: YOUR_API_KEY" \
    -H "Content-Type: application/json"
```

> A sample response would look as follows:

```json
{
    "description": "Successful",
    "status": "finished"
}
```

This endpoint allows you to view the status of a specific job you might have run to see if it's done processing.

### HTTP Request

`GET https://api.sievedata.com/v1/get_job_status`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```job_id``` | string | the job id of a videeo you've submitted

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
curl 'https://api.sievedata.com/v1/get_metadata?project_name=demo_project&blur=slightly_blurry&lighting=dim&person_detected=True&noise=clear&start_index=0&end_index=5000' \
    -X GET \
    -H "X-API-Key: YOUR_API_KEY"
```

> A sample response would look as follows (truncated):

```json
{
    "description": "Successful. Returned with start index 0 and end index 5000",
    "metadata":
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
                "video_name":"PRG1",
                "per_video_metadata_1": "your_val",
                "per_video_metadata_2": "your_other_val"
            },
            thousands of more samples...
        ],
    "next_start": 5000,
    "total_samples": 113533
}

    
```

This endpoint is for retreiving a set of frames / images based on their defining metadata. Each tag can be specified as a part of the URL along with the matching output class, along with the size of a batch of objects that you want returned. You'll be returned a list of matching samples along with all their metadata. In addition, you will get the next start index in ```next_start``` to specify to get the next batch of objects from the query. If there is no next batch, ```next_start``` will be -1. The max batch size possible is 7500 objects, and the default batch size is 5000 objects. You also will get ```total_samples```, which is the total amount of samples that satisfy your query. If you choose to use us without hosting your video on our platform, ```signed_url``` and ```storage_path``` will not be included in the response. 

### HTTP Request

`GET https://api.sievedata.com/v1/get_metadata`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```start_index``` | (optional) string | the start index of objects to return from the query (defaults to 0)
```end_index``` | (optional) string | the end index (exclusive) of objects to return from the query (defaults to 5000)
```YOUR_TAG``` | (optional) string | one of many tags you've requested. (you can specify as many of these as you want)

## Query For Intervals by Metadata

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
curl 'https://api.sievedata.com/v1/get_intervals?project_name=demo_project&blur=slightly_blurry&lighting=dim&person_detected=True&noise=clear' \
    -X GET \
    -H "X-API-Key: YOUR_API_KEY"
```

> A sample response would look as follows (truncated):

```json
[
    {
        "video_name":"PRG1",
        "intervals":[
            [0, 343],
            [400, 599]
            [758, 1203]
            ...
            [34599, 35900]
        ]
    },
    {
        "video_name":"PRG3",
        "intervals":[
            [0, 200],
            [333, 890]
            ...
            [25000, 26432]
        ]
    },
    thousands of more samples...
]
```

This endpoint is for retreiving the set of intervals (inclusive), grouped by each video, that satisfy the conditions of the metadata filter that you specify. You'll be returned a list of all intervals and associated video name, for all videos in your project.

### HTTP Request

`GET https://api.sievedata.com/v1/get_intervals`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```YOUR_TAG``` | (optional) string | one of many tags you've requested. (you can specify as many of these as you want)


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