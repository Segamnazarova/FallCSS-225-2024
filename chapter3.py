# chapter3.py

def start_chapter(player_name):
    print("\n--- Chapter 3: Darkness Strategy ---")
    print(f"{player_name}, the military discovers that zombies remain stationary in dark areas.")
    print("You need to strategize and take action.")
    print("What will you do?")
    print("1. Collect zombies in dark areas")
    print("2. Keep shooting and bombing")
    print("3. Ask for additional help")
    print("4. Set up diversions")

    choice = input("Choose an action (1-4): ")

    if choice == "1":
        print("You carefully lead the zombies into dark areas where they remain still.")
        print("This strategy works for now, but the dark areas are quickly filling up.")
    elif choice == "2":
        print("You continue shooting and bombing the zombies.")
        print("You manage to slow them down, but your resources are depleting fast.")
    elif choice == "3":
        print("You call for reinforcements and additional supplies.")
        print("Help arrives, boosting morale and resources!")
    elif choice == "4":
        print("You set up diversions to lure zombies away from populated areas.")
        print("This buys the team some time to regroup and strategize.")
    else:
        print("Invalid choice. The zombies advance while you hesitate.")
