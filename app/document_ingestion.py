from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models import Document
from sklearn.feature_extraction.text import TfidfVectorizer
import json

router = APIRouter(prefix="/documents", tags=["Documents"])

vectorizer = TfidfVectorizer()

@router.post("/ingest/")
async def ingest_document(title: str, content: str, db: AsyncSession = Depends(get_db)):
    # Generate TF-IDF embeddings
    embeddings = vectorizer.fit_transform([content]).toarray().tolist()[0]
    
    doc = Document(title=title, content=content, embeddings=json.dumps(embeddings))
    db.add(doc)
    await db.commit()
    return {"message": "Document ingested successfully", "id": doc.id}
