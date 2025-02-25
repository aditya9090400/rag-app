from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_db
from app.models import Document
from pydantic import BaseModel
import json

class DocumentIngestRequest(BaseModel):
    title: str
    content: str

router = APIRouter(prefix="/documents", tags=["Documents"])

@router.post("/ingest/")
async def ingest_document(request: DocumentIngestRequest, db: AsyncSession = Depends(get_db)):
    doc = Document(title=request.title, content=request.content, embeddings=None)  # Embeddings handled later
    db.add(doc)
    await db.commit()
    return {"message": "Document ingested successfully", "id": doc.id}

@router.get("/")
async def get_all_documents(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Document))
    documents = result.scalars().all()
    return [{"id": doc.id, "title": doc.title} for doc in documents]

@router.get("/{doc_id}/")
async def get_document(doc_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Document).filter(Document.id == doc_id))
    doc = result.scalar_one_or_none()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return {"id": doc.id, "title": doc.title, "content": doc.content}
