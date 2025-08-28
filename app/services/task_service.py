from sqlalchemy.orm import Session
from app.models.task import Task

def create_task(db: Session, title: str) -> Task:
    task = Task(title=title)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_task(db: Session, task_id: int) -> Task | None:
    return db.get(Task, task_id)

def get_tasks(db: Session, search: str | None = None):
    query = db.query(Task)
    if search:
        query = query.filter(Task.title.contains(search))
    return query.all()

def toggle_task(db: Session, task_id: int) -> Task | None:
    task = db.get(Task, task_id)
    if task:
        task.completed = not task.completed
        db.commit()
        db.refresh(task)
    return task

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

def delete_task(db: Session, task_id: int) -> Task | None:
    task = db.get(Task, task_id)
    if task:
        db.delete(task)
        db.commit()
    return task
