# Using Google Tasks API

The Google Tasks API using Python.

## References

- [Google Tasks API Documentation](https://developers.google.com/tasks/reference/rest/v1/tasks/list)
- [Google's Python Quickstart Guide](https://developers.google.com/tasks/quickstart/python)

## Retrieving Tasks from a Task List

To retrieve tasks from a specific task list, we can use the Python client library provided by Google. Follow these steps:

1. **Set up your Python environment** and install the required libraries as explained in the Google Python Quickstart Guide.  
```commandline
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

2. I set my authentication as an external user which worked fine for me, just add read-only permission. Download the credential file, save it and rename as "credentials.json".  
3. To retrieve tasks from a specific task list(obtained from tasklist() api), I used the following code snippet-

```python
from googleapiclient.discovery import build

# build the service, same as tasklist() api
service = build("tasks", "v1", credentials=creds)

# retrieve task from a specific task list
task_list_id = "MTY4MjkwOTYwNjkxMDE0MzA4MjU6MDow"  # Replace with the actual task list ID
tasks = service.tasks().list(tasklist=task_list_id).execute()

for task in tasks.get("items", []):
    print(task["title"])
    print(task["due"])
    print()
```
The output will be like this:
```commandline
task 1
2024-04-11

task 2
2024-04-13

task 2
2024-04-12
```
I encountered an error related to the "due" key not found, it was due to the presence of an empty task with "" title and no due date.  
```commandline
{
      "kind": "tasks#task",
      "id": "id",
      "etag": "\"etag\"",
      "title": "",
      "updated": "2023-06-19T13:52:12.000Z",
      "selfLink": "a_link",
      "position": "00000000000000000012",
      "status": "needsAction",
      "links": [],
      "webViewLink": "a_web_link"
    }
```
![error](https://github.com/Adnan525/google_task_api/blob/main/json_access.png)