
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

pytestmark = pytest.mark.regression

def test_inventory_sorting_hilo(page, base_url):
    LoginPage(page).open(base_url)
    LoginPage(page).login("standard_user", "secret_sauce")
    inv = InventoryPage(page)
    inv.expect_loaded()
    inv.sort_select.select_option("hilo")
    prices = page.locator(".inventory_item_price")
    first_price = float(prices.nth(0).inner_text().replace("$", ""))
    last_price = float(prices.nth(prices.count()-1).inner_text().replace("$", ""))
    assert first_price >= last_price
