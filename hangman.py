import random
import time
n = input('Enter players name:')
print('Welcome ' + n + ' to the Hangman game !')
time.sleep(2)
carCom = ['audi', 'BMW', 'mercedes', 'jaguar', 'mini', 'jeep', 'lamborghini',
          'ferrari', 'porsche', 'bentley', 'rollsroyce', 'toyota']
car = random.choice(carCom)
time.sleep(2)
print('Guess the car name you will get 10 chances to guess the name')
time.sleep(2)
carName = ""
t = 10
while t > 0:
    failed = 0
    for char in car:
        if char in carName:
            print(char)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You Win")
        print("The car is: ", car)
        break
    guess = input("guess a character:")
    carName += guess
    if guess not in car:
        t -= 1
        print("Wrong")
        time.sleep(2)
        print("You have", + t, 'more guesses')
        time.sleep(2)
        if t == 0:
            print("You Loose")
