from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import select,delete
from pydantic import BaseModel

app=FastAPI()

#Database Setup
DATABASE_URL= "sqlite:///./notes.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":False})
SessionLocal= sessionmaker(bind=engine)
Base = declarative_base()

# Note Table
class Note(Base):
    __tablename__="notes"
    id = Column(Integer,primary_key=True, index=True)
    title = Column(String)
    content = Column(String)

class NoteCreate(BaseModel):
    title: str
    content: str

# Create the Table
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return{"message": "Notes API is running"}

@app.post("/Notes")
def create_note(note: NoteCreate):
    db=SessionLocal()
    new_note=Note(title=note.title, content=note.content)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    db.close()
    return new_note

@app.get("/notes")
def get_notes():
    db=SessionLocal()
    stmt=select(Note)
    result =db.execute(stmt)
    notes=result.scalars().all()
    db.close()
    response=[]
    for note in notes:
        response.append({
            "id":note.id,
            "title":note.title,
            "content":note.content,

        })
    return response

@app.get("/notes/{id}")
def get_specific_note(id:int):
    db=SessionLocal()
    notes=db.get(Note,id)
    db.close()
    return{
        "id":notes.id,
        "title": notes.title,
        "content":notes.content
    }

@app.delete("/notes/{id}")
def delete_specific_note(id:int):
    db=SessionLocal()
    stmt=delete(Note).where(Note.id== id)
    db.execute(stmt)
    db.commit()
    db.close()
    return{
    "message": "Note deleted successfully"
}
@app.put("/notes/{id}")
def update_note(id:int,u_title:str,u_content:str):
    db=SessionLocal()
    u_note=db.get(Note,id)
    if u_note:
        u_note.title = u_title
        u_note.content = u_content
    db.commit()
    db.close()
    return{
        "id": id,
        "title": u_title,
        "content": u_content
    }
