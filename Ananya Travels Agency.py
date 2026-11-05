class Travel_Agency:
    def __init__(self):
        self.products = {
            "Age": (
                ("Infant", 1000),
                ("Children", 2000),
                ("Young Adult", 3000),
                ("Adult", 5000),
                ("Senior Citizen", 4000)
            ),
            "Location": (
                ("Los Angeles", 100000),
                ("New York", 120000),
                ("Seoul", 150000),
                ("Tokyo", 200000),
                ("London", 180000),
                ("Paris", 170000),
                ("Dubai", 160000),
                ("Singapore", 140000),
                ("Sydney", 130000),
                ("Toronto", 110000)
                
            ),
            "Inter Transport Mode": (
                ("Bus", 50000),
                ("Rental Car", 80000),
                ("None", 0)
            ),
            "Accommodation": (
                ("Hotel", 30000),
                ("Airbnb", 20000),
                ("Villa", 40000),
                ("Bungalow", 35000),
                ("None", 0)
            ),
        }

    def get_number(self, number):
        try:
            return int(input(number))
        except ValueError:
            print("Please enter a valid number.")
            return None

    def print_bill(
        self, cart: list[tuple[str, tuple[str, int], int]]
    ):
        total = sum(product[1] * quantity for _, product, quantity in cart)
        print("\n" + "=" * 50)
        print("          ANANYA TRAVELS AGENCY")
        print("                 CUSTOMER BILL")
        print("=" * 50)
        for category, (name, price), quantity in cart:
            print(f"Product Category : {category}")
            print(f"Product Name     : {name}")
            print(f"Price            : Rs. {price:,}")
            print(f"Quantity         : {quantity}")
            print(f"Item Total       : Rs. {price * quantity:,}")
            print("-" * 50)
        print(f"TOTAL AMOUNT     : Rs. {total:,}")
        print("=" * 50)
        print("\nThank You for Visiting Ananya Travels Agency!")
        print("Please visit Ananya Travels Agency again!")
        print("=" * 50)

    def run(self):
        print("=" * 50)
        print("   WELCOME TO ANANYA TRAVELS AGENCY")
        print("=" * 50)
        print("We are happy to have you here!\n")
        categories = tuple(self.products)
        cart: list[tuple[str, tuple[str, int], int]] = []
        selected_categories: set[str] = set()

        while True:
            print("Go back to the main menu?\n")
            for number, category in enumerate(categories, start=1):
                print(f"{number}. {category}")

            category_choice = self.get_number(
                f"\nEnter your choice (1-{len(categories)}): "
            )
            if category_choice is None or not 1 <= category_choice <= len(categories):
                print("Invalid category choice!")
                return

            category = categories[category_choice - 1]
            category_products = self.products[category]

            print("\n" + "=" * 50)
            print(f"Available {category}s:")
            print("=" * 50)
            for number, (name, price) in enumerate(category_products, start=1):
                print(f"{number}. {name} - Rs. {price:,}")

            product_choice = self.get_number(
                "\nEnter the corresponding number: "
            )
            if (
                product_choice is None
                or not 1 <= product_choice <= len(category_products)
            ):
                print("Invalid product choice!")
                return

            if category == "Location":
                quantity = 1
            else:
                quantity = self.get_number("Enter quantity: ")
                if quantity is None or quantity <= 0:
                    print("Quantity must be a positive number.")
                    return

            product = category_products[product_choice - 1]
            cart.append((category, product, quantity))
            selected_categories.add(category)

            while True:
                prompt = (
                    "Would you like to go back to the main menu? (yes/no): "
                )
                answer = input(prompt).strip().lower()
                if answer in ("yes", "y"):
                    break
                if answer in ("no", "n"):
                    missing_categories = [
                        category
                        for category in categories
                        if category not in selected_categories
                    ]
                    if missing_categories:
                        print(
                            "\nPlease go back and input a product for each of "
                            "these categories before printing your bill:"
                        )
                        for missing_category in missing_categories:
                            print(f"- {missing_category}")
                        break
                    age_selections = {
                        product[0]
                        for item_category, product, _ in cart
                        if item_category == "Age"
                    }
                    if (
                        age_selections.intersection({"Infant", "Children"})
                        and not age_selections.intersection(
                            {"Adult", "Senior Citizen"}
                        )
                    ):
                        print(
                            "An Adult is required to travel with Infants and Children"
                        )
                        break
                    self.print_bill(cart)
                    return
                print("Please answer yes or no.")


if __name__ == "__main__":
    Travel_Agency().run()