from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models import Document, UserQuery
from app.rag_pipeline import generate_answer

router = APIRouter(prefix="/qa", tags=["Q&A"])

@router.post("/")
async def qa_endpoint(question: str, db: AsyncSession = Depends(get_db)):
    docs = await db.execute("SELECT title, content FROM documents")
    docs = [{"title": row[0], "content": row[1]} for row in docs.fetchall()]
    
    answer = await generate_answer(question, docs)
    return {"question": question, "answer": answer}
