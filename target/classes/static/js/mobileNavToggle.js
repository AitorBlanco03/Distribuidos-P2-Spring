/**
 * Módulo JS encargado de controlar y gestionar la visibilidad del menú
 * de navegación de nuestra aplicación en dispositivos móviles.
 *
 * @author Aitor Blanco Fernández, abf1005@alu.ubu.es
 * @version 1.0.0, 18 de Abril de 2025.
 */

document.addEventListener("DOMContentLoaded", () => {

    // Obtenemos el ícono y el menú de navegación dentro de la página web.
    const toggleButton = document.getElementById("menu-toggle");
    const mobileMenu = document.getElementById("mobile-menu");

    // Creamos un evento para controlar y gestionar la visibilidad del menú cuando se hace click al ícono del menú.
    toggleButton.addEventListener("click", () => {
        mobileMenu.classList.toggle("hidden");
    })
})