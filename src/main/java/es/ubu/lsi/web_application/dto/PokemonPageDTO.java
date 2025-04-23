package es.ubu.lsi.web_application.dto;

import lombok.Getter;
import lombok.Setter;
import java.util.List;
import lombok.ToString;
import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;

/**
 * Data Transfer Object (DTO) que se encarga de representar una página de
 * la Pokédex. Se utiliza para transferir los datos desde el contrador hasta
 * la vista.
 *
 * @author Aitor Blanco Fernández, abf1005@alu.ubu.es
 * @version 1.0.0, 22 de Abril de 2025.
 */

@Getter
@Setter
@ToString
@NoArgsConstructor
@AllArgsConstructor
public class PokemonPageDTO {

    /** Campo que representa el enlace a la página anterior, o null si no hay enlace. */
    private String previousPage;

    /** Campo que representa el enlace a la página siguiente, o null si no hay enlace. */
    private String nextPage;

    /** Campo que representa la información de los Pokémons dentro de la página. */
    private List<PokemonInfoDTO> pokemonsInfo;
}