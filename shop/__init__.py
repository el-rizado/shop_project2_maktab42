
from logging.config import dictConfig
from flask import Flask, render_template
from shop.db import p_list, s_list, categories, goods_of_store1
from shop.auth import login_required


dictConfig({
    'version': 1,
    'formatters': {'default': {
    'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
    'class': 'logging.StreamHandler',
    'stream': 'ext://flask.logging.wsgi_errors_stream',
    'formatter': 'default'
    }},
    'root': {
    'level': 'INFO',
    'handlers': ['wsgi']
    }
    })



def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
    # a default secret that should be overridden by instance config
    SECRET_KEY="dev",
    # store the database in the instance folder
    # DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    # DATABASE={"name": "flaskr",
    #           "username": "postgres",
    #           "password": "postgres"},
    )

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile("config.py", silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.update(test_config)

    # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass


    @app.route('/hello')
    def hello():
        return 'Hello World!'


    @app.route('/login')
    def login():
        return render_template('./login.html')


    @app.route('/itemID')
    def itemID():
        return render_template('./product_page.html', item=goods_of_store1[0])
    
    my_order=[
        [100000,
        4,
        25000,
        'something'],
        [9000,
        1,
        9000,
        'nothing']
    ]

    total = sum((item[0] for item in my_order))

    @app.route('/purchase')
    def purchase():
        return render_template('./purchase.html', order=my_order, total=total)
    
    
    @app.route('/fin_pur')
    def fin_pur():
        return render_template('./fin_pur.html')



    @app.route("/product")
    @login_required
    def product():
        return render_template('./management/products.html',list=p_list)


    @app.route("/store")
    @login_required
    def store():
        return render_template('./management/stores.html',list=s_list)


    @app.route("/inv_pri")
    @login_required
    def inv_pri():
        return render_template('./management/Inventory_price.html')


    @app.route("/order")
    @login_required
    def order():
        return render_template('./management/orders.html')


    @app.route("/index")
    def index():
        return render_template('main_page.html', categories_key=list(categories.keys()),
                                                                categories=categories,
                                                                Goods=goods_of_store1)

    # register the database commands
    # from flaskr import db

    # db.init_app(app)

    # apply the blueprints to the app
    from shop import auth
    #
    app.register_blueprint(auth.bp)
    # app.register_blueprint(blog.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="index")
    return app
