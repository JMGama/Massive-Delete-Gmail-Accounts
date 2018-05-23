import configparser
import time
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DeleteScript:

    def load_settings(self):
        """
        Loading and assigning global variables from our settings.txt file
        """
        config_parser = configparser.RawConfigParser()
        config_file_path = 'settings.txt'
        config_parser.read(config_file_path)

        browser = config_parser.get('config', 'BROWSER')
        browser_path = config_parser.get('config', 'BROWSER_PATH')
        page = config_parser.get('config', 'PAGE')
        user = config_parser.get('config', 'USER_NAME')
        user_email = config_parser.get('config', 'USER_EMAIL')

        settings = {
            'browser': browser,
            'browser_path': browser_path,
            'page': page,
            'user_name': user,
            'user_email': user_email
        }
        return settings

    def load_driver(self):
        """
        Load the Selenium driver depending on the browser
        (Edge and Safari are not running yet in this program)
        """
        driver = ''
        if self.settings['browser'] == 'firefox':
            firefox_profile = webdriver.FirefoxProfile(self.settings['browser_path'])
            driver = webdriver.Firefox(firefox_profile)
        elif self.settings['browser'] == 'edge':
            pass
        elif self.settings['browser'] == 'chrome':
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("user-data-dir=" + self.settings['browser_path'])
            driver = webdriver.Chrome(chrome_options=chrome_options)
        elif self.settings['browser'] == 'safari':
            pass

        driver.implicitly_wait(10)
        return driver

    def search_user(self):
        """
        Seaching the for the user in the search bar
        """

        search_bar = self.driver.find_element_by_xpath("//input[@class='gb_9e gb_lf']")
        search_bar.send_keys(self.settings['user_email'])
        try:
            if WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='ARN6LL-f-a']"))):
                time.sleep(3)
                if WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='iconWidgetHeader ARN6LL-d-O']"))):
                    user_container = self.driver.find_element_by_xpath("//div[@class='ARN6LL-f-a']")
                    searched_user_name = re.sub(' +',' ', user_container.find_element_by_xpath("//div[@class='iconWidgetHeader ARN6LL-d-O']").text.lower().strip())
                    searched_user_email = re.sub(' +',' ', user_container.find_element_by_xpath("//div[@class='ARN6LL-d-Cc']").text.lower().strip())
                    user_name = self.settings['user_name'].lower().strip()
                    user_email = self.settings['user_email'].lower().strip()

                if user_name == searched_user_name and user_email == searched_user_email:
                    user_container.click()
                    return True
        except Exception as e:
            return False

    def delete_user(self):
        search_menu = True
        while search_menu:
            try:
                delete_menu = self.driver.find_element_by_xpath("//div[@class='JRtysb WzwrXb yoFPvf vlPjFe']").click()
                search_menu = False
            except Exception as e:
                pass

        if WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='JPdR6b null qjTEB']"))):
            for container in self.driver.find_elements_by_xpath("//div[@class='uyYuVb oJeWuf']"):
                text = 'Eliminar usuario'.lower().strip()
                searched_text = container.find_element_by_xpath(".//span[@class='pnwrL']").text.lower().strip()
                if text == searched_text:
                    container.click()
                    return True
        return False

    def uncheck_combobox(self):
        if WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//content[@class='Wvd84e C2Jvlf Ckc5P ey07cb']"))):
            container = self.driver.find_element_by_xpath("//content[@class='Wvd84e C2Jvlf Ckc5P ey07cb']")
            containeer_checkbox_1 = container.find_element_by_xpath(".//div[@class='yVCmid']")
            checkbox_1 = containeer_checkbox_1.find_element_by_xpath(".//div[@class='rq8Mwb']").click()

            containeer_checkbox_2 = container.find_element_by_xpath(".//div[@class='yVCmid V08y4b']")
            checkbox_2 = containeer_checkbox_2.find_element_by_xpath(".//div[@class='rq8Mwb']").click()

            containeer_checkbox_3 = container.find_element_by_xpath(".//div[@class='uVccjd UePkWc N2RpBe']")
            checkbox_3 = containeer_checkbox_3.find_element_by_xpath(".//div[@class='rq8Mwb']").click()

    def press_delete_button(self):
        if WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='nL3Jpb J9fJmf']"))):
            time.sleep(2)
            container = self.driver.find_element_by_xpath("//div[@class='nL3Jpb J9fJmf']")
            #button_container = container.find_element_by_xpath(".//div[@class='O0WRkf oG5Srb HQ8yf C0oVfc kHssdc HvOprf sPNV2d M9Bg4d']")
            button = container.find_element_by_xpath(".//span[@class='RveJvd snByac' and text()='Eliminar']").click()

    def check_correct_delete(self):
        time.sleep(4)
        if WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//a[@class='gb_me gb_fc gb_Be' and @id='sdgBod']"))):
            self.driver.find_element_by_xpath("//a[@class='gb_me gb_fc gb_Be' and @id='sdgBod']").click()
            if WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='ARN6LL-v-m']"))):
                if not self.search_user():
                    print("usuario borrado exitosamente")
                    return True
            print("error al cargar ")

    def main(self):
        """
        Loading all the configuration and opening the website
        (Browser profile where whatsapp web is already scanned)
        """
        self.settings = self.load_settings()
        self.driver = self.load_driver()
        self.driver.get(self.settings['page'])
        time.sleep(3)
        if self.search_user():
            time.sleep(3)
            if self.delete_user():
                self.uncheck_combobox()
                self.press_delete_button()
                self.check_correct_delete()
        else:
            print('no coincide el usuario')

        while True:

            pass

if __name__ == '__main__':
    x = DeleteScript()
    x.main()
