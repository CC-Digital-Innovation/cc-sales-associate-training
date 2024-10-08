try:
    file = open('file1.txt')
    name = file.read()
except FileNotFoundError:
    name = input('What is your name? ')
    file = open('file1.txt', 'w')
    file.write(name)
finally:
    file.close()
print('hello ' + name + '!')