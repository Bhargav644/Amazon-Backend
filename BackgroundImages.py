from re import T
from uuid import uuid1
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from tkinter import Tk
from pynput.keyboard import Key, Controller
from db import getData
from script import getHTMLParser
from headers import header
from db import setData

import chromedriver_autoinstaller
chromedriver_autoinstaller.install()


def BackImages():
    '''
        working: fetches background images
        returns: None
    '''

    # # ?basic requirement
    # dict = {'services': []}
    # link = 'https://www.amazon.in/'
    # soupHome = getHTMLParser(link, header)
    # lsits_of_images = soupHome.find_all_next('li', class_="a-carousel-card")

    # ?chome driver for selenium
    chrome_options = Options()
    chrome_options.add_experimental_option(
        'excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=chrome_options)

    # ?getting url of the amazon
    driver.get('https://www.amazon.in/')
    driver.maximize_window()
    action = ActionChains(driver)
    keyborad = Controller()

    # ?getting all t
    # he images
    images = dict()
    flag = False
    for i in range(8):
        element = driver.find_element(
            By.CSS_SELECTOR, ".a-link-normal .aok-inline-block")
        action.context_click(element).perform()

        # if not flag:
        #     time.sleep(1)
        #     flag = True
        # else:
        #     time.sleep(4)
        time.sleep(2.5)
        # for j in range(5):
        keyborad.press(Key.up)
        keyborad.press(Key.up)
        keyborad.press(Key.up)
        keyborad.press(Key.up)
        keyborad.press(Key.up)

        keyborad.press(Key.enter)
        images[str(uuid1())] = Tk().clipboard_get()
        nextImage = driver.find_element(
            By.CSS_SELECTOR, ".a-carousel-goto-nextpage")
        time.sleep(1.6)
        action.click(nextImage).perform()

    temp = []
    images_without_duplicacy = dict()
    for key, value in images.items():
        if value not in temp:
            temp.append(value)
            images_without_duplicacy[key] = value

    if(len(getData("BackgroundImages")) < len(images_without_duplicacy)):
        setData("BackgroundImages", images_without_duplicacy)
