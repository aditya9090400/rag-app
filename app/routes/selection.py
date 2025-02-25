from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_db
from app.models import Document

router = APIRouter(prefix="/selection", tags=["Document Selection"])

selected_doc_ids = set()  # In-memory store for selected document IDs

@router.post("/select/")
async def select_documents(doc_ids: list[int], db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Document).filter(Document.id.in_(doc_ids)))
    docs = result.scalars().all()
    
    if not docs:
        raise HTTPException(status_code=404, detail="No matching documents found")
    
    selected_doc_ids.update(doc_ids)
    return {"message": "Documents selected successfully", "selected_ids": list(selected_doc_ids)}

@router.get("/selected/")
async def get_selected_documents(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Document).filter(Document.id.in_(selected_doc_ids)))
    documents = result.scalars().all()
    
    return [{"id": doc.id, "title": doc.title} for doc in documents]
