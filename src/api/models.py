from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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

class Taller_Articulo(db.Model):
    __tablename__='taller_articulo'
    taller= db.relationship('Taller',backref='articulo')
    articulo=db.relationship('Articulo',backref='taller')

class Mensajes_Usuarios(db.Model):
    __tablename__='mensajes_usuarios'
    mensaje =db.relationship('Mensaje',backref='users')
    user= db.relationship('User',backref='mensaje')
    #aqui se deberia agregar usuaridestino_id 

class User(Base):
    __tablename__= 'users'
    username =db.Column(db.Integer,unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    direccion= db.Column(db.String(200),nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    rol_id= db.Column(db.Integer,db.ForeingKey('rol.id'),primary_key(True))
    mensaje = db.relationship('Mensaje', secondary='mensajes_usuarios')
    taller = db.relationship('Taller',backref='users')
    evento = db.relationship('Evento',backref='users')
    noticia = db.relationship('Noticia',backref='users')
    
   # def __repr__(self):
   #     return f'<User {self.email}>'

    def serialize_user(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password":self.password,
            "direccion":self.direccion,
            "is_active":self.is_active,
            "created_at":self.created_at,
            "update_at":self.updated_at
            # do not serialize the password, its a security breach
        }

    class Rol(Base):
        __tablename__='rol'
        tipo = db.Column(db.String(80),unique=False,nullable=False)
        user = db.relationship('User',backref='rol') 

        def serialize_rol(self):
            return{
            "id":self.id,
            "tipo":self.tipo, 
            "created_at":self.created_at,
            "update_at":self.updated_at
            }
    
    class Taller(Base):
        __tablename__='taller'
        nombretaller= db.Column(db.String(120),unique=False)
        region_taller=db.Column(db.String(120),unique=False)
        direccion_taller=db.Column(db.String(250), unique=False)
        user_id =db.Column(db.Integer,db.ForeingKey('user.id'),primary_key(True))
        articulo = db.relationship('Articulo', secondary='taller_articulo')


        def serialize_taller(self):
            return{
            "id":self.id,
            "nombretaller":self.nombretaller,
            "region_taller": self.region_taller,
            "direccion_taller":self.direccion_taller,
            "created_at":self.created_at,
            "update_at":self.updated_at
            }

    class Articulo(Base):
        __tablename__='articulo'
        articulo= db.Column(db.String(100), nullable=False)
        precio =db.Column(db.float(20),nullable=False)
        promocion =db.Column(db.Boolean(),unique=False,nullable=False)
        precio_oferta=db.Column(db.float(20),nullable=False)
        taller = db.relationship('Taller', secondary='taller_articulo')
        #taller_id =db.relationship(db.Integer,db.ForeingKey('taller.id'),primary_key(True))

        def serialize_articulo(self):
            return{
                "id":self.id,
                "articulo":self.articulo,
                "precio":self.precio,
                "promocion":self.promocion,
                "precio_oferta":self.precio_oferta,
                "created_at":self.created_at,
                "update_at":self.updated_at
            }
    
     
    class Mensaje(Base):
        __tablename__='mensaje'
        titulo_mensaje= db.Column(db.String(150),nullable=False)
        autor_mensaje= db.Column(db.String(150),nullable=False,unique=True)
        descripcion_mensaje= db.Column(db.String(500),nullable=True)
        destino_mensaje=db.Column(db.Integer, nullable=False)
        user = db.relationship('User', secondary='mensajes_usuarios')

        def serialize_mensaje(self):
            return{
                "id":self.id,
                "titulo_mensaje":self.titulo_mensaje,
                "autor_mensaje":self.autor_mensaje,
                "descripcion_mensaje":self.descripcion_mensaje,
                "destino_mensaje":self.descripcion_mensaje,
                "created_at":self.created_at,
                "update_at":self.updated_at
            }

    class Evento(Base):
        __tablename__='evento'
        titulo_evento= db.Column(db.String(150),nullable=False)
        autor_evento= db.Column(db.String(150),nullable=False,unique=True)
        descripcion_evento= db.Column(db.String(500),nullable=True)
        destino_evento=db.Column(db.Integer, nullable=False)
        user_id= db.Column(db.Integer,ForeingKey('user.id'),primary_key=True)

        def serialize_evento(self):
            return{
                "id":self.id,
                "titulo_evento":self.titulo_evento,
                "autor_evento":self.autor_evento,
                "descripcion_evento":self.descripcion_evento,
                "destino_evento":self.descripcion_evento,
                "created_at":self.created_at,
                "update_at":self.updated_at
            }
    
    class Noticia(Base):
        __tablename__='noticia'
        titulo_noticia= db.Column(db.String(150),nullable=False)
        autor_noticia= db.Column(db.String(150),nullable=False,unique=True)
        descripcion_noticia= db.Column(db.String(500),nullable=True)
        destino_noticia=db.Column(db.Integer, nullable=False)
        user_id= db.Column(db.Integer,ForeingKey('user.id'),primary_key=True)

        def serialize_noticia(self):
            return{
                "id":self.id,
                "titulo_noticia":self.titulo_noticia,
                "autor_noticia":self.autor_noticia,
                "descripcion_noticia":self.descripcion_noticia,
                "destino_noticia":self.descripcion_noticia,
                "created_at":self.created_at,
                "update_at":self.updated_at
            }
