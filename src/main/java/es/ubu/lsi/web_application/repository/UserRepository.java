package es.ubu.lsi.web_application.repository;

import es.ubu.lsi.web_application.model.User;
import org.springframework.stereotype.Repository;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

/**
 * Repositorio que gestiona y registra los usuarios del
 * sistema (en memoria).
 *
 * @author Aitor Blanco Fernández, abf1005@alu.ubu.es
 * @version 1.0.0, 25 de Abril de 2025.
 */

@Repository
public class UserRepository {

    // Diccionario para gestionar y registrar a los diferentes usuarios.
    private Map<String, User> users = new HashMap<>();
    private Long nextID = 1L;

    /**
     * Regsitra un usuario dentro del sistema.
     *
     * @param user Nuevo usuario dentro del sistema.
     */
    public void saveUser(User user) {
        user.setId(nextID++);
        users.put(user.getEmail(), user);
    }

    /**
     * Busca un usuario por su email de entre todos los usuarios.
     *
     * @param email Email asociado al usuario que se desea buscar.
     * @return El usuario encontrado después de la búsqueda.
     */
    public User searchUser(String email) {
        return users.get(email);
    }

    /**
     * Obtiene todos los diferentes usuarios que están en el sistema.
     *
     * @return Todos los usuarios dentro del sistema.
     */
    public Collection<User> obtainAll() {
        return users.values();
    }
}