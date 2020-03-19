from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker


def create_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()


@contextmanager
def session_scope(engine):
    """Provide a transactional scope around a series of operations."""
    session = create_session(engine)
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
