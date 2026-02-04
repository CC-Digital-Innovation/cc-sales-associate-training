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
header: 'Conditionals and Loops'
footer: '© 2024 Computacenter Digital Innovation  All Rights Reserved'


---
<!-- _class: title -->
# Conditionals and Loops
Anthony Farina
DevOps Engineer
Computacenter US


---
# Conditionals
<div style='margin-top:60px'></div>
<div class="columns">
<div>

- Conditionals are pieces of code that check if a condition is true or false
- In math, we know that 1 = 1
- This is a "true" mathematical statement
- However, we know that 1 =/= 2
- This is a "false" mathematical statement
- "if-else" statements allow us to check if a condition is met

</div>
<div>

```python
x = 1
y = 2

if x == y:
  print("Condition is true")
else:
  print("Condition is false")
```

</div>
</div>


---
# Loops
<div style='margin-top:60px'></div>
<div class="columns">
<div>

- Loops are blocks of code that will run again and again until a condition is met
- As long as the looping condition is true, the loop will continue
- When the condition becomes false, the loop will end
- Watch out for infinite loops!

</div>
<div>

```python
x = 1

while x <= 10:
  print("x is " + x)
  x = x + 1

print("I am done")
```

</div>
</div>
