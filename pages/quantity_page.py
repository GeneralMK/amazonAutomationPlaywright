import logging
from pages.base_page import BasePage
from playwright.sync_api import Page


class QuantityPage(BasePage):
     def __init__(self, page: Page) -> None:
        self.page = page

     def increase_qauntity(self, quantity):
         self.page.wait_for_timeout(10000)
         self.page.screenshot(path="screenshots/cart_product.png")
         price_locator = self.page.locator("//form[@id='activeCartViewForm']//div[@data-name='Subtotals']//span[@class='a-size-medium a-color-base sc-price sc-white-space-nowrap']")
         self.page.get_by_label("Qty:").select_option(quantity)

         # Get the initial price
         initial_price = price_locator.inner_text()

         # making sure that the price locator is visible before proceeding
         self.page.wait_for_selector("//div[@class='a-section a-spacing-mini']//span", state='visible', timeout=60000)

         # Wait for the price to change using a loop
         
         timeout = 60000  # 60 seconds
         interval = 500  # 0.5 seconds
         elapsed = 0

         while elapsed < timeout:
            updated_price = price_locator.inner_text()
            logging.info(f"Elapsed time: {elapsed}ms, Updated Price: {updated_price}")

            if updated_price != initial_price:
                break

            self.page.wait_for_timeout(interval)
            elapsed += interval

        # Check if price actually changed
         updated_price = price_locator.inner_text()

         assert updated_price != initial_price, "Price did not change after selecting quantity."
         logging.info(f"Price change: {updated_price}")
         self.page.screenshot(path="screenshots/quantity.png")
         

