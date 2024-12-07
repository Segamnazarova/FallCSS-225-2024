def start_chapter(player_name):
    print("\n--- Chapter 2: Zombie Encounter ---")
    print(f"{player_name}, the colonels confirm that the zombie infection is spreading rapidly.")
    print("The military is preparing for a counterattack.")
    print("What action will you take?")
    print("1. Shoot at zombies")
    print("2. Welcome survivors")
    print("3. Throw bombs")
    print("4. Set up ultrasound")

    choice = input("Choose an action (1-4): ")

    if choice == "1":
        print("You aim at the incoming zombies and start firing!")
        print("Your shots take down several zombies, but the horde keeps advancing.")
    elif choice == "2":
        print("You welcome the survivors into the military base and help them find safety.")
        print("The survivors thank you, but the base is now more crowded.")
    elif choice == "3":
        print("You throw bombs at the zombies, creating a massive explosion!")
        print("The horde slows down, but your resources are limited.")
    elif choice == "4":
        print("You set up ultrasound equipment to track zombie movements.")
        print("Unfortunately, the zombies don't respond to the ultrasounds.")
    else:
        print("Invalid choice. The situation worsens as chaos grows.")

