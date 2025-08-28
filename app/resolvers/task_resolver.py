import strawberry
from strawberry.types import Info
from typing import List, Optional
from app.schemas.task_schema import TaskType
from app.services.task_service import create_task, get_task, get_tasks, toggle_task, update_task, delete_task

@strawberry.type
class TaskQuery:
    @strawberry.field
    def tasks(self, info: Info, search: Optional[str] = None) -> List[TaskType]:
        db = info.context["db"]
        return [TaskType.from_model(t) for t in get_tasks(db, search)]

    @strawberry.field
    def task(self, info: Info, id: strawberry.ID) -> Optional[TaskType]:
        db = info.context["db"]
        task = get_task(db, int(id))
        return TaskType.from_model(task) if task else None

@strawberry.type
class TaskMutation:
    @strawberry.mutation
    def add_task(self, info: Info, title: str) -> TaskType:
        db = info.context["db"]
        task = create_task(db, title)
        return TaskType.from_model(task)

    @strawberry.mutation
    def toggle_task(self, info: Info, id: strawberry.ID) -> Optional[TaskType]:
        db = info.context["db"]
        task = toggle_task(db, int(id))
        return TaskType.from_model(task) if task else None

    @strawberry.mutation
    def update_task(self, info: Info, id: strawberry.ID, title: Optional[str] = None, completed: Optional[bool] = None) -> Optional[TaskType]:
        db = info.context["db"]
        task = update_task(db, int(id), title, completed)
        return TaskType.from_model(task) if task else None

    @strawberry.mutation
    def delete_task(self, info: Info, id: strawberry.ID) -> Optional[TaskType]:
        db = info.context["db"]
        task = delete_task(db, int(id))
        return TaskType.from_model(task) if task else None
