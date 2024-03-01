
from sqlmodel import Session, select
from fastapi import FastAPI, Depends, HTTPException, Query
from typing import Annotated

from .database import create_db_and_tables
from .depend import get_session
from .models import TaskCreate, TaskResponse,  Tasks, TaskUpdate
from fastapi.middleware.cors import CORSMiddleware

# Plain API without Dependency injection


app = FastAPI(
    title="Task Master",
    description="The GPT is designed to assist users in managing their todo lists. It will help users create, update, prioritize, and organize their tasks. It should guide users in breaking down tasks into manageable steps, suggest deadlines, and remind them of upcoming tasks. The GPT will focus on productivity and task management, providing tips and strategies for effective todo list management. It will avoid giving personal advice or opinions, focusing instead on task-related assistance. It should clarify task details with users if necessary, and adapt its responses to suit the user's preferred task management style.",
    version="0.1.0",
    servers=[
        {
            "url": "https://ab64-39-53-236-47.ngrok-free.app/api",
            "description":"Production Server"
        },
        {
            "url": "http://127.0.0.1:8000/",
            "description":"Development Server"},
        ]
)

# CORS middleware configuration
origins = [
    "http://localhost:8000",   # Another example with a different port
    "https://cool-probable-seasnail.ngrok-free.app/",     # Example for a different domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    create_db_and_tables()

@app.get("/api")
async def root():
    return {"message": "Your Todo App is Running ;-)"}



@app.get("/api/tasks", response_model=list[TaskResponse] | None, tags=["Namaz"])
def get_tasks(session: Annotated[Session, Depends(get_session)]):
    tasks = session.exec(select(Tasks)).all()
    return tasks


@app.post("/api/tasks", response_model=TaskResponse, tags=["Namaz"])
def create_task(task: TaskCreate, session: Annotated[Session, Depends(get_session)]):
    task_to_add = Tasks(**task.model_dump(exclude_unset=True))
    session.add(task_to_add)
    session.commit()
    session.refresh(task_to_add)
    return task_to_add


@app.get("/api/tasks/{task_title}", response_model=TaskResponse, tags=["Namaz"]) 
def get_single_task(task_title: str, session: Annotated[Session, Depends(get_session)]):
    task = session.exec(select(Tasks).where(Tasks.title == task_title)).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.patch("/api/tasks/{task_title}", tags=["Namaz"])
def update_task(task_title: str, task_data: TaskUpdate, session: Annotated[Session, Depends(get_session)]):
    task = session.exec(select(Tasks).where(Tasks.title == task_title)).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    print("Hero in DB:", task)
    print("Hero Data from client:", task_data)
    
    hero_dict_data = task_data.model_dump(exclude_unset= True)
    print("Hero Dict Data:", hero_dict_data)
    
    for key, value in hero_dict_data.items():
        setattr(task, key, value)
    print("Hero after update:", task)
    
    session.add(task)
    session.commit()
    session.refresh(task)
    
    return task


@app.delete("/api/tasks/{task_title}", tags=["Namaz"])
def delete_task(task_title: str, session: Annotated[Session, Depends(get_session)]):
    task = session.exec(select(Tasks).where(Tasks.title == task_title)).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    session.delete(task)
    session.commit()
    return {"message": "Task deleted successfully"}
