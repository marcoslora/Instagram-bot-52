from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from passwo import INSTA_EMAIL, INSTA_PASSWORD
s = Service("/Users/ml/Documents/Development/chromedriver")
SIMILAR_ACCOUNT = "buzzfeedtasty"


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(service=s)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")

        username.send_keys(INSTA_EMAIL)
        time.sleep(2)
        password.send_keys(INSTA_PASSWORD)

        time.sleep(3)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(8)
        followers = self.driver.find_element(By.XPATH, "//a[contains(@href, '/followers')]")
        followers.click()

        time.sleep(3)
        # modal = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_hu"]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]')
        # for i in range(10):
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        #     time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        value = 0
        for button in all_buttons:
            if value < 3:
                button.click()
                value += 1
                time.sleep(5)
        # for button in all_buttons:
        #     try:
        #         button.click()
        #         time.sleep(1)
        #
        #     except ElementClickInterceptedException:
        #         cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
        #         cancel_button.click()


bot = InstaFollower(s)
bot.login()
bot.find_followers()
bot.follow()