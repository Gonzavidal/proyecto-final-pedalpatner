from flask import Blueprint, request, jsonify, render_template
from api.models import db, User,Tipo,Comunicacion
from flask_jwt_extended import JWTManager,get_jwt_identity,create_access_token,jwt_required
from werkzeug.security import generate_password_hash,check_password_hash

bpComunicacion = Blueprint('bpComunicacion', __name__)

@bpComunicacion.route('/register_comunicacion', methods=['POST'])
#@jwt_required
def post_comunicacion():
    try:
            #id = get_jwt_identity()
            titulo = request.json.get('titulo')
            email = request.json.get('email')
            descripcion= request.json.get('descripcion')
            destino = request.json.get('destino')
            tipos_id=request.json.get('tipos_id')
            users_id= request.json.get('users_id')

            if not titulo: return jsonify({"status": "failed", "code": 400, "msg": "Titulo is required"}), 400
            if not email: return jsonify({"status": "failed", "code": 400, "msg": "email is required"}), 400
            if not descripcion: return jsonify({"status": "failed", "code": 400, "msg": "descripcion is required"}), 400
            if not destino: return jsonify({"status": "failed", "code": 400, "msg": "destino is required"}), 400
            if not tipos_id: return jsonify({"status": "failed", "code": 400, "msg": "tipo is required"}), 400
  

            comunic = Comunicacion()
            comunic.titulo = titulo
            comunic.email = email
            comunic.descripcion= descripcion
            comunic.destino = destino
            comunic.tipos_id= tipos_id
            comunic.users_id= users_id
            comunic.save()

            data={
                "comunicacion":comunic.serialize_comunication()
            }

            return jsonify({"msg":"Exito en registro de Comunicacion","comunicacion":data}),200
    except Exception as e:
        print("falla al registrar comunicacion",e)
    
    return jsonify({"msg":"Intentarlo mas tarde"}), 400

#Gestion CRUD Tipos
@bpComunicacion.route('/register_tiposmens',methods=['POST'])
#@jwt_required
def post_registromensaj():
    try:
        #id = get_jwt_identity()
        nombre = request.json.get('nombre')

        tipo = Tipo()

        tipo.nombre = nombre
        tipo.save()

        data ={
            "rol": tipo.serialize_tipo()
        }
        return jsonify({"msg":"Tipo agregado exitosamente","tipo":data}), 200
    except Exception as e:
        print(e)
        return jsonify({"msg":"Falla en registro de tipos"}), 400


@bpComunicacion.route('/gettiposmens',methods=['GET'])
#@jwt_required
def gettromensaje():
    try:
        tipos = Tipo.query.all()
     
        tipos = list(map(lambda tipo:tipo.serialize_tipo(), tipos))
    
        return jsonify({"Datos de tipos":tipos}), 200
    except Exception as e:
        print("falla en leer tipos",e)
        return jsonify({"msg": "No existe aun ningun tipo registrado"})


@bpComunicacion.route('/updatetiposmens/<int:id>',methods=['PUT'])
#@jwt_required
def updatetromensaje(id):
    try:
        nombre = request.json.get('nombre')  # None
        
        tipos = Tipo.query.get(id)
        tipos.nombre = nombre
        
        tipos.update()

        data={
            "resultado":tipos.serialize_tipo()
        }
    
        return jsonify({"Datos actualizados de tipos":data}), 200
    except Exception as e:
        print("falla en actualizar tipos",e)
        return jsonify({"msg": "No existe aun ningun tipo "})


@bpComunicacion.route('/deletetipo/<int:id>', methods=['DELETE'])
def deletetipo(id):
    try:
        tipo = Tipo.query.get(id)

        tipo.delete()
            
        return jsonify({"message": "Tipo Deleted"}), 202
    except Exception as e:
        return jsonify({"message": "No se logro eliminar Tipo"}), 400


