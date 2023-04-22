from flask import Blueprint, request, jsonify, render_template
from api.models import db, User,Rol,Taller,Pago_Taller,Tipo,Articulo, Comunicacion
from flask_jwt_extended import JWTManager,get_jwt_identity,create_access_token,jwt_required
from werkzeug.security import generate_password_hash,check_password_hash

bpComunicacion = Blueprint('bpComunicacion', __name__)

@bpComunicacion.route('/register_comunicacion', methods=['POST'])
#@jwt_required
def post_comunicacion():
    try:
            #id = get_jwt_identity()
            titulo= request.json.get('titulo')
            descripcion= request.json.get('descripcion')
            destino = request.json.get('destino')
            tipos_id=request.json.get('tipos_id')
            users_id= request.json.get('users_id')

            if not titulo: return jsonify({"status": "failed", "code": 400, "msg": "Titulo is required"}), 400
            if not descripcion: return jsonify({"status": "failed", "code": 400, "msg": "descripcion is required"}), 400
            if not destino: return jsonify({"status": "failed", "code": 400, "msg": "destino is required"}), 400
            if not tipos_id: return jsonify({"status": "failed", "code": 400, "msg": "tipo is required"}), 400
  

            comunic = Comunicacion()
            comunic.titulo = titulo
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



