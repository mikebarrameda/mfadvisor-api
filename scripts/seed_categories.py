from db import session_scope
from models import Category


def seed_categories(engine):
    with session_scope(engine) as session:
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
