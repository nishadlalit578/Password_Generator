import random

letter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabets = list(letter)

num = '0123456789'
numbers = list(num)

sp_ch = "!@#$%^&*()<>}{[]"
symbols = list(sp_ch)

print("##********* PASSWORD GENERATOR *********##")

no_of_alphabets = int(input("How many alphabets you want in your password ? "))
no_of_numbers = int(input("How many numbers you want in your password ? "))
no_of_symbols = int(input("How many special character you want in your password ? "))



while True:
    password_list= []
    for char in range(1,no_of_alphabets+1):
        password_list.append(random.choice(alphabets))

    for char in range(1 , no_of_numbers+1):
        password_list.append(random.choice(numbers))

    for char in range(1, no_of_symbols+1):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)
    
    password = ""
    for char in password_list:
        password += char

    print(password)

    play_again = input("Do you want a new password ? (y / n) ").lower()   
    if not play_again == "y" : 
        break