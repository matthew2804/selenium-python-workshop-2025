Feature: Login de intu
    Scenario: Credenciales incorrectas intu
        Given el ususario se encuentra en la pagina de login de intu 
        When el usuario escribe credenciales erroneas 
        Then aparece un mensaje de error 