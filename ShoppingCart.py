class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_item(self, item_name: str, qty: int, unit_price: float):
        self.items.append((item_name, qty, unit_price))

    def remove_item(self, item_name: str):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def calculate_total(self) -> float:
        total = 0.0
        for name, qty, price in self.items:
            total += qty * price
        return total

    def cart_contents(self):
        print("Cart Contents:")
        for name, qty, price in self.items:
            print(f"  {name}:- {qty} @ Ksh {price:.2f} each")
        print(f"Total: Ksh {self.calculate_total():.2f}\n")


class DiscountedCart(ShoppingCart):
    def __init__(self, discount_rate: float):
        super().__init__()
        self.discount_rate = discount_rate 

    def calculate_total(self) -> float:
        """Override this method to apply a discount to the initial total."""
        initial_total = super().calculate_total()
        discount = initial_total * self.discount_rate
        return initial_total - discount


class TaxedCart(ShoppingCart):
    def __init__(self, tax_rate: float):
        super().__init__()
        self.tax_rate = tax_rate

    def calculate_total(self) -> float:
        """Override to add tax on the initial total."""
        initial_total = super().calculate_total()
        tax = initial_total * self.tax_rate
        return initial_total + tax



def checkout(cart: ShoppingCart):
    cart.cart_contents()
    print(f"Total amount: Ksh {cart.calculate_total():.3f}\n")



# IMPLEMENTATION
if __name__ == "__main__":
    # 1) Ordinary Cart
    obj_cart = ShoppingCart()
    obj_cart.add_item("Papaya", 76, 6.20)
    obj_cart.add_item("Orange", 96, 11.50)
    obj_cart.add_item("Kiwi", 85, 9.60)
    print(">>> Ordinary Cart Without Tax & Discount <<<")
    checkout(obj_cart)

    # 2) Discounted Cart
    disc_cart = DiscountedCart(discount_rate=0.15)
    disc_cart.add_item("Papaya", 76, 6.20)
    disc_cart.add_item("Orange", 96, 11.50)
    disc_cart.add_item("Kiwi", 85, 9.60)
    print(">>> Applying a 15% Discount <<<")
    checkout(disc_cart)

    # 3) Taxed Cart
    taxed_cart = TaxedCart(tax_rate=0.12)  # Corrected to 12%
    taxed_cart.add_item("Papaya", 5, 2.00)
    taxed_cart.add_item("Orange", 96, 11.50)
    taxed_cart.add_item("Kiwi", 3, 1.50)
    print(">>> Applying a 12% Tax <<<")
    checkout(taxed_cart)
