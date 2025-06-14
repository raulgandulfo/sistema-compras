from models import db, Usuario
from werkzeug.security import generate_password_hash
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    if not Usuario.query.filter_by(username='admin').first():
        nuevo = Usuario(
            nombre='Administrador',
            username='admin',
            password=generate_password_hash('admin123'),
            rol='gerente'
        )
        db.session.add(nuevo)
        db.session.commit()
        print("✅ Usuario 'admin' creado")
    else:
        print("⚠️ Usuario 'admin' ya existe")
