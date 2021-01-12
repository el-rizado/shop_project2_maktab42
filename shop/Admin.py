import functools
from flask import Blueprint, current_app, flash, g, redirect, render_template, request, session, url_for
from shop.db import Categories, Products, Orders, Stores
from shop.db import get_db

# from werkzeug.security import check_password_hash
# from werkzeug.security import generate_password_hash

my_products = Products()
my_categories = Categories()
my_orders = Orders()
my_stores = Stores()


bp = Blueprint("Admin", __name__, url_prefix="/Admin")


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("Admin.login"))

        return view(**kwargs)

    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        db = get_db()
        g.user = db['amir']
        # with db:
        #     with db.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as curs:
        #         curs.execute("SELECT * FROM \"user\" WHERE id = %s", (user_id,))
        #         g.user = curs.fetchone()


# @bp.route("/register", methods=("GET", "POST"))
# def register():
#     """Register a new user.
#
#     Validates that the username is not already taken. Hashes the
#     password for security.
#     """
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]
#         db = get_db()
#         error = None
#
#         if not username:
#             error = "Username is required."
#         elif not password:
#             error = "Password is required."
#         else:
#             with db:
#                 with db.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as curs:
#                     curs.execute("SELECT id FROM \"user\" WHERE username = %s", (username,))
#                     user = curs.fetchone()
#                     if user is not None:
#                         error = f"User {username} is already registered."
#
#         if error is None:
#             # the name is available, store it in the database and go to
#             # the login page
#             with db:
#                 with db.cursor() as curs:
#                     curs.execute(
#                         "INSERT INTO \"user\" (username, password) VALUES (%s, %s)",
#                         (username, generate_password_hash(password)),
#                     )
#             return redirect(url_for("auth.login"))
#
#         flash(error)
#
#     return render_template("auth/register.html")


@bp.route("/login", methods=["GET", "POST"])
def login():
    """Log in a registered user by adding the user id to the session."""
    print(request)
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()

        error = None
        # with db:
        #     with db.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as curs:
        #         curs.execute(
        #             "SELECT * FROM \"user\" WHERE username = %s", (username,)
        #         )
        #         user = curs.fetchone()

        # if user is None:
        #     error = "Incorrect username."
        # elif not check_password_hash(user["password"], password):
        #     error = "Incorrect password."
        try:
            if db[username] != password:
                error = 'incorrect password'
                current_app.logger.info("incorrect password")
        except KeyError:
            error = "incorrect username"

        if error is None:
            # store the user id in a new session and return to the index
            session.clear()
            # session["user_id"] = user["id"]
            session["user_id"] = db['id']
            print(session)
            current_app.logger.info(session)
            current_app.logger.info("redirect to hello func")
            return redirect(url_for("Admin.management"))
        flash(error)

    else:
        current_app.logger.info("rendering login template")
        return render_template("login.html")


# @bp.route("/logout")
# def logout():
#     """Clear the current session, including the stored user id."""
#     session.clear()
#     return redirect(url_for("index"))


@bp.route("/warehouses")
@login_required
def warehouses():
    return render_template('./management/warehouses.html', my_list=my_stores.ware_list())


@bp.route("/products")
@login_required
def products():
    return render_template('./management/products.html', my_list=my_products.get_all())


@bp.route("/quantities")
@login_required
def quantities():
    return render_template('./management/quantities.html', my_list=my_stores.ware_quantity())


@bp.route("/orders")
@login_required
def orders():
    return render_template('./management/orders.html')



@bp.route("/")
@login_required
def management():
    return render_template('./management/base.html')
