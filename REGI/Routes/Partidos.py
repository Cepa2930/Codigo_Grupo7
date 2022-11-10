from flask import jsonify, request, Blueprint
from Controlador.ControladorPartidos import ControladorPartidos

miControladorPartidos = ControladorPartidos()

partidos = Blueprint('partidos', __name__)


@partidos.route("/Partidos/<string:id>", methods=['GET'])             #funciona
def getPartidos(id):
    json = miControladorPartidos.show(id)
    return jsonify(json)


@partidos.route("/Partidos", methods=['GET'])                         #funciona
def getPartidosAll():
    json = miControladorPartidos.index()
    return jsonify(json)


@partidos.route("/Partidos", methods=['POST'])                        #funciona
def postPartidos():
    data = request.get_json()
    json = miControladorPartidos.create(data)
    return jsonify(json)


@partidos.route("/Partidos/<string:id>", methods=['PUT'])             #funciona siempre y cuando se incluyan todos los campos en el request
def putPartidos(id):
    data = request.get_json()
    json = miControladorPartidos.update(id, data)
    return jsonify(json)


@partidos.route("/Partidos/<string:id>", methods=['DELETE'])          #funciona
def deletePartidos(id):
    json = miControladorPartidos.delete(id)
    return jsonify(json)
