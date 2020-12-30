from bson import json_util
from flask import Blueprint, render_template, jsonify
from shop.db import categories, goods_of_store1
import json
bp = Blueprint("store", __name__)

def parse_json(data):
    return json.loads(json_util.dumps(data))

@bp.route("/")
def index():
    return render_template('main_page.html', categories_key=list(categories.keys()),
                           categories=categories,
                           Goods=parse_json(goods_of_store1))


@bp.route('/category', methods=['GET'])
def category():
    return jsonify(categories)


@bp.route('/product/goods', methods=['GET'])
def myproduct():
    return jsonify(goods_of_store1)


@bp.route('/cart', methods=['GET'])
def cart():
    return jsonify(goods_of_store1)


@bp.route('/cart/approve', methods=['GET'])
def approve():
    return jsonify(goods_of_store1)
