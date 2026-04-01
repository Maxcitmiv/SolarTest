import allure
from selene import browser, have, be, by


class StartPage:
    def __init__(self):
        self.product = browser.element('.main-nav__submenu-item')
        self.product_button = browser.element('.main-nav__link-first-level')
        self.search_button=browser.element('.page-header__open-search-btn.js-open-button')
        self.intput_header_search=browser.element('[placeholder="Поиск по сайту"]')
        self.search_url='/search'
        self.title_h1=browser.element('.search-promo__title')
        self.title_text='Поиск по сайту'
        self.button_consultation=browser.element('.page-header__consultation_desctop')
        self.title_form_consultation=browser.element('.callback__text_short-margin')
        self.text_title_consultation='Запросить консультацию'
        self.company_intput=browser.element('[name="form_text_4192"]')
        self.fio_intput=browser.element('#user-name')
        self.phone_intput=browser.element('#user-phone')
        self.email_intput=browser.element('#user-mail')
        self.consultation_submit_button=browser.element('[name="web_form_submit"]')
        self.sberbank_company_intput=browser.element(by.text('ПАО СБЕРБАНК'))
        self.analitics_button=browser.element('[href="/analytics/reports/"]')
        self.analitics_url='/analytics/reports/'
        self.title_analitics_page=browser.element('.products-promo__wrapper_full-width')
        self.title_analitics_text='В данном разделе публикуются аналитические исследования компании «Солар»'
        self.product_promo_button=browser.element('.products-promo__btn')
        self.product_promo_title=browser.element('.callback__text')
    @allure.step('Открытие главной страницы')
    def open(self):
        browser.open('/')
        return self
    @allure.step('Клик по поиску в хедере')
    def click_search_button(self):
        self.search_button.click()
        return self
    @allure.step('Ввод значения в поле поиска')
    def fill_intput(self, value):
        self.intput_header_search.type(value).press_enter()
        return self

    @allure.step('Проверка страницы поиска')
    def expect_page_search(self):
        browser.should(have.url_containing(self.search_url))
        self.title_h1.should(have.text(self.title_text))
        return self

    @allure.step('Клик по кнопке консультации в хедере')
    def click_consultation_button(self):
        self.button_consultation.click()
        return self

    @allure.step('Проверка страницы консультации')
    def expect_page_consultation(self):
        self.title_form_consultation.should(have.text(self.text_title_consultation))
        self.company_intput.should(be.visible)
        self.fio_intput.should(be.visible)
        self.email_intput.should(be.visible)
        self.consultation_submit_button.should(be.clickable)
        return self

    @allure.step('Ввод значения в поле компании')
    def fill_company_intput(self, value):
        self.company_intput.type(value)
        return self

    @allure.step('Клик по пункту "ПАО СБЕРБАНК" в выпадающем списке')
    def click_sber(self):
        self.sberbank_company_intput.click()
        return self

    @allure.step('Проверка, что поле компании заполнилось корректно')
    def expect_fill_company(self):
        self.company_intput.should(have.value('ПАО СБЕРБАНК'))
        return self

    @allure.step('Клик по кнопке аналитики в хедере')
    def analitics_button_click(self):
        self.analitics_button.click()
        return self

    @allure.step('Проверка страницы аналитики')
    def expect_page_analitics(self):
        browser.should(have.url_containing(self.analitics_url))
        self.title_analitics_page.should(have.text(self.title_analitics_text))
        return self

    @allure.step('Клик по кнопке продукты в хедере')
    def products_button_click(self):
        self.product_button.should(have.text('Продукты')).click()
        return self

    @allure.step('Выбор продукта в выпавшем списке')
    def choise_product(self):
        self.product.should(have.text('Защита сайта от киберугроз')).click()
        return self

    @allure.step('Клик по промо-кнопке на странице продукта')
    def product_promo_button_click(self):
        self.product_promo_button.click()
        return self

    @allure.step('Проверка, что мы находимся на промо-странице продукта')
    def expect_modal_window_product(self):
        self.product_promo_title.should(have.text('Бесплатная защита сайта на 14 дней. Протестируйте наше решение и подберите подходящий тариф под ваши задачи')).should(be.visible)


