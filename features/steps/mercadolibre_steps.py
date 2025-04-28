from behave import given, when, then 
from selenium import webdriver
from pages.mercadolibre_page import mercadolibreSearch, searchIphone

@given('el ususario se encuentra en la pagina de mercadolibre')
def step_given_mercadolibre(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.mercadolibre.com.co/')
    context.search_page = mercadolibreSearch(context.driver)  # objeto para buscar
    context.result_page = searchIphone(context.driver)         # objeto para verificar resultados

@when('el usuario escribe iphone 13 en el buscador')
def step_when_mercadolibre(context):
    context.search_page.search("iphone 13")


@then('aparece un resultado que contiene el texto iphone')
def step_then_mercadolibre(context):
    assert "iphone 13" in context.result_page.isElementPresent().lower()



    #ui-search-results ui-search-results--without-disclaimer