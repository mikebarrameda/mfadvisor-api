from functions.get_transactions import get_transactions


def test_get_all_transactions(engine, dummy_transaction_id):
    transactions = get_transactions(engine)

    assert dummy_transaction_id in [transaction.id for transaction in transactions]


def test_get_transactions_by_month(engine):
    assert 1


def test_get_transactions_by_account(engine):
    assert 1

