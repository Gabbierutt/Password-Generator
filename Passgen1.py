# Password Generator
# Created By : Gabbierutt

import random
import os

print()

def passwordGenerator():
    
    while True:
        try:
            title = "Password Generator"
            print(title)
            print()

            characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890#$&@?*!~"

            length = int(input("Enter password length: "))
            print()
            number_of_passwords = int(input("Enter number of passwords: "))

            print()

            results = "Here is your passwords:"
            print(results)
            print()
            print()
     
            for numbers in range(number_of_passwords): 
                for generate in range(length):
                    randomize = random.choice(characters)
                    print(randomize, end = "")
                print()
    
            print()
    
            while True:
                response = input("Do you want to generate again [y/n] ? ")
                response = response.lower()
                print()
        
                if response == 'y':
                    os.system('cls')
                    passwordGenerator()
                    break
                elif response == 'n':
                    os.system('cls')
                    quit()
                else:
                    print("Invalid keyword!")
                    print()
        except ValueError:
            os.system('cls')
            print()
    
passwordGenerator()
        


