from math import sqrt
from app.cars import Car


class Customer:

    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: float,
            car: dict
    ) -> None:
        self.name = name
        self.car = car
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(*car.values())

    def __repr__(self) -> str:
        return f"Customer: {self.__dict__}"

    def distance(self, shop_location: list) -> float:
        _x = abs(self.location[0] - shop_location[0])
        _y = abs(self.location[1] - shop_location[1])
        return sqrt(abs(_x ** 2 + _y ** 2))
