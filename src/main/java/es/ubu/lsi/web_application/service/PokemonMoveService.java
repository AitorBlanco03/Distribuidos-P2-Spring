package es.ubu.lsi.web_application.service;

import es.ubu.lsi.web_application.dto.PokemonMoveDTO;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.web.client.RestTemplate;
import org.springframework.stereotype.Service;
import com.fasterxml.jackson.databind.JsonNode;
import java.util.ArrayList;
import java.util.List;

/**
 * Servicio que se encarga de realizar una petición a la API para
 * obtener todos los movimientos Pokémon disponibles.
 *
 * @author Aitor Blanco Fernández, abf1005@alu.ubu.es
 * @version 1.0.0, 21 de Abril de 2025.s
 */

@Service
public class PokemonMoveService {

    // Instanciamos los objetos para procesar las solicitudes HTTP y objetos/respuestas JSON.
    private final RestTemplate restTemplate = new RestTemplate();
    private final ObjectMapper objectMapper = new ObjectMapper();

    /**
     * Realiza una petición a la API y obtenemos todos los movimientos disponibles en el
     * universo Pokémon.
     *
     * @return Lista con los movimientos Pokémons (y sus características) obtenidos.
     */
    public List<PokemonMoveDTO> getAllPokemonMoves() {
        // Definimos la URL de la API que vamos a consumir y una lista para almacenar los resultados obtenidos.
        String API_URL = "http://localhost:5000/api/moves";
        List<PokemonMoveDTO> moves = new ArrayList<>();

        try {
            // Realizamos una petición a la API y procesamos la respuesta obtenida.
            String response = restTemplate.getForObject(API_URL, String.class);
            JsonNode responseJSON = objectMapper.readTree(response);

            // Iteramos sobre la respuesta obtenida, y extraemos cada movimiento y sus características.
            for (JsonNode responseItem : responseJSON) {
                String name = responseItem.get("name").asText();
                String type = responseItem.get("type").asText();
                String category = responseItem.get("category").asText();
                String power = responseItem.get("power").asText();
                String accuracy = responseItem.get("accuracy").asText();
                String pp = responseItem.get("pp").asText();
                String effect = responseItem.get("effect").asText();

                // Registramos el movimiento obtenido dentro de los resultados.
                PokemonMoveDTO moveDTO = new PokemonMoveDTO(name, type, category, power, accuracy, pp, effect);
                moves.add(moveDTO);
            }
        } catch (Exception e) {
            System.out.println("Error al obtener la información de los movimientos desde la API.");

            // Registramos un objeto desconocido para informar del error.
            PokemonMoveDTO moveDTO = new PokemonMoveDTO("???", "", "", "???", "???", "???", "???");
            moves.add(moveDTO);
        }

        // Devolvemos los movimientos junto a sus características obtenidas.
        return moves;
    }
}