---
marp: true
theme: beam
style: |
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
paginate: true
header: 'Presentation Tile'
footer: '© 2024 Computacenter Digital Innovation  All Rights Reserved'

---
<!-- _class: title -->
# Variable Constants and IO - The Basics
Ben Verley
Computacenter
Lesson 1

<!--
** Slide Notes
-->

---
# Agenda
<div style='margin-top:60px'></div>
<div class="columns">
<div>


- Output
- Variables and Constants
- Inputs

</div>
</div>

<!--
** Slide Notes
-->


---
# Output
## Show me your work
Code is just a set of instructions that gets sent to the cpu to be proccessed. How do we see the result of that execution?

### Places to output
- On screen console
- File
- Other Code

---
# Output
## Hello World!
```python
print("Hello World!")
```

- Python prints stuff to the console with the print function
- Simplest way to output what your code did

<!--
Notes:
-->

---
# Variables And Constants
<div class="columns">
<div>

## Variable
- Kept in memory
- Named for easy reference
- Has types
- Changeable

</div>
<div>

## Constant
- Kept in memory
- Named for easy reference
- Has types
- Not changeable or should not be changed

</div>
</div>

### Common Types
- Integer: A whole number
- String:  A collection of characters
- Float:   Decimal value

---

# Variables and Constants
## Naming conventions and restrictions
- Avoid using built in function names
- Cannot start with a number 
- two_words or twoWords
- avoid funny characters
- put constants in all capital letters

<!--
Notes:
Try to avoid using numbers at all, variable names should be descriptive so someone reading it knows what they are for and simple so the length of the line is kept short
-->
---

# Example
## Adding two things
```python
CONSTANT = 10 
x=5
print(x)
x=5+CONSTANT  
print(x)
```

- We create a constant of 10 and a variable of 5
- we can add 10 to the variable by using the constant
- you can then pass the variable to the print to the print function

<!--
Notes:
While we can indicate that a value is SUPPOSED to be constant with capital letters, the python interpreter doesn't actually PREVENT you from changing them, so they can be changed, but shouldn't be

Variables also shouldnt be named the same thing as certain keywords that python uses like with, if, 
-->
---

# Input
## Can we interact with it?
What if we want to print something else that the code doesn't know about until we tell it?


---
# Input
## Name Me!
```python
name = input("Please enter your name:") 
print(f"Hello {name}") #f string
print("Hello " + name) #You can concatinate strings with +
print("Hello", name) #print can take several statements
```

- Input function will wait for user input from the console
- Whatever the user inputs will be assigned to name
- Each of the print statements will print the same thing.






