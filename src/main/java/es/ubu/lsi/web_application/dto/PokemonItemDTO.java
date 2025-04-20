package es.ubu.lsi.web_application.dto;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;
import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;

/**
 * Data Transfer Object (DTO) que se encarga de representar un objeto del universo
 * Pokémon. Se utiliza para transferir los datos desde el controlador hasta la vista.
 *
 * @author Aitor Blanco Fernández, abf1005@alu.ubu.es
 * @version 1.0.0, 20 de Abril de 2025.
 */

@Getter
@Setter
@ToString
@NoArgsConstructor
@AllArgsConstructor
public class PokemonItemDTO {

    /** Campo que representa el nombre del objeto. */
    private String name;

    /** Campo que representa la categoria a la que pertenece el objeto. */
    private String category;

    /** Campo que representa el efecto/descripción que proporciona el objeto. */
    private String effect;
}