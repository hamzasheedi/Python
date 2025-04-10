# 1. Creating a list
fruits = ["apple", "banana", "cherry"]
print("🍎 Original list:", fruits)

# 2. Indexing and Slicing
print("📍 First fruit:", fruits[0])
print("📍 Last fruit:", fruits[-1])
print("🔪 Slice [0:2]:", fruits[0:2])

# 3. Modifying list elements
fruits[1] = "blueberry"
print("✏️ After modifying second item:", fruits)

# 4. Adding elements
fruits.append("orange")
print("➕ After append:", fruits)

fruits.extend(["kiwi", "grape"])
print("➕ After extend:", fruits)

fruits.insert(1, "mango")
print("🪄 After insert at index 1:", fruits)

# 5. Removing elements
fruits.remove("cherry")  # Removes first occurrence
print("🗑️ After remove 'cherry':", fruits)

popped = fruits.pop()  # Removes last item
print("👋 Popped item:", popped)
print("🧼 After pop:", fruits)

fruits.clear()
print("🧹 After clear:", fruits)

# 6. Rebuilding list for further examples
numbers = [3, 6, 1, 9, 2, 3]
print("\n🔢 Numbers list:", numbers)

# 7. Index, Count
print("🔍 Index of 3:", numbers.index(3))
print("🔢 Count of 3:", numbers.count(3))

# 8. Sort and Reverse
numbers.sort()
print("⬆️ After sort:", numbers)

numbers.reverse()
print("⬇️ After reverse:", numbers)

# 9. Looping through a list
print("\n🔁 Looping through list:")
for number in numbers:
    print(number)

# 10. List Comprehensions
squares = [x**2 for x in range(5)]
print("🧮 List comprehension (squares):", squares)

# 11. Filtering with list comprehension
evens = [x for x in numbers if x % 2 == 0]
print("🧊 Even numbers:", evens)

# 12. Nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("🧱 Nested list (matrix):", matrix)
print("🎯 Accessing matrix[1][2]:", matrix[1][2])  # Should print 6
