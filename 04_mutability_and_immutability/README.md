# Python Memory Management, Objects, and References

- Everything is an object in Python.
- For mutable objects, the data is not reused, but for immutable objects, the same data `can` be reused (depending on the context).

## 1. Mutability and Immutability in Python

### What is Mutability?

- **Mutable objects** can be changed after they are created.
  - Example: Lists, Dictionaries, Sets
  - Changes to mutable objects reflect in all references pointing to them.

#### Example: Mutable List

```python
# Mutable object: List
a = [1, 2, 3]
b = a  # b and a point to the same list
a.append(4)  # Modify the list

print(a)  # Output: [1, 2, 3, 4]
print(b)  # Output: [1, 2, 3, 4]
```

### What is Immutability?

- **Immutable objects** cannot be changed after creation.
  - Example: Integers, Strings, Tuples
  - Creating a new value for an immutable object creates a new object rather than modifying the original.

#### Example: Immutable Integer

```python
# Immutable object: Integer
x = 10
y = x  # y and x reference the same integer
x = 20  # Reassign x, creating a new integer object

print(x)  # Output: 20
print(y)  # Output: 10 (y still references the original integer)
```

### Immutable object: String

```python
s1 = "hello"
s2 = s1  # s1 and s2 reference the same string
s1 = "world"  # Reassign s1, creating a new string object

print(s1)  # Output: world

# But the "hello" object didn't itself change and s1 was just re-assigned to point to "world" instead of "hello" and it will be garbage collected later if it's not being pointed by any other variable

print(s1)  # Output: world
print(s2)  # Output: hello (s2 still references the original string)
```

## 2. Memory Management in Python (Stack and Heap)

### Stack vs Heap

- **Stack**: Stores function calls, local variables, and references to objects. It’s fast but limited in size.
- **Heap**: Stores objects (like lists, dictionaries, class instances) and allows dynamic memory allocation.

#### Memory Allocation Example:

```python
def my_function():
    a = 10  # a is stored on the stack (local variable)
    b = [1, 2, 3]  # b is stored on the heap (list object)

my_function()
```

- **Stack** holds the reference to the list (`b`), while the actual list object `[1, 2, 3]` is stored in the **Heap**.

### Object Creation

- When an object is created, it’s allocated in the heap memory, and a reference is stored in the stack (if it's a local variable).

## 3. Objects and References in Python

In Python, everything is an **object**, and variables are just **references** to those objects.

- **Object**: The actual data or structure stored in memory (e.g., integer, list, string).
- **Reference**: A variable or pointer that refers to the object in memory.

#### Example:

```python
a = [1, 2, 3]  # `a` references the list [1, 2, 3] in memory
b = a  # `b` is another reference to the same list object

b.append(4)  # Modifies the object referenced by both a and b

print(a)  # Output: [1, 2, 3, 4]
print(b)  # Output: [1, 2, 3, 4]
```

- `a` and `b` are different references to the same list object in memory.

## 4. Garbage Collection in Python

### How Garbage Collection Works

- Python uses **automatic garbage collection** to manage memory. When an object is no longer referenced, it is eligible for garbage collection.
- **Reference Counting**: Each object has a reference count. When this count drops to zero, the object is garbage collected.
- **Cyclic Garbage Collector**: For objects involved in reference cycles (e.g., objects referencing each other), Python uses a cyclic garbage collector to detect and clean up these cycles.
