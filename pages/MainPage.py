import time

from selenium.webdriver import ActionChains

from pages.BaseApp import BasePage
from src_pages.MainPageElements import *
from src_pages.Text.MainPageText import key_search, correct_text, not_correct_text, correct_basket_text


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

    def open_more_header_links(self, browser):
        for i in range(3):
            more_btn = self.find_element(LCT_MORE_BTN)
            self.hover_over(browser, more_btn)
            time.sleep(1.5)
            self.click_btn(get_more_header_btn_lct(i))
            time.sleep(1.5)
            self.go_to_back()

    def open_links_club(self, browser, locator):
        for i in range(0, self.find_len(locator)):
            time.sleep(1.5)
            elements = self.find_elements(locator)
            self.click_js(browser, elements[i])
            time.sleep(1.5)
            self.go_to_site(self.base_url+'club/')

    def search_block(self, browser):
        for i in range(len(key_search)):
            action = ActionChains(browser)
            action.move_to_element(self.find_element(LCT_INPUT_SEARCH)).perform()
            self.clear_input(LCT_INPUT_SEARCH)
            self.send_answer(LCT_INPUT_SEARCH, key=key_search[i])
            self.click_btn(LCT_SUBMIT_SEARCH_BTN)
            time.sleep(1)
            if i == 0:
                answer = self.get_text(LCT_CORRECT_ANSWER_SEARCH_TEXT)
                assert answer == correct_text, f"Текст НЕ соответствует: факт.текст. {answer}, ожид.текст. {correct_text}"
            else:
                answer = self.get_text(LCT_NOT_CORRECT_ANSWER_TEXT)
                assert answer == not_correct_text, f"Текст НЕ соответствует: факт.текст. {answer}, ожид.текст. {correct_text}"

    def check_text_basket(self, browser):
        answer = self.get_text(LCT_NTFCN_BASKET)
        assert correct_basket_text in answer, f"Текст НЕ соответствует: факт.текст. {answer}, ожид.текст. {correct_basket_text}"
