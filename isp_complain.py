from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PROMISED_UP = 300.00
PROMISED_DOWN = 200.00


class Bot:
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.up = 0.00
        self.down = 0.00

    def speed_test(self):
        """This method checks the internet speed for now"""

        self.driver.get("https://www.speedtest.net/")
        
        go_btn = self.driver.find_element(By.XPATH,
                                          '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_btn.click()

        sleep(40)
        up_speed = self.driver.find_element(By.XPATH,

                                            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                            '3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')

        down_speed = self.driver.find_element(By.XPATH,
                                              '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                              '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')

        self.up = float(up_speed.text)
        self.down = float(down_speed.text)

    def sign_in(self):
        """This method sign in into twitter"""

        self.driver.get('https://twitter.com/')
        signin_btn = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span')))
        signin_btn.click()

    def verification(self):
        verify = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                      '//*[@id="layers"]/div['
                                                                                      '2]/div/div/div/div/div/div['
                                                                                      '2]/div['
                                                                                      '2]/div/div/div[2]/div[2]/div['
                                                                                      '1]/div/div[2]/label/div/div['
                                                                                      '2]/div/input')))

        verify.send_keys(self.config['username'])
        sleep(10)
        verify_btn = self.driver.find_element(By.XPATH,
                                              '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                              '2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span')
        verify_btn.click()

    def input_credentials(self):
        """Inputting user credentials into twitter"""
        sleep(10)
        signin_input = self.driver.find_element(By.XPATH,
                                                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                '2]/div/div/div[2]/div['
                                                '2]/div/div/div/div[5]/label/div/div[2]/div/input')

        signin_input.send_keys(self.config['email'])
        next_btn = self.driver.find_element(By.XPATH,
                                            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                            '2]/div['
                                            '2]/div/div/div/div[6]/div/span/span')
        next_btn.click()

        sleep(10)
        password_input = self.driver.find_element(By.XPATH,
                                                  '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                  '2]/div/div/div[2]/div['
                                                  '2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_input.send_keys(self.config['password'])

        login_btn = self.driver.find_element(By.XPATH,
                                             '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                             '2]/div['
                                             '2]/div[2]/div/div[1]/div/div/div/div')
        login_btn.click()
        sleep(30)

    def type_tweet(self):
        """This method type tweet into Twitter"""

        post_input = self.driver.find_element(By.CSS_SELECTOR,
                                              'br[data-text="true"]')
        post_input.send_keys(
            f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay "
            f"for {PROMISED_DOWN}down/{PROMISED_UP}up?")

        post_btn = self.driver.find_element(By.XPATH,
                                            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div['
                                            '3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div['
                                            '2]/div[3]/div/span/span')
        post_btn.click()
