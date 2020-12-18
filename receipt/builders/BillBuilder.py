class BillBuilder(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        product = self._product
        self.reset()
        return product

    @abstractproperty
    def product(self) -> None:
        pass

    @abstractmethod
    def add_shop_infos(self) -> None:
        pass

    @abstractmethod
    def add_cash_infos(self) -> None:
        pass

    @abstractmethod
    def add_date(self) -> None:
        pass

    @abstractmethod
    def add_product_list(self) -> None:
        pass