from db import db

class TransactionModel(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80), unique=False, nullable=False)
    amount = db.Column(db.Float(precision=2), unique=False, nullable=False)
    recipient = db.Column(db.String(80), unique=False, nullable=True)
    account_id = db.Column(db.Integer, db.ForeignKey("accounts.id"), unique=False, nullable=False)
    account = db.relationship("AccountModel", back_populates="transactions")