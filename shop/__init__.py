import os

from flask import Flask, render_template
from shop.db import p_list, s_list

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
    def hell0():
        return 'Hello World!'


    @app.route("/product")
    def product():
        return render_template('./management/products.html',list=p_list)
        
       
    @app.route("/store")
    def store():
        return render_template('./management/stores.html',list=s_list)


    @app.route("/inv_pri")
    def inv_pri():
        return render_template('./management/inventory_price.html')
        
       
    @app.route("/order")
    def order():
        return render_template('./management/orders.html')


    @app.route("/index")
    def index():
        return render_template('main_page.html')

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
