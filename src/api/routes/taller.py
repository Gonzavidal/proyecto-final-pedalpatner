import datetime
from flask import Blueprint, request, jsonify, render_template
from api.models import db, User,Taller,Articulo,Taller_Articulo,Rol,Pago
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash, generate_password_hash

bpTaller = Blueprint('bpTaller', __name__)

@bpTaller.route('/register_pago',methods=['POST'])
def post_registropago():
    try:
        tipopago = request.json.get('tipopago')

        pago = Pago()

        pago.tipopago = tipopago
        pago.save()

        data ={
            "pago": pago.serialize_pago()
        }
        return jsonify({"msg":"Exito con registro de pago","dato":data}),200
    except Exception as e:
        print(e)
    return jsonify({"msg":"Fallo al registrar tipo de pago"}),400
    