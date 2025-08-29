import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def graphql_query(query: str):
    """Helper to send GraphQL queries."""
    response = client.post("/graphql", json={"query": query})
    assert response.status_code == 200
    return response.json()


def create_task(title="temp task"):
    """Utility: create a task and return it."""
    query = f"""
    mutation {{
        addTask(input: {{ title: "{title}" }}) {{
            id
            title
            completed
        }}
    }}
    """
    data = graphql_query(query)
    return data["data"]["addTask"]


def test_add_task():
    task = create_task("first Task")
    assert task["title"] == "first Task"
    assert task["completed"] is False


def test_list_tasks():
    create_task("list me")
    query = """
    query {
        tasks {
            id
            title
            completed
        }
    }
    """
    data = graphql_query(query)
    tasks = data["data"]["tasks"]
    assert len(tasks) > 0


def test_search_task_by_id():
    task = create_task("search by id")
    query = f"""
    query {{
        task(id: {task["id"]}) {{
            id
            title
            completed
        }}
    }}
    """
    data = graphql_query(query)
    found = data["data"]["task"]
    assert found["id"] == task["id"]
    assert found["title"] == "search by id"


def test_search_tasks_by_title():
    create_task("find me by title")
    query = """
    query { 
        tasks(search: "find me") { 
            id 
            title 
            completed 
        } 
    }
    """
    data = graphql_query(query)
    tasks = data["data"]["tasks"]
    assert any("find me" in t["title"] for t in tasks)


def test_toggle_task():
    task = create_task("toggle me")
    query = f"""
    mutation {{
        toggleTask(id: "{task["id"]}") {{
            id
            title
            completed
        }}
    }}
    """
    data = graphql_query(query)
    toggled = data["data"]["toggleTask"]
    assert toggled["id"] == task["id"]
    assert isinstance(toggled["completed"], bool)


def test_update_task():
    task = create_task("update me")
    query = f"""
    mutation {{
        updateTask(id: "{task["id"]}", input: {{ title: "updated task", completed: true }}) {{
            id
            title
            completed
        }}
    }}
    """
    data = graphql_query(query)
    updated = data["data"]["updateTask"]
    assert updated["title"] == "updated task"
    assert updated["completed"] is True


def test_delete_task():
    task = create_task("delete me")
    query = f"""
    mutation {{
        deleteTask(id: "{task["id"]}") {{
            id
            title
        }}
    }}
    """
    data = graphql_query(query)
    deleted = data["data"]["deleteTask"]
    assert deleted["id"] == task["id"]
    assert "delete" in deleted["title"]
