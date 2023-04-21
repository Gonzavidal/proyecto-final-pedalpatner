import datetime
from flask import Blueprint, request, jsonify, render_template
from api.models import db, User,Taller,Articulo,Taller_Articulo,Rol
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash, generate_password_hash

bpAuth = Blueprint('bpAuth', __name__)

@bpAuth.route('/register_usuario', methods=['POST'])
def post_registrouser():
    try:
        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')
        direccion = request.json.get('direccion')
        #is_active = request.json.get('is_active')
        roles_id = request.json.get('roles_id')

        if not email: return jsonify({"status": "failed", "code": 400, "msg": "email is required"}), 400
        if not password: return jsonify({"status": "failed", "code": 400, "msg": "Password is required"}), 400

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


        data ={
            "user":user.serialize_user()
        }

        return jsonify({"msg":"Exito con ingreso de usuario","user":data}),200
    except Exception as e:
        print(e)
    return jsonify({"msg":"Fallo ingreso de usuario"}),400


@bpAuth.route('/register_admin', methods=['POST'])
def post_registroadmin():
    try:
        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')
        direccion = request.json.get('direccion')
        #is_active = request.json.get('is_active')
        roles_id = request.json.get('roles_id')

        if not email: return jsonify({"status": "failed", "code": 400, "msg": "email is required"}), 400
        if not password: return jsonify({"status": "failed", "code": 400, "msg": "Password is required"}), 400

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

        data ={
            "admin":user.serialize_user()
        }

        return jsonify({"msg":"Exito con ingreso de admin","admin":data}),200
    except Exception as e:
        print(e)
    return jsonify({"msg":"Fallo ingreso de admin"}),400



@bpAuth.route('/register_mecanico', methods=['POST'])
def post_registromecanico():
    try:
        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')
        direccion = request.json.get('direccion')
        #is_active = request.json.get('is_active')
        roles_id = request.json.get('roles_id')

        tallernom = request.json.get('tallernom')
        regiontall = request.json.get('regiontall')
        direcciontall = request.json.get('direcciontall')
        pagos_id = request.json.get('pagos_id')
        users_id = request.json.get('users_id')

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
        user.password =  generate_password_hash(password)
        user.direccion = direccion
       # user.is_active = is_active
        user.roles_id = roles_id
        user.save()

        taller = Taller()
        taller.tallernom = tallernom
        taller.regiontall = regiontall
        taller.direcciontall = direcciontall
        taller.pagos_id = pagos_id
        taller.users_id = users_id
        user.taller = taller
        user.save() 

        articulo = Articulo()
        articulo.articulonom = articulonom
        articulo.precio = precio
        articulo.promocion = promocion
        articulo.precio_oferta = precio_oferta
        user.articulo = articulo
        user.save()

        access_token = create_access_token(
                identity=user.email)

        data = {
                "access_token": access_token,
                "user": user.serialize_user(),
                "taller":taller.serialize_taller(),
                "articulo":articulo.serialize_articulo()
            }

        return jsonify({"msg":"Mecanico registrado con exito!","datos":data}), 200
    except Exception as e:
        print(e)

    return jsonify({"msg":"Falla en el registro de Usuario"}), 400


@bpAuth.route('/register_roles',methods=['POST'])
def post_rregistroroles():
    try:
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
