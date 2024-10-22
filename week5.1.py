number=4

guessed_number = int(input("Please guess a number between 1 and 5: "))

if guessed_number <= 5:
    print("good guess!!!!")
elif guessed_number < number:
    print("guess higher!!!!")
elif guessed_number  > number:
    print("guess lower!!!!")
else:
    print("Invalid choice!!!!")

