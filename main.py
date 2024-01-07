class TripPlanner:
    def __init__(self):
        self.users = []
        self.countries = {
            'Italy': ['Colosseum', 'Vatican City', 'Florence Cathedral'],
            'Spain': ['Sagrada Familia', 'Park Guell', 'Prado Museum'],
            'Germany': ['Brandenburg Gate', 'Neuschwanstein Castle', 'Cologne Cathedral'],
            'France': ['Eiffel Tower', 'Louvre Museum', 'Versailles Palace'],
            'United Kingdom': ['Big Ben', 'Tower of London', 'Buckingham Palace'],
            'Netherlands': ['Anne Frank House', 'Rijksmuseum', 'Keukenhof Gardens'],
            'Norway': ['Fjords of Norway', 'Viking Ship Museum', 'Northern Lights Tour']
        }

    def create_account(self, username, password):
        user = {'username': username, 'password': password}
        self.users.append(user)
        print(f"\nAccount created successfully for user: {username}")

    def user_login(self, username, password):
        for user in self.users:
            if user['username'] == username and user['password'] == password:
                return True
        return False

    def plan_trip(self, username):
        print("\nWelcome to the Trip Planner!")
        if not self.user_login(username, input("Enter your password: ")):
            print("Invalid login credentials. Exiting.")
            return

        print("\nSelect the countries you want to visit:")
        for i, country in enumerate(self.countries.keys(), start=1):
            print(f"{i}. {country}")

        selected_countries = []
        while True:
            choice = int(input("Enter the country number to add to your trip (0 to finish): "))
            if choice == 0:
                break
            elif 1 <= choice <= len(self.countries):
                selected_countries.append(list(self.countries.keys())[choice - 1])

        num_people = int(input("Enter the number of people in your group: "))
        total_charge = 0

        print("\nYour Trip Itinerary:")
        for country in selected_countries:
            print(f"\nCountry: {country}")
            attractions = self.countries[country]
            print("Attractions:")
            for attraction in attractions:
                print(f"- {attraction}")

            charge_per_country = 100  # Placeholder charge, you can adjust based on your actual pricing.
            total_charge += charge_per_country * num_people
            print(f"Charge for {country}: ${charge_per_country * num_people}")

        print(f"\nTotal Charge for the trip: ${total_charge}")
        print("\nThank you for planning your trip with us!")

    def run(self):
        while True:
            print("\nTrip Planning Management System")
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")

            choice = int(input("Enter your choice: "))
            if choice == 1:
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                self.create_account(username, password)
            elif choice == 2:
                username = input("Enter your username: ")
                self.plan_trip(username)
            elif choice == 3:
                print("Exiting the Trip Planning Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    trip_planner = TripPlanner()
    trip_planner.run()
