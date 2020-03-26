from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from model.search import Search


def clear(self, s):
    return re.sub(r'[,:() - ^A-zА-я]', "", re.sub(r'\([^()]*\)', "", s))


class SearchHelper:

    def __init__(self, app):
        self.app = app

    # Получение курса с сайта медуза
    def get_rates_meduza(self):
        wd = self.app.wd
        self.app.open_home_page()
        usd_m = wd.find_element_by_css_selector(".ExchangeRates-usd").text
        return usd_m

    # Получение курса с сайта яндекс
    def get_rates_yandex(self):
        wd = self.app.wd
        wd.get('https://yandex.ru/')
        usd = wd.find_element_by_css_selector(".inline-stocks__value_inner").text
        return usd

    # Получение слова из первого абзаца статьи
    def get_value(self, search):
        wd = self.app.wd
        self.app.open_home_page()
        self.go_to_article_page(search)
        self.wait_element_for_css('p:nth-child(1)')
        text = wd.find_element_by_css_selector('p:nth-child(1)').text.split()
        global word
        word = text[3]

    # Переход на страницу найденной статьи.
    def go_to_article_page(self, search):
        wd = self.app.wd
        self.search_value(search)
        self.wait_element_for_css('div:nth-child(4) > a > div > div')
        wd.find_element_by_css_selector('div:nth-child(4) > a > div > div').click()

    # Поиск значения на сайте medusa
    def search_value(self, text):
        wd = self.app.wd
        wd.find_element_by_css_selector(' .Header-buttons [type="button"]').click()
        wd.find_element_by_css_selector('.Search-header > div > input').send_keys(text)

    # Проверка условий приёмки
    def verification_of_acceptance_conditions(self, search):
        wd = self.app.wd
        self.app.open_home_page()
        self.search_value(search.value)
        if search.there_is_a_mistake == "Yes":
            print("Известная ошибка")
        elif len(wd.find_elements_by_css_selector(".Chronology-item")) > 0 and search.acceptance_conditions == "есть результаты":
            return True
        elif wd.find_element_by_css_selector(".Search-message") and search.acceptance_conditions == "нет результатов":
            return True

    # Переход на google.com в новой вкладке и поиск слова
    def google_search(self):
        wd = self.app.wd
        wd.execute_script("window.open('https://www.google.com');")
        new_window = wd.window_handles[1]
        wd.switch_to.window(new_window)
        wd.find_element(By.NAME, "q").click()
        wd.find_element(By.NAME, "q").send_keys(word)
        self.wait_element('btnK')
        wd.find_element(By.NAME, 'btnK').click()

    def find_result(self):
        wd = self.app.wd
        text = wd.find_element_by_xpath('//*[@id="result-stats"]').text
        only_digits = clear(text)
        return int(only_digits)

    def wait_element(self, button_name):
        wd = self.app.wd
        WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, button_name)))

    def wait_element_for_css(self, selector):
        wd = self.app.wd
        WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
