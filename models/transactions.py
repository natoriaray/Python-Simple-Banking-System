from db import db

class TransactionModel(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80), unique=False, nullable=False)
    amount = db.Column(db.Float(precision=2), unique=False, nullable=False)
    submitter_id = db.Column(db.Integer, db.ForeignKey("accounts.id"), unique=False, nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey("accounts.id"), unique=False, nullable=False)
    submitter = db.relationship("AccountModel", foreign_keys=[submitter_id], back_populates="submitted_transactions")
    recipient = db.relationship("AccountModel", foreign_keys=[recipient_id], back_populates="received_transactions")