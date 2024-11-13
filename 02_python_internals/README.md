# Python Internal Workings

- Python code is **compiled** down to **bytecode**, similar to Java.
- The bytecode is then fed into the **Python Virtual Machine (PVM)**, which can run both Python scripts and bytecode.
- Python is considered an **interpreted language** because the bytecode fed to the Python Virtual Machine is executed **line-by-line** rather than being compiled directly into machine code.
- It is a garbage collected language.

## Python Virtual Machine (PVM)
- The PVM has a **code loop** that iterates over Python bytecode or the `.py` scripts.
- It has been implemented in **C** (for CPython) and **Java** (for Jython/JPython).
- The PVM is the **runtime engine** for Python, and it is also known as the **Python Interpreter**.

## Versions of Python
- Python has several versions, including **CPython**, **Jython/JPython**, **IronPython**, **Stackless Python** (an extension of CPython with concurrency features), and **PyPy** (a high-performance alternative to CPython).
- These versions consist of various components such as the **compiler**, **interpreter**, **PVM implementation**, and **runtime engine**.
- Different Python implementations may be written in languages like **C** (CPython) or **Java** (Jython).
- When we talk about a Python version, we're referring to the entire implementation package, as described above.
- **CPython** is the default implementation and most commonly used.

## Python Bytecode
- Python uses an intermediate step that compiles **source code** (`.py` files) into **bytecode**. This bytecode runs faster than parsing and interpreting the source code each time.
- **Bytecode is not machine instruction** but a **Python-specific instruction set** that the PVM can interpret.
- Bytecode is an optimized version of the `.py` files. It is created when a Python file is **executed or imported** (not just when importing functions or libraries). 
- The bytecode is then fed to the PVM for execution.

## Importance of the `__pycache__` Folder and `.pyc` Files
- The `__pycache__` folder is created when a module is imported, and it contains `.pyc` files that store the **bytecode**.
- `.pyc` files are a **platform-independent, lower-level representation** of the original Python code, optimized for faster execution by the PVM.
- **Python uses timestamp-based comparison** to determine if the `.pyc` file needs to be re-generated. When the source code is modified, the bytecode is recompiled.
- `.pyc` files are not **frozen binaries** but are compiled **bytecode** that is optimized for execution. They are platform-independent but are **not machine code**.
- Just having the **PVM** to run `.pyc` files is not always enough. The code might require the correct **Python version**, relevant **dependencies**, and potentially other **platform-specific libraries** to run successfully. Therefore, it's often better to distribute the **`.py` source files** rather than `.pyc` files.
- Bytecode is always generated but might not be visible for simple scripts.

## Difference Between .pyc Files and Frozen Binaries

### .pyc Files

- **Platform-independent bytecode**: `.pyc` files are compiled bytecode files generated from Python source code (`.py` files). They are **platform-independent** and are used to speed up the execution of Python programs.
- **Not executable**: Unlike frozen binaries, `.pyc` files are not executable on their own. They need the **Python interpreter** to run.
- **Part of Python's internal mechanism**: These files are part of Python’s internal mechanism to optimize code execution. They are generated when a module is imported or a script is run, and are stored in the `__pycache__` directory.
- **Execution requires Python interpreter**: Since `.pyc` files are compiled bytecode, they still rely on the Python interpreter (like CPython) to run. You cannot execute `.pyc` files independently.

#### Key Points:
- Created from `.py` source code.
- Stored in `__pycache__` for faster access.
- Platform-independent.
- Cannot be executed on their own; require the Python interpreter.

### Frozen Binaries

- **Fully compiled executable**: Frozen binaries are **self-contained executable files** that have been compiled from Python code. They include the Python code, the Python interpreter, and all necessary libraries, all bundled into one file.
- **Standalone executables**: These binaries can be executed directly on a target platform (e.g., `.exe` files on Windows) without requiring the Python interpreter to be installed separately.
- **Generated using tools**: Tools like **PyInstaller**, **cx_Freeze**, or **py2exe** are used to create frozen binaries by packaging Python code along with its dependencies into a single executable file.
- **Platform-dependent**: Unlike `.pyc` files, frozen binaries are platform-dependent. They are compiled for a specific operating system and architecture, such as Windows, Linux, or macOS.

#### Key Points:
- Contains Python code, Python interpreter, and dependencies.
- Standalone executable for a specific platform.
- Can be executed without a Python environment.
- Generated using third-party tools like PyInstaller, cx_Freeze, or py2exe.
