package Grupo_7.Seguridad.Repositorios;
import Grupo_7.Seguridad.Modelos.Usuario;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioUsuario extends MongoRepository<Usuario,String> {
}