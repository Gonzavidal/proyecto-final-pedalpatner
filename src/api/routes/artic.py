from flask import Blueprint, request, jsonify, render_template
from api.models import db, User,Rol,Taller,Pago_Taller,Tipo
from flask_jwt_extended import JWTManager,get_jwt_identity,create_access_token,jwt_required
from werkzeug.security import generate_password_hash,check_password_hash

bpArticulo = Blueprint('bpArticulo', __name__)

@bpArticulo.route('/register_articulo', methods=['POST'])
def post_registarticulo():
    bass