from db import session_scope
from models import Account


def seed_accounts(engine):
    with session_scope(engine) as session:
        session.add(Account(name="Chase Checking 7526"))
