from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from warnings import filterwarnings
filterwarnings("ignore")

browser = webdriver.Chrome()

browser.get("https://demo.guru99.com/test/login.html")
email_field = browser.find_element(By.ID, "email")
email_field.clear()
email_field.send_keys('correoprueba@gmail.com')
password_field = browser.find_element(By.ID, "passwd")
password_field.clear()
password_field.send_keys('password1234xD')
sign_in_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
sign_in_button.send_keys(Keys.ENTER)

try:
    print("Navegador abierto. Presiona Ctrl+C para salir.")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nCerrando navegador...")
    browser.quit()
