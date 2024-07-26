age = int(input("Enter your age: "))
if age < 13:
    category = 'Child'
elif 13 <= age < 20:
    category = 'Teenager'
elif 20 <= age < 65:
    category = 'Adult'
else:
    category = 'Senior'
print(f"You are categorized as a {category}.")