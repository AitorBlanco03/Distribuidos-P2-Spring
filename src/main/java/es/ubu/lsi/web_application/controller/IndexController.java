package es.ubu.lsi.web_application.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

/**
 * Controlador web encargado de mostrar la página principal de
 * la aplicación web.
 *
 * @author Aitor Blanco Fernndez, abf1005@alu.ubu.es
 * @version 1.0.0, 17 de Abril de 2025.
 */

@Controller
public class IndexController {

    /**
     * Muestra por pantalla la página principal de nuestra aplicación
     * web.
     *
     * @return el nombre de la página HTML que se debe de rendizar.
     */
    @GetMapping("/")
    public String showMainPage() {
        return "index";
    }
}