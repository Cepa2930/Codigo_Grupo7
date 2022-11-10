package Grupo_7.Seguridad.Repositorios;

import Grupo_7.Seguridad.Modelos.Rol;
import org.springframework.data.mongodb.repository.MongoRepository;


public interface RepositorioRol extends MongoRepository<Rol,String> {
}
