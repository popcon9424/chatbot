import os

print(os.listdir('.'))

os.chdir(r'c:\Users\student\chatbot\day1\list')

print(os.getcwd())

name_list = os.listdir('.')

# 이름 바꾸기(rename)
# for i in name_list:
#    os.rename(i, 'ssafy_' + i)

# 이름 바꾸기(slicing)
# for i in name_list:
#    os.rename(i, i[6:])

print(os.listdir('.'))