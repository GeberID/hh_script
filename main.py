from selenium import webdriver
from selenium.webdriver.common.by import By

class Driver:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(options=self.options)
    def get_driver(self):
        return self.driver

class SiteWorker(Driver):
    def __init__(self,site):
        super().__init__()
        self.site = site

    def go_to_the_site(self):
        self.driver.get(self.site)

    def login_hh(self):
        with open("login.txt","r") as file:
            log_pass = [i for i in file]

        elements = self.driver.find_elements(By.CLASS_NAME,'bloko-link_pseudo')
        elements[1].click()
        elements = self.driver.find_elements(By.CLASS_NAME,'bloko-input')
        elements[1].send_keys(log_pass[0])
        elements[2].send_keys(log_pass[1])
        elements = self.driver.find_elements(By.CLASS_NAME,'bloko-button_kind-primary')
        elements[1].click()

hh = SiteWorker('https://hh.ru/account/login?backurl=%2F&hhtmFrom=main')
hh.go_to_the_site()
#hh.login_hh()
