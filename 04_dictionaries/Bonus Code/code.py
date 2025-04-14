# Mega Dictionary Concepts in Python

def dict_basics():
    print("\n--- 1. Creating and Accessing Dictionary ---")
    student = {"name": "Hamza", "age": 21, "city": "Karachi"}
    print("Student Dictionary:", student)
    print("Name:", student["name"])
    print("Age:", student.get("age"))  # Safe way to get value

def dict_update_add():
    print("\n--- 2. Adding and Updating Values ---")
    student = {"name": "Ali", "age": 20}
    student["city"] = "Lahore"  # Adding
    student["age"] = 21  # Updating
    print("Updated Dictionary:", student)

def dict_delete():
    print("\n--- 3. Deleting Keys ---")
    student = {"name": "Sara", "age": 22, "course": "Python"}
    del student["age"]  # Delete using del
    removed = student.pop("course")  # Delete and get value
    print("After Deletion:", student)
    print("Removed Value:", removed)

def dict_looping():
    print("\n--- 4. Looping Through Dictionary ---")
    person = {"name": "Ali", "age": 25, "city": "Islamabad"}
    for key in person:
        print(f"Key: {key}, Value: {person[key]}")

    print("\nUsing .items():")
    for key, value in person.items():
        print(f"{key}: {value}")

def dict_checking():
    print("\n--- 5. Key Existence ---")
    user = {"username": "admin", "password": "1234"}
    print("username" in user)  # True
    print("email" not in user)  # True

def dict_nested():
    print("\n--- 6. Nested Dictionaries ---")
    employees = {
        "emp1": {"name": "Ali", "position": "Manager"},
        "emp2": {"name": "Sara", "position": "Developer"}
    }
    print("Employees Dictionary:", employees)
    print("Emp2 Name:", employees["emp2"]["name"])

def dict_keys_values():
    print("\n--- 7. Getting Keys and Values ---")
    data = {"brand": "Toyota", "model": "Corolla", "year": 2020}
    print("Keys:", list(data.keys()))
    print("Values:", list(data.values()))

def dict_from_list():
    print("\n--- 8. Dictionary from List ---")
    keys = ["a", "b", "c"]
    values = [1, 2, 3]
    combined = dict(zip(keys, values))
    print("Created from lists:", combined)

def dict_comprehension():
    print("\n--- 9. Dictionary Comprehension ---")
    squares = {x: x**2 for x in range(1, 6)}
    print("Squares Dictionary:", squares)

def dict_count_elements():
    print("\n--- 10. Counting Occurrences ---")
    items = ["apple", "banana", "apple", "orange", "banana", "apple"]
    counter = {}
    for item in items:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    print("Item Counts:", counter)

def dict_clear_copy():
    print("\n--- 11. Clear and Copy ---")
    original = {"x": 10, "y": 20}
    copy_dict = original.copy()
    original.clear()
    print("Original (cleared):", original)
    print("Copy:", copy_dict)

def mega_dict_main():
    dict_basics()
    dict_update_add()
    dict_delete()
    dict_looping()
    dict_checking()
    dict_nested()
    dict_keys_values()
    dict_from_list()
    dict_comprehension()
    dict_count_elements()
    dict_clear_copy()

if __name__ == '__main__':
    mega_dict_main()
