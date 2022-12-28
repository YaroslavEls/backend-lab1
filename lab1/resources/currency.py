from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required

from sqlalchemy.exc import IntegrityError

from lab1.db import db
from lab1.schemas import CurrencySchema
from lab1.models.currency import CurrencyModel


blp = Blueprint('currency', __name__, description='Operations on currencies')

@blp.route('/currency')
class Currency(MethodView):
    @blp.arguments(CurrencySchema)
    @blp.response(200, CurrencySchema)
    def post(self, req_data):
        currency = CurrencyModel(**req_data)
        try:
            db.session.add(currency)
            db.session.commit()
        except IntegrityError:
            abort(400, message='Error while creating new currency')
        return currency

    @jwt_required()
    @blp.response(200, CurrencySchema(many=True))
    def get(self):
        return CurrencyModel.query.all()