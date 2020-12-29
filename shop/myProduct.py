from flask import Blueprint, jsonify
from shop.db import goods_of_store1

bp = Blueprint("myProduct", __name__, url_prefix="/myProduct")

@bp.route('/api/v1/resources/products/all', methods = ['GET'])
def api_all():

    return jsonify(goods_of_store1)
