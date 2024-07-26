numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]

if len(numbers) == 0:
    print("The list is empty.")
else:
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    print(f"The largest number in the list is {largest}.")