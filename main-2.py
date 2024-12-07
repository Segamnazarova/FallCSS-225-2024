import chapter1
import chapter2
import chapter3
import chapter4
import chapter5


def main():
    print("Welcome to the Zombie Apocalypse Game!")
    player_name = input("Enter your name: ")
    print(f"Hello, {player_name}. Let's begin your adventure.")

    # Start the game chapters in sequence
    chapter1.start_chapter(player_name)
    chapter2.start_chapter(player_name)
    chapter3.start_chapter(player_name)
    chapter4.start_chapter(player_name)
    chapter5.start_chapter(player_name)

    print("\n--- The End ---")
    print("Thank you for playing! Your bravery and decisions shaped the outcome of this story.")
    print("Goodbye!")

if __name__ == "__main__":
    main()
