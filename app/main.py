import json
import datetime
from shop import Shop
from customers import Customer


def shop_trip() -> None:
    with (open("config.json", "r") as f):
        all_data = json.load(f)
        shops = [Shop(*item.values()) for item in all_data["shops"]]
        customers = [
            Customer(*item.values())
            for item
            in all_data["customers"]
        ]
        for customer in customers:
            print(f"{customer.name} has {customer.money} dollars")
            list_trip = []
            for shop in shops:
                coast_cart = shop.cost_products(customer.product_cart)
                distance = customer.distance(shop.location)
                coast_trip = (customer.car.amount_of_fuel(distance)
                              * all_data["FUEL_PRICE"])
                full_coast = round((coast_cart + coast_trip), 2)
                list_trip.append([full_coast, shop])
                print(
                    f"{customer.name}'s trip to the"
                    f" {shop.name} costs {full_coast}")

            best_trip = min(list_trip)

            if customer.money >= best_trip[0]:
                print(f"{customer.name} rides to {best_trip[1].name}")
                print("")
                print(f"Date {datetime.datetime.now()}")

                print(f"Thanks, {customer.name}, for your purchase!")
                print("You have bought: ")
                for product, quantity in customer.product_cart.items():
                    print(
                        f"{quantity} {product}s for"
                        f" {shop.products[product] * quantity} dollars")
                print(
                    f"Total cost is"
                    f" {shop.cost_products(customer.product_cart)} dollars"
                )
                print("See you again!")

                print(f"{customer.name} rides home")
                customer.money = customer.money - best_trip[0]
                print(
                    f"{customer.name} now has"
                    f" {customer.money} dollars")
                print("")
                print("")
            else:
                print(
                    f"{customer.name}'s trip to the"
                    f" {best_trip[1].name} costs {best_trip[0]}"
                )
                print(
                    f"{customer.name} doesn't have enough money"
                    f" to make a purchase in any shop"
                )
