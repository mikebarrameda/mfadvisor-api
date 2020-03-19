import re

from loaders.base_loader import BaseLoader
from models import Transaction


class ChaseCheckingLoader(BaseLoader):
    def load_file(self, _file):
        result = []
        _file.readline()

        line = _file.readline()
        while line:

            # strip comma in desription
            match = re.match('.*".*(,).*".*', line)
            if match and match.groups():
                line = line[: match.start(1)] + line[match.start(1) + 1 :]

            line_items = line.split(",")

            txn_type = 1
            if line_items[0] == "CREDIT":
                txn_type = 2

            result.append(
                Transaction(
                    date=line_items[1],
                    description=line_items[2],
                    amount=line_items[3],
                    transaction_type_id=txn_type,
                    category_id=1,
                    account_id=1,
                )
            )
            line = _file.readline()

        return result
