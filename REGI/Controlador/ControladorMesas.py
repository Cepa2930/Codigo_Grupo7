from Repositorios.RepositorioMesas import RepositorioMesas
from Modelos.Mesas import Mesas

class ControladorMesas():
    def __init__(self):
        self.repositorioMesas = RepositorioMesas()

    def index(self):
        return self.repositorioMesas.findAll()


    def create(self,infoMesas):
        laMesa = Mesas(infoMesas)
        return self.repositorioMesas.save(laMesa)

    def show(self,id):
        mesa = Mesas(self.repositorioMesas.findById(id))
        return mesa.__dict__

    def update(self,id,infoMesas):
        mesa = Mesas(self.repositorioMesas.findById(id))
        mesa.numero_mesa = infoMesas['numero_mesa']
        mesa.cantidad_inscritos = infoMesas['cantidad-inscritos']
        mesa.activo = infoMesas ['activo']
        return self.repositorioMesas.save(mesa)

    def delete(self,id):
        mesa = Mesas(self.repositorioMesas.findById(id))
        mesa.activo = False
        return self.repositorioMesas.save(mesa)