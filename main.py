import configparser
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def load_settings():
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


def load_driver(settings):
    """
    Load the Selenium driver depending on the browser
    (Edge and Safari are not running yet in this program)
    """
    driver = ''
    if settings['browser'] == 'firefox':
        firefox_profile = webdriver.FirefoxProfile(settings['browser_path'])
        driver = webdriver.Firefox(firefox_profile)
    elif settings['browser'] == 'edge':
        pass
    elif settings['browser'] == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("user-data-dir=" + settings['browser_path'])
        driver = webdriver.Chrome(chrome_options=chrome_options)
    elif settings['browser'] == 'safari':
        pass

    driver.implicitly_wait(10)
    return driver

def search_user(driver, settings):
    """
    Seaching the for the user in the search bar
    """

    search_bar_container = driver.find_element_by_xpath("//form[@class='gb_Qe cpanelSearchBarOgb']")
    search_bar = search_bar_container.find_element_by_xpath("//input[@class='gb_9e']")
    search_bar.send_keys(settings['user_email'])

    if WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='ARN6LL-f-a']"))):
        time.sleep(3)
        user_container = driver.find_element_by_xpath("//div[@class='ARN6LL-f-a']")
        if WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='iconWidgetHeader ARN6LL-d-O']"))):
            searched_user_name = user_container.find_element_by_xpath("//div[@class='iconWidgetHeader ARN6LL-d-O']").text.lower().strip()
            searched_user_email = user_container.find_element_by_xpath("//div[@class='ARN6LL-d-Cc']").text.lower().strip()
            user_name = settings['user_name'].lower().strip()
            user_email = settings['user_email'].lower().strip()

        if user_name == searched_user_name and user_email == searched_user_email:
            user_container.click()
            return True
        else:
            return False

def delete_user(driver):
    search_menu = True
    while search_menu:
        try:
            delete_menu = driver.find_element_by_xpath("//div[@class='JRtysb WzwrXb yoFPvf vlPjFe']").click()
            search_menu = False
        except Exception as e:
            pass

    if WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='JPdR6b null qjTEB']"))):
        for container in driver.find_elements_by_xpath("//div[@class='uyYuVb oJeWuf']"):
            text = 'Eliminar usuario'.lower().strip()
            searched_text = container.find_element_by_xpath(".//span[@class='pnwrL']").text.lower().strip()
            if text == searched_text:
                container.click()
                uncheck_combos(driver)


def uncheck_combos(driver):
    if WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//content[@class='Wvd84e C2Jvlf Ckc5P ey07cb']"))):
        container = driver.find_element_by_xpath("//content[@class='Wvd84e C2Jvlf Ckc5P ey07cb']")
        containeer_checkbox_1 = container.find_element_by_xpath(".//div[@class='yVCmid']")
        checkbox_1 = containeer_checkbox_1.find_element_by_xpath(".//div[@class='rq8Mwb']").click()

        containeer_checkbox_2 = container.find_element_by_xpath(".//div[@class='yVCmid V08y4b']")
        checkbox_2 = containeer_checkbox_2.find_element_by_xpath(".//div[@class='rq8Mwb']").click()

        containeer_checkbox_3 = container.find_element_by_xpath(".//div[@class='uVccjd UePkWc N2RpBe']")
        checkbox_3 = containeer_checkbox_3.find_element_by_xpath(".//div[@class='rq8Mwb']").click()

def main():
    """
    Loading all the configuration and opening the website
    (Browser profile where whatsapp web is already scanned)
    """
    settings = load_settings()
    driver = load_driver(settings)
    driver.get(settings['page'])

    time.sleep(3)

    if search_user(driver, settings):
        time.sleep(3)
        delete_user(driver)
    else:
        print('no coincide el usuario')
        print('usuario encontrado: ' + searched_user_name + ", " + searched_user_email)
        print('usuario buscado: ' + settings['user'] + ", " + settings['user_email'])

    while True:

        pass

if __name__ == '__main__':
    main()
