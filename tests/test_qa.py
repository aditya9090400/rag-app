import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_qa_response():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/qa/", json={"question": "What is the document about?"})
    assert response.status_code == 200
    assert "answer" in response.json()
