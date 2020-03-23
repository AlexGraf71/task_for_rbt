from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchHelper:

    def __init__(self, app):
        self.app = app

    # Получение слова из первого абзаца статьи
    def search_value(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.go_to_article_page()
        self.wait_element_for_css('p:nth-child(1)')
        text = wd.find_element_by_css_selector('p:nth-child(1)').text.split()
        global word
        word = text[3]

    # Переход на страницу найденной статьи.
    def go_to_article_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(' .Header-buttons [type="button"]').click()
        wd.find_element_by_css_selector('.Search-header > div > input').send_keys('коронавирус')
        self.wait_element_for_css('div:nth-child(4) > a > div > div')
        wd.find_element_by_css_selector('div:nth-child(4) > a > div > div').click()

    # Переход на google.com и поиск слова

    def google_search(self):
        wd = self.app.wd
        wd.get('https://www.google.com')
        wd.find_element(By.NAME, "q").click()
        wd.find_element(By.NAME, "q").send_keys(word)
        self.wait_element('btnK')
        wd.find_element(By.NAME, 'btnK').click()

    def wait_element(self, button_name):
        wd = self.app.wd
        WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, button_name)))

    def wait_element_for_css(self, selector):
        wd = self.app.wd
        WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
