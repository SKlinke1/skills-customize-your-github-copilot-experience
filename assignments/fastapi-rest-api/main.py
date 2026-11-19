from fastapi import FastAPI

app = FastAPI(title="Study Task Tracker")

tasks = {
    1: {"id": 1, "title": "Review variables", "completed": False},
    2: {"id": 2, "title": "Practice loops", "completed": True},
}
next_task_id = 3

# Add your task endpoints below.
