from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.labirint.ru/'

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(locator))

    def check_button_active(self, locator):
        return WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable(locator)).click()

    def find_element(self, locator):
        return WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(locator), message=f"Can't find "
                                                                                    f"element by locator {locator}")
    def send_answer(self, locator, key):
        return self.find_element(locator).send_keys(key)

    def clear_input(self, locator):
        return self.find_element(locator).clear()

    def get_text(self, locator):
        try:
            return self.find_element(locator).text
        except:
            return None

    def go_to_site(self, url):
        return self.driver.get(url)

    def find_elements(self, locator):
        return WebDriverWait(self.driver, 7).until(EC.presence_of_all_elements_located(locator),message="Can't find"
                                                                                    "elements by locator {locator}")

    def get_title(self):
        return self.driver.title

    def click_btn(self, locator):
        return WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable(locator)).click()

    def check_equal_texts(self, text1, text2):
        return text1 == text2

    def go_to_back(self):
        return self.driver.back()

    def click_js(self, browser, locator):
        WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable(locator))
        return browser.execute_script("arguments[0].click();", locator)

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)
        time.sleep(2)

    def check_assert_url(self, browser, url_assert):
        assert browser.current_url in url_assert or url_assert in browser.current_url, f'Открыта неправильная ссылка: ' \
                                                                                       f'ожидаемая ссылка {url_assert}, ' \
                                                                                       f'фактическая {browser.current_url}'

    def find_len(self, locator):
        return len(self.find_elements(locator))

    def open_link_and_assertion(self, browser, locator, url, urls):
        for i in range(0, self.find_len(locator)):
            time.sleep(1.5)
            elements = self.find_elements(locator)
            self.click_js(browser, elements[i])
            time.sleep(1.5)
            self.check_assert_url(browser, urls[i])
            self.go_to_site(url)

    def open_links(self, browser, locator):
        for i in range(0, self.find_len(locator)):
            time.sleep(1.5)
            elements = self.find_elements(locator)
            self.click_js(browser, elements[i])
            time.sleep(1.5)
            self.go_to_back()

    def hover_over(self, browser, locator):
        action = ActionChains(browser)
        action.move_to_element(locator).perform()

    def switch_to_next_tab(self, browser):
        current_tab_index = browser.window_handles.index(browser.current_window_handle)
        next_tab_index = (current_tab_index + 1) % len(browser.window_handles)
        browser.switch_to.window(browser.window_handles[next_tab_index])

    def switch_to_previous_tab(self, browser):
        current_tab_index = browser.window_handles.index(browser.current_window_handle)
        previous_tab_index = (current_tab_index - 1) % len(browser.window_handles)
        print(previous_tab_index, current_tab_index)
        browser.switch_to.window(browser.window_handles[previous_tab_index])
