if __name__ == "__main__":
    import sys

    sys.path.append("/Users/mike.barrameda/Projects/mfadvisor/mfadvisor-api")

    from db import local_engine
    from db.base import Base

    from models import Account, Category, Transaction, TransactionType

    from scripts.seed_categories import seed_categories
    from scripts.seed_transaction_types import seed_transaction_types
    from scripts.seed_accounts import seed_accounts
    from scripts.seed_chase_checking import seed_chase_checking

    engine = local_engine()
    engine.execute("DROP TABLE IF EXISTS transactions;")
    engine.execute("DROP TABLE IF EXISTS categories;")
    engine.execute("DROP TABLE IF EXISTS transaction_types;")
    engine.execute("DROP TABLE IF EXISTS accounts;")

    Base.metadata.create_all(engine)

    seed_categories(engine)
    seed_transaction_types(engine)
    seed_accounts(engine)
    seed_chase_checking(engine)
