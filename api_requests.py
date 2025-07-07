import allure
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from selene import browser, have
import logging


LOGIN = "meschenenkovjob@gmail.com"
PASSWORD = "D3m05h0p"
WEB_URL = "https://demowebshop.tricentis.com/"
API_URL = "https://demowebshop.tricentis.com/"


def add_product_in_cart(product_name, product_id):
    f"""add_{product_name}_in_cart"""
    with step("Login with API"):
        result = requests.post(
            url=API_URL + "/login",
            data={"Email": LOGIN, "Password": PASSWORD, "RememberMe": False},
            allow_redirects=False
        )
        allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")

    with step("Get cookie from API"):
        cookie = result.cookies.get("NOPCOMMERCE.AUTH")

    with step("Set cookie from API"):
        browser.open(WEB_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        browser.open(WEB_URL)

    with step(f"add {product_name} in cart with API"):
        requests.post(f"https://demowebshop.tricentis.com/addproducttocart{product_id}",
                      cookies={'NOPCOMMERCE.AUTH': cookie}, allow_redirects=False)
        allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.text)

    with step("UI verify cart"):
        browser.element("#topcartlink").click()
        browser.element(".product-name").should(have.exact_text(f'{product_name}'))
