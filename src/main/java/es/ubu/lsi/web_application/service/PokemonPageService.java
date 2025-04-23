package es.ubu.lsi.web_application.service;

import es.ubu.lsi.web_application.dto.PokemonInfoDTO;
import es.ubu.lsi.web_application.dto.PokemonPageDTO;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import com.fasterxml.jackson.databind.JsonNode;
import java.util.ArrayList;
import java.util.List;

/**
 * Servicio que se encarga de obtener la página y su información desde la
 * API.
 *
 * @author Aitor Blanco Fernández, abf1005@alu.ubu.es
 * @version 1.0.0, 22 de Abril de 2025.
 */

@Service
public class PokemonPageService {

    // Instanciamos los objetos para procesar solicitudes HTTP y objetos/respuetas JSON.
    private final RestTemplate restTemplate = new RestTemplate();
    private final ObjectMapper objectMapper = new ObjectMapper();

    /**
     * Solicita a la API la página solicitada junto a toda su información.
     *
     * @param pageNumber Número de la página que se desea obtener de la API.
     * @return La página y su información obtenida desde la API.
     */
    public PokemonPageDTO getPokemonPage(int pageNumber) {
        // Inicializamos y definimos la URL de la API para obtener la página.
        String API_URL = "http://localhost:5000/api/pokemons?page=" + pageNumber;

        try {
            // Realizamos una petición a la API obtener esa página.
            String response = restTemplate.getForObject(API_URL, String.class);
            JsonNode responseJSON = objectMapper.readTree(response);

            // Obtenemos la página anterior y la página siguiente de la información obtenida.
            String previousPage = responseJSON.get("previous").asText(null);
            String nextPage = responseJSON.get("next").asText(null);

            // Obtenemos y procesamos la información de los Pokémons asociados a esta página.
            List<PokemonInfoDTO> pokemonsInfo = new ArrayList<>();
            JsonNode pokemonJSON = responseJSON.get("pokemons");

            // De cada uno de los Pokémon, obtenemos su ID, nombre, sprite y tipos.
            for (JsonNode pokemonNode : pokemonJSON) {
                int id = pokemonNode.get("id").asInt();
                String name = pokemonNode.get("name").asText();
                String sprite = pokemonNode.get("sprite").asText();

                List<String> types = new ArrayList<>();
                for (JsonNode typeNode : pokemonNode.get("types")) {
                    types.add(typeNode.asText());
                }
                pokemonsInfo.add(new PokemonInfoDTO(id, name, sprite, types));
            }
            return new PokemonPageDTO(previousPage, nextPage, pokemonsInfo);
        } catch (Exception e) {
            System.out.println("Error al obtener la información de la página " + pageNumber + " desde la API.");

            // Registramos una página vacía en caso de que produzca algún error.
            return new PokemonPageDTO(null, null, new ArrayList<>());
        }
    }
}