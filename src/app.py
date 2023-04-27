"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
import uuid
from flask import Flask, request, jsonify, url_for, send_from_directory
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from flask_jwt_extended import JWTManager,get_jwt_identity,create_access_token,jwt_required
from werkzeug.security import generate_password_hash,check_password_hash
from api.utils import APIException, generate_sitemap
from api.models import db
#from api.routes import api
from api.admin import setup_admin
from api.commands import setup_commands
from api.routes.regis import bpRegis
from api.routes.main import bpMain
from api.routes.taller import bpTaller
from api.routes.artic import bpArticulo
from api.routes.comunic import bpComunicacion
from api.routes.auth import bpAuth 


# from models import Person

ENV = os.getenv("FLASK_ENV")
static_file_dir = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), '../public/')
app = Flask(__name__)
app.url_map.strict_slashes = False

# database condiguration
db_url = os.getenv("DATABASE_URL")
#app.config['SQLALCHEMY_DATABASE_URI']= db_url
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace(
        "postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db, compare_type=True)
app.config["JWT_SECRET_KEY"] = "JWT_SECRET_KEY"
app.config["JWT_ALGORITHM"] = "HS256"
db.init_app(app)

jwt = JWTManager(app)
# Allow CORS requests to this API
CORS(app)

# add the admin
# setup_admin(app)

# add the admin
# setup_commands(app)

# Add all endpoints form the API with a "api" prefix
#app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(bpMain)
app.register_blueprint(bpRegis, url_prefix='/api')
app.register_blueprint(bpTaller, url_prefix='/api')
app.register_blueprint(bpArticulo, url_prefix='/api')
app.register_blueprint(bpComunicacion, url_prefix='/api')
app.register_blueprint(bpAuth, url_prefix='/api')

# Handle/serialize errors like a JSON object

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints


#@app.route('/')
#def sitemap():
#    if ENV == "development":
#        return generate_sitemap(app)
#    return send_from_directory(static_file_dir, 'index.html')

# any other endpoint will try to serve it like a static file


#@app.route('/<path:path>', methods=['GET'])
#def serve_any_other_file(path):
#    if not os.path.isfile(os.path.join(static_file_dir, path)):
#        path = 'index.html'
#    response = send_from_directory(static_file_dir, path)
#    response.cache_control.max_age = 0  # avoid cache memory
#    return response


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3001))
    app.run(host='0.0.0.0', port=PORT, debug=True)

stores = []
items = []

@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}

@app.post("/store")
def create_store():
    store_data = request.data_json()
    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store
    return store, 201

@app.post("/item")
def create_item():
    item_data = request.data_json()
    if item_data["store_id"] not in stores:
        return {"message": "Store not found"}, 404

    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item
    
    return item, 201

@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}

@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return store[stodes_id]
    except KeyError:
        return {"message": "Store not found"}, 404

@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        return {"message": "Item not found"}, 404

