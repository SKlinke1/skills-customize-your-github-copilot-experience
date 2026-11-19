# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to manage study tasks. You will practice defining resource endpoints, validating request data, and returning appropriate HTTP status codes.

## 📝 Tasks

### 🛠️ Read Study Tasks

#### Description
Use the provided starter file to build the foundation of a study task API. The sample tasks are stored in memory, so changes do not need to be saved after the server stops.

Run the API from the assignment folder with:

```bash
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/docs` to explore and call the endpoints.

#### Requirements
Completed program should:

- Define `GET /tasks` to return all study tasks
- Define `GET /tasks/{task_id}` to return one task by its ID
- Return HTTP 404 when the requested task ID does not exist


### 🛠️ Create Study Tasks

#### Description
Add an endpoint for creating tasks. Define a Pydantic request model so FastAPI can validate the incoming task data.

#### Requirements
Completed program should:

- Define a request model with a required, non-empty `title` and an optional `completed` value that defaults to `false`
- Define `POST /tasks` to validate and add a task, assigning it a unique ID
- Return the created task with HTTP 201, and let invalid request data receive a validation error


### 🛠️ Update and Remove Study Tasks

#### Description
Complete the API's CRUD operations by allowing an existing task to be updated or removed. Try each endpoint in the interactive API documentation.

#### Requirements
Completed program should:

- Define `PUT /tasks/{task_id}` to update a task's title and completion state
- Define `DELETE /tasks/{task_id}` to remove a task and return HTTP 204 on success
- Return HTTP 404 when an update or delete request uses an unknown task ID
