from flask import jsonify, request, Blueprint
from Controlador.ControladorCandidatos import ControladorCandidatos

miControladorCandidatos = ControladorCandidatos()

candidato = Blueprint('candidato', __name__)


@candidato.route("/Candidatos/<string:id>", methods=['GET'])       #funciona
def getCandidatos(id):
    json = miControladorCandidatos.show(id)
    return jsonify(json)


@candidato.route("/Candidatos", methods=['GET'])                   #funciona
def getCandidatosAll():
    json = miControladorCandidatos.index()
    return jsonify(json)


@candidato.route("/Candidatos", methods=['POST'])                  #funciona
def postCandidatos():
    data = request.get_json()
    json = miControladorCandidatos.create(data)
    return jsonify(json)


@candidato.route("/Candidatos/<string:id>", methods=['PUT'])       #funciona siempre y cuando se incluyan todos los campos en el request
def putCandidatos(id):
    data = request.get_json()
    json = miControladorCandidatos.update(id, data)
    return jsonify(json)


@candidato.route("/Candidatos/<string:id>", methods=['DELETE'])    #funciona
def deleteCandidatos(id):
    json = miControladorCandidatos.delete(id)
    return jsonify(json)

