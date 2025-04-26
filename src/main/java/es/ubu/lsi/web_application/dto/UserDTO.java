package es.ubu.lsi.web_application.dto;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;
import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;

/**
 * DTO (Data Transfer Object) para almacenar la información de los
 * usuarios dentro del sistema.
 * Sirve para transferir los datos del usuario a la vista.
 *
 * @author Aitor Blanco Fernández, abf1005@alu.ubu.es
 * @version 1.0.0, 25 de Abril de 2025.
 */

@Getter
@Setter
@ToString
@NoArgsConstructor
@AllArgsConstructor
public class UserDTO {

    /** Campo que representa el nombre completo del usuario dentro del sistema. */
    private String fullName;

    /** Campo que representa el email del usuario dentro del sistema. */
    private String email;

    /** Campo que representa la contraseña del usuario dentro del sistema. */
    private String password;

    /** Campo para confirmar la contraseña del usuario unicamente dentro del registro. */
    private String confirmPassword;
}