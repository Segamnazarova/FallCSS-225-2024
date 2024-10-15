

age = int(input("Enter your age: "))

if age >= 18:
    print("you can vote")
    print("Enter an X in the box")
else:
    print("You are {1} years old, you can't vote, thanks {0}.".format( age,name))