import datetime
import os
import requests
from flask import Blueprint, request, jsonify
from api.models import db, User, Rol, Taller,UserTaller
from flask_jwt_extended import (
    JWTManager,
    get_jwt_identity,
    create_access_token,
    jwt_required,
)
from werkzeug.security import generate_password_hash, check_password_hash

bpRegis = Blueprint("bpRegis", __name__)


def send_simple_message(to, subject, body):
    domain = os.getenv("MAILGUN_DOMAIN")
    return requests.post(
		f"https://api.mailgun.net/v3/{domain}/messages",
		auth=("api", os.getenv("MAILGUN_API_KEY")),
		data={"from": "PedalPartner <mailgun@{domain}>",
			"to": [to],
			"subject": subject,
			"text": body})


#CRUD DE USER
# gestion de registro de usuario-admin SE PUEDE INICIAR INTEGRACION CON FROND (1)
@bpRegis.route("/registeruser", methods=["POST"])
def post_registrouser():
    try:
        username = request.json.get("username")
        email = request.json.get("email")
        password = request.json.get("password")
       # direccion = request.json.get("direccion")
        roles_id = request.json.get("roles_id")

        if not email:
            return (
                jsonify({"status": "failed", "code": 400, "msg": "email is required"}),
                400,
            )
        if not password:
            return (
                jsonify(
                    {"status": "failed", "code": 400, "msg": "Password is required"}
                ),
                400,
            )

        # user = User.query.filter(User.email==email).all()
        user = User.query.filter_by(email=email).first()
        if user:
            return jsonify({"msg": "usuario ya se encuentra registrado"}), 400

        user = User()
        user.username = username
        user.email = email
        user.password = generate_password_hash(password)
      #  user.direccion = direccion
        user.roles_id = roles_id
        user.save()

        access_token = create_access_token(identity=user.email)

        data = {"access_token": access_token, "user": user.serialize_user()}

        send_simple_message(
            to=user.email,
            subject="Te has inscrito satisfactoriamente",
            body=f"Hola {user.username}! Te has registrado satisfactoriamente a PedalPartner!"
        )

        return jsonify({"msg": "Exito con ingreso de user!!", "user": data}), 201
    except Exception as e:
        print("falla en reg usuario", e)
    return jsonify({"msg": "Fallo ingreso!!"}), 400


# Admin gestion de modificacion usuario-admin SE PUEDE INICIAR INTEGRACION CON FROND (1)
@bpRegis.route("/puttuser/<int:id>", methods=["PUT"])
def puttuser(id):
    try:
        username = request.json.get("username")
        email = request.json.get("email")
        password = request.json.get("password")
        #direccion = request.json.get("direccion")
        roles_id = request.json.get("roles_id")

        user = User.query.get(id)
        user.username = username
        user.email = email
        user.password = generate_password_hash(password)
        #user.direccion = direccion
        user.roles_id = roles_id
        user.update()

        access_token = create_access_token(identity=user.email)

        data = {"access_token": access_token, "usuario": user.serialize_user()}

        return jsonify({"msg": "se logro actualizacion", "user": data}), 200
    except Exception as e:
        print("falla en actualizacion de usuario", e)
    return jsonify({"msg": "Fallo en actualizacion"}), 400


# gestion de leer usuario-admin SE PUEDE INICIAR INTEGRACION CON FROND (1)
@bpRegis.route("/getuser", methods=["GET"])
# @jwt_required
def getuser():
    try:
        users = User.query.all()

        users = list(map(lambda user: user.serialize_user(), users))

        return jsonify({"Datos de user": users}), 200
    except Exception as e:
        print("falla leer users", e)
        return jsonify({"msg": "No existe aun ningun user"})


# gestion de borrar usuario-admin SE PUEDE INICIAR INTEGRACION CON FROND (1)
@bpRegis.route("/deleteuser/<int:id>", methods=["DELETE"])
def deleteuser(id):
    try:
        users = User.query.get(id)

        users.delete()

        return jsonify({"message": "User Deleted"}), 202
    except Exception as e:
        print("falla al borrar user", e)
        return jsonify({"message": "No se logro eliminar a usuario"}), 400


# ------------------------------------------------------------------------------------------------------
# CRUD registro mecanico
# gestion de registro de mecanico
@bpRegis.route("/registermecanico", methods=["POST"])
def post_registromecanico():
    try:
        username = request.json.get("username")
        email = request.json.get("email")
        password = request.json.get("password")
        roles_id = request.json.get("roles_id")
        tallernom = request.json.get("tallernom")
        regiontall = request.json.get("regiontall")
        direcciontall = request.json.get("direcciontall")
        #users_id = request.json.get("users_id")

        if not email:
            return (
                jsonify({"status": "failed", "code": 400, "msg": "email is required"}),
                400,
            )
        if not password:
            return (
                jsonify(
                    {"status": "failed", "code": 400, "msg": "Password is required"}
                ),
                400,
            )

        # user = User.query.filter(User.email==email).all()
        user = User.query.filter_by(email=email).first()
        if user:
            return jsonify({"msg": "usuario ya se encuentra registrado"}), 400

        user = User()
        user.username = username
        user.email = email
        user.password = generate_password_hash(password)
        user.roles_id = roles_id

        taller = Taller()
        taller.tallernom = tallernom
        taller.regiontall = regiontall
        taller.direcciontall = direcciontall
        
        
        a= UserTaller()
        a.taller= taller
        user.usertalleres.append(a)

        user.save()

        access_token = create_access_token(identity=user.email)
        print("user taller a",user,taller,a)

        data = {
            "access_token": access_token
        
            #"user": user.serialize_usertaller()
           # "taller": taller.serialize_taller()
        }

        send_simple_message(
            to=user.email,
            subject="Te has inscrito satisfactoriamente",
            body=f"Hola {user.username}! Te has registrado satisfactoriamente a PedalPartner!"
        )

        return (
            jsonify({"msg": "Exito con ingreso datos de Mecanico!!", "info": data}),
            200,
        )
    except Exception as e:
        print("falla en reg mecanico", e)
        db.session.rollback()
        return jsonify({"msg": "Fallo registro mecanico!!"}), 400


# gestion de leer mecanico
@bpRegis.route("/getmecanico", methods=["GET"])
# @jwt_required
def getmecanico():
    try:
        resultall = User.query.filter_by(User.roles_id == 3).all()
        resultall = list(map(lambda result: result.serialize_usertaller(), resultall))

        return jsonify({"usuario": resultall}), 200
    except Exception as e:
        print("falla leer mecanico", e)
        return jsonify({"msg": "No existe aun ningun Mecanico registrado"})


# gestion de modificacion mecanico
@bpRegis.route("/putmecanico/<int:id>", methods=["PUT"])
def putmecanico(id):
    try:
        username = request.json.get("username")
        email = request.json.get("email")
        password = request.json.get("password")
       # direccion = request.json.get("direccion")
        roles_id = request.json.get("roles_id")

        tallernom = request.json.get("tallernom")
        regiontall = request.json.get("regiontall")
        direcciontall = request.json.get("direcciontall")
        users_id = request.json.get("users_id")

        user = User.query.get(id)
        user.username = username
        user.email = email
        user.password = generate_password_hash(password)
       # user.direccion = direccion
        user.roles_id = roles_id

        taller = Taller.query.get(users_id)
        taller.tallernom = tallernom
        taller.regiontall = regiontall
        taller.direcciontall = direcciontall
        taller.users_id = users_id

        user.taller = taller

        user.update()

        access_token = create_access_token(identity=user.email)

        data = {
            "access_token": access_token,
            "usuario": list(map(lambda user: user.serialize_usertaller())),
        }

        return (
            jsonify({"msg": "se logro actualizacion de mecanico", "mecanico": data}),
            200,
        )
    except Exception as e:
        print("falla en mecanico", e)
    return jsonify({"msg": "Fallo de actualizacion en Mecanico"}), 400


# gestion de borrar mecanico
@bpRegis.route("/deletemecanico/<int:users_id>", methods=["DELETE"])
def deletemecanico(users_id):
    try:
        mecanico0 = User.query.filter_by(users_id=users_id).filter()
        mecanico1 = Taller.query.filter_by(users_id=users_id).filter()
        mecanico0.delete()
        mecanico1.delete()

        return jsonify({"message": "Mecanico Deleted"}), 202
    except Exception as e:
        print("falla al borrar mecanico", e)
        return jsonify({"message": "No se logro eliminar a mecanico"}), 400


# -------------------------------------------------------------------------------------------------------
# CRUD  de ROL
# gestion de registrsr roles  SE PUEDE INICIAR INTEGRACION CON FROND  (2)
@bpRegis.route("/register_roles", methods=["POST"])
# @jwt_required
def post_registroroles():
    try:
        # id = get_jwt_identity()
        tiporol = request.json.get("tiporol")

        rol = Rol()

        rol.tiporol = tiporol
        rol.save()

        data = {"rol": rol.serialize_rol()}
        return jsonify({"msg": "Rol agregado exitosamente", "rol": data}), 200
    except Exception as e:
        print(e)
        return jsonify({"msg": "Falla en registro de roles"}), 400


# gestion de leer roles  SE PUEDE INICIAR INTEGRACION CON FROND (2)
@bpRegis.route("/getroles", methods=["GET"])
# @jwt_required
def getroles():
    try:
        roles = Rol.query.all()

        roles = list(map(lambda rol: rol.serialize_rol(), roles))

        return jsonify({"Datos de rol": roles}), 200
    except Exception as e:
        print("print falla leer roles", e)
        return jsonify({"msg": "No existe aun ningun rol"})


# gestion de modificar roles SE PUEDE INICIAR INTEGRACION CON FROND (2)
@bpRegis.route("/updateroles/<int:id>", methods=["PUT"])
# @jwt_required
def updateroles(id):
    try:
        tiporol = request.json.get("tiporol")  # None

        roles = Rol.query.get(id)
        roles.tiporol = tiporol

        roles.update()

        data = {"resultado": roles.serialize_rol()}

        return jsonify({"datos modificados": data}), 202
    except Exception as e:
        print("falla en update", e)
        return jsonify({"No se logro actualizar el cambio"}), 400


# gestion de borrar roles  SE PUEDE INICIAR INTEGRACION CON FROND (2)
@bpRegis.route("/deleteroles/<int:id>", methods=["DELETE"])
def deleteroles(id):
    try:
        roles = Rol.query.get(id)

        roles.delete()

        return jsonify({"message": "Rol Deleted"}), 202
    except Exception as e:
        print("falla al borrar rol", e)
        return jsonify({"message": "No se logro eliminar a rol"}), 400
