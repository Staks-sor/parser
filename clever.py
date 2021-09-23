from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from multiprocessing import Process, Lock
from multiprocessing import Pool
from colorama import Fore, Back
from selenium import webdriver
from colorama import init
import time
import multiprocessing
import os
import win32ctypes.core
import sys
import logging
from fake_useragent import UserAgent
from threading import Timer


while True:

    def fuc():

        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.headless = False #переключение режима видимости

        ua = UserAgent()
        a = ua.random
        user_agent = ua.random
        print(Fore.CYAN + user_agent)
        options.add_argument(f"user-agent={user_agent}")
        ua = UserAgent()
        opts = Options()
        opts.add_argument("user-agent=" + ua.google)
        d = DesiredCapabilities.CHROME
        d["loggingPrefs"] = {"browser": "ALL"}
        path = r"Путь к хромдрайверу"
        driver = webdriver.Chrome(
            options=options, desired_capabilities=d, executable_path=path
        )

        driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {
                "source": """
                          const newProto = navigator.__proto__
                          delete newProto.webdriver
                          navigator.__proto__ = newProto
                          """
            },
        )
        driver.get("https://yandex.ru")
        search = driver.find_element_by_id("text")
        search.send_keys("Поиск в поисковой строке")
        search.send_keys(Keys.ENTER)
        driver.implicitly_wait(3)
        driver.find_element_by_partial_link_text("нажатие на нужный поиск").click()
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        driver.implicitly_wait(3)
        elements = driver.find_elements_by_xpath(
            "если нужен элемент после перехода"
        )

        time.sleep(5)


        if elements:

            print(Fore.GREEN + "вывод")
            time.sleep(30)
            driver.quit()
        else:

            print(Fore.RED + "вывод")
        driver.quit()

    if fuc():
        break
