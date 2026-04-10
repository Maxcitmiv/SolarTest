import allure
import pytest

from pages.start_page import StartPage


@allure.title('Проверка работоспособности поиска в хедере')
def test_search():
    (StartPage().open()
     .click_search_button()
     .fill_intput('dns')
     .expect_page_search())


@allure.title('Проверка корректности работы кнопки консультации и страницы консультации')
def test_consultation():
    (StartPage().open()
     .click_consultation_button()
     .expect_page_consultation())


@allure.title('Проверка дозаполнения поля компании на странице консультации')
def test_search_company():
    (StartPage().open()
     .click_consultation_button()
     .fill_company_intput('сбер')
     .click_sber()
     .expect_fill_company()
     .expect_page_consultation()
     )


@allure.title('Проверка перехода на страницу аналитики при клике по кнопке в хедере')
def test_transfer_to_analitics_page():
    (StartPage().open()
     .analitics_button_click()
     .expect_page_analitics())

@pytest.mark.xfail(reason='bug')
@allure.title('Выбор продукта и проверка промо-страницы продукта')
def test_expect_product_page():
    (StartPage().open()
     .products_button_click()
     .choise_product()
     .product_promo_button_click()
     .expect_modal_window_product()
     )
