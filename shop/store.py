from flask import Blueprint, render_template, jsonify
from shop.db import categories, goods_of_store1

bp = Blueprint("store", __name__)


@bp.route("/")
def index():
    return render_template('main_page.html', categories_key=list(categories.keys()),
                           categories=categories,
                           Goods=goods_of_store1)


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
