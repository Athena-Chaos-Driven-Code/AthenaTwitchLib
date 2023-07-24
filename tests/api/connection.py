# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest
import tracemalloc

# Athena Packages

# Local Imports
from tests._connection import connection

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class TestApiReference(unittest.IsolatedAsyncioTestCase):
    # ------------------------------------------------------------------------------------------------------------------
    # - Tests -
    # ------------------------------------------------------------------------------------------------------------------
    async def test_validate_token(self):
        tracemalloc.start()
        async with connection() as api_connection:
            data = await api_connection.validate_token()
            print(data)
