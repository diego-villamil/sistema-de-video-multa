class Config:
    # Asegúrate de que los datos de conexión a MySQL son correctos
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root@localhost/proyecto_grado'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
