import datetime

class TicketDirector:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def createReceip(self, builder):
        self.builder.get_receip()

    def get_data(product_list, payment, cash_number, casher_id)
        return data = {
            'date': datetime.datetime.now(),
            'product_list':product_list,
            'payment': payment,
            'cash_number': cash_number,
            'casher_id': casher_id,
            'shop_informations': {
                'name': 'Blabla',
                'adress' : 'Blablabla'
            }
        }

    def createReceip()
    
