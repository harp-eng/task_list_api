# Tasks GraphQL API

A simple GraphQL API for managing tasks using **FastAPI**, **Strawberry GraphQL**, and **SQLite**.

---

## Installation & Run

1. Clone the repository:
    ```bash
    git clone https://github.com/harp-eng/task_list_api.git
    cd task_list_api

2. Install dependencies:
    ```bash
    pip install -r requirements.txt

3. Run the FastAPI server:
    ```bash
    uvicorn app.main:app --reload

4. Open the GraphQL Playground in your browser:

    http://127.0.0.1:8000/graphql


    ##  Examples
    ### Add a Task
    ```graphql
        mutation {
            addTask(title: "Learn FastAPI") {
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
