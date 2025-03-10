import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_select_documents():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/selection/select/", json={"doc_ids": [1]})
    assert response.status_code in [200, 404]

@pytest.mark.asyncio
async def test_get_selected_documents():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/selection/selected/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
