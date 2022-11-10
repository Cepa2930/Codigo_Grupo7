from flask import jsonify, request, Blueprint
from Controlador.ControladorMesas import ControladorMesas

miControladorMesas = ControladorMesas()

mesas = Blueprint('mesas', __name__)


@mesas.route("/Mesas", methods=['GET'])                    #funciona
def getMesas():
    json = miControladorMesas.index()
    return jsonify(json)


@mesas.route("/Mesas/<string:id>", methods=['GET'])        #funciona
def getMesa(id):
    json = miControladorMesas.show(id)
    return jsonify(json)


@mesas.route("/Mesas", methods=['POST'])                   #funciona
def crearMesas():
    data = request.get_json()
    json = miControladorMesas.create(data)
    return jsonify(json)


@mesas.route("/Mesas/<string:id>", methods=['PUT'])        #funciona siempre y cuando se incluyan todos los campos en el request
def modificarMesas(id):
    data = request.get_json()
    json = miControladorMesas.update(id, data)
    return jsonify(json)


@mesas.route("/Mesas/<string:id>", methods=['DELETE'])     #funciona
def eliminarMesas(id):
    json = miControladorMesas.delete(id)
    return jsonify(json)
