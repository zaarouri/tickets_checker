import time
import pygame
pygame.init()
from selenium import webdriver
from selenium.webdriver.common.by import By
pygame.mixer.music.load("alarm.mp3")
# Start a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to the website you want to test
# driver.get("https://queueing.fcwc2022.com/0725/inQueue/568/fr/?origin=https%3A%2F%2Fticket.fcwc2022.com%3A3451%2Fshop%2FfListeManifs.aspx%3Fidstructure%3D0725")
driver.get("https://ticket.fcwc2022.com/shop/fListeManifs.aspx?idstructure=0725&tn=55579&quHash=af9867ce2e4e651cff571e2f16db78ad25cf4d398eb46f7a8aced2ab9f59c04d")

while True:
    # Reload the website
    driver.refresh()
    time.sleep(15)
    # Find the button on the page
    # button = driver.find_element(By.CLASS_NAME, "eventFull btn btn-block")
    button = driver.find_element(By.XPATH, "//div[ @disabled='disabled']")

    
    # Check if the button is enabled and displayed
    if button.is_enabled() or not button.is_displayed():
       print("Button is not clickable")
    else:
         pygame.mixer.music.play()
         print("ticket is availlable mr abdelmounime")
         pygame.mixer.music.play()
         print("ticket is availlable mr abdelmounime")
        
    
    # Wait for 20 seconds before reloading the website
    time.sleep(15)