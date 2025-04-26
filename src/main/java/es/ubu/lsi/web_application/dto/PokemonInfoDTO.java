package es.ubu.lsi.web_application.dto;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;
import java.util.List;
import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;

/**
 * Data Transfer Object (DTO) que se encarga de representar los detalles de los
 * Pokémons dentro de una página de la Pokédex.
 *
 * @author Aitor Blanco Fernández, abf1005@alu.ubu.es
 * @version 1.0.0, 22 de Abril de 2025.
 */

@Getter
@Setter
@ToString
@NoArgsConstructor
@AllArgsConstructor
public class PokemonInfoDTO {

    /** Identificador único para identificar de manera única a un Pokémon. */
    private int id;

    /** Nombre del Pokémon. */
    private String name;

    /** URL con la imagen/sprite del Pokémon. */
    private String sprite;

    /** Lista con los tipos asociados al Pokémon. */
    private List<String> types;
}