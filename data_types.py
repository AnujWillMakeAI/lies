'''

Data types in python
1.String = "Hello this is string data type"
    first_name = "anuj"
    last_name = "wadhwa"
    full_name = first_name + " " +last_name
    long_dash = "--" * 2
    print(full_name)
    print(long_dash)
    
f"{}" f string method
    name = "anuj"
    string = f"hi i am {name}"
    
    String methods:
    .(). makes everything uppercase
    .lower() makes everything lowercase
    .title() makes the first letter of upperevery word uppercase
    .strip() removes whitespace or certain words
    
2.Integer = 1,2,3,45,9348
    Math operations
        1. + 5+4 = 9
        2. - 5-4=1
        3. * 5*4=20
        4. / 5/4= 1.25
        5. **  =5**4 = 625
        6. // 5//4 = 1
    age = 18
        print(age == 18)    # True  - Equal to
        print(age != 21)    # True  - Not equal to
        print(age > 17)     # True  - Greater than
        print(age < 20)     # True  - Less than
        print(age >= 18)    # True  - Greater than or equal
        print(age <= 18)    # True  - Less than or equal

3.Float = 1.111, 12.33
4.Boolean = True or False, 1 or 0
    age = int(input("what is your age? :"))
    if age >= 18:
        print("True")
    else:
        print("False")
    common types of operators in boolean: 
    ==, equal
    !=, not equal
    >=, greater than or equal
    <=, less than or qual
    <, less than
    >, greater than
    
    age = 25
        has_license = True

        # AND - both must be true
        can_drive = age >= 16 and has_license
        print(can_drive)  # True

        # OR - at least one must be true
        day = "Saturday"
        is_weekend = day == "Saturday" or day == "Sunday"
        print(is_weekend)  # True

        # NOT - reverses the value
        is_adult = age >= 18
        is_child = not is_adult
        print(is_child)  # False

5.List = [red,1,neo,3,4,5,kabir]
    numbers = [3, 1, 4, 1, 5, 9]

        # Information
        print(len(numbers))         # 6 (length)
        print(numbers.count(1))     # 2 (count occurrences)
        print(numbers.index(4))     # 2 (find position)
        # Sorting
        numbers.sort()              # Sort in place
        print(numbers)              # [1, 1, 3, 4, 5, 9]
        numbers.reverse()           # Reverse order
        print(numbers)              # [9, 5, 4, 3, 1, 1]
        # Copy
        new_list = numbers.copy()   # Create a copy
        
 Fruits = [apple,  banana, orange]   
if "apple" in Fruits:
    print("yea")
    
        
6.Tuple = (1,2,3,4,5)

# Empty tuple
empty = ()
# Tuple with items
point = (3, 5)
colors = ("red", "green", "blue")
# Single item tuple needs comma!
single = (42,)  # Note the comma
not_tuple = (42)  # This is just 42 in parentheses
# Without parentheses (implicit)
coordinates = 10, 20

# Unpack values
point = (3, 5)
x, y = point  # x = 3, y = 5

# Multiple assignment
a, b, c = 1, 2, 3  # Same as (1, 2, 3)

# Swap variables elegantly
x, y = y, x  # Swaps values!





7.Dictionary = {"name": "John", "age": 36}
# Empty dictionary
my_dict = {}
# Dictionary with data
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
# Different ways to create
scores = dict(math=95, english=87, science=92)

person = {"name": "Alice", "age": 30, "city": "New York"}

# Get all keys, values, or items
print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 30, 'New York'])
print(person.items())   # dict_items([('name', 'Alice'), ...])

# Check if key exists
if "name" in person:
    print("Name found!")

# Update multiple values
person.update({"age": 31, "job": "Engineer"})

# Dictionary of dictionaries
students = {
    "alice": {"age": 20, "grade": "A"},
    "bob": {"age": 21, "grade": "B"},
    "charlie": {"age": 19, "grade": "A"}
}

# Access nested data
print(students["alice"]["grade"])  # "A"




8.Sets = {1,2,3,4,5}

# Empty set (careful!)
empty_set = set()  # NOT {} - that's a dict!
# Set with values - both ways work
numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "banana", "orange"])
# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)  # {85, 90, 92}
colors = {"red", "blue"}
# Add items
colors.add("green")
print(colors)  # {'red', 'blue', 'green'}
# Remove items
colors.remove("blue")    # Error if not found
colors.discard("yellow") # No error if not found

# Check membership
if "red" in colors:
    print("Red is available")
    
names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = list(set(names))
print(unique_names)  # ['Alice', 'Bob', 'Charlie']   
    
allowed_users = {"alice", "bob", "charlie"}

if "alice" in allowed_users:  # Very fast!
    print("Access granted")
    
    
    
    
    

Control FLow :
    if, else, elif statements
        Temp = int(input("what is the temperature outside? :"))
            if Temp > 32:
                print("It's hot than usual")
            elif Temp <32:
                print("it's hot today")
            else:
                print("It's a nice weather today")
        
        has_ticket = True
        age = 22
        if has_ticket:
            if age >=18:
                print("enjoy your movie, sir!")

Loops : 
# count by 1s
for i in range(1,6):
    print(i)
1,2,3,4,5
#count bby 2s
for i in range(0,10,2):
    print(i)
2,4,6,8

colors = ["red", "blue", "green"]
for color in colors:
    print(f"I like {color}")


name = "python"
for letter in name:
    print(letter)
p,y,t,h,o,n






'''
































