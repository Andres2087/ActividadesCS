
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import unittest
import time
from time import sleep

class AnimeFLVTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_list_animes_en_emision(self):
        browser = self.browser
        browser.maximize_window()
        browser.get("https://www3.animeflv.net/")  
        self.assertIn("AnimeFLV", browser.title)

        contenedor = browser.find_element(By.ID, "mCSB_1")
        animes_list = contenedor.find_elements(By.TAG_NAME, "a")  

        print("Animes en emisión:")
        for anime in animes_list:
            print(anime.text)

    def test_busqueda_anime(self):
        browser = self.browser
        browser.maximize_window()
        browser.get("https://www3.animeflv.net/")  
        self.assertIn("AnimeFLV", browser.title)
        search = browser.find_element(By.ID, "search-anime")
        search.clear()
        search.send_keys("Naruto")
        search.submit()
        

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()