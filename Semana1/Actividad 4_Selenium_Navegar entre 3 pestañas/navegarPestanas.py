from selenium import webdriver
import time

from warnings import filterwarnings
filterwarnings("ignore")

browser = webdriver.Chrome()
browser.get("https://www.twitch.tv/")
time.sleep(3)
browser.execute_script("window.open('');")  
time.sleep(3)
browser.switch_to.window(browser.window_handles[1])  
browser.get("https://store.steampowered.com/?l=spanish")
time.sleep(3)
browser.execute_script("window.open('');") 
time.sleep(3)
browser.switch_to.window(browser.window_handles[2]) 
browser.get("https://www.mercadolibre.com.co")
time.sleep(2)
browser.switch_to.window(browser.window_handles[0])  
time.sleep(2)
browser.switch_to.window(browser.window_handles[1])  
time.sleep(2)
browser.switch_to.window(browser.window_handles[2])  
time.sleep(2)
browser.switch_to.window(browser.window_handles[1]) 
time.sleep(2)
browser.switch_to.window(browser.window_handles[0]) 


try:
    print("Navegador abierto. Presiona Ctrl+C para salir.")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nCerrando navegador...")
    browser.quit()
