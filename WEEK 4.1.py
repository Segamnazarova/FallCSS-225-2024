direction = input("Which way would youlist to go [left] [right]: ")
print(direction)

if direction.casefold() == 'lef':
    print("going left")
elif direction.casefold() == 'right':
    print("going right")
else:
    print("Invalid direction!")