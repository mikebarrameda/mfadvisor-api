from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship

from db.base import Base


class TransactionType(Base):
    __tablename__ = "transaction_types"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    transactions = relationship("Transaction", back_populates="transaction_type")
