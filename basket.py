from abc import ABC


class BasketOnHold:

    def __init__(self, basket):
        self.basket = basket
        self.basket.lock = True

    def retrieve_basket(self):
        self.__delattr__('lock')
        return self.basket

    def __str__(self):
        return 'On hold'

    def __iter__(self):
        return self.basket.__iter__()

    def __next__(self):
        return self.basket.__next__()

    def __getattr__(self, item):
        print(self.__dict__)
        return getattr(self.__dict__['basket'], item)

    def __setattr__(self, key, value):
        if key == 'basket':
            self.__dict__[key] = value
        else:
            setattr(self.__dict__['basket'], key)

    def __delattr__(self, item):
        delattr(self.__dict__['basket'], item)


class Basket:
    products = []
    totalPrice = 0

    def __init__(self):
        print('new basket')

    def add_product(self, product):
        self.products.append(product)
        self.totalPrice += product.price
        print(self)

    def remove_product(self, product):
        self.products.remove(product)

    def __str__(self):
        return 'Products: {}'.format(self.products)


