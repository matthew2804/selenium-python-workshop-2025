import unittest
import time
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        """
        Método que se ejecuta antes de cada prueba. Inicializa el navegador y realiza login.
        """
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.login_page = LoginPage(self.driver)
        self.login_page.login("standard_user", "secret_sauce")
        self.inventory_page = InventoryPage(self.driver)

    def test_add_single_product_to_cart(self):
        """
        Verifica que se puede agregar un producto al carrito y que el contador muestra 1.
        """
        self.inventory_page.add_product_to_cart("Sauce Labs Backpack")
        cart_count = self.inventory_page.get_cart_count()
        time.sleep(3)
        self.assertEqual(cart_count, "1", "El número de productos en el carrito no es correcto.")

    def tearDown(self):
        """
        Cierra el navegador después de cada prueba.
        """
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
