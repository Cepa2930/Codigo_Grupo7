from Repositorios.RepositorioCandidatos import RepositorioCandidatos
from Repositorios.RepositorioPartidos import RepositorioPartidos
from Modelos.Candidatos import Candidatos
from Modelos.Partidos import Partidos


class ControladorCandidatos():
    def __init__(self):
        self.repositorioCandidatos = RepositorioCandidatos()
        self.repositorioPartido = RepositorioPartidos()

    def index(self):
        return self.repositorioCandidatos.findAll()

    def create(self, infoCandidato):
        elCandidato = Candidatos(infoCandidato)
        return self.repositorioCandidatos.save(elCandidato)

    def show(self, id):
        print(id)
        elCandidato = Candidatos(self.repositorioCandidatos.findById(id))

        return elCandidato.__dict__


    def update(self, id, infoCandidato):
        elCandidato = Candidatos(self.repositorioCandidatos.findById(id))
        elCandidato.nombres = infoCandidato["nombres"]
        elCandidato.apellidos = infoCandidato["apellidos"]
        elCandidato.numero_resolucion = infoCandidato["numero_resolucion"]
        elCandidato.id_partido = infoCandidato["id_partido"]
        elCandidato.activo = infoCandidato["activo"]
        return self.repositorioCandidatos.save(elCandidato)

    def delete(self, id):
        elCandidato = Candidatos(self.repositorioCandidatos.findById(id))
        elCandidato.activo = False
        return self.repositorioCandidatos.save(elCandidato)

