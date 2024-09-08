from app import app  # Importar la app desde app.py
from endpoints.login import login_bp
from endpoints.register import register_bp

# Registrar los blueprints
app.register_blueprint(login_bp, url_prefix='/api')
app.register_blueprint(register_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
