from db import session_scope


class BaseLoader:
    def __init__(self, filepath, engine):
        self.filepath = filepath
        self.engine = engine

    def load(self):
        transactions = []

        with session_scope(self.engine) as session:
            with open(self.filepath, "r") as _file:
                transactions = self.load_file(_file)
            session.add_all(transactions)

    def load_file(self, _file):
        raise NotImplementedError
