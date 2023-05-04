# aqui se deben agregar login + logout
import datetime
from api.models import User, Rol, Taller
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash

bpAuth = Blueprint("bpAuth", __name__)


# login SE PUEDE INICIAR INTEGRACION CON FROND (9)
@bpAuth.route("/login", methods=["POST"])
def login_user():
    try:
       
        email = request.json.get("email")
        password = request.json.get("password")

        if not email:
            return jsonify({"status": 422, "message": "Email is required"}), 422
        if not password:
            return jsonify({"status": 422, "message": "Password is required"}), 422

        user = User.query.filter_by(email=email).first()

        if not user:
            return (
                jsonify({"status": 401, "message": "Email/Password are incorrects"}),
                401,
            )

        if not check_password_hash(user.password, password):
            return (
                jsonify({"status": 401, "message": "Email/Password are incorrects"}),
                401,
            )

        # token con vencimiento
        expire = datetime.timedelta(days=2)
        access_token = create_access_token(identity=user.id, expires_delta=expire)

        # token sin vencimiento
        # access_token = create_access_token(identity=user.id)

        data = {
            "access_token": access_token,
            "user": user.serialize_user(),
            "expire": expire.total_seconds()
        }

        return (
            jsonify({"status": 200, "message": "You have been logged", "data": data}),
            200,
        )
    except Exception as e:
        print("Error en login", e)
        return jsonify({"msg": "Intentarlo mas tarde"})
