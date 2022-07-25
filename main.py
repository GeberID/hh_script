from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Driver:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--user-data-dir=/home/alexander/.config/google-chrome")
        self.options.add_argument("--profile-directory=Profile 1")
        self.driver = webdriver.Chrome(options=self.options)
    def get_driver(self):
        return self.driver

class SiteWorker(Driver):
    def __init__(self,site):
        super().__init__()
        self.site = site

    def go_to_the_site(self):
        self.driver.get(self.site)

    def update_summary(self):
        try:
            elements = self.driver.find_elements(By.CLASS_NAME,'supernova-link')
            elements[3].click()
            self.driver.find_element(By.CLASS_NAME,"b-marker").click()
            elements = WebDriverWait(self.driver,100)\
                .until(EC.presence_of_element_located((By.XPATH,
            '''//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/
            div[2]/div/div/div[4]/div[2]/div/div[2]/div/div/div[2]/div[4]/div/button''')))
            if elements.is_enabled() == True:
                elements.click()
                with open('log.txt', 'a') as file:
                    file.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + ' Update\n')
            else:
                with open('log.txt', 'a') as file:
                    file.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")  + ' Locked\n')

        except Exception as err:
            with open('log.txt', 'a') as file:
                file.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + ' Error ' + str(err)+'\n')

    def close_site(self):
        self.driver.close()
        self.driver.quit()



hh = SiteWorker('https://hh.ru/account/login?backurl=%2F&hhtmFrom=main')
hh.go_to_the_site()
hh.update_summary()
hh.close_site()
