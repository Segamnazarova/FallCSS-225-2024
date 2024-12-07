def start_chapter(player_name):
    print("\n--- Chapter 1: Chaos at the Base ---")
    print(f"{player_name}, you are training at the military base when chaos erupts.")
    print("What will you do?")
    print("1. Start panicking")
    print("2. Run home")
    print("3. Deny the situation")
    print("4. Ask the colonels about the situation")

    choice = input("Choose an action (1-4): ")

    if choice == "1":
        print("You start panicking, but it doesn't help!")
        print("You lose precious time, and the situation worsens.")
    elif choice == "2":
        print("You decide to run home. The streets are chaotic, and danger is everywhere.")
        print("You manage to reach home safely for now.")
    elif choice == "3":
        print("You deny the situation and dismiss the reports as rumors.")
        print("However, the chaos grows, and you realize it's real.")
    elif choice == "4":
        print("You ask the colonels about the situation.")
        print("They brief you on the zombie attack and tell you to stay ready.")
    else:
        print("Invalid choice. The chaos continues as you stand frozen.")
