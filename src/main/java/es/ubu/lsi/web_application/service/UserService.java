package es.ubu.lsi.web_application.service;

import es.ubu.lsi.web_application.dto.UserDTO;
import es.ubu.lsi.web_application.model.User;
import es.ubu.lsi.web_application.repository.UserRepository;
import org.springframework.stereotype.Service;
import org.springframework.beans.factory.annotation.Autowired;

/**
 * Servicio encargado de gestionar y tratar con los usuarios
 * dentro del sistema.
 *
 * @author Aitor Blanco Fernández, abf1005@alu.ubu.es
 * @version 1.0.0, 25 de Abril de 2025.
 */

@Service
public class UserService {

    // Conectamos al servicio, el repositorio que gestiona los datos de los usuarios.
    @Autowired
    private UserRepository userRepository;

    /**
     * Registra un usuario dentro del sistema con toda su información
     * y detalles.
     *
     * @param userDTO Usuario que se desea registrar dentro del sistema.
     */
    public void saveUser(UserDTO userDTO) {
        User user = new User();
        user.setFullName(userDTO.getFullName());
        user.setEmail(userDTO.getEmail());
        user.setPassword(userDTO.getPassword());
        userRepository.saveUser(user);
    }

    /**
     * Busca entre todos los usuarios, el usuario al que le pertenece
     * el email
     */
    public User searchUser(String email) {
        return userRepository.searchUser(email);
    }
}