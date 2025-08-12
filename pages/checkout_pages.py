
from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_btn = page.locator("[data-test='checkout']")
    def checkout(self):
        self.checkout_btn.click()

class CheckoutStepOne:
    def __init__(self, page: Page):
        self.page = page
        self.first = page.locator("[data-test='firstName']")
        self.last = page.locator("[data-test='lastName']")
        self.postal = page.locator("[data-test='postalCode']")
        self.continue_btn = page.locator("[data-test='continue']")
    def fill(self, first, last, postal):
        self.first.fill(first)
        self.last.fill(last)
        self.postal.fill(postal)
        self.continue_btn.click()

class CheckoutStepTwo:
    def __init__(self, page: Page):
        self.page = page
        self.finish_btn = page.locator("[data-test='finish']")
    def finish(self):
        self.finish_btn.click()

class CheckoutComplete:
    def __init__(self, page: Page):
        self.page = page
        self.heading = page.locator(".complete-header")
    def expect_success(self):
        expect(self.heading).to_have_text("Thank you for your order!")
