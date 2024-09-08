from app import db  # Importar db desde app.py

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    rol = db.Column(db.String(20), nullable=False, default='user')
