package Grupo_7.Seguridad.Repositorios;

import Grupo_7.Seguridad.Modelos.Permiso;
import org.springframework.data.mongodb.repository.MongoRepository;


public interface RepositorioPermiso extends MongoRepository<Permiso,String> {
}