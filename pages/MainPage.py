import time

from pages.BaseApp import BasePage
from src_pages.MainPageElements import LCT_BOOKS_BTN


class MainPage(BasePage):
    def close_shipping_window(self, close_lct):
        time.sleep(7)
        self.click_btn(close_lct)
        time.sleep(7)

    def open_header_links(self, browser, locator):
        for i in range(0, self.find_len(locator)):
            print(i)
            books_btn = self.find_element(LCT_BOOKS_BTN)
            self.hover_over(browser, books_btn)
            time.sleep(1.5)
            elements = self.find_elements(locator)[i]
            self.hover_over(browser, elements)
            self.click_js(browser, elements)
            time.sleep(1.5)
            self.go_to_back()
            print(i)