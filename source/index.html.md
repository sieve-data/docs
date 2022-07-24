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
    content: Documentation for the Sieve API
---

# Introduction

Welcome to the Sieve API! You can use our API to access Sieve API endpoints, which can help you submit visual data to Sieve and then make queries on that data.

If you haven't already, you can [sign up on our home page](https://sievedata.com/).

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
    "config_url": "YOUR_CONFIG_URL"
  }'
```

> A sample response would look as follows:

```json
{
    "description": "Created project amazing_project_1",
    "project_id": "18ff75d5-8f7d-4c7b-b3ed-7c66615d9808"
}
```

This endpoint creates a new Sieve project. A new project is defined by a workflow configuration. A workflow is set of rules that specify the different models and algorithms that run on data submitted to the project. If you're using our public free trial, you'll have a constrained set of preconfigured projects to try out though Sieve does support all sorts of custom use cases given the flexibility of Sieve workflows.

If you're interested in custom projects, please
<a href="https://docs.google.com/forms/d/e/1FAIpQLScXC2lotHC_9PTgYyqzJUsPgfeU2W5sii7sEWcQB1kfNGKQxw/viewform?usp=sf_link" target="_blank">reach out here</a>.

To see sample configs of some pre-configured projects that are available, refer to the list below.

<a href="https://storage.googleapis.com/sieve-preconfigured-projects/configs/broadcast-news-media.json" target="_blank">Broadcast / News & Media</a>
<br />
<a href="https://storage.googleapis.com/sieve-preconfigured-projects/configs/dashcam.json" target="_blank">Dashcam</a>
<br />
<a href="https://storage.googleapis.com/sieve-preconfigured-projects/configs/esports.json" target="_blank">Esports</a>
<br />
<a href="https://storage.googleapis.com/sieve-preconfigured-projects/configs/live-social.json" target="_blank">Live Social</a>
<br />
<a href="https://storage.googleapis.com/sieve-preconfigured-projects/configs/pet-monitoring.json" target="_blank">Pet Monitoring</a>
<br />
<a href="https://storage.googleapis.com/sieve-preconfigured-projects/configs/player-identification.json" target="_blank">Player Jersey Identification</a>
<br />
<a href="https://storage.googleapis.com/sieve-preconfigured-projects/configs/security.json" target="_blank">Security</a>
<br />
<a href="https://storage.googleapis.com/sieve-preconfigured-projects/configs/street-cams.json" target="_blank">Street Cameras</a>


### HTTP Request

`POST https://api.sievedata.com/v1/init_project`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```config_url``` | string (optional) | url to custom config json
```config``` | object (optional) | custom config json

<aside class="notice">
A project name needs to be specified on every API request having to do with project data.
</aside>

## Get All User / Organization Info

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
        "hours_left": NUM_HOURS_LEFT
    }
}
```

This endpoint retrieves the names of all projects you've created within your organization along with other information such
as the number of hours of video left in your API quota.

### HTTP Request

`GET https://api.sievedata.com/v1/get_projects`

## Get Project Info

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
curl 'https://api.sievedata.com/v1/get_project_info?project_name=amazing_project_1' \
  -X GET \
  -H "X-API-Key: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> A sample response would look as follows:

```json
{"description": "Successful",
 "project_info": {"_id": "98dc895e-6ab5-438b-90fa-4cfc3ffefece",
  "batch_size": 10,
  "fps": 5,
  "levels": [{"entry": "batch_video",
    "filter_workflow": ["none"],
    "models": [{"class_restrictions": {"classes": ["person",
        "bicycle",
        "car",
        "motorcycle",
        "bus",
        "train",
        "truck",
        "traffic light",
        "fire hydrant",
        "stop sign",
        "parking meter",
        "bird",
        "cat",
        "dog"],
       "keep": True},
      "model_name": "coco_yolo_tracking_detector"}]},
   {"entry": "batch_video",
    "filter_workflow": ["none"],
    "models": [{"model_name": "consolidate_tracking_data_interval"}]},
   {"entry": "batch_objects",
    "filter_workflow": ["none"],
    "models": [{"model_name": "reassign_object_ids"}]},
   {"entry": "batch_video",
    "filter_workflow": ["none"],
    "models": [{"model_name": "bbox_info_predictor",
      "model_topic": "bbox_info_predictor_input",
      "model_version": "v1",
      "status": "up",
      "type": "metadata_cf"},
     {"model_name": "counts_predictor",
      "model_topic": "counts_predictor_input",
      "model_version": "v1",
      "status": "up",
      "type": "metadata_cf"}]}],
  "network_optimized": True,
  "num_samples": 0,
  "preconfigured_type": "Dashcam",
  "project_name": "demo_project",
  "tags": {"class": {"_items": ["person",
     "bicycle",
     "car",
     "motorcycle",
     "bus",
     "train",
     "truck",
     "traffic light",
     "fire hydrant",
     "stop sign",
     "parking meter",
     "bird",
     "cat",
     "dog"],
    "_type": "string"},
   "object_id": {"_type": "string"},
   "project_name": {"_type": "string"},
   "temporal": {"bbox": {"position": {"area": {"_type": "number"},
      "height": {"_type": "number"},
      "width": {"_type": "number"},
      "x1": {"_type": "number"},
      "x2": {"_type": "number"},
      "y1": {"_type": "number"},
      "y2": {"_type": "number"}},
     "speed": {"bottom_left": {"_type": "number"},
      "bottom_right": {"_type": "number"},
      "top_left": {"_type": "number"},
      "top_right": {"_type": "number"}},
     "velocity": {"x1": {"_type": "number"},
      "x2": {"_type": "number"},
      "y1": {"_type": "number"},
      "y2": {"_type": "number"}}},
    "center": {"position": {"x": {"_type": "number"},
      "y": {"_type": "number"}},
     "speed": {"_type": "number"},
     "velocity": {"x": {"_type": "number"}, "y": {"_type": "number"}}},
    "count": {"_type": "number"},
    "frame_number": {"_type": "number"}},
   "video_name": {"_type": "string"}}}
}

```

This endpoint allows you to view the project configuration for a particular project you've made.
This returns the tag schema, the FPS, the pipeline configuration, and other fields of the project.

### HTTP Request

`GET https://api.sievedata.com/v1/get_project_info`

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

This endpoint allows you to submit video data to Sieve. Every video you submit to Sieve either needs to have a URL that is signed (secure) or public. Learn more about signed URLs for
<a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html" target="_blank">AWS</a>
or
<a href="https://cloud.google.com/storage/docs/access-control/signed-urls" target="_blank">GCP</a>
at the respective links. In addition, you need to supply a unique video name for each video. Optionally, you can also submit custom metadata for the video as a whole, alone with it's associated value. For example, if you have internal indexes or fields you want to track with our platform, this would be an easy way for you to access those within Sieve as well.

### HTTP Request

`POST https://api.sievedata.com/v1/push_video`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```video_url``` | string | valid URL to video
```video_name``` | string | valid name for video
```user_metadata``` | JSON object with string keys and values (optional) | all per_video user-specified metadata

## Get Status of All Jobs

```shell
curl 'https://api.sievedata.com/v1/get_all_jobs?project_name=amazing_project_1' \
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

This endpoint allows you to view the properties of all jobs you have submitted to a project. A job is a single video you submitted to Sieve. You can retrieve the registered size of the video, its processing status, the timestamp it was submitted, any user metadata that was supplied, and of course, the video name and job_id. The timestamps are ordered from most recent to least recent.

### HTTP Request

`GET https://api.sievedata.com/v1/get_all_jobs`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project

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

This endpoint allows you to view the status of a specific job.

### HTTP Request

`GET https://api.sievedata.com/v1/get_job_status`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```job_id``` | string | the job id of a videeo you've submitted

# Querying Data

You can think of Sieve almost like a database for video data. Push video, and make queries. Below, we introduce key concepts
to understand the power of Sieve's query system.

<b>Everything in a video is an object.</b> <br />
A person, a car, a dog, and even the frame itself. Videos are just objects defined by various properties.

![](images/concepts/object-paradigm.png)
<br />

<b>Objects have different properties that change over time.</b> <br />
Objects can more specifically be defined by properties that do and don't change over time. For example, every object might have a `class` attribute such as `person`, `car`, or something else which doesn't change. However, other items such as `position`, `speed`, `lighting`, and others do.

![](images/concepts/object-over-time.png)

<b>Sieve is a database for video which allows you to query in a way that makes sense.</b> <br />
Traditionally, videos could only be "queried" by a timestamp to find the information in that frame. Sieve instead takes an object-first approach.
Sieve treats everything as an object. Every object has stationary attributes such as `class`, `start_frame`, `end_frame`, `object_id`, and more.
Every object also has attributes which change over time. This could include information such as `position`, `speed`, `size`, and more.

Video frames are also treated as objects (which has bounding boxes that take up the entire frame). They can also have their own attributes such as
`lighting`, `resolution`, or other classifications performed on the frame-level.

Sieve automatically tracks objects across frames which is why this information is retrievable in this way.

## Query for Metadata

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
curl 'https://api.sievedata.com/v1/query' \
  -X POST \
  -H "X-API-Key: YOUR_API_KEY" \ 
  -H "Content-Type: application/json" \
  -d '{
  "video_name": "video_1",
  "project_name": "amazing_project_1"
    "temporal.frame_number": {"$lte": 500, "$gte": 100},
    "class": {
      "$in": [
          "car",
          "frame
      ]
    },
	}'
```

> A sample response would look as follows (truncated):

```json
{"description": "Successful. Returned 167 objects",
 "next_start": 167,
 "objects": [{"_id": "4af23cae-58ae-49d5-bbb3-2cd23ab69c54",
   "class": "car",
   "end_frame": 1248,
   "object_id": "4af23cae-58ae-49d5-bbb3-2cd23ab69c54",
   "project_name": "amazing_project_1",
   "start_frame": 1230,
   "temporal": [{"bbox": {"position": {"area": 1346.6105655468766,
       "height": 29.85799212551774,
       "width": 45.10050642005541,
       "x1": 448.0669623507817,
       "x2": 493.1674687708371,
       "y1": 309.0682736427327,
       "y2": 338.92626576825046},
      "speed": {"bottom_left": 4.315388630606474,
       "bottom_right": 30.15500296597246,
       "top_left": 10.622436250109503,
       "top_right": 31.67866437734206},
      "velocity": {"x1": 2.3676354637587047,
       "x2": -29.938392116710077,
       "y1": 10.355213865410631,
       "y2": -3.607891537161244}},
     "center": {"position": {"x": 470.6172155608094, "y": 323.9972697054916},
      "speed": 14.192189586332075,
    ...
     "count": 12,
     "frame_number": 342}],
   "video_name": "video_1"}],
 "query_latency": 0.810,
 "total_samples": 167}

    
```

This endpoint allows the retrieval of a set of objects that match a query. Sieve can be queried in way that's similar to MongoDB. Currently, the following MongoDB operations are supported on all tags that exist within an object.

Operation |
--------- | -----------
```$exists``` |
```$gte``` |
```$gt``` |
```$lte``` |
```$lt``` |
```$ne``` |
```$in``` |

To see the schema of your project (which will determine how you use the above operations), you can call the [`/get_project_info`](#get-project-info) endpoint. Attributes that change over time are encoded under the `temporal` attribute of an object while static attributes exist on the top-level.

Because return payload can be large, Sieve batches that payload into multiple pages which can be specificied using the `next_start` param. You will get the next start index in ```next_start``` everytime you make a query which you can include in your next query. If there are no more pages, ```next_start``` will be -1. The max batch size possible is 7500 objects, and the default batch size is 5000 objects. You also will get ```total_samples```, which is the total amount of samples that satisfy your query. 

### HTTP Request

`POST https://api.sievedata.com/v1/query`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```next_start``` | (optional) int | the amount of objects to skip in query (defaults to 0, used for paging)
```YOUR_TAG``` | (optional) object or string | one of many tags in your schema. (you can specify as many of these as you want). These can be queried for in mongo format.

<aside class="notice">
For more information on how to construct queries in MongoDB syntax to interface with the data, here is a link to the <a href="https://www.mongodb.com/docs/manual/reference/">MongoDB Reference</a>.
</aside>

<aside class="notice">
For projects with a field in the tag schema that contains has a "_type" of "text", you can use the <a href="https://www.mongodb.com/docs/manual/core/text-search-operators/">MongoDB Legacy text query engine</a> to search for text information throughout the project. For more information, get started with a text enabled project like E-Sports or Live Social today!
</aside>

## Query For Intervals

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
curl 'https://api.sievedata.com/v1/intervals' \
    -X POST \
    -H "X-API-Key: YOUR_API_KEY" \ 
    -H "Content-Type: application/json" \
    -d '{
	  "video_name": "video_1",
	  "project_name": "amazing_project_1"
      "class": {
        "$in": [
            "car",
            "frame
        ]
        },
	}'
```

> A sample response would look as follows (truncated):

```json
{"description": "Successful, returned 1 groups of intervals",
 "intervals": [
    {
        "video_name":"video_1",
        "intervals":[
            [0, 1200],
            [1300, 1330]
            ...
            [34599, 35900]
        ]
    },
    {
        "video_name":"video_2",
        "intervals":[
            [0, 200],
            [333, 890]
            ...
            [25000, 26432]
        ]
    },
    thousands of more samples...
    ],
 "next_start": -1,
 "query_latency": "0.088"}
```

This endpoint allows the retrieval of a set of intervals within a video which match a query. Usage works in the same way as the [`/query`](#query-for-metadata) endpoint. The only difference is the return payload which will be a list of all intervals that match your query within each video you've submitted to your project.

### HTTP Request

`GET https://api.sievedata.com/v1/intervals`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```next_start``` | (optional) int | the amount of objects to skip in query (defaults to 0, used for paging)
```YOUR_TAG``` | (optional) object or string | one of many tags in your schema. (you can specify as many of these as you want). These can be queried for in mongo format.


<aside class="notice">
For more information on how to construct queries in MongoDB syntax to interface with the data, here is a link to the <a href="https://www.mongodb.com/docs/manual/reference/">MongoDB Reference</a>.
</aside>

<aside class="notice">
For projects with a field in the tag schema that contains has a "_type" of "text", you can use the <a href="https://www.mongodb.com/docs/manual/core/text-search-operators/">MongoDB Legacy text query engine</a> to search for text information throughout the project. For more information, get started with a text enabled project like E-Sports or Live Social today!
</aside>

# Deleting Data

## Delete Video Data

```shell
curl 'https://api.sievedata.com/v1/delete_video_data?project_name=CamNet&video_name=MyVideo' \
  -X DELETE \
  -H "X-API-Key: YOUR_API_KEY"
```

> A sample response would look as follows (truncated):

```json
{
    "description":"Deleted video data of MyVideo in project CamNet successfully.",
}
```

### HTTP Request

`POST https://api.sievedata.com/v1/delete_video_data`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```video_name``` | string | the name of the video

# Feedback Loop

Sieve's system is not only a database for video that you can query, but also a system that can automatically improve over time. No machine learning
system is perfect, but machine learning systems do have ways of incrementally improving themselves. This is made seamless with Sieve's feedback loop.
Just provide feedback whenever you'd like, and Sieve's systems will take care of the rest.

## Corrections

> Correct object with id "12345" in project "some_project" and video "some_video" to a new class "person"

```shell
curl 'https://api.sievedata.com/v1/feedback/correct_object' \
  -X POST \
  -H "X-API-Key: YOUR_API_KEY" \
  -d '{
    "project_name": "some_project",
    "video_name": "some_video",
    "corrections": [
      {
        "object_id": "12345",
        "class": "person"
      }
    ]
  }'
```

> Correct object with id "12345" in project "some_project" and video "some_video" to a new bounding box position

```shell
curl 'https://api.sievedata.com/v1/feedback/correct_object' \
  -X POST \
  -H "X-API-Key: YOUR_API_KEY" \
  -d '{
    "project_name": "some_project",
    "video_name": "some_video",
    "corrections": [
      {
        "object_id": "12345",
        "temporal": [
          {
            "bbox": {
              "position": {
                "x1": 5,
                "x2": 50,
                "y1": 5,
                "y2": 10
              }
            },
            "frame_number": 5
          }
        ]
      }
    ]
  }'
```

> A sample response would look as follows (truncated):

```json
{
    "description": "Corrected successfully.",
    "corrected_object_ids": [12345],
}
```

This endpoint allows the correction of any given set of objects in a video as a way to correct mistakes made by the system. Feedback is specified
in the `corrections` parameter in the same format as the payloads returned by the [`/query`](#query-for-metadata) endpoint. The system will automatically
make corrections to the data specified and then improve itself automatically based on the feedback.

Eech correction must specify the `object_id` of the object to be corrected. All other fields depend on the project schema.

### HTTP Request

`POST https://api.sievedata.com/v1/feedback/correct_object`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```video_name``` | string | the name of the video
```corrections``` | list | list of corrections to make

## Additions

> Add new dog object in project "some_project" and video "some_video"

```shell
curl 'https://api.sievedata.com/v1/feedback/add_object' \
  -X POST \
  -H "X-API-Key: YOUR_API_KEY" \
  -d '{
    "project_name": "some_project",
    "video_name": "some_video",
    "additions": [
      {
        "class": "dog",
        "temporal": [
          {
            "bbox": {
              "position": {
                "x1": 5,
                "x2": 50,
                "y1": 5,
                "y2": 10
              }
            },
            "frame_number": 5
          }
        ]
      }
    ]
  }'
```

> A sample response would look as follows:

```json
{
    "description": "Added successfully."
}
```

This endpoint allows the additions of any objects the system completely missed in a video. Feedback is specified in the `additions` parameter in the same format as the payloads returned by the [`/query`](#query-for-metadata) endpoint. The system will automatically add the objects specified and then improve itself automatically based on the feedback.

The additions must specify the `class` of the object to be added along with atleast one temporal bounding box position.

### HTTP Request

`POST https://api.sievedata.com/v1/feedback/add_object`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```video_name``` | string | the name of the video
```additions``` | list | list of additions to make

## Removals

> Delete objects with id "12345", "56789" and "98765" in project "some_project" and video "some_video"

```shell
curl 'https://api.sievedata.com/v1/feedback/remove_object' \
  -X POST \
  -H "X-API-Key: YOUR_API_KEY" \
  -d '{
    "project_name": "some_project",
    "video_name": "some_video",
    "removals": [
      "12345",
      "56789",
      "98765"
    ]
  }'
```

> A sample response would look as follows:

```json
{
    "description": "Deleted successfully.",
    "removed_object_ids": ["12345", "56789", "98765"]
}
```

This endpoint allows the removal of any objects the system incorrectly detected in a video. Feedback is specified in the `removals` parameter in the same format as the payloads returned by the [`/query`](#query-for-metadata) endpoint. The system will automatically remove the objects specified and then improve itself automatically based on the feedback.

The `removals` parameter is a list of object ids to remove.

### HTTP Request

`POST https://api.sievedata.com/v1/feedback/remove_object`

### Parameters

Parameter | Type | Description
--------- | ------- | -----------
```project_name``` | string | the name of the project
```video_name``` | string | the name of the video
```removals``` | list | list of removals to make