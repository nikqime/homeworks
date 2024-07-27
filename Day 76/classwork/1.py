numbers = [5, 8, 13, 22, 36, 41, 57, 68, 79, 84, 95, 102, 117, 124, 139]
even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print(even_numbers)
print(odd_numbers)