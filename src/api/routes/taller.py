import datetime
from flask import Blueprint, request, jsonify, render_template
from api.models import db,Taller,TallerArticulo,Pago,PagoTaller,UserTaller
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash, generate_password_hash

bpTaller = Blueprint('bpTaller', __name__)

# Gestion PAGO CRUD
# registrar pago  SE PUEDE INICIAR INTEGRACION CON FROND (3)
@bpTaller.route('/register_pago',methods=['POST'])
#@jwt_required
def post_registropago():
    try:
        #id = get_jwt_identity()
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

# leer pago  SE PUEDE INICIAR INTEGRACION CON FROND  (3)
@bpTaller.route('/getpago',methods=['GET'])
#@jwt_required
def getpago():
    try:
        pagos = Pago.query.all()
     
        pagos = list(map(lambda pago:pago.serialize_pago(), pagos))
    
        return jsonify({"Datos de pagos":pagos}), 200
    except Exception as e:
        print(e)
        return jsonify({"msg": "No existe aun ningun usuario"})

# modificar pago  SE PUEDE INICIAR INTEGRACION CON FROND (3)
@bpTaller.route('/updatepago/<int:id>', methods=['PUT'])
def updatepago(id):
    try:
        tipopago = request.json.get('tipopago')  # None
        
        pago = Pago.query.get(id)
        pago.tipopago = tipopago
        
        pago.update()

        data={
            "resultado":pago.serialize_pago()
        }
      
        return jsonify({"datos modificados":data}), 202
    except Exception as e:
        print("falla en update",e)
        return jsonify({"No se logro actualizar el cambio"}), 400

# borrar pago SE PUEDE INICIAR INTEGRACION CON FROND  (3)
@bpTaller.route('/deletepago/<int:id>', methods=['DELETE'])
def deletepago(id):
    try:
        pago = Pago.query.get(id)

        pago.delete()
            
        return jsonify({"message": "User Deleted"}), 202
    except Exception as e:
        return jsonify({"message": "No se logro eliminar a usuario"}), 400

#----------------------------------------------------------------------------------------------------------
# gestion CRUD Taller registrsr taller SE PUEDE INICIAR INTEGRACION CON FROND  (6)
@bpTaller.route('/register_taller', methods=['POST'])
#@jwt_required
def post_registrotaller():
    try:
        #id = get_jwt_identity()
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
      
        return jsonify({"msg":"Taller registrado con exito!","taller":data}), 200
    except Exception as e:
        print("falla reg Taller",e)

    return jsonify({"msg":"Falla en el registro de Taller"}), 400

# gestion leer taller SE PUEDE INICIAR INTEGRACION CON FROND  (6)
@bpTaller.route('/gettaller',methods=['GET'])
#@jwt_required
def gettaller():
    try:
        talleres = Taller.query.all()
     
        talleres = list(map(lambda taller:taller.serialize_taller(), talleres))
    
        return jsonify({"Datos de talleres":talleres}), 200
    except Exception as e:
        print("falla en leer talleres",e)
        return jsonify({"msg": "No existe aun ningun Taller registrado"})

# gestion modificar taller SE PUEDE INICIAR INTEGRACION CON FROND  (6)
@bpTaller.route('/updatetaller/<int:id>', methods=['PUT'])
def updatetaller(id):
    try:
        tallernom = request.json.get('tallernom')
        regiontall = request.json.get('regiontall')
        direcciontall = request.json.get('direcciontall')
        users_id = request.json.get('users_id')
        # SELECT * FROM users WHERE id = ?
        taller = Taller.query.get(id)
        taller.tallernom = tallernom
        taller.regiontall = regiontall
        taller.direcciontall = direcciontall
        taller.users_id = users_id
        
        taller.update() 

        data ={
            "taller actualizado": taller.serialize_taller()
        }
      
        return jsonify({"msg":"Taller actualizado con exito!","taller":data}), 200
    except Exception as e:
        print("falla en update",e)
        return jsonify({"No se logro actualizar el cambio"}), 400

# gestion borrar taller SE PUEDE INICIAR INTEGRACION CON FROND  (6)
@bpTaller.route('/delettaller/<int:id>', methods=['DELETE'])
def deletetaller(id):
    try:
        taller = Taller.query.get(id)

        taller.delete()
            
        return jsonify({"message": "Taller Deleted"}), 202
    except Exception as e:
        print("falla eliminacion",e)
        return jsonify({"message": "No se logro eliminar Taller"}), 400

#--------------------------------------------------------------------------------------------------------------------------
# CRUD de PAGO-TALLER
# registrar pago-taller
@bpTaller.route('/register_pagotaller',methods=['POST'])
#@jwt_required
def post_registropagotaller():
    try:
        #id = get_jwt_identity()
        pagos_id = request.json.get('pagos_id')
        talleres_id =request.json.get('talleres_id')
        
        pagotall = PagoTaller()
        pagotall.pagos_id = pagos_id
        pagotall.talleres_id = talleres_id
        pagotall.save()

        data ={
            "pago": pagotall.serialize_pagotaller()
        }
        return jsonify({"msg":"Exito con registro de pago taller","dato":data}),200
    except Exception as e:
        print("fallo en pago taller",e)
    return jsonify({"msg":"Fallo al registrar tipo de pago taller"}),400

@bpTaller.route('/get_pagotaller',methods=['GET'])
#@jwt_required
def getpagotaller():
    try:
        pagotalleres = PagoTaller.query.all()
     
        pagotalleres = list(map(lambda pagotaller:pagotaller.serialize_pagotaller(), pagotalleres))

        return jsonify({"msg":"Exito con registro de pago taller","dato":pagotalleres}),200
    except Exception as e:
        print("fallo en pago taller",e)
    return jsonify({"msg":"Fallo al registrar tipo de pago taller"}),400

#@bpTaller.route('/updatepagotaller/<int:pagos_id>/<int:talleres_id>', methods=['PUT'])
#def updatetaller(pagos_id,talleres_id)#
   # try:
   #     pagos_id = request.json.get('pagos_id')
   #     talleres_id = request.json.get('talleres_id')
#
   #     pagostaller = PagosTaller.query.get(pagos_id)
   #     pagostaller.pagos_id = pagos_id
   #     pagostaller.talleres_id = talleres_id
   #     pagostaller.update()
   # 
   #     return jsonify({"msg":"Exito en actualizacion de pago"}),202
   # except Exception as e:
   #     print("falla en pagotaller",e)
   #     return jsonify({"msg":"Falla en la actualizacion de pagotaller intentarlo mas tarde"}),400

@bpTaller.route('/deletpagotaller/<int:id>', methods=['DELETE'])
def deletepagotaller():
    bass

#-----------------------------------------------------------------------------------------------------
#CRUD de usuario-taller
# registrar usuario-taller
@bpTaller.route('/register_usertaller',methods=['POST'])
#@jwt_required
def post_registrousertaller():
    try:
        #id = get_jwt_identity()
        users_id = request.json.get('users_id')
        talleres_id = request.json.get('talleres_id')
        
        usertaller = UserTaller()
        usertaller.users_id = users_id
        usertaller.talleres_id = talleres_id

        usertaller.save()

        data ={
            "usuario-taller": usertaller.serialize_usertaller()
        }
        return jsonify({"msg":"Exito con registro de taller-usuario","dato":data}),200
    except Exception as e:
        print("falla registro usertaller",e)
    return jsonify({"msg":"Fallo al registrar tipo de usuario-taller"}),400
