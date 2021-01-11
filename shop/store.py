from bson import json_util
from flask import Blueprint, render_template, jsonify
from shop.db import Categories, Products, Orders, Stores
import json

my_product = Products()
my_categories = Categories()
my_orders = Orders()
my_stores = Stores()


bp = Blueprint("store", __name__)


def parse_json(data):
    return json.loads(json_util.dumps(data))


@bp.route("/")
def index():
    return render_template('main_page.html', categories_key=my_categories.get_category(),
                           categories={cat: my_categories.get_sub_category(cat) for cat in my_categories.get_category()},
                           goods_in_cat = {cat: parse_json(my_product.get_product_by_cat(cat)) for cat in my_categories.get_category()},
                           )


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



