from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# creamos la clase base que heredara de las demas


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(), default=db.func.now())
    updated_at = db.Column(db.DateTime(), default=db.func.now(), onupdate=db.func.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Comunicacion(db.Model):
    __tablename__ = "comunicacion"
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(140), nullable=False)
    email = db.Column(db.String(110), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(), default=db.func.now())
    updated_at = db.Column(db.DateTime(), default=db.func.now(), onupdate=db.func.now())
    tipos_id = db.Column(db.ForeignKey("tipos.id"), nullable=False)
    roles_id = db.Column(db.ForeignKey("roles.id"), nullable=True)
    rol = db.relationship("Rol", back_populates="comunicacion")
    data = db.Column(db.LargeBinary, nullable=True)
    imagen = db.Column(db.String(250), nullable=True)
    tipo = db.relationship("Tipo", back_populates="comunicacion")
    users_id = db.Column(db.ForeignKey("users.id"), nullable=True)
    user = db.relationship("User", back_populates="comunicacion")

    def serialize_comunicacion(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "email": self.email,
            "descripcion": self.descripcion,
            "tipos_id": self.tipos_id,
            "users_id": self.users_id,
            "roles_id": self.roles_id,
            "data": self.data,
            "created_at": self.created_at,
            "update_at": self.updated_at,
            "imagen": self.imagen,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class PagoTaller(db.Model):
    __tablename__ = "pagotalleres"
    pagos_id = db.Column(db.ForeignKey("pagos.id"), nullable=False, primary_key=True)
    talleres_id = db.Column(
        db.ForeignKey("talleres.id"), nullable=False, primary_key=True
    )
    created_at = db.Column(db.DateTime(), default=db.func.now())
    updated_at = db.Column(db.DateTime(), default=db.func.now(), onupdate=db.func.now())
    pago = db.relationship("Pago", back_populates="talleres")
    taller = db.relationship("Taller", back_populates="pagos")

    def serialize_pagotaller(self):
        return {
            "pagos_id": self.pagos_id,
            "talleres_id": self.talleres_id,
            "created_at": self.created_at,
            "update_at": self.updated_at,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class TallerArticulo(db.Model):
    __tablename__ = "tallerarticulos"
    talleres_id = db.Column(
        db.ForeignKey("talleres.id"), nullable=False, primary_key=True
    )
    articulos_id = db.Column(
        db.ForeignKey("articulos.id"), nullable=False, primary_key=True
    )
    created_at = db.Column(db.DateTime(), default=db.func.now())
    updated_at = db.Column(db.DateTime(), default=db.func.now(), onupdate=db.func.now())
    taller = db.relationship("Taller", back_populates="articulos")
    articulo = db.relationship("Articulo", back_populates="talleres")

    def serialize_tallerarticulo(self):
        return {
            "talleres_id": self.talleres_id,
            "articulos_id": self.articulos_id,
            "created_at": self.created_at,
            "update_at": self.updated_at,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class UserTaller(db.Model):
    __tablename__ = "usertalleres"
    talleres_id = db.Column(
        db.ForeignKey("talleres.id"), nullable=False, primary_key=True
    )
    users_id = db.Column(db.ForeignKey("users.id"), nullable=False, primary_key=True)
    created_at = db.Column(db.DateTime(), default=db.func.now())
    updated_at = db.Column(db.DateTime(), default=db.func.now(), onupdate=db.func.now())
    taller = db.relationship("Taller", back_populates="usertalleres")
    user = db.relationship("User", back_populates="usertalleres", uselist=True)

    def serialize_usertaller(self):
        return {
            "talleres_id": self.talleres_id,
            "users_id": self.users_id,
            "created_at": self.created_at,
            "update_at": self.updated_at,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class User(Base):
    __tablename__ = "users"
    username = db.Column(db.String(120), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(400), nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False, default=True)
    roles_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=True)
    rol = db.relationship("Rol", back_populates="user")
    comunicacion = db.relationship(
        "Comunicacion", cascade="all,delete", back_populates="user", uselist=False
    )
    usertalleres = db.relationship(
        "UserTaller", cascade="all,delete", back_populates="user", uselist=True
    )

    def serialize_user(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "is_active": self.is_active,
            "roles_id": self.roles_id,
            "created_at": self.created_at,
            "update_at": self.updated_at,
        }

    def serialize_usertaller(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "is_active": self.is_active,
            "roles_id": self.roles_id,
            "created_at": self.created_at,
            "update_at": self.updated_at,
            "taller": list(map(lambda tall: tall.serialize_taller(), self.taller)),
        }


class Rol(Base):
    __tablename__ = "roles"
    tiporol = db.Column(db.String(100), nullable=False)
    user = db.relationship(
        "User", cascade="all,delete", back_populates="rol", uselist=False
    )
    comunicacion = db.relationship(
        "Comunicacion", cascade="all,delete", back_populates="rol", uselist=False
    )

    def serialize_rol(self):
        return {
            "id": self.id,
            "tiporol": self.tiporol,
            "created_at": self.created_at,
            "update_at": self.updated_at,
        }

class Taller(Base):
    __tablename__ = "talleres"
    tallernom = db.Column(db.String(110), unique=False)
    regiontall = db.Column(db.String(110), unique=False)
    direcciontall = db.Column(db.String(250), unique=False)
    articulos = db.relationship(
        "TallerArticulo", back_populates="taller", uselist=False
    )
    pagos = db.relationship("PagoTaller", back_populates="taller", uselist=False)
    usertalleres = db.relationship(
        "UserTaller", cascade="all,delete", back_populates="taller"
    )

    def serialize_taller(self):
        return {
            "id": self.id,
            "tallernom": self.tallernom,
            "regiontall": self.regiontall,
            "direcciontall": self.direcciontall,
            "created_at": self.created_at,
            "update_at": self.updated_at,
        }


class Articulo(Base):
    __tablename__ = "articulos"
    articulonom = db.Column(db.String(200), nullable=False)
    mantencion = db.Column(db.Integer, nullable=True)
    indumentaria = db.Column(db.Integer, nullable=True)
    bicicletas = db.Column(db.Integer, nullable=True)
    talleres = db.relationship(
        "TallerArticulo", back_populates="articulo", uselist=True
    )

    def serialize_articulo(self):
        return {
            "id": self.id,
            "articulonom": self.articulonom,
            "mantencion": self.mantencion,
            "indumentaria": self.indumentaria,
            "bicicletas": self.bicicletas,
            "created_at": self.created_at,
            "update_at": self.updated_at,
        }


class Tipo(Base):
    __tablename__ = "tipos"
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    comunicacion = db.relationship(
        "Comunicacion", cascade="all,delete", back_populates="tipo", uselist=False
    )

    def serialize_tipo(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "created_at": self.created_at,
            "update_at": self.updated_at,
        }


class Pago(Base):
    __tablename__ = "pagos"
    tipopago = db.Column(db.String(100), unique=True, nullable=False)
    talleres = db.relationship("PagoTaller", back_populates="pago", uselist=False)
    

    def serialize_pago(self):
        return {
            "id": self.id,
            "tipopago": self.tipopago,
            "created_at": self.created_at,
            "update_at": self.updated_at,
        }