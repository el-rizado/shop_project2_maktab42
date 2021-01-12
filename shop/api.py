
import json
from bson import json_util, ObjectId
from flask import Blueprint, jsonify, request, redirect, render_template
from shop.db import Categories, Products, Orders, Stores


my_product = Products()
my_categories = Categories()
my_orders = Orders()
my_stores = Stores()

bp = Blueprint("api", __name__, url_prefix="/api")


def parse_json(data):
    return json.loads(json_util.dumps(data))


@bp.route('/product/list', methods=['GET'])
def prod_list():
    return jsonify(parse_json(goods_of_store1))


@bp.route('/product/', methods=['GET'])
def prod_details():
    query_parameters = request.args
    id = query_parameters.get('id')
    return render_template('./product_page.html', item=my_product.get_by_id(ObjectId(id)))

#   return redirect('./product_page.html')
#	return redirect(url_for('api/product', email=x, listOfObjects=y))

@bp.route('/product/add', methods=['GET'])
def prod_add():
    return "prod_add"


@bp.route('/product/edit', methods=['GET'])
def prod_edit():
    return 'prod_edit'


@bp.route('/product/delete/', methods=['GET'])
def prod_delete():
    return 'prod_delete'


@bp.route('/product/upload', methods=['GET'])
def prod_upload():
    return 'prod_upload'


@bp.route('/warehouse/list', methods=['GET'])
def ware_list():
    return 'ware_list'


@bp.route('/warehouse/add/', methods=['GET'])
def ware_add():
    return 'ware_add'


@bp.route('/warehouse/edit', methods=['GET'])
def ware_edit():
    return 'ware_edit'


@bp.route('/warehouse/delete/', methods=['GET'])
def ware_delete():
    return 'ware_delete'


@bp.route('/quantity/list', methods=['GET'])
def quantity_list():
    return 'quantity_list'


@bp.route('/warehouse/add', methods=['GET'])
def quantity_add():
    return 'quantity_add'


@bp.route('/warehouse/edit', methods=['GET'])
def quantity_edit():
    return 'quantity_edit '


@bp.route('/warehouse/delete/', methods=['GET'])
def quantity_delete():
    return 'quantity_delete'


@bp.route('/order/list', methods=['GET'])
def order_list():
    return 'order_list'


@bp.route('/order/', methods=['GET'])
def order_details():
    return 'order_details'
