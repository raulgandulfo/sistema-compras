from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    rol = db.Column(db.String(50), nullable=False)  # 'gerente', 'encargado', 'compras'

    pedidos = db.relationship('Pedido', backref='usuario', lazy=True)

class Proyecto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    activo = db.Column(db.Boolean, default=True)

    pedidos = db.relationship('Pedido', backref='proyecto', lazy=True)

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sector = db.Column(db.String(100), nullable=False)
    solicitante = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    unidad = db.Column(db.String(20), nullable=False)
    urgente = db.Column(db.Boolean, default=False)
    justificacion = db.Column(db.Text)
    estado = db.Column(db.String(50), default='pendiente')  # pendiente, autorizado, rechazado, comprado, recibido
    fecha_pedido = db.Column(db.DateTime, default=datetime.utcnow)

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    proyecto_id = db.Column(db.Integer, db.ForeignKey('proyecto.id'))

    presupuesto = db.relationship('Presupuesto', uselist=False, backref='pedido', lazy=True)

class Presupuesto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'), nullable=False)
    filename = db.Column(db.String(255), nullable=False)  # nombre del archivo de imagen o PDF
    fecha_carga = db.Column(db.DateTime, default=datetime.utcnow)
    aprobado = db.Column(db.Boolean, default=False)
