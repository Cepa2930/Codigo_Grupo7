from Repositorios.RepositorioPartidos import RepositorioPartidos
from Modelos.Partidos import Partidos

class ControladorPartidos():
    def __init__(self):
       self.repositorioPartido = RepositorioPartidos()

    def index(self):
        return self.repositorioPartido.findAll()

    def create(self,infoPartidos):
        elPartido = Partidos(infoPartidos)
        return self.repositorioPartido.save(elPartido)

    def show(self,id):
        elPartido = Partidos(self.repositorioPartido.findById(id))
        return elPartido.__dict__


    def update(self,id,infoPartidos):
        elPartido = Partidos(self.repositorioPartido.findById(id))
        elPartido.nombre = infoPartidos['nombre']
        elPartido.frase = infoPartidos['frase']
        elPartido.activo = infoPartidos['activo']
        return self.repositorioPartido.save(elPartido)

    def delete(self,id):
        elPartido = Partidos(self.repositorioPartido.findById(id))
        elPartido.activo = False
        return self.repositorioPartido.save(elPartido)