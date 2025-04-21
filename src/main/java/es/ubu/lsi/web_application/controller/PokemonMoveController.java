package es.ubu.lsi.web_application.controller;

import org.springframework.ui.ModelMap;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.beans.factory.annotation.Autowired;
import es.ubu.lsi.web_application.service.PokemonMoveService;

/**
 * Controlador web encargado de gestionar la vista de la página de los
 * movimientos de los Pokémon y actualizarla de acuerdo a los datos
 * obtenidos de la API.
 *
 * @author Aitor Blanco Fernández, abf1005@alu.ubu.es
 * @version 1.0.0, 21 de Abril de 2025.
 */

@Controller
public class PokemonMoveController {

    // Conectamos al controlador, el servicio responsable de obtener los movimientos
    // de los Pokémon desde la API.
    @Autowired
    private PokemonMoveService pokemonMoveService;

    /**
     * Muestra por pantalla la página de los movimientos de los Pokémon junto a
     * sus datos obtenidos desde la API a través del servicio.
     */
    @GetMapping("/moves")
    public String showPokemonMovePage(ModelMap pokemonMovePage) {
        // Mostramos en la vista los diferentes movimientos obtenidos desde la API.
        pokemonMovePage.addAttribute("moves", pokemonMoveService.getAllPokemonMoves());
        return "moves_list";
    }
}