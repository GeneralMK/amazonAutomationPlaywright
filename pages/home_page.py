from .base_page import BasePage
from playwright.sync_api import Page

class HomePage(BasePage):
    def __init__(self, page: Page) -> None:
        self.page = page

    def launch_browser(self):
        self.page.goto("https://www.amazon.com/")
        self.page.screenshot(path="screenshots/home.png")
        
       

    def search_field(self, product_name):
        self.page.click("//input[@id='twotabsearchtextbox']")
        self.page.fill("//input[@id='twotabsearchtextbox']", product_name)
        self.page.click("//input[@id='nav-search-submit-button']")
        self.page.screenshot(path="screenshots/searchedIterm.png")
        

        