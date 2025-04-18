package es.ubu.lsi.web_application.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

/**
 * Controlador web encargado de gestionar el flujo de autentificación y registro de usuarios
 * dentro de nuestra aplicación.
 *
 * Se encarga de mostrar las páginas relacionadas con el inicio de sesión y el registro de
 * usuarios. Además, gestiona la lógica necesaria para autentificar a los usuarios y procesar
 * el registro de nuevos usuarios dentro del sistema.
 *
 * @author Aitor Blanco Fernández, abf1005@alu.ubu.es
 * @version 1.1.0, 18 de Abril de 2026.
 */

@Controller
public class AuthController {

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
    public String showRegisterPage() {
        return "signup";
    }
}