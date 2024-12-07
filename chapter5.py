# chapter5.py

def start_chapter(player_name):
    print("\n--- Chapter 5: Sacrifice ---")
    print(f"{player_name}, this is the final stand.")
    print("After luring all the zombies into a secluded area, you prepare to detonate the explosives.")
    print("Your decision to sacrifice yourself will save the village and possibly the world.")
    print("What will you do?")
    print("1. Send a final message")
    print("2. Press the button to detonate the bomb")

    choice = input("Choose an action (1-2): ")

    if choice == "1":
        print(f"{player_name}: 'This is for humanity. Tell my story!'")
        print(f"{player_name} sends a final heartfelt message to their comrades and loved ones.")
        print("With courage and resolve, you press the button.")
        print("The explosion wipes out all zombies, but your sacrifice saves countless lives.")
    elif choice == "2":
        print(f"{player_name} silently presses the button, knowing this is the only way to stop the zombie threat.")
        print("The explosion eradicates the zombies, and your name becomes a legend in the village.")
    else:
        print("Invalid choice. The bomb remains unactivated, and the zombies break free.")
        print("The village falls to the horde as chaos reigns.")
