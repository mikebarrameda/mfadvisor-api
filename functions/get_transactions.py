from db import session_scope
from models import Transaction


def get_transactions(engine):
    with session_scope(engine) as session:
        transactions = session.query(Transaction).all()
        session.expunge_all()

    return transactions
