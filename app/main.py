from fastapi import FastAPI
from app.routes import document, qa, selection

app = FastAPI(title="RAG Q&A System")

app.include_router(document.router)
app.include_router(qa.router)
app.include_router(selection.router)

@app.get("/")
async def root():
    return {"message": "RAG Q&A System is running"}
