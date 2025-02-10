import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import pytest_asyncio
import asyncio
from tortoise import Tortoise

DB_URL = "sqlite://:memory:"

TORTOISE_TEST_CONFIG = {
    "connections": {"default": DB_URL},
    "apps": {
        "models": {
            "models": ["app.models.animal", "app.models.parto", "app.models.user"],
            "default_connection": "default",
        },
    },
}

# Removed the event_loop fixture as it's now handled by pytest-asyncio

@pytest_asyncio.fixture(scope="session")
async def initialize_tests(request):
    """Initialize test database"""
    await Tortoise.init(config=TORTOISE_TEST_CONFIG)
    await Tortoise.generate_schemas()
    yield
    await Tortoise.close_connections()

@pytest_asyncio.fixture(autouse=True)
async def clean_tables(request, initialize_tests):
    """Clean data in tables before each test"""
    if "db" in request.keywords:
        conn = Tortoise.get_connection("default")
        await conn.execute_query('DELETE FROM users')
        await conn.execute_query('DELETE FROM partos')
        await conn.execute_query('DELETE FROM animals')
    yield