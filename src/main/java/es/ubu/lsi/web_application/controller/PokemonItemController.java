package es.ubu.lsi.web_application.controller;

import org.springframework.ui.ModelMap;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.beans.factory.annotation.Autowired;
import es.ubu.lsi.web_application.service.PokemonItemService;

/**
 * Controlador web encargado de gestionar la vista de la página de los objetos Pokémon y
 * actualizarla de acuerda a los datos obtenidos de la API.
 *
 * @author Aitor Blanco Fernández, abf1005@alu.ubu.es
 * @version 1.0.0, 20 de Abril de 2025.
 */

@Controller
public class PokemonItemController {

    // Conectamos al controlador, el servicio resposable de obtener los objetos Pokémons desde la API.
    @Autowired
    private PokemonItemService pokemonItemService;

    /**
     * Muestra por pantalla la página de los objetos Pokémons junto a sus datos obtenidos desde
     * la API a través del servicio.
     */
    @GetMapping("/items")
    public String showPokemonItemPage(ModelMap pokemonItemPage) {
        // Mostramos en la vista los diferentes objetos obtenidos desde la API.
        pokemonItemPage.addAttribute("items", pokemonItemService.getAllPokemonItems());
        return "items_list";
    }
}