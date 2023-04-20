import datetime
from flask import Blueprint, request, jsonify, render_template
#from models import db, User,Rol,Taller,Articulo,Taller_Articulo,Tipo,Comunicacion
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash, generate_password_hash

bpAuth = Blueprint('bpAuth', __name__)

@bpAuth.route('/register_mecanico', methods=['POST'])
def post_registermecanico():
    try:
        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')
        direccion = request.json.get('direccion')
        tallernom = request.json.get('tallernom')
        regiontall = request.json.get('regiontall')
        direcciontall = request.json.get('direcciontall')
        tipospago = request.json.get('tipospago')
        articulonom = request.json.get('articulonom')
        precio = request.json.get('precio')
        promocion = request.json.get('promocion')
        precio_oferta = request.json.get('precio_oferta')


        if not email: return jsonify({"status": "failed", "code": 400, "msg": "email is required"}), 400
        if not password: return jsonify({"status": "failed", "code": 400, "msg": "Password is required"}), 400

        user = User.query.filter_by(email=email).first()
        if user:
                return jsonify({"msg": "usuario ya se encuentra registrado"})

        user = User()
        user.username = username
        user.email = email
        user.password = password
        user.direccion = direccion

        taller = Taller()
        taller.tallernom = tallernom
        taller.regiontall = regiontall
        taller.direcciontall = direcciontall
        taller.tipospago = tipospago

        articulo = Articulo()
        articulo.articulonom = articulonom
        articulo.precio = precio
        articulo.promocion = promocion
        articulo.precio_oferta = precio_oferta

        return jsonify({"msg":"Mecanico registrado con exito!"})
    except Exception as e:
        print(e)

    return jsonify({"msg":"Falla en el registro de Usuario"})