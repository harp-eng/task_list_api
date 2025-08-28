import strawberry
from typing import Optional
from app.models.task import Task

@strawberry.type
class TaskType:
    id: strawberry.ID
    title: str
    completed: bool
    created_at: str
    updated_at: str

    @staticmethod
    def from_model(task: Task) -> "TaskType":
        return TaskType(
            id=str(task.id),
            title=task.title,
            completed=task.completed,
            created_at=task.created_at.isoformat(),
            updated_at=task.updated_at.isoformat(),
        )
