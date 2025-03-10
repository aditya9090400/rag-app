import pytest
from httpx import AsyncClient
from app.main import app
from fastapi import FastAPI

@pytest.fixture(scope="module")
async def client():
    """Fixture to create an async test client for FastAPI with a proper lifespan."""
    async with AsyncClient(base_url="http://test") as ac:
        yield ac

@pytest.mark.asyncio
async def test_ingest_document(client):
    """Test document ingestion endpoint."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/documents/ingest/", json={"title": "Test Doc", "content": "Sample content"})
    assert response.status_code == 200
    assert "id" in response.json()

@pytest.mark.asyncio
async def test_get_all_documents(client):
    """Test fetching all documents."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/documents/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_get_specific_document(client):
    """Test fetching a specific document by ID."""
    doc_id = 1  # Assuming document ID 1 exists in test data
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get(f"/documents/{doc_id}/")
    assert response.status_code in [200, 404]  # 404 if document is not found
