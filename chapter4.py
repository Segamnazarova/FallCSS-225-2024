def start_chapter(player_name):
    print("\n--- Chapter 4: The Final Plan ---")
    print(f"{player_name}, the village is in complete disarray, and morale is low.")
    print("You realize that zombies are best contained in dark areas, but space is running out.")
    print("It's time to come up with a decisive plan to save the village.")
    print("What will you do?")
    print("1. Sacrifice yourself")
    print("2. Keep running")
    print("3. Set up a trap")

    choice = input("Choose an action (1-3): ")

    if choice == "1":
        print(f"{player_name}, you bravely decide to sacrifice yourself to save the village.")
        print("You suit up with explosives and prepare to lure the zombies into a secluded area.")
    elif choice == "2":
        print(f"{player_name} decides to keep running, but the zombies continue to spread.")
        print("The situation worsens as the zombies grow in number and overwhelm the village.")
    elif choice == "3":
        print(f"{player_name} sets up traps to lure the zombies into a secluded area.")
        print("The traps work temporarily, but the situation remains critical.")
    else:
        print("Invalid choice. The zombies continue advancing as time runs out.")
