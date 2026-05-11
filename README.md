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

### Chapters 3-6 (In Progress)

- [ ] Chapter 3: Functions
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
