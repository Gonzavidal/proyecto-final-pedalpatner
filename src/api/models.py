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

class User(Base):
    __tablename__= 'users'
    username =db.Column(db.Integer,unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    direccion= db.Column(db.String(200),nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    taller = db.relationship('Taller',backref='users')
    

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
      
    class Taller(Base):
        __tablename__='taller'
        nombretaller= db.Column(db.String(120),unique=False)
        region_taller=db.Column(db.String(120),unique=False)
        direccion_taller=db.Column(db.String(250), unique=False)
        user =db.Column(db.Integer,db.ForeingKey('user.id'))
        user = db.relationship('User', backref='taller')


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
        promocion =db.Column(db.Boolean(),nullable=False)
        precio_oferta=db.Column(db.float(20),nullable=False)
        taller =db.Column(db.Integer,db.ForeingKey('taller.id'))
        taller= db.relationship('Taller', backref='articulo')

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
    
     #class Rol(Base):
    #    __tablename__='rol'
    #    
    