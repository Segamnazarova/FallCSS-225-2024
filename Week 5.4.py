# list1 =[0,1,2,3,4]
#
# for i in list1:
#     print("This is i:", i)
#
#     for i in range(6):
#         print("This is a i:", i)

weapons= ["sword", 'stone', "shield"]

weapons2 = ["sword", 'stone', "Hammer"]


for weapon in weapons:
    print("Weapon in your bag: ", weapon)
    if weapon in weapons2:
            print("You already have that weapon!!!")
    else:
        print("Weapon: ", weapon, " has been added to your bag!")