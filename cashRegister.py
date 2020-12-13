import sys
from basket import Basket
from product import Product
from productDbConnector import ProductDbConnector


class CashRegister:
    basket = None

    def __init__(self):
        self.basket = Basket()
        self.db_connector = ProductDbConnector()

    def scan_product(self, code):
        product = self.db_connector.get_product_by_code(code)
        product_to_add = Product(product)
        self.basket.add_product(product_to_add)

    def delete_product_from_basket(self, product):
        try:
            self.basket.remove_product(product)
        except ValueError:
            return "Product not found"

    def pay(self):
        return self.basket.totalPrice
        print('Pay')

    # def on_hold(self):
    #     print('On hold')
    #
    # def quit(self):
    #     print("ByeBye")
    #     sys.exit(0)
    #
    # def retrieve_basket_on_hold(self):
    #     print('retrieve on hold basket')
