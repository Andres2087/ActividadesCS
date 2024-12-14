
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import unittest
import time
from time import sleep

# Configurar opciones para el navegador Chrome
options = Options()
options.add_argument('--headless') # Ejecuta Chrome en modo headless
options.add_argument('--no-sandbox') # Recomendado en entornos de CI como GitHub Actions
options.add_argument('--disable-dev-shm-usage') # Ayuda a evitar algunos errores en contenedores

class AnimeFLVTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(options=options)

    def test_list_animes_en_emision(self):
        browser = self.browser
        browser.maximize_window()
        browser.get("https://www3.animeflv.net/")  

        contenedor = browser.find_element(By.ID, "mCSB_1")
        animes_list = contenedor.find_elements(By.TAG_NAME, "a")  

        res = []
        for anime in animes_list:
            res.append(anime.text)

        self.assertGreater(len(res), 0, "No se encontraron animes en emisión.")

        print("Animes en emisión:")
        for anime in res:
            print(anime)

    def test_busqueda_anime(self):
        browser = self.browser
        browser.maximize_window()
        browser.get("https://www3.animeflv.net/")  
        search = browser.find_element(By.ID, "search-anime")
        search.clear()
        search.send_keys("Naruto")
        search.submit()
        sleep(5) 
        results = browser.find_elements(By.CLASS_NAME, "ListAnimes")  # Ajusta la clase si es diferente
        self.assertGreater(len(results), 0, "No se encontraron resultados para 'Naruto'.")

        

       
        

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()