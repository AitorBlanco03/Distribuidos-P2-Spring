package es.ubu.lsi.web_application.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

/**
 * Controlador web encargado de gestionar la vista de la página de los
 * Pokémons y actualizarla de acuerdo a los datos obtenidos de la API.
 *
 * @author Aitor Blanco Fernández, abf1005@alu.ubu.es
 * @version 1.0.0, 22 de Abril de 2025.
 */

@Controller
public class PokemonInfoController {

    /**
     * Muestra por pantalla la página de Pokémons y la actualiza en función de
     * los datos obtenidos a través de la API.
     *
     * @return el nombre de la página HTML que se debe de renderizar.
     */
    @GetMapping("/pokemons")
    public String showPokedexPage() {
        return "pokedex";
    }
}