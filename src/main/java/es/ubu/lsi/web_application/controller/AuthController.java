package es.ubu.lsi.web_application.controller;

import es.ubu.lsi.web_application.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import es.ubu.lsi.web_application.dto.UserDTO;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

/**
 * Controlador web encargado de gestionar el flujo de autentificación y registro de usuarios
 * dentro de nuestra aplicación.
 *
 * Se encarga de mostrar las páginas relacionadas con el inicio de sesión y el registro de
 * usuarios. Además, gestiona la lógica necesaria para autentificar a los usuarios y procesar
 * el registro de nuevos usuarios dentro del sistema.
 *
 * @author Aitor Blanco Fernández, abf1005@alu.ubu.es
 * @version 1.2.0, 25 de Abril de 2025.
 */

@Controller
public class AuthController {

    // Conectamos al controlador, el servicio para tratar y manejar con los datos de los usuarios.
    @Autowired
    private UserService userService;

    /**
     * Muestra por pantalla la página y el formulario de inicio de sesión
     * de nuestra aplicación.
     *
     * @return el nombre de la página HTML que se debe de renderizar.
     */
    @GetMapping("/login")
    public String showLoginPage() {
        return "login";
    }

    /**
     * Muestra por pantalla la página y el formulario de registro de usuarios
     * de nuestra aplicación.
     *
     * @return el nombre de la página HTML que se debe de renderizar.
     */
    @GetMapping("/register")
    public String showRegisterPage(ModelMap registerPage) {
        UserDTO userDTO = new UserDTO();
        registerPage.addAttribute("user", userDTO);
        return "signup";
    }

    /**
     * Controla y gestiona la lógica para permitir el registro de un nuevo usuario
     * dentro del sistema.
     */
    @PostMapping("/register")
    public String registerUser(@ModelAttribute("user") UserDTO userDTO, ModelMap registerPage) {
        // Comprobamos la contraseña coincide en ambos campos.
        if (!userDTO.getPassword().equals(userDTO.getConfirmPassword())) {
            registerPage.addAttribute("errorMessage", "Las contraseñas no coinciden");
            return "signup";
        }

        // Si el registro es válido, se le registra dentro del sistema y le manda al home.
        userService.saveUser(userDTO);
        return "redirect:/home";
    }
}