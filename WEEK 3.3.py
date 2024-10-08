
name = input("What is your name?")
print("Hello, ",name)


age = int(input("How old are you? "))
print("You are", age, " years old.")

if age >= 65:
    print("You should retire!")
elif age <= 18:
    print("Have you finish high school?")
else:
    print("good age!")