package es.ubu.lsi.web_application.controller;

import org.springframework.ui.ModelMap;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.beans.factory.annotation.Autowired;
import es.ubu.lsi.web_application.service.PokemonPageService;
import org.springframework.web.bind.annotation.RequestParam;
import es.ubu.lsi.web_application.dto.PokemonPageDTO;

/**
 * Controlador web encargado de gestionar la vista de la página de los
 * Pokémons y actualizarla de acuerdo a los datos obtenidos de la API.
 *
 * @author Aitor Blanco Fernández, abf1005@alu.ubu.es
 * @version 1.1.0, 22 de Abril de 2025.
 */

@Controller
public class PokemonInfoController {

    // Conectamos al controlador, el servicio responsable de obtener la información
    // de las páginas.
    @Autowired
    private PokemonPageService pokemonPageService;

    // Contador interno encargado de controlar la página de la Pokédex que se desea renderizar.
    int currentPage = 0;

    /**
     * Muestra por pantalla la página de con los Pokémons y la actualiza en función a
     * la página de la Pokédex que se desea renderiizar.
     *
     * @param pageNumber Número de la página Pokédex que queremos mostrar (por defecto, es 1).
     * @param pokedexPage Modelo que se usará para mandar los datos de la página a la vista.
     * @return Nombre de la página HTML que se debe de renderizar.
     */
    @GetMapping("/pokemons")
    public String showPokedexPage(@RequestParam(name = "pageNumber", defaultValue = "0") int pageNumber, ModelMap pokedexPage) {
        // Actualizamos el contador asociado a la página actual.
        currentPage = pageNumber;

        // Obtenemos y mostramos los detalles de la página.
        PokemonPageDTO pageData = pokemonPageService.getPokemonPage(pageNumber);
        pokedexPage.addAttribute("previousPage", pageData.getPreviousPage());
        pokedexPage.addAttribute("pokemons", pageData.getPokemonsInfo());
        pokedexPage.addAttribute("nextPage", pageData.getNextPage());
        return "pokedex";
    }

    /**
     * Controlador que se encarga de mostrar y cargar la anterior página
     * al hacer click en "Anterior".
     *
     * @param pokedexPage Modelo que se usará para mandar los datos de la página a la vista.
     */
    @GetMapping("/pokemons/previous")
    public String showPreviousPage(ModelMap pokedexPage) {
        return showPokedexPage(currentPage - 1, pokedexPage);
    }

    /**
     * Controlador que se encarga de mostrar y cargar la página siguiente
     * al hacer click en "Siguiente".
     *
     * @param pokedexPage Modelo que se usará para mandar los datos de la página a la vista.
     */
    @GetMapping("/pokemons/next")
    public String showNextPage(ModelMap pokedexPage) {
        return showPokedexPage(currentPage + 1, pokedexPage);
    }
}