# **Differences Between Lambda Functions and Normal Functions**

| **Parameter**        | **Lambda Function**                                 | **Normal Function**                        |
| -------------------- | --------------------------------------------------- | ------------------------------------------ |
| **Definition**       | Anonymous (defined using `lambda`)                  | Named (defined using `def`)                |
| **Syntax**           | Single-line, concise                                | Multi-line, supports complex logic         |
| **Reusability**      | Generally used for short, one-time purposes         | Used for reusable, structured logic        |
| **Readability**      | Less readable for complex operations                | More readable for complex tasks            |
| **Return Statement** | Implicit (always returns the expression result)     | Explicit (must use `return` keyword)       |
| **Naming**           | Usually unnamed or assigned to a variable briefly   | Explicitly named                           |
| **Scope**            | Limited to the enclosing block                      | Global or function-level scope             |
| **Use Case**         | Simple tasks like inline operations (e.g., sorting) | Complex operations, reusable functionality |
| **Example**          | `lambda x: x ** 3`                                  | `def cube(x): return x ** 3`               |
| **Debugging**        | Harder to debug (no name for traceback)             | Easier to debug with named references      |
| **Code Blocks**      | Cannot contain multiple statements or blocks        | Can contain multiple statements or blocks  |

---

### **Examples**

#### Lambda Use Case:

```python
# Sorting a list of dictionaries by a key
people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
sorted_people = sorted(people, key=lambda person: person["age"])
print(sorted_people)
```

#### Normal Function Use Case:

```python
def calculate_area(radius):
    return 3.14159 * radius ** 2

area = calculate_area(5)
print(area)  # Output: 78.53975
```

---

### **Key Takeaways**

1. **Lambda Functions**:

   - Ideal for short, one-liner operations that need to be used temporarily.
   - Commonly used in functional programming contexts like `map`, `filter`, and `sorted`.

2. **Normal Functions**:
   - Preferred for more complex logic, better readability, and reusability.
   - Easier to debug and test due to their explicit naming and structure.

### **Distinction Between Calling and Referencing a Function**

- **Calling a Function (`cube(3)`):**

  - Executes the function immediately.
  - Returns the result of the function's execution.
  - The result is assigned to the variable, making it a fixed value.

- **Referencing a Function (`cube`):**
  - Does not execute the function.
  - Assigns the function object itself to the variable.
  - The new variable can now be used to call the function dynamically with different arguments.

**Example:**

```python
# Normal function
def cube(x):
    return x ** 3

# Calling the function
result = cube(3)  # result is 27
print(result)  # Output: 27

# Referencing the function
reference = cube  # reference points to the function
print(reference(3))  # Output: 27
print(reference(4))  # Output: 64
```

```python
cube = (
    lambda x: x**3
)  # lambda function which takes x as a parameter and returns the cube of it

another_cube = cube  # this is a reference and now it can be called with dynamic values
print(another_cube(4))  # prints 64

```

# **Generators and `yield` in Python**

### **What Are Generators?**

Generators are a special type of iterable in Python that allow you to yield items one at a time **on demand**. They are defined using functions but use the `yield` keyword instead of `return`.

- A **generator function** returns a generator object that can be iterated over lazily.
- Unlike normal functions, generator functions do not execute completely when called. Instead, they pause execution at each `yield` statement and resume from there when the generator is iterated.

---

### **What Is `yield`?**

- The `yield` keyword is used in a function to **produce a value** without terminating the function.
- When `yield` is executed:
  - The function's state is saved.
  - Control is returned to the caller with the yielded value.
  - The function can be resumed later, continuing from where it left off.

---

### **Difference Between `yield` and `return`**

| **Aspect**       | **`yield`**                                    | **`return`**                        |
| ---------------- | ---------------------------------------------- | ----------------------------------- |
| **Execution**    | Pauses the function, saving its state.         | Terminates the function completely. |
| **Use Case**     | Used to produce a sequence of values lazily.   | Used to return a single result.     |
| **Iteration**    | Returns a generator object.                    | Returns a single value.             |
| **Memory Usage** | Efficient; doesn't store all values in memory. | Stores the result in memory.        |

---

### **Example:**

#### Using `yield`:

```python
def generate_numbers(n):
    for i in range(n):
        yield i

gen = generate_numbers(5)
for num in gen:
    print(num)
```

**Output:**

```
0
1
2
3
4
```

- Here, the generator yields numbers one by one. Memory usage is efficient because values are computed lazily.

#### Using `return`:

```python
def return_numbers(n):
    return [i for i in range(n)]

nums = return_numbers(5)
for num in nums:
    print(num)
```

**Output:**

```
0
1
2
3
4
```

- This consumes more memory because the entire list is created and stored in memory at once.

---

### **Use Cases of Generators**

1. **Handling Large Data Streams**:

   - Useful for reading files line by line or streaming data from APIs without loading everything into memory.

   ```python
   def read_large_file(file_path):
       with open(file_path) as f:
           for line in f:
               yield line.strip()
   ```

2. **Infinite Sequences**:

   - Generators can produce infinite sequences (e.g., Fibonacci numbers).

   ```python
   def fibonacci():
       a, b = 0, 1
       while True:
           yield a
           a, b = b, a + b
   ```

3. **Efficient Pipelines**:

   - Use generators to process data in steps (e.g., filter, map, reduce) while keeping memory usage low.

4. **Custom Iterables**:
   - Create custom iterable objects without implementing `__iter__` and `__next__`.

---

### **Key Advantages of Generators**

1. **Memory Efficiency**:
   - Only one value is stored in memory at a time.
2. **Lazy Evaluation**:
   - Values are generated only when needed, improving performance.
3. **Readable and Concise**:
   - Simplifies code for producing sequences.

---

### **Key Points to Remember**

- Generators are **iterables**, meaning you can use them with loops or tools like `next()`.
- Once exhausted, a generator cannot be reused unless recreated.
- Generators are best for **on-the-fly computations** and reducing memory overhead.

---

This concise summary covers generators, their working with `yield`, key differences from `return`, use cases, and advantages.

# Case discussion for generators and `yield`

1. **Normal Function `even_generator`**:

   - The `return` statement in `even_generator` causes the function to terminate immediately after yielding the first even number (0 in this case). This is why the loop doesn't iterate over multiple values.

   ```python
   print(even_generator(5))
   # Output: 0
   ```

   Since the function doesn't support iteration, calling it in a loop will result in an error (`int` is not iterable).

---

2. **Generator Function `even_gen`**:

   - The `yield` keyword allows the function to produce a sequence of values lazily. When the loop is executed:
     - The generator pauses after yielding each value.
     - It resumes from where it left off for the next iteration.
     - It prints all even numbers till 5 as expected.

   ```python
   for even_numbers in even_gen(5):
       print(even_numbers)
   ```

   This works perfectly and outputs all even numbers in the range.

---

3. **Calling `next(even_gen(5))`**:

   - `even_gen(5)` returns a **generator object**.
   - Calling `next(even_gen(5))` directly creates a new generator object, **yields the first value, and terminates the object**.
   - **Behavior**:
     - If you use `next(even_gen(5))`, it will always yield `0` because a new generator object is created each time.

   **Example**:

   ```python
   gen_obj = even_gen(5)
   print(next(gen_obj))  # Output: 0
   print(next(gen_obj))  # Output: 2
   ```

   However:

   ```python
   print(next(even_gen(5)))  # Output: 0
   print(next(even_gen(5)))  # Output: 0
   ```

   This happens because a **new generator object** is created on each call to `even_gen(5)`.

---

### **Key Observations**

1. **Generators Are Iterators**:

   - The object returned by `even_gen(5)` behaves like an iterator. It implements both the `__iter__()` and `__next__()` methods.
   - You can use `next()` on a generator object.

2. **Independence of Loops**:

   - Each call to `even_gen(5)` creates a **new independent generator object**.
   - These objects are not connected to one another.

   **Example**:

   ```python
   gen1 = even_gen(5)
   gen2 = even_gen(5)

   print(next(gen1))  # Output: 0
   print(next(gen2))  # Output: 0
   ```

---

### **Output Behavior Recap**

- Looping through `even_gen(5)`:
  ```
  0
  2
  4
  ```
- Calling `next(even_gen(5))` repeatedly without saving the object:
  - Always yields `0`.
- Saving the generator object and using `next()`:
  - Yields values sequentially: `0`, `2`, `4`, etc.
