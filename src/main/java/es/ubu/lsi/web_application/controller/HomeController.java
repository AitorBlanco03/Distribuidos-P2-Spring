package es.ubu.lsi.web_application.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

/**
 * Controlador web encargado de mostrar la pantalla de home de
 * la aplicación web.
 *
 * @author Aitor Blanco Fernández, abf1005@alu.ubu.es
 * @version 1.0.0, 22 de Abril de 2025.
 */

@Controller
public class HomeController {

    /**
     * Muestra por pantalla la página home de nuestra aplicación
     * web.
     *
     * @return el nombre de la página HTML que se debe de renderizar.
     */
    @GetMapping("/home")
    public String showHomePage() {
        return "home";
    }
}