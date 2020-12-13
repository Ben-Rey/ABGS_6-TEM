from cashRegister import CashRegister
from fakeDbProduct import FakeDbProduct
from productDbConnector import ProductDbConnector

db_products = FakeDbProduct()
products = db_products.products
cash_register = CashRegister()
db_connector = ProductDbConnector()


def test_price():
    # We add 3 products to the basket
    cash_register.scan_product(products[0]["code"])
    cash_register.scan_product(products[1]["code"])
    cash_register.scan_product(products[2]["code"])
    assert cash_register.pay() == 15


def test_remove_product_from_basket():
    # We delete one product
    product = cash_register.basket.products[0]
    cash_register.delete_product_from_basket(product)
    assert len(cash_register.basket.products) == 2 and product not in cash_register.basket.products

    # We try to delete again the same product
    assert cash_register.delete_product_from_basket(product) == "Product not found"




