class TicketingSystem:
    def __init__(self):
        self.available_tickets = 100  # Total tickets available
        self.ticket_price = 50  # Price per ticket

    def display_tickets(self):
        print(f"Tickets Available: {self.available_tickets}")
        print(f"Price per ticket: ${self.ticket_price}")
        
    def book_tickets(self):
        self.display_tickets()
        
        # Get number of tickets to book
        try:
            tickets_to_book = int(input("Enter the number of tickets you want to book: "))
            
            if tickets_to_book > self.available_tickets:
                print(f"Sorry, only {self.available_tickets} tickets are available.")
            elif tickets_to_book <= 0:
                print("Please enter a valid number of tickets.")
            else:
                total_price = tickets_to_book * self.ticket_price
                print(f"Total amount: ${total_price}")
                
                # Process payment
                payment = float(input(f"Please enter the amount to pay (Total: ${total_price}): $"))
                
                if payment < total_price:
                    print("Insufficient funds. Try again.")
                else:
                    self.available_tickets -= tickets_to_book
                    change = payment - total_price
                    print(f"Booking successful! Your change is: ${change:.2f}")
                    print(f"Tickets remaining: {self.available_tickets}")
                    
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
    def run(self):
        print("Welcome to the Online Ticketing System!")
        while True:
            print("\n1. View Available Tickets")
            print("2. Book Tickets")
            print("3. Exit")
            
            choice = input("Choose an option: ")
            
            if choice == '1':
                self.display_tickets()
            elif choice == '2':
                self.book_tickets()
            elif choice == '3':
                print("Thank you for using the Online Ticketing System!")
                break
            else:
                print("Invalid option. Please choose again.")

# Run the system
if __name__ == "__main__":
    system = TicketingSystem()
    system.run()
