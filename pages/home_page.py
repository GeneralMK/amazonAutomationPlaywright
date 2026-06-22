from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_box = page.locator("#twotabsearchtextbox")
        self.search_button = page.locator("#nav-search-submit-button")

    def launch_browser(self):
        self.page.goto("https://www.amazon.com/", wait_until="domcontentloaded", timeout=60000)

        if "captcha" in self.page.url.lower() or self.page.locator("text=Enter the characters you see").is_visible():
            raise Exception("Amazon bot-check/captcha detected. This test cannot run reliably in CI against amazon.com.")

        expect(self.search_box).to_be_visible(timeout=60000)

    def search_field(self, product_name: str):
        expect(self.search_box).to_be_visible(timeout=60000)
        self.search_box.fill(product_name)
        self.search_button.click()