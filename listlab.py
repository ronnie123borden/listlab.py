
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)

fruit = input("Enter another fruit > ")
fruits.append(fruit)
print(fruits)

number = int(input("Enter a number > "))
print(fruits[number - 1])

fruit = input("Enter a fruit to add to the beginning > ")
fruits = [fruit] + fruits
print(fruits)

fruit = input("Enter another fruit to add to the beginning > ")
fruits.insert(0, fruit)
print(fruits)

for fruit in fruits:
    if fruit[0] == "P":
        print(fruit)

print(fruits)

fruits.pop()
print(fruits)

fruit = input("Enter a fruit to delete > ")
if fruit in fruits:
    fruits.remove(fruit)
print(fruits)

fruits = fruits * 2

fruit = input("Enter a fruit to delete > ")
while fruit not in fruits:
    fruit = input("Enter a fruit to delete > ")

while fruit in fruits:
    fruits.remove(fruit)

fruits = ["Apples", "Pears", "Oranges", "Peaches"]

for fruit in fruits[:]:
    answer = input("Do you like " + fruit.lower() + "? > ")
    while answer != "yes" and answer != "no":
        answer = input("Please answer yes or no > ")
    if answer == "no":
        fruits.remove(fruit)

print(fruits)

fruits = ["Apples", "Pears", "Oranges", "Peaches"]
reversed_fruits = []

for fruit in fruits:
    reversed_fruits.append(fruit[::-1])

fruits.pop()

print(fruits)
print(reversed_fruits)
