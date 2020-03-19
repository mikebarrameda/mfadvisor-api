import pytest
from sqlalchemy import create_engine

from db.base import Base
from db import session_scope, local_engine
from models import Account, Category, Transaction, TransactionType


@pytest.fixture()
def engine():
    engine = local_engine()

    engine.execute("DROP TABLE IF EXISTS transactions;")
    engine.execute("DROP TABLE IF EXISTS categories;")
    engine.execute("DROP TABLE IF EXISTS transaction_types;")
    engine.execute("DROP TABLE IF EXISTS accounts;")
    Base.metadata.create_all(engine)

    with session_scope(engine) as session:

        # See Transaction Types
        session.add_all([TransactionType(name="Debit"), TransactionType(name="Credit")])

        # Seed Categories
        session.add_all(
            [
                Category(name="Uncategorized"),
                Category(name="Travel"),
                Category(name="Going Out"),
                Category(name="Utilities"),
                Category(name="Rent"),
                Category(name="Paycheck"),
            ]
        )

        # Seed Account
        session.add(Account(name="Chase Checking 7526"))

    yield engine
