import datetime
from flask import Blueprint, request, jsonify, render_template
from api.models import db,Taller,Articulo,Taller_Articulo,Pago, Pago_Taller
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


@bpTaller.route('/register_taller', methods=['POST'])
def post_registrotaller():
    try:
    
        tallernom = request.json.get('tallernom')
        regiontall = request.json.get('regiontall')
        direcciontall = request.json.get('direcciontall')
        #pagos_id = request.json.get('pagos_id')
        users_id = request.json.get('users_id')

       # articulonom = request.json.get('articulonom')
       # precio = request.json.get('precio')
       # promocion = request.json.get('promocion')
       # precio_oferta = request.json.get('precio_oferta')

        taller = Taller()
        taller.tallernom = tallernom
        taller.regiontall = regiontall
        taller.direcciontall = direcciontall
        #taller.pagos_id = pagos_id
        taller.users_id = users_id
        #user.taller = taller
        taller.save() 

        #articulo = Articulo()
        #articulo.articulonom = articulonom
        #articulo.precio = precio
        #articulo.promocion = promocion
        #articulo.precio_oferta = precio_oferta
        #user.articulo = articulo
        #user.save()
#
        data ={
            "taller": taller.serialize_taller()
        }
      
        return jsonify({"msg":"Taller registrado con exito!","datos":data}), 200
    except Exception as e:
        print("falla reg Taller",e)

    return jsonify({"msg":"Falla en el registro de Taller"}), 400

