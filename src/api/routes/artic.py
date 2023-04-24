from flask import Blueprint, request, jsonify, render_template
from api.models import db,Articulo,TallerArticulo
from flask_jwt_extended import JWTManager,get_jwt_identity,create_access_token,jwt_required
from werkzeug.security import generate_password_hash,check_password_hash

bpArticulo = Blueprint('bpArticulo', __name__)

# CRUD de articulo
# registrar articulo
@bpArticulo.route('/register_articulo', methods=['POST'])
#@jwt_required
def post_registarticulo():
    try:
        #id = get_jwt_identity()
        articulonom = request.json.get('articulonom')
        precio= request.json.get('precio')
        precio_oferta = request.json.get('precio_oferta')

        if not articulonom: return jsonify({"status": "failed", "code": 400, "msg": "articulo is required"}), 400
        if not precio: return jsonify({"status": "failed", "code": 400, "msg": "precio is required"}), 400
        if not precio_oferta: return jsonify({"status": "failed", "code": 400, "msg": "precio-oferta is required"}), 400

            #taller = Taller.query.filter(Taller.tallernom==tallernom).all()
        articulo = Articulo.query.filter_by(articulonom=articulonom).first()
        if articulo:
              return jsonify({"msg": "Articulo ya se encuentra registrado"}),400
    
        articulo = Articulo()
        articulo.articulonom = articulonom
        articulo.precio = precio
        articulo.precio_oferta = precio_oferta
        articulo.save()

        data ={
            "articulo": articulo.serialize_articulo()
        }
        return jsonify({"msg":"Exito al registrar Articulo", "articulo": data})
    except Exception as e:
        print("fala en articulo", e)

        return jsonify({"msg":"Ingreso de Articulo Fallido"})

# gestion leer articulo
@bpArticulo.route('/getarticulo',methods=['GET'])
#@jwt_required
def getarticulo():
    try:
        articulos = Articulo.query.all()
     
        articulos = list(map(lambda articulo:articulo.serialize_articulo(), articulos))
    
        return jsonify({"Datos de Articulos":articulos}), 200
    except Exception as e:
        print("falla en leer Articulos",e)
        return jsonify({"msg": "No existe aun ningun Articulo registrado"})

# gestion modificar articulo
@bpArticulo.route('/updatearticulo/<int:id>', methods=['PUT'])
def updatearticulo(id):
    try:
        articulonom = request.json.get('articulonom')
        precio= request.json.get('precio')
        precio_oferta = request.json.get('precio_oferta')

        # SELECT * FROM users WHERE id = ?
        articulo =  Articulo.query.get(id)
        articulo.articulonom = articulonom
        articulo.precio = precio
        articulo.precio_oferta = precio_oferta
        articulo.save()

        data ={
            "articulo": articulo.serialize_articulo()
        }
        return jsonify({"msg":"Exito al actualizar Articulo", "articulo": data})
    except Exception as e:
        print("falla en articulo", e)

        return jsonify({"msg":"Actualizacion de Articulo Fallido"})

# gestion borrar articulo
@bpArticulo.route('/deletearticulo/<int:id>', methods=['DELETE'])
def deletearticulo(id):
    try:
        articulo = Articulo.query.get(id)

        articulo.delete()
            
        return jsonify({"message": "Articulo Deleted"}), 202
    except Exception as e:
        print("falla eliminacion",e)
        return jsonify({"message": "No se logro eliminar Articulo"}), 400

#---------------------------------------------------------------------------------------------------------------------------------
# CRUD de Taller-Articulo
# registrar taller-articulo
@bpArticulo.route('/register_tallerarticulo', methods=['POST'])
#@jwt_required
def post_registrotallerarticulo():
    try:
        #id = get_jwt_identity()
        articulos_id = request.json.get('articulos_id')
        talleres_id = request.json.get('talleres_id')
        
        artictaller = TallerArticulo()
        artictaller.articulos_id = articulos_id
        artictaller.talleres_id = talleres_id

        artictaller.save()

        data ={
            "articulo-taller": artictaller.serialize_tallerarticulo()
        }
        return jsonify({"msg":"Exito con registro de taller-articulo","dato":data}),200
    except Exception as e:
        print("falla registro articulo taller",e)
    return jsonify({"msg":"Fallo al registrar tipo de articulo-taller"}),400

# gestion leer taller-articulo
@bpArticulo.route('/gettallerarticulo',methods=['GET'])
#@jwt_required
def gettallerarticulo():
    try:
        tallerarticulos = TallerArticulo.query.all()
     
        tallerarticulos = list(map(lambda tallerarticulo:tallerarticulo.serialize_tallerarticulo(), tallerarticulos))
    
        return jsonify({"Datos de Taller-Articulos":tallerarticulos}), 200
    except Exception as e:
        print("falla en leer Taller-Articulos",e)
        return jsonify({"msg": "No existe aun ningun Taller-Articulo registrado"}),400

# gestion borrarr taller-articulo
@bpArticulo.route('/deletetallerarticulo/<int:talleres_id>/<int:articulos_id>', methods=['DELETE'])
def deletetallerarticulo(talleres_id,articulos_id):
    try:
        # SELECT * FROM users WHERE id = ?
        #tallerarticulos = TallerArticulo.query.get(talleres_id,articulos_id)
        tallerarticulos = TallerArticulo.query.filter_by(talleres_id=talleres_id,articulos_id=articulos_id).first()
        print("esto trae",tallerarticulos)
        tallerarticulos.delete()
        
        
        return jsonify({"msg":"Exito al eliminar Taller-Articulo"}),200
    except Exception as e:
        print("falla en taller-articulo", e)

        return jsonify({"msg":"Eliminacion de Taller-Articulo Fallido"}),400


    try:
        articulo = Articulo.query.get(id)

        articulo.delete()
            
        return jsonify({"message": "Articulo Deleted"}), 202
    except Exception as e:
        print("falla eliminacion",e)
        return jsonify({"message": "No se logro eliminar Articulo"}), 400

