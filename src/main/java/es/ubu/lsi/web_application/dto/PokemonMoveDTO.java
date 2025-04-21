package es.ubu.lsi.web_application.dto;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;
import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;

/**
 * Data Transfer Object (DTO) que se encarga de representar un movimiento
 * Pokémon. Se utiliza para transferir los datos desde el controlador hasta la vista.
 *
 * @author Aitor Blanco Fernández, abf1005@alu.ubu.es
 * @version 1.0.0, 21 de Abril de 2025.
 */

@Getter
@Setter
@ToString
@NoArgsConstructor
@AllArgsConstructor
public class PokemonMoveDTO {

    /** Campo que representa el nombre del movimiento. */
    private String name;

    /** Campo que representa el tipo del movimiento. */
    private String type;

    /** Campo que representa la categoria del movimiento. */
    private String category;

    /** Campo que representa la potencia del movimiento. */
    private String power;

    /** Campo que representa la precisión del movimiento. */
    private String accuracy;

    /** Campo que representa los puntos de poder (o PP) del movimiento. */
    private String pp;

    /** Campo que representa el efecto/descripción del movimiento. */
    private String effect;
}