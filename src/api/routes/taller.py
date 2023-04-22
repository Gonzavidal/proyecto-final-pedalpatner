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
        users_id = request.json.get('users_id')

        if not tallernom: return jsonify({"status": "failed", "code": 400, "msg": "Taller is required"}), 400
        if not regiontall: return jsonify({"status": "failed", "code": 400, "msg": "Region is required"}), 400
        if not direcciontall: return jsonify({"status": "failed", "code": 400, "msg": "Direccion is required"}), 400
        if not users_id: return jsonify({"status": "failed", "code": 400, "msg": "usuario is required"}), 400

        #taller = Taller.query.filter(Taller.tallernom==tallernom).all()
        taller = Taller.query.filter_by(tallernom=tallernom).first()
        if taller:
                return jsonify({"msg": "Taller ya se encuentra registrado"}),400
        
        taller = Taller()
        taller.tallernom = tallernom
        taller.regiontall = regiontall
        taller.direcciontall = direcciontall
        taller.users_id = users_id
        
        taller.save() 
      #  print("esto trae taller",talleres.serialize_taller())
    
        data ={
            "taller": taller.serialize_taller()
        }
      
        return jsonify({"msg":"Taller registrado con exito!"}), 200
    except Exception as e:
        print("falla reg Taller",e)

    return jsonify({"msg":"Falla en el registro de Taller"}), 400

@bpTaller.route('/register_pagotaller',methods=['POST'])
def post_registropagotaller():
    try:
        pago_id = request.json.get('pago_id')
        taller_id =request.json.get('taller_id')
        
        pagotall = Pago_Taller()
        pagotall.pago_id = pago_id
        pagotall.taller_id = taller_id
        pagotall.save()

        data ={
            "pago": pagotall.serialize_pago()
        }
        return jsonify({"msg":"Exito con registro de pago taller","dato":data}),200
    except Exception as e:
        print("fallo en pago taller",e)
    return jsonify({"msg":"Fallo al registrar tipo de pago taller"}),400
