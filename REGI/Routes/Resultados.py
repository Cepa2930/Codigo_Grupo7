from flask import jsonify, request, Blueprint
from Controlador.ControladorResultados import ControladorResultados
from Controlador.ControladorPartidos import ControladorPartidos
from Controlador.ControladorCandidatos import ControladorCandidatos
from Controlador.ControladorMesas import ControladorMesas

miControladorPartidos = ControladorPartidos()
miControladorResultados = ControladorResultados()
miControladorCandidatos = ControladorCandidatos()
miControladorMesas = ControladorMesas()

resultados = Blueprint('resultados', __name__)

#Obtener todos los resultados
@resultados.route("/resultados", methods = ["GET"])
def getResultados():
    json = miControladorResultados.index()
    return jsonify(json)


#Añadir un resultado a una mesa
@resultados.route("/resultados/mesa/<string:id_mesa>/candidato/<string:id_candidato>", methods =["POST"])
def crearResultado(id_mesa, id_candidato):
    data = request.get_json()
    json = miControladorResultados.create(data, id_mesa, id_candidato)
    return jsonify(json)


#Obtener resultado especifico
@resultados.route("/resultados/<string:id>", methods=["GET"])
def getResultado(id):
    json = miControladorResultados.show(id)
    return jsonify(json)

#Modificar un resultado
@resultados.route("/resultados/<string:id_resultado>/mesa/<string:id_mesa>/candidato/<string:id_candidato>", methods=["PUT"])
def modificarResultado(id_resultado, id_mesa, id_candidato):
    data={}
    json = miControladorResultados.update(id_resultado, data, id_mesa, id_candidato)
    return jsonify(json)

#Eliminar Resultado
@resultados.route("/resultados/<string:id>", methods=["DELETE"])
def borrarResultado(id):
    json = miControladorResultados.delete(id)
    return jsonify(json)

#Buscar los candidatos votados en una mesa
@resultados.route("/resultados/mesa/<string:id_mesa>", methods=["GET"])
def inscritosMesa(id_mesa):
    json = miControladorResultados.getListarCandidatosMesa(id_mesa)
    return jsonify(json)

#Buscar el candidato en las mesas
@resultados.route("/resultados/mesas/<string:id_candidato>", methods=["GET"])
def inscritoEnMesas(id_candidato):
    json = miControladorResultados.getListarMesasDeInscritoCandidato(id_candidato)
    return jsonify(json)

#Buscar mayor cédula
@resultados.route("/resultados/maxdocument", methods=["GET"])
def getMaxDocument():
    json = miControladorResultados.getMayorCedula()
    return jsonify(json)