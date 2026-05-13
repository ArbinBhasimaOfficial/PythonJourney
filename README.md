# PythonJourney

Learning Python from **Automate the Boring Stuff with Python** by [Al Sweigart](https://automatetheboringstuff.com/).

## Structure

```
Python_Programming_Basics/
├── Chapter1/
│   ├── firstprogram.py   # Interactive program (name + age)
│   ├── main.py           # Core examples & syntax
│   ├── answers.py        # Practice questions & round() examples
│   └── venv/             # Virtual environment
├── Chapter2/
│   ├── main.py           # Flow control examples & exercises
│   ├── answers.py        # Practice questions
│   ├── exitExample.py    # exit() function example
│   ├── printRandom.py    # Random number examples
│   └── venv/             # Virtual environment
├── Chapter3/
│   ├── main.py           # Function examples
│   ├── magic8Ball.py     # Magic 8-Ball program with return values
│   └── venv/             # Virtual environment
├── notes.txt             # Learning notes
└── README.md
```

## Part I: Python Programming Basics

### Chapter 1: Python Basics (Completed)

- **Expressions** - Values + operators that evaluate to single value
- **Math Operators** - `**`, `%`, `//`, `/`, `*`, `-`, `+`
- **Precedence** - `()` > `**` > `* / // %` > `+ -`
- **Data Types** - Integer, Float, String (str)
- **String Concatenation & Replication** - `+` and `*` with strings
- **Variables** - Naming conventions, snake_case
- **Built-in Functions** - `print()`, `input()`, `len()`, `str()`, `int()`, `float()`, `round()`

### Chapter 2: Flow Control (Completed)

- **Boolean Values** - True and False
- **Comparison Operators** - `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Boolean Operators** - `and`, `or`, `not`
- **Truth Tables** - AND, OR, NOT logic
- **if Statements** - Conditional execution
- **else Statements** - Default fallback case
- **elif Statements** - Multiple conditions
- **while Loops** - Repetition with condition
- **break Statements** - Exit loop early
- **continue Statements** - Jump back to loop start
- **Truthy/Falsey Values** - 0, 0.0, '' are False; others are True

### Chapter 3: Functions (Completed)

- **def Statements** - Creating functions with parameters
- **return Values** - Returning values from functions
- **None Value** - The None datatype
- **Arguments vs Parameters** - Understanding the difference
- **Local vs Global Scope** - Variable scope rules
- **try/except Statements** - Handling errors

### Chapters 4-6 (Pending)

- [ ] Chapter 4: Lists
- [ ] Chapter 5: Dictionaries and Structuring Data
- [ ] Chapter 6: Manipulating Strings

## Running the Code

```powershell
# Activate venv
cd Chapter1\venv
.\Scripts\Activate.ps1

# Run programs
python firstprogram.py
python main.py
python answers.py

# Chapter 3
cd Chapter3\venv
.\Scripts\Activate.ps1
python magic8Ball.py
python main.py
```

## Key Concepts Learned

### Chapter 1
| Concept | Example |
|---------|---------|
| Expression | `2 + 2` evaluates to `4` |
| String concatenation | `"Arbin" + " Bhasima"` |
| String replication | `"spam" * 3` |
| Type conversion | `str(99)`, `int("42")` |
| Variable assignment | `age = 23` |

### Chapter 2
| Concept | Example |
|---------|---------|
| Boolean values | `True`, `False` |
| Comparison | `42 > 100` is `False` |
| AND logic | `True and False` is `False` |
| OR logic | `True or False` is `True` |
| NOT | `not True` is `False` |
| if//else | `if x > 0: ... else: ...` |
| elif | `if a: ... elif b: ... else: ...` |
| while loop | `while x < 5: x += 1` |
| break/continue | `break` exits loop early, `continue` jumps to start |
| Truthy/Falsey | `bool(0)` is `False`, `bool('')` is `False` |

### Chapter 3
| Concept | Example |
|---------|---------|
| Function definition | `def hello(name):` |
| Function call | `hello('Arbin')` |
| Parameters | `def hello(name)` - `name` is a parameter |
| Arguments | `hello('Zion')` - `'Zion'` is an argument |
| return statement | `return 42` returns a value |
| None | `print()` returns `None` |
| Keyword arguments | `print('hi', end='')` |
| Local scope | Variables inside function |
| Global scope | Variables outside functions |
