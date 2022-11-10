package Grupo_7.Seguridad.Repositorios;

import org.springframework.data.mongodb.repository.MongoRepository;
import Grupo_7.Seguridad.Modelos.permisosRoles;


public interface RepositorioPermisosRoles extends MongoRepository<permisosRoles,String> {
}