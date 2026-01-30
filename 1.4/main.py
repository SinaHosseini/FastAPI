from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
import numpy as np
import cv2
from deepface import DeepFace

import models
import crud
import schemas
from db import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return "Hello world"


@app.post("/tasks", response_model=schemas.TaskOut)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)


@app.get("/tasks", response_model=list[schemas.TaskOut])
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)


@app.get("/tasks/{task_id}", response_model=schemas.TaskOut)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/tasks/{task_id}", response_model=schemas.TaskOut)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    updated_task = crud.update_task(db, task_id, task)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted_task = crud.delete_task(db, task_id)
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}


@app.post("/analyze_image")
async def image_processing(inp_file: UploadFile = File(None)):
    if not inp_file.content_type.startswith("image/"):
        raise HTTPException(status_code=415, detail="Unsupported file type")
    
    contents = await inp_file.read()
    np_array = np.frombuffer(contents, dtype=np.uint8)
    image_path = cv2.imdecode(np_array, cv2.IMREAD_UNCHANGED)
    # cv2.imwrite("img.jpg", image_path)

    objs = DeepFace.analyze(img_path=image_path, actions=[
                            "age", "gender", "race", "emotion"],
                            enforce_detection=False)
    for obj in objs:
        age = obj["age"]
        gender = obj["dominant_gender"]
        race = obj["dominant_race"]
        emotion = obj["dominant_emotion"]

    return {"age" : age, "gender" : gender, "race" : race, "emotion" : emotion}
