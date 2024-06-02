import pytest
import allure
from pytest_bdd import given, when, then, scenarios,parsers
from pages.home_page import HomePage as HP
from pages.results_page import ResultsPage as RP
from pages.cart_page import CartPage as CP
from pages.quantity_page import QuantityPage as QP


scenarios('amazon.feature')
allure.feature('amazon.feature')
allure.story("Amazon Product Shopping")

@given('I am on the Amazon homepage')
def launch_amazon_website(page):
    HP(page).launch_browser()
    

@when(parsers.parse('I search for "{product_name}"'))
def product(page, product_name):
    HP(page).search_field(product_name)
    

@then(parsers.parse('I click the "{produt_name}" product to view it and add to my cart')) 
def click_and_view_product_and_add_to_cart(page, produt_name):
    RP(page).select_product(produt_name)
    CP(page).add_to_cart()
    

@then(parsers.parse('I increase the quantity to "{quantity}"'))
def quantity(page, quantity):
    QP(page).increase_qauntity(quantity)
    




    
