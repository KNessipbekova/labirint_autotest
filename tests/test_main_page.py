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


# def test_header(browser):
    # main_page = MainPage(browser)
    # main_page.go_to_site(main_page.base_url)
    # main_page.open_header_links(browser, LCT_BOOKS_LIST_BTN)
    # time.sleep(2)

def test_open_foreign_page(browser):
    main_page = MainPage(browser)
    main_page.go_to_site(main_page.base_url)
    main_page.click_btn(LCT_FOREIGN_BTN)
    main_page.open_links(browser, LCT_FOREIGN_GENRE_BTNS)
    time.sleep(5)

def test_open_mainbooks_page(browser):
    main_page = MainPage(browser)
    main_page.go_to_site(main_page.base_url)
    main_page.click_btn(LCT_MBOOKS_BTN)
    main_page.open_links(browser, LCT_MBOOKS_IN_BTNS)
    time.sleep(5)

def test_open_school_page(browser):
    main_page = MainPage(browser)
    main_page.go_to_site(main_page.base_url)
    main_page.click_btn(LCT_SCHOOL_BTN)
    main_page.open_links(browser, LCT_SCHOOL_IN_BTNS)
    time.sleep(5)

def test_open_stationery_page(browser):
    main_page = MainPage(browser)
    main_page.go_to_site(main_page.base_url)
    main_page.click_btn(LCT_STAT_BTN)
    main_page.open_links(browser, LCT_STAT_IN_BTNS)
    time.sleep(5)

def test_open_toys_page(browser):
    main_page = MainPage(browser)
    main_page.go_to_site(main_page.base_url)
    main_page.click_btn(LCT_TOYS_BTN)
    main_page.open_links(browser, LCT_TOYS_IN_BTNS)
    time.sleep(5)

def test_open_toys_page(browser):
    main_page = MainPage(browser)
    main_page.go_to_site(main_page.base_url)
    main_page.click_btn(LCT_TOYS_BTN)
    main_page.open_links(browser, LCT_TOYS_IN_BTNS)
    time.sleep(5)

def test_more_header(browser):
    main_page = MainPage(browser)
    main_page.go_to_site(main_page.base_url)
    main_page.open_more_header_links(browser)
    time.sleep(2)

def test_check_search(browser):
    main_page = MainPage(browser)
    main_page.go_to_site(main_page.base_url)
    main_page.search_block(browser)

def test_open_club_page(browser):
    main_page = MainPage(browser)
    main_page.go_to_site(main_page.base_url)
    main_page.click_btn(LCT_CLUB_BTN)
    main_page.open_links_club(browser, LCT_CLUB_IN_BTNS)
    time.sleep(5)

def test_add_to_basket(browser):
    main_page = MainPage(browser)
    main_page.go_to_site(main_page.base_url)
    main_page.click_btn(LCT_FIRST_BOOK_BTN)
    main_page.click_btn(LCT_ADD_FIRST_BOOK_BTN)
    main_page.check_text_basket(browser)
    time.sleep(5)