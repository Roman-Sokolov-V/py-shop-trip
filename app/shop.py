from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def cost_products(self, product_cart: dict) -> float:
        coast = 0
        for product, value in product_cart.items():
            coast += self.products[product] * value
        return coast
