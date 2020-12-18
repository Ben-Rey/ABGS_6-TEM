class ReceipBuilder(BuilderInterface):

    def __init__(self) -> None:
        self.shop_name = None
        self.shop_adress = None
        self.cash_number = None
        self.casher_id = None
        self.product_list = None
        self.payment = None
        self.date = None

    @property
    def get_receip(self):
        return self

    def add_shop_infos(self, infos ) -> None:
        self.shop_name = infos['shop_informations']['name']
        self.shop_adress = infos['shop_informations']['adress']

    def add_cash_infos(self, cash_number) -> None:
        self.cash_number = cash_number

    def add_date(self, date) -> None:
        self.date = date

    def add_product_list(self, product_list) -> None:
        self.product_list = product_list