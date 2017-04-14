#4-1
pizzas=["Pepperoni","Cheese Lover","Mushroom"]
for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print("My fav pizza is "+pizza)

print("Thanks for liking pizzas")

#4-2
pets=["Cat","Dog","Fish"]
for pet in pets:
    print(pet)

for pet in pets:
    print(pet+ " is a great pet")

print("Thanks for liking my pets")

#4-3
numbers = list(range(1, 21))
for number in numbers:
    print(number)
#4-4
#numbers = list(range(1, 10000001))
#for number in numbers:
#    print(number)

#4-5
numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#4-6 summ odd num
numbers = list(range(1,21))
for number in numbers:
    if number%2 == 1:
        print(number)

#4-7
numbers = list(range(1,31))
for number in numbers:
    if number % 3 == 0:
        print(number)

#4-8/4-9
cubes =[]
for number in range(1, 11):
    cube =number**3
    cubes.append(cube)
for cube in cubes:
    print(cube)


#4-10
numList =list(range(1,10))
print(numList[0:3])#first slice
print(numList[3:6])#2nd slice
print(numList[6:10])#third slice

#4-11
favorite_pizzas =["Tikka", "Cheese", "Supremo"]
friend_pizzas =favorite_pizzas[:]
favorite_pizzas.append("Beef Lovers")
friend_pizzas.append("Sausages")
print("My favorite pizzas are:")

for pizza in favorite_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")

for pizza in friend_pizzas:
    print(pizza)

#4-12
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
for food in my_foods:
    print(food)
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)

#4-13
menu_items =( "Steaks", "Burger", "Pita Wraps", "Barbeque", "Sea Food", )

print("You can choose from the following menu items:")
for item in menu_items:
    print(item)

menu_items =( "Fish Burger", "Chicken Strips", "Chowder Soup", "Fried Calamari", "Manchurian", )
print("\nOur menu has been updated.")

print("You can now choose from the following items:")
for item in menu_items:
    print(item)