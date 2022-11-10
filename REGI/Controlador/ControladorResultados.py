from Repositorios.RepositorioResultados import RepositorioResultados
from Repositorios.RepositorioCandidatos import RepositorioCandidatos
from Repositorios.RepositorioMesas import RepositorioMesas

from Modelos.Candidatos import Candidatos
from Modelos.Resultados import Resultados
from Modelos.Mesas import Mesas

class ControladorResultados():
    def __init__(self):
        self.repositorioResultado = RepositorioResultados()
        self.repositorioMesa = RepositorioMesas()
        self.repositorioCandidato = RepositorioCandidatos()

    def create(self,infoResultado, id_mesa, id_candidato):
        nuevoResultado =Resultados(infoResultado)
        elCandidato = Candidatos(self.repositorioCandidato.findById(id_candidato))
        laMesa = Mesas(self.repositorioMesa.findById(id_mesa))
        nuevoResultado.id_candidato = elCandidato
        nuevoResultado.id_mesa = laMesa
        return self.repositorioResultado.save(nuevoResultado)

    def index(self):
        return self.repositorioResultado.findAll()


    def show(self, id):
        elResultado = Resultados(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    def update(self,id,infoResulatos, id_mesa, id_candidato):
        elResultado = Resultados(self.repositorioResultado.findById(id))
        laMesa = Mesas(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidatos(self.repositorioCandidato.findById(id_candidato))
        elResultado.mesa = laMesa
        elResultado.candidato = elCandidato
        return self.repositorioResultado.save(elResultado)

    def delete(self,id):
        return self.repositorioResultado.delete(id)

    def getListarCandidatosMesa(self, id_mesa):
        return self.repositorioResultado.getListadoCandidatosInscritosMesa(id_mesa)

    def getListarMesasDeInscritoCandidato(self, id_candidato):
        return self.repositorioResultado.getListadoMesasCandidatoInscrito(id_candidato)

    def getMayorCedula(self):
        return self.repositorioResultado.getNumeroCedulaMayorCandidato()
