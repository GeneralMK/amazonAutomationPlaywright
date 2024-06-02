from pages.base_page import BasePage
from playwright.sync_api import Page, expect



class CartPage(BasePage):
       def __init__(self, page: Page) -> None:
        self.page = page

       def add_to_cart(self):
        self.page.click("//input[@id='add-to-cart-button']")
         #validate that product has been added
        expect(self.page.get_by_role(role="heading", name="Added to Cart")).to_have_text('Added to Cart')
        #go to cart
        self.page.click("//a[@href='/cart?ref_=sw_gtc']")
        

    




            

