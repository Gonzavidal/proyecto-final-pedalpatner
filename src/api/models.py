from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#Modelo pendiente de ajustes en construccion.......
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
    taller_id = db.Column(ForeignKey("taller.id"), primary_key=True)
    articulo_id = db.Column(ForeignKey("articulo.id"), primary_key=True)
    taller = db.relationship("Taller", back_populates="articulos")
    articulo =db.relationship("Articulo", back_populates="talleres")
   
class Comunicacion(Base):
        __tablename__='comunicacion'
        titulo= db.Column(db.String(100),nullable=False)
        autor= db.Column(db.String(100), nullable=False) 
        descripcion= db.Column(db.String(400),nullable=False)
        destino = db.Column(db.Integer,nullable=False)
        tipo_id = db.Column(db.ForeignKey("tipo.id"), primary_key=True)
        usuario_id = db.Column(db.ForeignKey("usuario.id"), primary_key=True)
        tipo = db.relationship("Tipo", back_populates="usuarios")
        user = db.relationship("User", back_populates="tipos")
# falta crear el serialize de comunicacion

class User(Base):
    __tablename__= 'users'
    username =db.Column(db.Integer,unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    direccion= db.Column(db.String(200),nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    rol_id= db.Column(db.Integer,db.ForeingKey('rol.id'),primary_key(True))
    taller = db.relationship('Taller',backref='users')
    tipos = db.relationship("Comunicacion", back_populates="user")
    
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
        articulos = db.relationship("Taller_Articulo", back_populates="taller")
        
        #articulo = db.relationship('Articulo', secondary='taller_articulo')


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
        precio_oferta= db.Column(db.float(20),nullable=False)
        talleres = db.relationship("Taller_Articulo",back_populates="articulo")
        #taller = db.relationship('Taller', secondary='taller_articulo')
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
    
        
    class Tipo(Base):
        __tablename__='tipos'
        nombre= db.Column(db.String(150),unique=True)
        usuarios = db.relationship("Comunicacion", back_populates="tipo")
   #falta crear serialize de tipo