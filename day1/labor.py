import os

print(os.listdir('.'))

os.chdir(r'c:\Users\student\chatbot\day1\list')

print(os.getcwd())

# print(os.listdir('.'))

os.rename('hello.txt', 'changed.txt')