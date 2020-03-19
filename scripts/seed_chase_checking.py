import os

TEST_FILE = "assets/Chase6010_Activity_20200318.CSV"


def seed_chase_checking(engine):
    from loaders import ChaseCheckingLoader

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, TEST_FILE)

    loader = ChaseCheckingLoader(filename, engine)
    loader.load()
