package es.ubu.lsi.web_application.service;

import es.ubu.lsi.web_application.dto.PokemonItemDTO;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.web.client.RestTemplate;
import org.springframework.stereotype.Service;
import com.fasterxml.jackson.databind.JsonNode;
import java.util.ArrayList;
import java.util.List;

/**
 * Servicio que se encarga de realizar una petición a la API para obtener todos los
 * objetos en el universo Pokémon.
 *
 * @author Aitor Blanco Fernández, abf1005@alu.ubu.es
 * @version 1.0.0, 20 de Abril de 2025.
 */

@Service
public class PokemonItemService {

    // Instanciamos los objetos para procesar las solicitudes HTTP y objetos/respuestas JSON.
    private final RestTemplate restTemplate = new RestTemplate();
    private final ObjectMapper objectMapper = new ObjectMapper();

    /**
     * Realiza una petición a la API y obtenemos todos los objetos en el universo Pokémon.
     *
     * @return Lista con los objetos (y sus características) obtenidos.
     */
    public List<PokemonItemDTO> getAllPokemonItems() {
        // Definimos la URL de la API que vamos a consumir y una lista para almacenar los resultados.
        String API_URL = "http://flask-api:5000/api/items";
        List<PokemonItemDTO> items = new ArrayList<>();

        try {
            // Realizamos una petición a la API y procesamos la respuesta obtenida.
            String response = restTemplate.getForObject(API_URL, String.class);
            JsonNode responseJSON = objectMapper.readTree(response);

            // Iteramos sobre la respuesta obtenida y, extraemos cada objeto y sus características.
            for (JsonNode responseItem : responseJSON) {
                String name = responseItem.get("name").asText();
                String category = responseItem.get("category").asText();
                String effect = responseItem.get("effect").asText();

                // Registramos el objeto obtenido dentro de los resultados.
                items.add(new PokemonItemDTO(name, category, effect));
            }
        } catch (Exception e) {
            System.out.println("Error al obtener la información de los objetos desde la API.");

            // Registramos un objeto desconocido para informar del error.
            items.add(new PokemonItemDTO(null, null, null));
        }

        // Devolvemos los objetos junto a sus características obtenidas.
        return items;
    }
}