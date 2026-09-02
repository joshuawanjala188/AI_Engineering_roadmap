
#A list stores multiple values in a specific order.
numbers = [10, 20, 30, 40, 50]

#Slicing a list

print(numbers[1:3])

number = int(input("Enter a number: "))

#append is adding a number to the end
#numbers.append(number)

#insert adding a number to a specific position
#numbers.insert(1, number)

#Extend  add multiple items

numbers.extend([15, 16, 17])

# removing items

#list length check using len(list)

numbers.remove(17)

#pop it is basically removing an element using an index

numbers.pop(1)
for i in numbers:
    print(i)

print(f"Length is {len(numbers)}")
    

#They are mutable meaning you can modify them