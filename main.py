from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import json
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait



class InstagramFollower:
    def __init__(self,data):
        """This section contains data from config.json"""
        self.email = data['email']
        self.password = data['password']
        self.searched_account = data['searched_account']
        self.driver = webdriver.Chrome(executable_path=data['driver_path'])

    def login(self):
        """This section works for login into instagram account"""
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(5)

        allow_essential_cookies = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]').click()
        sleep(5)
        username = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.clear()
        username.send_keys(self.email)
        sleep(2)
        password_field = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_field.clear()
        password_field.send_keys(self.password)
        sleep(5)
        password_field.send_keys(Keys.ENTER)
        sleep(15)
        not_now_button = self.driver.find_element(By.CLASS_NAME, value='_ac8f').click()
        sleep(10)
        second_not_now = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()

    def find_followers(self):

        search_icon = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/a/div').click()
        sleep(5)
        search_field = self.driver.find_element(By.XPATH, value='//input[@aria-label="Search input"]')
        search_field.send_keys(self.searched_account)
        sleep(5)
        click_name = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/a')
        click_name.click()
        sleep(10)

        followers = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        sleep(5)
        
        follow_list = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div[3]/button')
        for i in range(100):
            follow_list.send_keys(Keys.END)
            

    def follow(self):
        follow_buttons = self.driver.find_elements(By.TAG_NAME, value='button')
        
        for button in follow_buttons:
            button.click()
            sleep(3)
        


if __name__ == "__main__":
    with open("config.json") as config_file:
        data = json.load(config_file)

    bot = InstagramFollower(data)

    bot.login()
    sleep(10)
    bot.find_followers()
    sleep(10)
    bot.follow()


