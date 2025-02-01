The behavior of the `in` keyword depends on the **data type** of the object being checked.

---

### **`in` for Different Data Types**

1. **For Lists (Arrays in Other Languages)**:
   - Lists in Python are not hash-based; they are essentially dynamic arrays.
   - The `in` keyword performs a **linear search** to check if the item exists in the list.
   - **Time Complexity**: \( O(N) \), where \( N \) is the length of the list.
   - **Example**:
     ```python
     items = [1, 2, 3, 4, 5]
     print(3 in items)  # True
     ```
     Here, the list is scanned element by element until the item `3` is found.

---

2. **For Sets**:
   - Sets use a **hash table** for storage.
   - The `in` keyword checks if the hash of the item exists in the set, making lookups \( O(1) \) on average.
   - **Time Complexity**: \( O(1) \) (average case), \( O(N) \) (worst case with collisions).
   - **Example**:
     ```python
     items = {1, 2, 3, 4, 5}
     print(3 in items)  # True
     ```

---

3. **For Dictionaries (Maps in Other Languages)**:
   - Dictionaries are hash-based, like sets, but they store key-value pairs.
   - The `in` keyword checks for **keys only** (not values) in \( O(1) \) time on average.
   - **Time Complexity**: \( O(1) \) (average case), \( O(N) \) (worst case with collisions).
   - **Example**:
     ```python
     items = {"a": 1, "b": 2, "c": 3}
     print("b" in items)  # True
     ```

---

4. **For Strings**:
   - Strings are not hash-based. The `in` keyword checks for substrings using a **search algorithm**.
   - **Time Complexity**: \( O(N) \), where \( N \) is the length of the string.
   - **Example**:
     ```python
     s = "hello"
     print("e" in s)  # True
     ```

---

5. **For Tuples**:
   - Tuples are similar to lists but immutable.
   - The `in` keyword performs a linear search on tuples, like lists.
   - **Time Complexity**: \( O(N) \).
   - **Example**:
     ```python
     items = (1, 2, 3, 4, 5)
     print(3 in items)  # True
     ```

---

### **Comparison Table**

| Data Type      | Storage Type    | `in` Time Complexity | Notes                  |
| -------------- | --------------- | -------------------- | ---------------------- |
| **List**       | Dynamic Array   | \( O(N) \)           | Linear search.         |
| **Set**        | Hash Table      | \( O(1) \) (avg)     | Hash-based lookup.     |
| **Dictionary** | Hash Table      | \( O(1) \) (avg)     | Checks keys only.      |
| **String**     | Array-like      | \( O(N) \)           | Checks for substrings. |
| **Tuple**      | Immutable Array | \( O(N) \)           | Linear search.         |

---

### **Conclusion**

- For **lists, tuples, and strings**, `in` takes \( O(N) \) time because it involves a linear scan.
- For **sets and dictionaries**, `in` takes \( O(1) \) on average because they use hash-based storage.
- Always choose the right data structure based on your performance requirements! For large collections where frequent lookups are needed, sets or dictionaries are preferable.
