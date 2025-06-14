from flask import Flask
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

# Página inicial de prueba
@app.route('/')
def index():
    return '¡App de sistema de compras funcionando en Render!'

# 🧠 Esto importa y ejecuta create_admin.py
import create_admin

if __name__ == '__main__':
    app.run(debug=True)
