from api_requests import add_product_in_cart
import pytest
from selene import browser

# команды для генерации и формирования отчета из урока
# allure generate allure-results -o allure-report-1
# allure open allure-report-1


@pytest.fixture(scope='function', autouse=True)
def clean_cart():
    yield
    browser.element('[name="removefromcart"]').click()
    browser.element('[name="updatecart"]').click()


def test_add_smartphone_in_cart():
    product_name = 'Smartphone'
    product_id = '/catalog/43/1/1'
    add_product_in_cart(product_name, product_id)


def test_add_health_book_in_cart():
    product_name = 'Health Book'
    product_id = '/catalog/22/1/1'
    add_product_in_cart(product_name, product_id)


def test_add_simple_computer_in_cart():
    product_name = 'Simple Computer'
    product_id = '/details/75/1'
    add_product_in_cart(product_name, product_id)