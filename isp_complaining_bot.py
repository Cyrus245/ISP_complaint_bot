from selenium import webdriver
from time import sleep
from dotenv import dotenv_values
from isp_complain import Bot

config = {**dotenv_values('.env')}

driver = webdriver.Chrome()
bot = Bot(driver, config)
bot.speed_test()
bot.sign_in()
bot.input_credentials()
bot.type_tweet()
sleep(180)
