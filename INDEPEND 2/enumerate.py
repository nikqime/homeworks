haystack = ["hay", "hay", "needle", "hay"]

# Using enumerate to get index and item
for index, item in enumerate(haystack):
    print(f"Index: {index}, Item: {item}")
'''Output:
Index: 0, Item: hay
Index: 1, Item: hay
Index: 2, Item: needle
Index: 3, Item: hay'''