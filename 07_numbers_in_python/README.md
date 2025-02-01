In Python, `repr()`, `str()`, and `print()` are all related to how data is presented or represented, but they serve different purposes:

### 1. **`repr()`**:

- **Purpose**: Returns a string representation of an object that is meant to be unambiguous and ideally suitable for debugging. It’s often used to provide a string that, when passed to `eval()`, would recreate the original object.
- **Goal**: To provide a detailed, machine-readable representation of the object.
- **Example**:

  ```python
  x = [1, 2, 3]
  print(repr(x))  # Output: '[1, 2, 3]'

  y = "hello"
  print(repr(y)) # Output : "'hello'"
  ```

  - In this case, `repr()` returns a string that looks like a valid Python expression for the list.

### 2. **`str()`**:

- **Purpose**: Returns a string representation of an object that is meant to be readable and user-friendly.
- **Goal**: To provide a "nice" or "informal" string representation of the object.
- **Example**:
  ```python
  x = [1, 2, 3]
  print(str(x))  # Output: '[1, 2, 3]'
  ```
  - `str()` often returns something simpler and more intuitive than `repr()`. For built-in types, `str()` and `repr()` may be the same, but for user-defined classes, they often differ.

### 3. **`print()`**:

- **Purpose**: Prints the result of evaluating an expression to the console. It is not a function for obtaining a string representation but is used to display output.
- **Goal**: To display content to the user or the console.
- **Example**:
  ```python
  x = [1, 2, 3]
  print(x)  # Output: [1, 2, 3]
  ```
  - `print()` uses the `str()` representation internally to output to the console. It doesn't return anything (its return value is `None`).

### Key Differences:

- **`repr()`**: Used for debugging or code inspection, gives a detailed and unambiguous representation.
- **`str()`**: Used for readable and user-friendly output.
- **`print()`**: Outputs to the console, calling `str()` on the argument automatically.

In general:

- If you need to represent an object in a way that can be re-executed or clearly seen by developers, use `repr()`.
- If you need a clean, readable output for the user, use `str()`.
- If you just want to show something in the console, use `print()`.
