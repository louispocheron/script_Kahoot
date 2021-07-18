# doc utilisé : 'https://selenium-python.readthedocs.io/' !! 'https://sites.google.com/a/chromium.org/chromedriver/downloads'
# dans le terminal windows installer selenium avec la codmmande 'pip install selenium'
# puis importez le driver de votre navigateur !!ATTENTION CHOISSISEZ LA BONNE VERSION OU CA NE MARCHERA PAS
from selenium import webdriver 

# creer variable pour declencher le driver
driver = webdriver.Chrome(executable_path = "chromedriver.exe")
driver.get("https://kahoot.it/")

# mettre l'id de l'input du code pin kahoot, puis mettre le code pin du jeu 
pin_input = driver.find_element_by_id("game-input")
pin_input.send_keys("7664929")

# recuper le bouton pour submit le code pin, et cliquez dessus 
submit_pin = driver.find_element_by_css_selector("button")
submit_pin.click()

# changement de page et trouver l'input et mettre son pseudo dedans
driver1 = webdriver.Chrome(executable_path = "chromedriver.exe")
driver1.get("https://kahoot.it/v2/join")
driver1.close()
pseudo = driver.find_element_by_id("nickname")
pseudo.send_keys("louis@besac")

# trouver le boutton submit pour cliquer dessus 
submit_pseudo = driver.find_element_by_css_selector("button")
submit_pseudo.click()

# WebDriverWait wait = new 





