# Tasks GraphQL API

A simple GraphQL API for managing tasks using **FastAPI**, **Strawberry GraphQL**, and **SQLite**.

---
## Features

- Add, toggle, delete tasks
- Query all tasks or search by title
- Query a single task by ID
- Timestamps for task creation and updates
- Fully GraphQL-based API

## Requirements

- Python 3.11+
- SQLite (built-in with Python)

## Installation & Run

1. Clone the repository:
    ```bash
    git clone https://github.com/harp-eng/task_list_api.git
    cd task_list_api
2. Create and activate a virtual environment
    ```bash
    python3 -m venv venv
    # Linux/Mac
    source venv/bin/activate
    # Windows
    venv\Scripts\activate
If you encounter the following error when running: The virtual environment was not created successfully because ensurepip is not available.


You can fix it by installing the python3.10-venv package:
    
    sudo apt install python3.10-venv

Note: After running this command, start from Step 2 again.

3. Install dependencies:
    ```bash
    pip install -r requirements.txt

4. Run the FastAPI server:
    ```bash
    uvicorn app.main:app --reload

5. Open the GraphQL Playground in your browser:

    http://127.0.0.1:8000/graphql


##  Examples
### Add a Task
        mutation {
            addTask(title: "first Task") {
                id
                title
                completed
            }
        }


### List Tasks
        query {
            tasks {
                id
                title
                completed
            }
        }

### Search task by ID
        query {
            task(id:1){
                id
                title
                completed
            }
        }

### Search tasks by title
        query { 
            tasks(search: "first") { 
                id 
                title 
                completed 
            } 
        }

### Toggle a Tasks Completion Status
    
    mutation {
        toggleTask(id: "1") {
            id
            title
            completed
        }
    }

### Update Task
    
    mutation {
        updateTask(id: "1" title:"updated first Task") {
            id
            title
            completed
        }
    }

### Delete a Task
    mutation {
        deleteTask(id: "1") {
            id
            title
        }
    }


### Error Handling

Right now, the system handles basic errors like:

1) Returning null if a task ID doesn’t exist when trying to toggle or delete a task.

2) Returning an empty list if no tasks match a search or query.

###  For more advanced error handling, we can do the following:

1) Custom GraphQL Errors

    Use Strawberry’s custom exceptions to show clear error messages.

    Example: If a task title is empty or too long, return a helpful message explaining the problem.
    ```
    class TaskError(Exception):
        def __init__(self, message: str):
            self.message = message

    if not title.strip():
            raise TaskError("Task title cannot be empty.")
    if len(title) > 50:
            raise TaskError("Task title cannot be longer than 50 characters.")

2) Logging and Monitoring

    Keep a log of all errors using Python’s logging module or services like Sentry.

    Track failed GraphQL requests and mutations so we can find and fix the issues.

### Additional queries or mutations 

1) Next mutation we can add to update the title of existing Task.
    In resolver file 
    ```
       @strawberry.mutation
        def update_task(self, info: Info, id: strawberry.ID, title: Optional[str] = None, completed: Optional[bool] = None) -> Optional[TaskType]:
            db = info.context["db"]
            task = update_task(db, int(id), title, completed)
            return TaskType.from_model(task) if task else None

    
In service file
```
    def update_task(db: Session, task_id: int, title: str | None = None, completed: bool | None = None) -> Task | None:
    task = db.get(Task, task_id)
    if task:
        if title is not None:
            task.title = title
        if completed is not None:
            task.completed = completed
        db.commit()
        db.refresh(task)
    return task

