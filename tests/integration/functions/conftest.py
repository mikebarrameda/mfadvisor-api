import pytest

from db import session_scope
from models import Transaction


@pytest.fixture()
def dummy_transaction_id(engine):
    with session_scope(engine) as session:

        dummy_txn = Transaction(
            date="01/01/2000",
            description="Test Transaction",
            amount="1000.00",
            transaction_type_id=1,
            category_id=1,
        )
        session.add(dummy_txn)
        session.flush()
        result = dummy_txn.id

    yield result
