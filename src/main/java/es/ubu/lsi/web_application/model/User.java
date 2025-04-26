package es.ubu.lsi.web_application.model;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;
import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;

/**
 * Modelo que define a un usuario y sus detalles dentro del
 * sistema.
 *
 * @author Aitor Blanco Fernández, 25 de Abril de 2025.
 * @version 1.0.0, 25 de Abril de 2025.
 */

@Getter
@Setter
@ToString
@NoArgsConstructor
@AllArgsConstructor
public class User {

    /** Campo que representa el ID y permite identificar de manera única a un usuario. */
    private Long id;

    /** Campo que representa el nombre completo del usuario. */
    private String fullName;

    /** Campo que representa el email del usuario. */
    private String email;

    /** Campo que representa la contraseña del usuario. */
    private String password;
}