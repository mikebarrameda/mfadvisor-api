from models import Transaction
from db import session_scope


def update_transaction(engine, txn_id, category_id=None, description=None):
    with session_scope(engine) as session:

        transaction = session.query(Transaction).filter(Transaction.id == txn_id).one()

        if category_id:
            transaction.category_id = category_id

        if description:
            transaction.description = description
