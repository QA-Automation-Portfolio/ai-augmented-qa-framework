
from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.add_to_cart_buttons = page.locator("button:has-text('Add to cart')")
        self.sort_select = page.locator("[data-test='product_sort_container']")
        self.cart_link = page.locator(".shopping_cart_link")

    def expect_loaded(self):
        expect(self.title).to_have_text("Products")

    def add_first_n_products(self, n: int = 2):
        count = self.add_to_cart_buttons.count()
        for i in range(min(n, count)):
            self.add_to_cart_buttons.nth(i).click()

    def open_cart(self):
        self.cart_link.click()
