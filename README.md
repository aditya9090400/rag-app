# RAG-Based Q&A System

## Overview
This project implements a **Retrieval-Augmented Generation (RAG) system** for Q&A. It provides a **FastAPI-based backend** for document ingestion, retrieval, and query answering.

## Features
- **Document Ingestion API**: Accepts and stores documents.
- **Document Retrieval API**: Fetches documents based on user queries.
- **Q&A API**: Uses retrieval algorithms (TF-IDF/BM25) to find relevant documents and generate answers.
- **Document Selection API**: Allows users to specify which documents to consider in Q&A.
- **PostgreSQL Database**: Stores documents and embeddings.
- **Asynchronous Processing**: Ensures efficient API handling.
- **Support for Multiple LLMs**: Uses LangChain, LlamaIndex, OpenAI API, or Hugging Face models.

## Technologies Used
- **Python** (FastAPI, SQLAlchemy, Asyncio)
- **PostgreSQL** (for document and embedding storage)
- **Retrieval Algorithms** (TF-IDF, BM25, Scikit-learn)
- **Vector Storage** (Optional, PostgreSQL or FAISS)
- **LLM Integration** (Ollama Llama 3.1, LangChain, OpenAI API, Hugging Face Transformers)

## Setup Instructions
### 1. Clone the Repository
```sh
git clone <repo-url>
cd <project-folder>
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

### 3. Set Up PostgreSQL Database
Update `DATABASE_URL` in `database.py`:
```python
DATABASE_URL = "postgresql+asyncpg://user:password@localhost/db_name"
```
Replace `user`, `password`, and `db_name` accordingly.

### 4. Start FastAPI Server
```sh
uvicorn app.main:app --reload
```

## API Endpoints

### Document Ingestion
- **POST /documents/ingest/**  
  **Body:**
  ```json
  { "title": "Sample Document", "content": "This is a test document." }
  ```

- **GET /documents/**  
  **Response:**
  ```json
  [ { "id": 1, "title": "Sample Document" } ]
  ```

- **GET /documents/{doc_id}/**  
  **Response:**
  ```json
  { "id": 1, "title": "Sample Document", "content": "This is a test document." }
  ```

### Document Selection
- **POST /selection/select/**  
  **Body:**
  ```json
  { "doc_ids": [1] }
  ```

- **GET /selection/selected/**  
  **Response:**
  ```json
  [ { "id": 1, "title": "Sample Document" } ]
  ```

### Q&A
- **POST /qa/**  
  **Body:**
  ```json
  { "question": "What is the document about?" }
  ```
  **Response:**
  ```json
  { "question": "What is the document about?", "answer": "This is a test document." }
  ```

## Testing with Postman
1. Start FastAPI server.
2. Use the API endpoints as listed above.
3. Validate responses for document ingestion, selection, and Q&A.

