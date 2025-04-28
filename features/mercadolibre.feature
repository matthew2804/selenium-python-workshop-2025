Feature: Buscar mercadolibre
    Scenario: Buscar Iphone 13 
        Given el ususario se encuentra en la pagina de mercadolibre
        When el usuario escribe iphone 13 en el buscador
        Then aparece un resultado que contiene el texto iphone