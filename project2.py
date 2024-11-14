import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')','_','+']
print("welcome to password generator")
letters1=int(input("how many letters you want in your password:"))
letters2=int(input("how many numbers you want in your password:"))
letters3=int(input("how many symbols you want in your password:"))
password_list=[]
for i in range(1,letters1+1):
    char=random.choice(letters)
    password_list=password_list+char
for i in range(1,letters2+1):
    char=random.choice(numbers)
    password_list=password_list+char
for i in range(1,letters3+1):
    char=random.choice(symbols)
    password_list=password_list+char
print(password_list)
random.shuffle(password_list)
print(password_list)
password=" "
for char in password_list:
    password=password+char
print(password)