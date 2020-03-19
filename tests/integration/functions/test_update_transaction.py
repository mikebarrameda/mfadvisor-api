from db import create_session
from models import Transaction
from functions.update_transaction import update_transaction


def test_update_transaction(engine, dummy_transaction_id):

    # test both parameters passed
    update_transaction(
        engine, dummy_transaction_id, category_id=2, description="Test New Description"
    )

    session = create_session(engine)
    transaction = (
        session.query(Transaction)
        .filter(Transaction.id == dummy_transaction_id)
        .one_or_none()
    )
    session.close()

    assert transaction
    assert transaction.category_id == 2
    assert transaction.description == "Test New Description"

    # test category parameter passed only
    update_transaction(engine, dummy_transaction_id, category_id=3)

    session = create_session(engine)
    transaction = (
        session.query(Transaction)
        .filter(Transaction.id == dummy_transaction_id)
        .one_or_none()
    )
    session.close()

    assert transaction
    assert transaction.category_id == 3
    assert transaction.description == "Test New Description"

    # test description parameter passed only
    update_transaction(
        engine, dummy_transaction_id, description="Test New New Description"
    )

    session = create_session(engine)
    transaction = (
        session.query(Transaction)
        .filter(Transaction.id == dummy_transaction_id)
        .one_or_none()
    )
    session.close()

    assert transaction
    assert transaction.category_id == 3
    assert transaction.description == "Test New New Description"

    # test no parameters passed
    update_transaction(engine, dummy_transaction_id)

    session = create_session(engine)
    transaction = (
        session.query(Transaction)
        .filter(Transaction.id == dummy_transaction_id)
        .one_or_none()
    )
    session.close()

    assert transaction
    assert transaction.category_id == 3
    assert transaction.description == "Test New New Description"
