from pydantic import BaseModel
from datetime import datetime

class NoteBase(BaseModel):
    title: str
    content: str | None = None

class NoteCreate(NoteBase):
    pass

class NoteUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    completed: bool | None = None

class NoteOut(NoteBase):
    id: int
    completed: bool
    created_at: datetime

    class Config:
        from_attributes = True
