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
header: 'Functions and Libraries'
footer: '© 2024 Computacenter Digital Innovation  All Rights Reserved'

---

<!-- _class: title -->
# Functions and Libraries
Jonny Le
Computacenter Digital Innovation
CC Sales Associate Training 10/09/2024 - 10/10/2024

---

# Problem

```python
# form to sign up

first_name = input('Enter first name: ')
# validate first name
if len(first_name) < 1:
    raise ValueError('Cannot be empty')

last_name = input('Enter last name: ')
# validate last name
if len(last_name) < 1:
    raise ValueError('Cannot be empty')

username = input('Enter username: ')
# validate username
if len(username) < 1:
    raise ValueError('Cannot be empty')
```

---

# Functions

<div class="columns">
<div>

```python
# form to sign up

def prompt_and_validate(prompt):
    data = input(prompt)
    if len(data) < 1:
        raise ValueError('Cannot be empty')
    return data

first_name = prompt_and_validate('Enter first name: ')
last_name = prompt_and_validate('Enter last name: ')
username = prompt_and_validate('Enter username: ')
```

</div>
<div>

- Blocks of **reusable** code
- Take inputs (sometimes)
- Returns an output

  or

- Creates side effect(s)

</div>
</div>

---

<h1><code style="background-color: gray;">def</code>ining and Calling Functions</h1>

<div class="columns">
<div>

```python
# form to sign up

def prompt_and_validate(prompt):
    data = input(prompt)
    if len(data) < 1:
        raise ValueError('Cannot be empty')
    return data

first_name = prompt_and_validate('Enter first name: ')
last_name = prompt_and_validate('Enter last name: ')
username = prompt_and_validate('Enter username: ')
```

</div>
<div>

- Functions begin with the keyword `def`
- Names are lowercased and separated by underscores ( _ )
- Block of code is indented
- Use keyword `return` to return data

</div>
</div>

---

# Built-in Functions

- <code><b>print</b>(*objects, sep=' ', end='\n', file=None, flush=False)</code>
- <code><b>input</b>(prompt)</code>
- <code><b>open</b>(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)</code>
- <code><b>len</b>(s)</code>

https://docs.python.org/3/library/functions.html

<!--
Segue by presenting problem of asking for password
-->

---

# Problem #2

```python
first_name = prompt_and_validate('Enter first name: ')
last_name = prompt_and_validate('Enter last name: ')
username = prompt_and_validate('Enter username: ')
password = prompt_and_validate('Enter password: ')
```

Running program:
```
...
Enter username: my-user
Enter password: supersecretpassword123
```

---

# Libraries

<div class="columns">
<div>

```python
import getpass

# form to sign up

def prompt_and_validate(prompt):
    data = input(prompt)
    if len(data) < 1:
        raise ValueError('Cannot be empty')
    return data

first_name = prompt_and_validate('Enter first name: ')
last_name = prompt_and_validate('Enter last name: ')
username = prompt_and_validate('Enter username: ')
password = getpass.getpass('Enter password: ')
# validate password...
```

</div>
<div>

- Use keyword `import` to add a module
- Call functions, constants, etc. using dot

  or

- Use keywords `from` and `import`
  - `from getpass import getpass`
- Call WITHOUT dot
  - `getpass('Enter password: ')`

</div>
</div>

<!--
Libraries, packages, modules
-->

---

# Standard and External Libraries

<div class="columns">
<div>

Standard library modules:
- datetime
- math
- zipfile
- csv

</div>
<div>

External libraries:
- slack-bolt
- pandas
- cryptography
- boto3

</div>
</div>

https://docs.python.org/3/library/index.html

https://github.com/ml-tooling/best-of-python
