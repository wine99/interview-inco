from flask import Flask, render_template, request, jsonify
from interview_inco.contorl import plan
from interview_inco.db import init_app as init_db, get_db

app = Flask(__name__)
app.config.from_pyfile("./config.py")
init_db(app)

turbines = None


@app.route("/turbines")
def get_turbines():
    global turbines
    if turbines is None:
        turbines = get_db().execute("SELECT id, capacity, cost FROM turbine").fetchall()
    return turbines


@app.route("/target")
def get_target_production_str() -> str:
    return str(get_target_production())

def get_target_production():
    return get_db().execute("SELECT production FROM target_production").fetchone()[0]


@app.route("/price")
def get_price_str():
    return str(get_price())

def get_price():
    return get_db().execute("SELECT price FROM price").fetchone()[0]


@app.route("/plan")
def get_plan():
    turbines = get_turbines()
    target = get_target_production()
    price = get_price()
    return jsonify(plan(turbines, target, price))


@app.route("/")
def index():
    return render_template(
        "index.html",
        turbines=get_turbines(),
    )


@app.route("/inc-target", methods=["POST"])
def inc_target():
    try:
        inc = float(request.get_json()["increase"])
    except:
        return jsonify({"message": "Wrong format."}), 400

    target = get_target_production() + inc
    turbines = get_turbines()
    if target > sum(list(map(lambda p: p[1], turbines))):
        return jsonify({"message": "Target should not exceed maximum production."}), 400

    get_db().execute("UPDATE target_production SET production = ? where id = 1", (target,))
    get_db().commit()
    return plan(turbines, target, get_price())


@app.route("/dec-target", methods=["POST"])
def dec_target():
    try:
        dec = float(request.get_json()["decrease"])
    except:
        return jsonify({"message": "Wrong format."}), 400

    target = get_target_production() - dec
    turbines = get_turbines()
    if target <= 0:
        return jsonify({"message": "Target should be greater than 0."}), 400

    get_db().execute(
        "UPDATE target_production SET production = ? where id = 1", (target,)
    )
    get_db().commit()
    return plan(turbines, target, get_price())


@app.route("/set-price", methods=["POST"])
def set_price():
    try:
        price = float(request.get_json()["price"])
    except:
        return jsonify({"message": "Wrong format."}), 400

    if price <= 0:
        return jsonify({"message": "Price should be greater than 0."}), 400

    get_db().execute("UPDATE price SET price = ? where id = 1", (price,))
    get_db().commit()
    return plan(get_turbines(), get_target_production(), price)
