import random
letters=list('abcdefghijklmnopqrstuvwxyz')
numbers=list('0123456789')
symbols=list('~!@#$%^&*')




print("Welcome to the Password Generator !") 

n_letters=int(input("How many letters would you like in your password ?"))
n_symbols=int(input("How many symbols would you like in your password ?"))



n_numbers=int(input("How many numbers would you like in your password ?"))
password_list=[]
for i in range(1,n_letters+1):
  char=random.choice(letters)
  password_list+=char
for i in range(1,n_symbols+1):
  char=random.choice(symbols)
  password_list+=char
for i in range(1,n_numbers+1):
  char=random.choice(numbers)
  password_list+=char
# print(password_list)
random.shuffle(password_list)
# print(password_list)
password=""
for i in password_list:
  password+=i
print(password)






