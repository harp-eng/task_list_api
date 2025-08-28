from fastapi import Request
from app.database import SessionLocal

async def get_context(request: Request):
    db = SessionLocal()
    try:
        return {"db": db, "request": request}
    finally:
        db.close() 
