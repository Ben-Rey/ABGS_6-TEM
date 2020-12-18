from abc import ABC, abstractmethod, abstractproperty
from typing import Any

class BuilderInterface(ABC):

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
