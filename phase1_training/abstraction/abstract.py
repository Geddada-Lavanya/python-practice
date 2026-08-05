from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def pay_method(self):
        pass