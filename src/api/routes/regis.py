import datetime
from flask import Blueprint, request, jsonify, render_template
from api.models import db, User,Rol,Tipo, Taller, PagoTaller, UserTaller
from flask_jwt_extended import JWTManager,get_jwt_identity,create_access_token,jwt_required
from werkzeug.security import generate_password_hash,check_password_hash

bpRegis = Blueprint('bpRegis', __name__)
#CRUD DE USER
# gestion de registro de usuario-admin
@bpRegis.route('/registeruser', methods=['POST'])
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

#gestion de modificacion user
@bpRegis.route('/puttuser/<int:id>', methods=['PUT'])
def puttuser(id):
    try:
        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')
        direccion = request.json.get('direccion')
        roles_id = request.json.get('roles_id')
    
        user = User.query.get(id)
        user.username = username
        user.email = email
        user.password = password
        user.direccion = direccion
        user.roles_id = roles_id
        user.update()

        data ={
            "usuario": user.serialize_user()
        }

        return jsonify({"msg":"se logro actualizacion","user":data}),200
    except Exception as e:
        print("falla en actualizacion de usuario",e)
    return jsonify({"msg":"Fallo en actualizacion"}),400

#gestion de leer user
@bpRegis.route('/getuser',methods=['GET'])
#@jwt_required
def getuser():
    try:
        users = User.query.all()
     
        users = list(map(lambda user:user.serialize_user(), users))
    
        return jsonify({"Datos de user":users}), 200
    except Exception as e:
        print("falla leer users",e)
        return jsonify({"msg": "No existe aun ningun user"})

#gestion de borrar user
@bpRegis.route('/deleteuser/<int:id>', methods=['DELETE'])
def deleteuser(id):
    try:
        users = User.query.get(id)

        users.delete()
            
        return jsonify({"message": "User Deleted"}), 202
    except Exception as e:
        print("falla al borrar user",e)
        return jsonify({"message": "No se logro eliminar a usuario"}), 400

#------------------------------------------------------------------------------------------------------
#CRUD registro mecanico
# gestion de registro de mecanico
@bpRegis.route('/registermecanico', methods=['POST'])
def post_registromecanico():
    try:
        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')
        direccion = request.json.get('direccion')
        roles_id = request.json.get('roles_id')
        tallernom = request.json.get('tallernom')
        regiontall = request.json.get('regiontall')
        direcciontall = request.json.get('direcciontall')
        users_id = request.json.get('users_id')
               
    
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
        user.roles_id = roles_id

        taller= Taller()
        taller.tallernom = tallernom
        taller.regiontall = regiontall
        taller.direcciontall = direcciontall
        taller.users_id = users_id
        user.taller = taller

        user.save()


        access_token = create_access_token(
                identity=user.email)

        data = {
                "access_token": access_token,
                "user": user.serialize_user(),
                "taller":taller.serialize_taller()
                              
            }

        return jsonify({"msg":"Exito con ingreso datos de Mecanico!!","info": data}),200
    except Exception as e:
        print("falla en reg mecanico",e)
        return jsonify({"msg":"Fallo registro mecanico!!"}),400

#gestion de modificacion user
#@bpRegis.route('/puttuser/<int:id>', methods=['PUT'])
#def puttuser(id):
#    try:
#        username = request.json.get('username')
#        email = request.json.get('email')
#        password = request.json.get('password')
#        direccion = request.json.get('direccion')
#        roles_id = request.json.get('roles_id')
#    
#        user = User.query.get(id)
#        user.username = username
#        user.email = email
#        user.password = password
#        user.direccion = direccion
#        user.roles_id = roles_id
#        user.update()
#
#        data ={
#            "usuario": user.serialize_user()
#        }
#
#        return jsonify({"msg":"se logro actualizacion","user":data}),200
#    except Exception as e:
#        print("falla en actualizacion de usuario",e)
#    return jsonify({"msg":"Fallo en actualizacion"}),400
#
##gestion de leer user
#@bpRegis.route('/getuser',methods=['GET'])
##@jwt_required
#def getuser():
#    try:
#        users = User.query.all()
#     
#        users = list(map(lambda user:user.serialize_user(), users))
#    
#        return jsonify({"Datos de user":users}), 200
#    except Exception as e:
#        print("falla leer users",e)
#        return jsonify({"msg": "No existe aun ningun user"})
#
##gestion de borrar user
#@bpRegis.route('/deleteuser/<int:id>', methods=['DELETE'])
#def deleteuser(id):
#    try:
#        users = User.query.get(id)
#
#        users.delete()
#            
#        return jsonify({"message": "User Deleted"}), 202
#    except Exception as e:
#        print("falla al borrar user",e)
#        return jsonify({"message": "No se logro eliminar a usuario"}), 400
#
#




#-------------------------------------------------------------------------------------------------------
# CRUD  de ROL
#gestion de registrsr roles (usuario-admin)
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

#gestion de leer roles
@bpRegis.route('/getroles',methods=['GET'])
#@jwt_required
def getroles():
    try:
        roles = Rol.query.all()
     
        roles = list(map(lambda rol:rol.serialize_rol(), roles))
    
        return jsonify({"Datos de rol":roles}), 200
    except Exception as e:
        print("print falla leer roles",e)
        return jsonify({"msg": "No existe aun ningun rol"})

#gestion de modificar roles
@bpRegis.route('/updateroles/<int:id>',methods=['PUT'])
#@jwt_required
def updateroles(id):
    try:

        tiporol = request.json.get('tiporol')  # None
        
        roles = Rol.query.get(id)
        roles.tiporol = tiporol
        
        roles.update()

        data={
            "resultado":roles.serialize_rol()
        }
      
        return jsonify({"datos modificados":data}), 202
    except Exception as e:
        print("falla en update",e)
        return jsonify({"No se logro actualizar el cambio"}), 400

#gestion de borrar roles
@bpRegis.route('/deleteroles/<int:id>', methods=['DELETE'])
def deleteroles(id):
    try:
        roles = Rol.query.get(id)

        roles.delete()
            
        return jsonify({"message": "Rol Deleted"}), 202
    except Exception as e:
        print("falla al borrar rol",e)
        return jsonify({"message": "No se logro eliminar a rol"}), 400




