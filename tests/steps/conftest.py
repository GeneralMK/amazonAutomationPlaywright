import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage as HP
from pages.results_page import ResultsPage as RP
from pages.cart_page import CartPage as CP
from pages.quantity_page import QuantityPage as QP


@pytest.fixture
def amazon_home_page(page:Page) -> HP:
    return HP

@pytest.fixture
def search_product(page:Page) -> RP:
    return RP

@pytest.fixture
def view_product_and_add_to_cart(page:Page) -> CP:
    return CP

@pytest.fixture
def increase_quantity(page:Page) -> QP:
    return QP
