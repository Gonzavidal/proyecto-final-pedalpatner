from flask import Blueprint, request, jsonify, render_template
from api.models import db, User, Tipo, Comunicacion
from cloudinary.uploader import upload
from flask_jwt_extended import JWTManager, get_jwt_identity, create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash

bpComunicacion = Blueprint('bpComunicacion', __name__)

# CRUD de Comunicacion
# registrar Comunicacion


@bpComunicacion.route("/register_comunicacion", methods=["POST"])
# @jwt_required
def post_comunicacion():
    # id = get_jwt_identity()
    try:
        print(request.form)
        tipos_id = request.form["tipos_id"]
        roles_id = request.form["roles_id"]
        email = request.form["email"]
        titulo = request.form["titulo"]
        descripcion = request.form["descripcion"]
        users_id = request.form["users_id"]
        data = request.files["avatar"]
        name_file = data.filename
        resp = upload(data, resource_type="image", folder="avatars", pubic_id=name_file)
        
        print("soy resp_",resp)
        if not titulo:
            return (
                jsonify({"status": "failed", "code": 400, "msg": "Titulo is required"}),
                400,
            )
        if not email:
            return (
                jsonify({"status": "failed", "code": 400, "msg": "email is required"}),
                400,
            )
        if not descripcion:
            return (
                jsonify(
                    {"status": "failed", "code": 400, "msg": "descripcion is required"}
                ),
                400,
            )
        if not tipos_id:
            return (
                jsonify({"status": "failed", "code": 400, "msg": "tipo is required"}),
                400,
            )
        if not users_id:
            users_id = None
        

        #print("que trae?",resp)

        if resp:
            comunic = Comunicacion()
            comunic.titulo = titulo
            comunic.email = email
            comunic.descripcion = descripcion
            comunic.roles_id = roles_id
            comunic.tipos_id = tipos_id
            comunic.users_id = users_id
            comunic.imagen = resp['url']
            comunic.save()

            datax = {"comunicacion": comunic.serialize_comunicacion()}

            return (
                jsonify(
                    {"msg": "Exito en registro de Comunicacion", "comunicacion": datax}
                ),
                200,
            )
    except Exception as e:
        print("falla al registrar comunicacion", e)

    return jsonify({"msg": "Intentarlo mas tarde"}), 400


# gestion leer comunicacion


@bpComunicacion.route("/getcomunicacion", methods=["GET"])
# @jwt_required
def get_comunicacion():
    try:
        comunicacion = Comunicacion.query.all()

        comunicacion = list(
            map(lambda comunic: comunic.serialize_comunicacion(), comunicacion)
        )

        return jsonify({"Datos_de_Comunicacion": comunicacion}), 200
    except Exception as e:
        print("falla en leer comunicacion", e)
        return jsonify({"msg": "No existe aun ninguna comunicacion registrada"})

# gestion modificar comunicacion


@bpComunicacion.route('/updatecomunicacion/<int:id>', methods=['PUT'])
def update_comunicacion(id):
    try:
        titulo = request.json.get('titulo')
        email = request.json.get('email')
        descripcion = request.json.get('descripcion')
        destino = request.json.get('destino')
        tipos_id = request.json.get('tipos_id')
        users_id = request.json.get('users_id')
        # SELECT * FROM users WHERE id = ?
        comunicacion = Comunicacion.query.get(id)
        comunicacion.titulo = titulo
        comunicacion.email = email
        comunicacion.descripcion = descripcion
        comunicacion.destino = destino
        comunicacion.tipos_id = tipos_id
        comunicacion.users_id = users_id
        comunicacion.update()

        data = {
            "comunicaciones": list(map(lambda comunicacion: comunicacion.serialize_comunicacion(), comunicacion))
        }

        return jsonify({"msg": "Comunicacion actualizada con exito!", "comunicacion": data}), 200
    except Exception as e:
        print("falla en update", e)
        return jsonify({"No se logro actualizar la comunicacion"}), 400

# gestion borrar comunicacion


@bpComunicacion.route('/deletcomunicacion/<int:id>', methods=['DELETE'])
def delete_comunicacion(id):
    try:
        comunicacion = Comunicacion.query.get(id)

        comunicacion.delete()

        return jsonify({"message": "Comunicacion Deleted"}), 202
    except Exception as e:
        print("falla eliminacion", e)
        return jsonify({"message": "No se logro eliminar Comunicacion"}), 400

# ------------------------------------------------------------------------------------------------------------------------
# Gestion CRUD Tipos
# registrar tipos  SE PUEDE INICIAR INTEGRACION CON FROND (4)


@bpComunicacion.route('/register_tipomensaje', methods=['POST'])
# @jwt_required
def post_registromensaj():
    try:
        # id = get_jwt_identity()
        nombre = request.json.get('nombre')

        tipo = Tipo()

        tipo.nombre = nombre
        tipo.save()

        data = {
            "rol": tipo.serialize_tipo()
        }
        return jsonify({"msg": "Tipo agregado exitosamente", "tipo": data}), 200
    except Exception as e:
        print(e)
        return jsonify({"msg": "Falla en registro de tipos"}), 400

# leer tipos  SE PUEDE INICIAR INTEGRACION CON FROND  (4)


@bpComunicacion.route('/getipomensaje', methods=['GET'])
# @jwt_required
def getipomensaje():
    try:
        tipos = Tipo.query.all()

        tipos = list(map(lambda tipo: tipo.serialize_tipo(), tipos))

        return jsonify({"Datos de tipos": tipos}), 200
    except Exception as e:
        print("falla en leer tipos", e)
        return jsonify({"msg": "No existe aun ningun tipo registrado"})

# modificar tipos  SE PUEDE INICIAR INTEGRACION CON FROND (4)


@bpComunicacion.route('/updatetipomensaje/<int:id>', methods=['PUT'])
# @jwt_required
def updatetipomensaje(id):
    try:
        nombre = request.json.get('nombre')  # None

        tipos = Tipo.query.get(id)
        tipos.nombre = nombre

        tipos.update()

        data = {
            "resultado": tipos.serialize_tipo()
        }

        return jsonify({"Datos actualizados de tipos": data}), 200
    except Exception as e:
        print("falla en actualizar tipos", e)
        return jsonify({"msg": "No existe aun ningun tipo "})

# borrar tipos  SE PUEDE INICIAR INTEGRACION CON FROND (4)


@bpComunicacion.route('/deletetipomensaje/<int:id>', methods=['DELETE'])
def deletetipomensaje(id):
    try:
        tipo = Tipo.query.get(id)

        tipo.delete()

        return jsonify({"message": "Tipo Deleted"}), 202
    except Exception as e:
        return jsonify({"message": "No se logro eliminar Tipo"}), 400
