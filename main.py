from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from colorama import Fore
from pystyle import Center, Colors, Colorate
import os


def print_info():

    os.system(f"title facior - Twitch Viewer Bot by github.com/facior ")

print(Colorate.Vertical(Colors.green_to_red, Center.XCenter("""


            ███████  █████   █████  ██  █████  ██████
            ██      ██   ██ ██   ██ ██ ██   ██ ██   ██
            █████   ███████ ██      ██ ██   ██ ██████
            ██      ██   ██ ██   ██ ██ ██   ██ ██   ██
            ██      ██   ██  █████  ██  █████  ██   ██

                Github github.com/facior
                                                    """)))



your_name = input("Input name of streamer ")
browser = int(input("How much viewers "))

site = "https://www.twitch.tv/"


for i in range(0,browser):
    stream = site + your_name

    website = stream

    path = '/chromedriver/chromedriver.exe'

    options = Options()
    options.add_experimental_option('detach', True)

    driver = webdriver.Chrome(options=options)

    driver.get(website)
    driver.set_window_size(640, 480)