import logging
from pages.base_page import BasePage
from playwright.async_api import Page, Mouse


class ResultsPage(BasePage):
    def __init__(self, page: Page) -> None:
        self.page = page

    def select_product(self, product):
        handle_elememt = self.page.wait_for_selector(f"//span[contains(text(),'{product}')]")
        handle_elememt.scroll_into_view_if_needed()
        if self.page.is_visible(f"//span[contains(text(),'{product}')]"):
            self.page.click(f"//span[contains(text(),'{product}')]")
        else:
            logging.info(f"Laptop stand is not available: {product}")
       
        self.page.screenshot(path="screenshots/item.png")
