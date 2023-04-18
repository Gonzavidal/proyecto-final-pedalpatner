from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# creamos la clase base que heredara de las demas


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(), default=db.func.now())
    updated_at = db.Column(
        db.DateTime(), default=db.func.now(), onupdate=db.func.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Comunicacion(Base):
    __tablename__ = 'comunicacion'
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(400), nullable=False)
    destino = db.Column(db.Integer, nullable=False)
    tipo_id = db.Column(db.ForeignKey("tipo.id"), primary_key=True)
    users_id = db.Column(db.ForeignKey("users.id"), primary_key=True)
    tipo = db.relationship("Tipo", back_populates="users")
    user = db.relationship("User", back_populates="tipos")

    def serialize_comunication(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "descripcion": self.descripcion,
            "destino": self.destino,
            "created_at": self.created_at,
            "update_at": self.updated_at
        }


class Taller_Articulo(db.Model):
    __tablename__ = 'taller_articulo'
    taller_id = db.Column(db.ForeignKey("talleres.id"), primary_key=True)
    articulo_id = db.Column(db.ForeignKey("articulo.id"), primary_key=True)
    taller = db.relationship("Taller", back_populates="articulo")
    articulo = db.relationship("Articulo", back_populates="taller")

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class User(Base):
    __tablename__ = 'users'
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    roles_id = db.Column(db.Integer, db.ForeignKey(
        "roles.id"), primary_key=True)
    roles = db.relationship("Rol", back_populates="user")
    talleres_ = db.relationship("Taller")
    tipos = db.relationship("Comunicacion", back_populates="user")

    def serialize_user(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "direccion": self.direccion,
            "is_active": self.is_active,
            "created_at": self.created_at,
            "update_at": self.updated_at
        }


class Rol(Base):

    __tablename__ = 'roles'


tipo = db.Column(db.String(100), nullable=False)
users = db.relationship("User", back_populates="rol")


def serialize_rol(self):
    return {
        "id": self.id,
        "tipo": self.tipo,
        "created_at": self.created_at,
        "update_at": self.updated_at
    }


class Taller(Base):

    __tablename__ = 'talleres'


taller = db.Column(db.String(120), unique=False)
region = db.Column(db.String(120), unique=False)
direccion = db.Column(db.String(250), unique=False)
users_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
# articulos = db.relationship("Taller_Articulo", back_populates="taller")


def serialize_taller(self):
    return {
        "id": self.id,
        "taller": self.taller,
        "region": self.region,
        "direccion": self.direccion,
        "created_at": self.created_at,
        "update_at": self.updated_at
    }


class Articulo(Base):

    __tablename__ = 'articulos'
    articulo = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    promocion = db.Column(db.Boolean(), unique=False, nullable=False)
    precio_oferta = db.Column(db.Integer, nullable=False)
    taller = db.relationship("Taller_Articulo", back_populates="articulo")

    def serialize_articulo(self):
        return {
            "id": self.id,
            "articulo": self.articulo,
            "precio": self.precio,
            "promocion": self.promocion,
            "precio_oferta": self.precio_oferta,
            "created_at": self.created_at,
            "update_at": self.updated_at
        }


class Tipo(Base):
    __tablename__ = 'tipo'
    nombre = db.Column(db.String(150), unique=True)
    users = db.relationship("Comunicacion", back_populates="tipo")

    def serialize_tipo(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "created_at": self.created_at,
            "update_at": self.updated_at
        }
