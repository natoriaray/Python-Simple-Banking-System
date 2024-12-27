from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

blp = Blueprint("transactions", __name__, description="Operation on transactions")

@blp.route("/account/<int:account_id>/transaction")
class AccountTransactions(MethodView):
    def get(self, account_id):
        #get all transactions from a specific account
        pass

    def post(self, account_data, account_id):
        #depending on the type of transaction will post to the specific account
        pass

@blp.route("/transaction/<int:transaction_id>")
class Transaction(MethodView):
    def get(self, transaction_id):
        pass