from sqlalchemy import create_engine


def local_engine():
    return create_engine("postgresql://postgres:password@localhost:5432/mfadvisor")
