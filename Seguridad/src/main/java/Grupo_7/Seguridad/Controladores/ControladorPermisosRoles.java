package Grupo_7.Seguridad.Controladores;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import Grupo_7.Seguridad.Modelos.Permiso;
import Grupo_7.Seguridad.Modelos.permisosRoles;
import Grupo_7.Seguridad.Modelos.Rol;
import Grupo_7.Seguridad.Repositorios.RepositorioPermiso;
import Grupo_7.Seguridad.Repositorios.RepositorioPermisosRoles;
import Grupo_7.Seguridad.Repositorios.RepositorioRol;
import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/permisos-roles")
public class ControladorPermisosRoles {
    @Autowired
    private RepositorioPermisosRoles miRepositorioPermisoRoles;

    @Autowired
    private RepositorioPermiso miRepositorioPermiso;

    @Autowired
    private RepositorioRol miRepositorioRol;


    @GetMapping("")
    public List<permisosRoles> index(){
        return this.miRepositorioPermisoRoles.findAll();
    }

    /**
     * Asignación rol y permiso
     * @param id_rol
     * @param id_permiso
     * @return
     */
    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping("rol/{id_rol}/permiso/{id_permiso}")
    public permisosRoles create(@PathVariable String id_rol,@PathVariable String id_permiso){
        permisosRoles nuevo=new permisosRoles();
        Rol elRol=this.miRepositorioRol.findById(id_rol).get();
        Permiso elPermiso=this.miRepositorioPermiso.findById(id_permiso).get();
        if (elRol!=null && elPermiso!=null){
            nuevo.setPermiso(elPermiso);
            nuevo.setRol(elRol);
            return this.miRepositorioPermisoRoles.save(nuevo);
        }else{
            return null;
        }
    }
    @GetMapping("{id}")
    public permisosRoles show(@PathVariable String id){
        permisosRoles PermisosRolesActual=this.miRepositorioPermisoRoles
                .findById(id)
                .orElse(null);
        return PermisosRolesActual;
    }

    /**
     * Modificación Rol y Permiso
     * @param id
     * @param id_rol
     * @param id_permiso
     * @return
     */
    @PutMapping("{id}/rol/{id_rol}/permiso/{id_permiso}")
    public permisosRoles update(@PathVariable String id,@PathVariable String id_rol,@PathVariable String id_permiso){
        permisosRoles PermisosRolesActual=this.miRepositorioPermisoRoles
                .findById(id)
                .orElse(null);
        Rol elRol=this.miRepositorioRol.findById(id_rol).get();
        Permiso elPermiso=this.miRepositorioPermiso.findById(id_permiso).get();
        if(PermisosRolesActual!=null && elPermiso!=null && elRol!=null){
            PermisosRolesActual.setPermiso(elPermiso);
            PermisosRolesActual.setRol(elRol);
            return this.miRepositorioPermisoRoles.save(PermisosRolesActual);
        }else{
            return null;
        }
    }

    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id){
        permisosRoles permisosRolesActual=this.miRepositorioPermisoRoles
                .findById(id)
                .orElse(null);
        if (permisosRolesActual!=null){
            this.miRepositorioPermisoRoles.delete(permisosRolesActual);
        }
    }
}
