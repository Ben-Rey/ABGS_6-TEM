from cashRegister import CashRegister
from basket import Basket, BasketOnHold
from fakeDbProduct import FakeDbProduct
from productDbConnector import ProductDbConnector

db_products = FakeDbProduct()
products = db_products.products
cash_register = CashRegister()
db_connector = ProductDbConnector()


def test_price():
    # We add 3 products to the basket
    cash_register.basket = Basket()
    cash_register.scan_product(products[0]["code"])
    cash_register.scan_product(products[1]["code"])
    cash_register.scan_product(products[2]["code"])
    assert cash_register.total_price() == 15


def test_code():
    # We add 3 products to the basket
    assert cash_register.scan_product('fake code') is None


def test_remove_product_from_basket():
    # We delete one product
    product = cash_register.basket.products[0]
    cash_register.delete_product_from_basket(product)
    assert len(cash_register.basket.products) == 2 and product not in cash_register.basket.products

    # We try to delete again the same product
    assert cash_register.delete_product_from_basket(product) == "Product not found"


def test_basket_on_hold():
    cash_register.put_basket_on_hold()
    assert cash_register.basket is None and isinstance(cash_register.basketOnHold, BasketOnHold)
