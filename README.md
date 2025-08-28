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
    python -m venv venv
    # Linux/Mac
    source venv/bin/activate
    # Windows
    venv\Scripts\activate
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
    ```graphql
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

### Search tasks 
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

### Delete a Task
    mutation {
        deleteTask(id: "1") {
            id
            title
        }
    }
