from sqlalchemy.orm import Session
from . import models, schemas

def get_note(db: Session, note_id: int):
    return db.query(models.Note).filter(models.Note.id == note_id).first()

def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Note).offset(skip).limit(limit).all()

def create_note(db: Session, note: schemas.NoteCreate):
    db_note = models.Note(**note.dict())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def update_note(db: Session, note_id: int, note: schemas.NoteUpdate):
    db_note = get_note(db, note_id)
    if not db_note:
        return None
    for field, value in note.dict(exclude_unset=True).items():
        setattr(db_note, field, value)
    db.commit()
    db.refresh(db_note)
    return db_note

def delete_note(db: Session, note_id: int):
    db_note = get_note(db, note_id)
    if not db_note:
        return None
    db.delete(db_note)
    db.commit()
    return db_note

def complete_note(db: Session, note_id: int):
    db_note = get_note(db, note_id)
    if not db_note:
        return None
    db_note.completed = True
    db.commit()
    db.refresh(db_note)
    return db_note
