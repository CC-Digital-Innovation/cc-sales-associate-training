file = open('file.txt','w')
file.write('hello, world!')
file.close()

file = open('file.txt')
output = file.read()
file.close()

print(output)