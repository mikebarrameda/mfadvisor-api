from db import session_scope
from models import TransactionType


def seed_transaction_types(engine):
    with session_scope(engine) as session:
        session.add_all([TransactionType(name="Debit"), TransactionType(name="Credit")])
