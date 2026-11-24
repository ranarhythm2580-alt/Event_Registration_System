event_name = "College Fest"
total_seats = 5
participants = []

while True:
    print("\n--- Event Registration System ---")
    print("1. Register")
    print("2. Cancel Registration")
    print("3. Show Participants")
    print("4. Show Available Seats")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter your name: ")

        if len(participants) < total_seats:
            participants.append(name)
            print("Registration Successful!")
        else:
            print("Sorry! No seats available.")

    elif choice == 2:
        name = input("Enter name to cancel: ")

        if name in participants:
            participants.remove(name)
            print("Registration Cancelled!")
        else:
            print("Participant not found.")

    elif choice == 3:
        print("Registered Participants:", participants)

    elif choice == 4:
        available = total_seats - len(participants)
        print("Available Seats:", available)

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid Choice!")