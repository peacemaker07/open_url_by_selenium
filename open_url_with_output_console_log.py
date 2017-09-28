import os
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 

# DRIVER_PATH = os.path.join(os.path.dirname(__file__), 'chromedriver')
SLEEP_TIME_MAIN = 3
SLEEP_TIME_POPUP = 3

def _is_skip(url_list):
    return (url_list[0] == "-" if len(url_list) > 0 else False)

def _is_login(url_list):
    return (url_list[0] == "login" if len(url_list) > 0 else False)

def _is_popup(url_list):
    return (url_list[0] == "◯" if len(url_list) > 0 else False)

def _log_print(driver, url):
    print('==> url: ' + url)
    for entry in driver.get_log('browser'):
        print("==browser==")
        print(entry)

def _login(driver, url_list):
    user_id_text = driver.find_element_by_id("user_id")
    user_id_text.send_keys(url_list[1])
    password_text = driver.find_element_by_id("password")
    password_text.send_keys(url_list[2])
    driver.find_element_by_class_name("submitbutton").click()

def open_popup(driver, url_list):

    driver.get(url_list[1])
    window_main = driver.window_handles[0]
    for find_text in url_list[2:]:
        elements = driver.find_elements_by_link_text(find_text)
        if not elements:
            elements = driver.find_elements_by_class_name(find_text)
            # sleep_time = 1
        for e in elements:
            e.click()
            sleep(SLEEP_TIME_POPUP)

            url = driver.current_url
            try:
                window_after = driver.window_handles[1]
                driver.switch_to_window(window_after)
                url = driver.current_url
                _log_print(driver, url)
                # sleep(10)
                driver.close()
                driver.switch_to_window(window_main)
            except:
                _log_print(driver, url)

def open_url(input_file):
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = { 'browser':'ALL' }
    # driver = webdriver.Chrome(DRIVER_PATH)
    driver = webdriver.Chrome(desired_capabilities=d)

    with open(input_file, 'r', encoding='utf-8') as f:
        urls_org = f.readlines()
        urls = list(map(lambda x: x.replace('\n', ''), urls_org))

        for url in urls:
            url_list = url.split(',')

            if _is_skip(url_list):
                continue

            if _is_login(url_list):
                _login(driver, url_list)
                _log_print(driver, url)
                continue

            if not _is_popup(url_list):
                # メインページ
                driver.get(url_list[0])
                _log_print(driver, url)
                sleep(SLEEP_TIME_MAIN)

                continue

            # ポップアップ
            open_popup(driver, url_list)

    driver.quit()

if '__main__' == __name__:
    if (len(sys.argv) != 2):
        print('Usage: # python %s filename' % argvs[0])
        quit()

    open_url(sys.argv[1])
