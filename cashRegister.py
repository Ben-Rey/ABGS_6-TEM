import sys
from basket import Basket, BasketOnHold
from product import Product
from productDbConnector import ProductDbConnector
import logging


class CashRegister:
    basket = None
    basketOnHold = None

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.db_connector = ProductDbConnector()

    def start(self):
        # verification caisse
        # Lancement nouveau panier
        self.new_basket()

    def new_basket(self):
        self.basket = Basket()
        while True:
            print("--------------------")
            print("Scan a product")
            code = input("code: ")
            print("--------------------")
            self.scan_product(code)

    def scan_product(self, code):
        product = self.db_connector.get_product_by_code(code)
        if product:
            product_to_add = Product(product)
            self.basket.add_product(product_to_add)
        else:
            print('Produit n\'existe pas')

    def delete_product_from_basket(self, product):
        try:
            self.basket.remove_product(product)
        except ValueError:
            return "Product not found"

    def total_price(self):
        return self.basket.totalPrice

    def pay(self):
        print('Pay')

    def put_basket_on_hold(self):
        self.basketOnHold = BasketOnHold(self.basket)
        self.basket = None
        print('On hold')

    def get_basket_on_hold(self):
        return self.basketOnHold

    # def quit(self):
    #     print("ByeBye")
    #     sys.exit(0)

    # def retrieve_basket_on_hold(self):
    #     print('retrieve on hold basket')
