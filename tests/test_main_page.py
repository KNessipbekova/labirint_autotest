import time

from conftest import browser
from pages.MainPage import MainPage
from src_pages.MainPageElements import *


def test_open_books_page(browser):
    main_page = MainPage(browser)
    main_page.go_to_site(main_page.base_url)
    main_page.click_btn(LCT_BOOKS_BTN)
    main_page.open_links(browser, LCT_GENRE_BTNS)
    time.sleep(5)


def test_header(browser):
    main_page = MainPage(browser)
    main_page.go_to_site(main_page.base_url)
    main_page.open_header_links(browser, LCT_BOOKS_LIST_BTN)
    time.sleep(2)
