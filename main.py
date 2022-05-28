string1 = input("Enter: ")

file1 = open("file.txt", 'r')

readfile = file1.read()

if string1 in readfile:
  print('String', string1, 'Found in file')
else:
  print('String', string1, 'Not found in file')  

file1.close()