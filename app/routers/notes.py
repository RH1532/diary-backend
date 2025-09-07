from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, db

router = APIRouter(prefix="/notes", tags=["notes"])

def get_db():
    database = db.SessionLocal()
    try:
        yield database
    finally:
        database.close()

@router.post("/", response_model=schemas.NoteOut)
def create_note(note: schemas.NoteCreate, database: Session = Depends(get_db)):
    return crud.create_note(database, note)

@router.get("/{note_id}", response_model=schemas.NoteOut)
def read_note(note_id: int, database: Session = Depends(get_db)):
    note = crud.get_note(database, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.get("/", response_model=list[schemas.NoteOut])
def list_notes(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    return crud.get_notes(database, skip, limit)

@router.patch("/{note_id}", response_model=schemas.NoteOut)
def update_note(note_id: int, note: schemas.NoteUpdate, database: Session = Depends(get_db)):
    db_note = crud.update_note(database, note_id, note)
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

@router.post("/{note_id}/complete", response_model=schemas.NoteOut)
def complete_note(note_id: int, database: Session = Depends(get_db)):
    db_note = crud.complete_note(database, note_id)
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

@router.delete("/{note_id}")
def delete_note(note_id: int, database: Session = Depends(get_db)):
    db_note = crud.delete_note(database, note_id)
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"ok": True}
