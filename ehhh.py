users = []
countries = {
    'Italy': ['Colosseum', 'Vatican City', 'Florence Cathedral'],
    'Spain': ['Sagrada Familia', 'Park Guell', 'Prado Museum'],
    'Germany': ['Brandenburg Gate', 'Neuschwanstein Castle', 'Cologne Cathedral'],
    'France': ['Eiffel Tower', 'Louvre Museum', 'Versailles Palace'],
    'United Kingdom': ['Big Ben', 'Tower of London', 'Buckingham Palace'],
    'Netherlands': ['Anne Frank House', 'Rijksmuseum', 'Keukenhof Gardens'],
    'Norway': ['Fjords of Norway', 'Viking Ship Museum', 'Northern Lights Tour']
    }

def create_account( username, password):
    user = {'username': username, 'password': password, 'trips': []}
    users.append(user)
    print(f"\nAccount created successfully for user: {username}")

def user_login( username, password):
        for user in users:
            if user['username'] == username and user['password'] == password:
                return True
        return False

def list_all():
        # r = str(input("do you want to write this to a text file? y/n"))
        print("\n\nthe current planned trips are :\n")
        for i in users :
            print(i["username"], " has the follwing ongoing trips :\n")
            for j in i["trips"]:
                print("\t\t", j["country"]," :")
                print("\t\t\titenerary : ")
                for l in countries[j["country"]] :
                    print("\t\t\t - ", l)
                print("\t\t\tnumber of people : ", j["number of people"])
                print("\t\t\tdate : ", j["date"])
                print("\t\t\tamount pending : ", j["amount pending"])

def plan_trip( username):
    print("\nWelcome to the Trip Planner!")
    if not user_login(username, input("Enter your password: ")):
        print("Invalid login credentials. Exiting.")
        return

    print("\nSelect the countries you want to visit:")
    for i, country in enumerate(countries.keys(), start=1):
        print(f"{i}. {country}")

    selected_countries = []
    while True:
        choice = int(input("Enter the country number to add to your trip (0 to finish): "))
        if choice == 0:
            break
        elif 1 <= choice <= len(countries):
            selected_countries.append(list(countries.keys())[choice - 1])

    num_people = int(input("Enter the number of people in your group: "))
    total_charge = 0

    print("\nYour Trip Itinerary:")
    for country in selected_countries:
            
        print(f"\nCountry: {country}")
        attractions = countries[country]
        print("Attractions:")
        for attraction in attractions:
            print(f"- {attraction}")

        charge_per_country = 100  # Placeholder charge, you can adjust based on your actual pricing.
        total_charge += charge_per_country * num_people
        curr = charge_per_country * num_people
        print(f"Charge for {country}: ${charge_per_country * num_people}")
        pay = str(input("has the payment been made? y/n\n"))
        date = str(input("input the date of the start of your 1 week trip in the format dd/mm/yy :"))
        matches = 0
        for k in users :
            for t in k['trips'] :
                try :
                    if t["date"] == date and t["country"] == country:
                        matches += 1
                except :
                        matches = matches

        for n in users :
            if n['username'] == username and pay == "n" and matches == 0:
                n['trips'].append({"country": country, "number of people": num_people, "date" : date, "amount pending" : curr})
            elif n['username'] == username and pay == "y" and matches == 0:
                n['trips'].append({"country": country, "number of people": num_people, "date" : date, "amount pending" : 0})
            elif matches != 0 :
                print("date not available for selected country")
                return
            else :
                print("invalid entry, trip terminated")
                return
    print(f"\nTotal Charge for the trip: ${total_charge}")
    print("\nThank you for planning your trip with us!")       

while True:
    print("\nTrip Planning Management System")
    print("1. Create Account")
    print("2. Login")
    print("3. List plans")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        create_account(username, password)
    elif choice == 2:
        username = input("Enter your username: ")
        plan_trip(username)
    elif choice == 3:
        list_all()
    elif choice == 4:
        print("Exiting the Trip Planning Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")