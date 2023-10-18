from selenium.webdriver.common.by import By


LCT_BOOKS_BEST_BTN = (By.XPATH, '//*[@id="header-genres"]/div/ul/li[2]/a')
LCT_BILINGUALS_BTN = (By.XPATH, '//*[@id="minwidth"]/div[2]/div[1]/div[4]/div/div[3]/ul/li[1]/a')

LCT_LABIRINT_BTN = (By.XPATH, '//*[@id="minwidth"]/div[3]/div/div[1]/div[1]/div/a[1]/span')

LCT_BOOKS_BTN = (By.XPATH, '//*[@id="minwidth"]/div[3]/div[1]/div[1]/div[4]/div/div[1]/ul/li[1]/span/a')
LCT_GENRE_BTNS = (By.XPATH, '//*[@id="minwidth"]/div[2]/div[1]/div[4]/div/div[3]/ul/li/a')
# CT_BOOKS_LIST_BTN = (By.XPATH, '//*[@id="header-genres"]/div/ul/li[@class="b-menu-second-item"]')

LCT_FOREIGN_BTN = (By.XPATH, '//*[@id="minwidth"]/div[3]/div/div[1]/div[4]/div/div[1]/ul/li[2]/span/a')
LCT_FOREIGN_GENRE_BTNS = (By.XPATH, '//*[@id="minwidth"]/div[2]/div[1]/div[4]/div/div[3]/ul/li/a')

LCT_MBOOKS_BTN = (By.XPATH, '//*[@id="minwidth"]/div[3]/div/div[1]/div[4]/div/div[1]/ul/li[3]/span/a')
LCT_MBOOKS_IN_BTNS = (By.XPATH, '//*[@id="minwidth"]/div[2]/div[1]/div[1]/div[2]/div/ul/li/a')

LCT_SCHOOL_BTN = (By.XPATH, '//*[@id="minwidth"]/div[3]/div/div[1]/div[4]/div/div[1]/ul/li[5]/span/a')
LCT_SCHOOL_IN_BTNS = (By.XPATH, '//*[@id="minwidth"]/div[2]/div[1]/ul/li/a')

LCT_STAT_BTN = (By.XPATH, '//*[@id="minwidth"]/div[3]/div/div[1]/div[4]/div/div[1]/ul/li[6]/span/a')
LCT_STAT_IN_BTNS = (By.XPATH, '//*[@id="minwidth"]/div[2]/div[1]/div[2]/div/div[3]/ul/li/a')

LCT_TOYS_BTN = (By.XPATH, '//*[@id="minwidth"]/div[3]/div/div[1]/div[4]/div/div[1]/ul/li[7]/span/a')
LCT_TOYS_IN_BTNS = (By.XPATH, '//*[@id="minwidth"]/div[2]/div[1]/div[2]/div/div[3]/ul/li/a')

LCT_DLVR_BTN = (By.XPATH, '//*[@id="minwidth"]/div[3]/div/div[2]/div/ul/li[1]/a')
LCT_DLVR_IN_BTNS = (By.XPATH, '//*[@id="aHelp"]')

LCT_CLUB_BTN = (By.XPATH, '//div/div[1]/div[4]/div/div[1]/ul/li[12]/span/a')
LCT_CLUB_IN_BTNS = (By.XPATH, '//*[@id="right-inner"]/div[1]/div[1]/div/ul/li/a')

LCT_INPUT_SEARCH = (By.XPATH, '//*[@id="search-field"]')
LCT_CORRECT_ANSWER_SEARCH_TEXT = (By.XPATH, '//*[@id="right-inner"]/div[1]/div/div[1]/h1')
LCT_NOT_CORRECT_ANSWER_TEXT = (By.XPATH, '//*[@id="search"]/div[1]/h1')
LCT_SUBMIT_SEARCH_BTN = (By.XPATH, '//*[@id="searchform"]/div[1]/button')

LCT_MORE_BTN = (By.XPATH, '//*[@id="minwidth"]/div[3]/div/div[1]/div[4]/div/div[1]/ul/li[11]/span')
LCT_MORE_IN_BTNS = (By.XPATH, '//div[@id="header-more"]//li[@class="b-menu-second-item"]')

LCT_DVD_BTN = (By.XPATH, '//div[@id="header-more"]//li[@class="b-menu-second-item"][1]')

def get_more_header_btn_lct(i):
    return (By.XPATH, f'//div[@id="header-more"]//li[@class="b-menu-second-item"][{i+1}]')

LCT_FIRST_BOOK_BTN = (By.XPATH, '//*[@id="minwidth"]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div/div/div/div/a/div')
LCT_ADD_FIRST_BOOK_BTN = (By.XPATH, '//div[@class="buying-btns"]/a')

LCT_NTFCN_BASKET = (By.XPATH, '//div[@class="b-basket-popinfo-e-text b-basket-popinfo-e-text-m-add b-basket-popinfo-e-text-m-gray"]')