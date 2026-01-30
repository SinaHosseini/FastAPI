from sqlalchemy.orm import Session
from models import Task
from schemas import TaskCreate, TaskUpdate


def commit_changed(db: Session, db_task):
    db.commit()
    db.refresh(db_task)


def get_tasks(db: Session):
    return db.query(Task).all()


def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


def create_task(db: Session, task: TaskCreate):
    db_task = Task(
        title=task.title,
        description=task.description,
        time=task.time,
        status=int(task.status),
    )
    db.add(db_task)
    commit_changed(db, db_task)
    return db_task


def update_task(db: Session, task_id: int, task: TaskUpdate):
    db_task = get_task(db, task_id)
    if not db_task:
        return None

    db_task.title = task.title
    db_task.description = task.description
    db_task.time = task.time
    db_task.status = int(task.status)

    commit_changed(db, db_task)
    return db_task


def delete_task(db: Session, task_id: int):
    db_task = get_task(db, task_id)
    if not db_task:
        return None

    db.delete(db_task)
    db.commit()
    return db_task
