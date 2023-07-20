from flask import Blueprint, jsonify, request
import uuid
from src.v1.db.conexion import conexion


empleados=Blueprint('empleados_blueprint',__name__)

@empleados.route('/')
def home():
    try:
        resultado=[]
        conn=conexion()
        conn.conectar()
        resultado=conn.ejecutarquery("select * from tbcatempleadosprueba")
        conn.cerrar()
        return jsonify({'mensage':'{0}'.format(resultado)}),200
    except Exception as ex:
        return jsonify({'mensage':str(ex)}),500
