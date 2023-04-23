import datetime
from flask import Blueprint, request, jsonify, render_template
from api.models import db, User,Rol,Tipo
from flask_jwt_extended import JWTManager,get_jwt_identity,create_access_token,jwt_required
from werkzeug.security import generate_password_hash,check_password_hash

bpRegis = Blueprint('bpRegis', __name__)

@bpRegis.route('/register', methods=['POST'])
def post_registrouser():
    try:
        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')
        direccion = request.json.get('direccion')
        roles_id = request.json.get('roles_id')
    
        if not email: return jsonify({"status": "failed", "code": 400, "msg": "email is required"}), 400
        if not password: return jsonify({"status": "failed", "code": 400, "msg": "Password is required"}), 400

        #user = User.query.filter(User.email==email).all()
        user = User.query.filter_by(email=email).first()
        if user:
                return jsonify({"msg": "usuario ya se encuentra registrado"}),400
        
        user = User()
        user.username = username
        user.email = email
        user.password =  generate_password_hash(password)
        user.direccion = direccion
       # user.is_active = is_active
        user.roles_id = roles_id
        user.save()


        access_token = create_access_token(
                identity=user.email)

        data = {
                "access_token": access_token,
                "user": user.serialize_user()
                
            }


        return jsonify({"msg":"Exito con ingreso!!","user":data}),200
    except Exception as e:
        print("falla en reg usuario",e)
    return jsonify({"msg":"Fallo ingreso!!"}),400



@bpRegis.route('/register_roles',methods=['POST'])
#@jwt_required
def post_registroroles():
    try:
        #id = get_jwt_identity()
        tiporol = request.json.get('tiporol')

        rol = Rol()

        rol.tiporol = tiporol
        rol.save()

        data ={
            "rol": rol.serialize_rol()
        }
        return jsonify({"msg":"Rol agregado exitosamente","rol":data}), 200
    except Exception as e:
        print(e)
        return jsonify({"msg":"Falla en registro de roles"}), 400



@bpRegis.route('/register_tiposmens',methods=['POST'])
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
