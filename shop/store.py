from bson import json_util
from flask import Blueprint, render_template, jsonify, request
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
                           goods_in_cat = {cat: parse_json(my_product.get_by_cat(cat)) for cat in my_categories.get_category()},
                           )


@bp.route('/category', methods=['GET'])
def category():
    cat = request.args.get('cat')
    items = my_product.get_by_cat(cat)
    return render_template('./category_page.html', item=items)


@bp.route('/subcat', methods=['GET'])
def subcat():
    cat = request.args.get('cat')
    items = my_product.get_by_subcat(cat)
    return render_template('./category_page.html', item=items)


@bp.route('/product/goods', methods=['GET'])
def myproduct():
    return jsonify(goods_of_store1)


@bp.route('/cart', methods=['GET'])
def cart():
    return jsonify(goods_of_store1)


@bp.route('/cart/approve', methods=['GET'])
def approve():
    return jsonify(goods_of_store1)



