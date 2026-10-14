
from abc import ABC, abstractmethod


# PILLAR 1: ABSTRACTION
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# PILLAR 2: INHERITANCE
class CashPayment(Payment):

    def pay(self, amount):
        print(f"Paid Rs. {amount:.2f} using Cash.")


class UpiPayment(Payment):

    def pay(self, amount):
        print(f"Paid Rs. {amount:.2f} using UPI.")


# RESTAURANT CLASS
class Restaurant:

    def __init__(self):
        self.menu = {
            1: ("Pizza", 199),
            2: ("Burger", 99),
            3: ("Pasta", 149),
            4: ("Coffee", 79),
            5: ("Sandwich", 89)
        }

        self.order = {}

    def show_menu(self):
        print("\n====== RESTAURANT MENU ======")

        for item_id, details in self.menu.items():
            name, price = details
            print(f"{item_id}. {name} - Rs. {price}")

    def add_order(self, item_id, quantity):
        if item_id not in self.menu:
            print("Invalid menu item!")
            return

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        # PILLAR 3: ENCAPSULATION
        # Order data is managed through this method.
        name, price = self.menu[item_id]

        if item_id in self.order:
            self.order[item_id][1] += quantity
        else:
            self.order[item_id] = [name, quantity, price]

        print(f"{quantity} x {name} added to your order!")

    def show_bill(self):
        if not self.order:
            print("Your order is empty!")
            return 0

        print("\n========== YOUR BILL ==========")
        total = 0

        for name, quantity, price in self.order.values():
            item_total = quantity * price
            print(
                f"{name} x {quantity} = Rs. {item_total:.2f}"
            )
            total += item_total

        print("-------------------------------")
        print(f"Total Bill: Rs. {total:.2f}")

        return total


# MAIN PROGRAM
def main():

    restaurant = Restaurant()

    print("Welcome to Python Restaurant!")

    while True:
        print("\n1. View Menu")
        print("2. Order Food")
        print("3. View Bill")
        print("4. Pay and Exit")
        print("5. Exit Without Paying")

        choice = input("Enter your choice: ")

        if choice == "1":
            restaurant.show_menu()

        elif choice == "2":
            restaurant.show_menu()

            try:
                item_id = int(input("Enter item number: "))
                quantity = int(input("Enter quantity: "))

                restaurant.add_order(item_id, quantity)

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "3":
            restaurant.show_bill()

        elif choice == "4":
            total = restaurant.show_bill()

            if total > 0:
                print("\nChoose payment method:")
                print("1. Cash")
                print("2. UPI")

                method = input("Enter choice: ")

                if method == "1":
                    payment = CashPayment()
                elif method == "2":
                    payment = UpiPayment()
                else:
                    print("Invalid payment method!")
                    continue

                payment.pay(total)
                print("Thank you! Visit again.")
                break

            else:
                print("Please order something first.")

        elif choice == "5":
            print("Thank you for visiting!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
