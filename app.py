from flask import Flask, render_template, request, redirect, url_for, session
from config import Config
from models import db, Usuario
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'supersecreto123'
db.init_app(app)

with app.app_context():
    db.create_all()

    # Crear usuario admin si no existe
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

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = Usuario.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            session['usuario'] = user.username
            session['rol'] = user.rol
            return redirect(url_for('dashboard'))
        else:
            error = 'Usuario o contraseña incorrectos'
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return f"Bienvenido {session['usuario']} - Rol: {session['rol']} <br><a href='/logout'>Cerrar sesión</a>"

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
