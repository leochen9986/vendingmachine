class VendingMachine:
    def __init__(self):
        # Items with price
        self.drinks = {
            1: ("100plus", 3),
            2: ("cola", 4),
            3: ("sprite", 2),
            4: ("mineral water", 1),
            5: ("coffee", 6),
            6: ("tea", 8),
            7: ("starbuck", 11)
        }
        # Type of notes
        self.notes = (1, 5, 10, 20, 50, 100)
        self.amount = 0

    def display_drinks(self):
        print("Available drinks and their prices:")
        for number, (drink, price) in self.drinks.items():
            print(f"{number}. {drink}: MYR {price}")

    def insert_money(self, amount):
        self.amount += amount
        print(f"Inserted MYR {amount}")
        print(f"Total amount inserted: MYR {self.amount}")

    def select_drink(self, drink_number):
        if drink_number not in self.drinks:
            print("Selected drink is not available.")
            return
        
        drink_name, drink_price = self.drinks[drink_number]
        if self.amount < drink_price:
            print(f"Not enough money. {drink_name} costs MYR {drink_price}")
            return
        
        change = self.amount - drink_price
        change_notes = self.calculate_change(change)
        print(f"Dispensing {drink_name}")
        if change > 0:
            print("Returning change:")
            for note, count in change_notes.items():
                print(f"MYR {note}: {count} note{'s' if count > 1 else ''}")
        
        # Reset the amount for the next transaction
        self.amount = 0

    def calculate_change(self, change):
        change_notes = {}
        for note in self.notes:
            if change >= note:
                count = change // note
                change_notes[note] = count
                change -= note * count
        return change_notes


def main():
    vm = VendingMachine()
    
    while True:
        vm.display_drinks()
        
        try:
            drink_number = int(input("Please select a drink by entering the number: "))
            if drink_number not in vm.drinks:
                print("Invalid selection. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        try:
            amount = int(input("Please insert money (e.g., 1, 5, 10, 20, 50, 100): "))
            if amount not in vm.notes:
                print("Invalid note. Please insert a valid note.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid note.")
            continue
        
        vm.insert_money(amount)
        vm.select_drink(drink_number)
        
        another = input("Would you like to buy another drink? (yes/no): ").strip().lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
