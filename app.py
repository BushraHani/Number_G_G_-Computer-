# Guess the number game in python project (computer)
import random

#Session start
def guess_the_number():
    """Guess the Number Game by Computer"""
    number = random.randint(1,30)
    guesses_left = 5
    # Welcome Message
    print("💭 welcome to the Number Guessing Game")
    print(" 🤔 Guess a Number Between 1 to 30")
    
    #Genarate the Loop
    while guesses_left > 0:
        print(f"\n You have {guesses_left} guesses left.")
        try:
            guess = int(input("🤔 Take a Guess of another number."))
        except ValueError:
            print("Invalid input: please Enter a number")
            continue
        
        if guess < number:
            print("🔅Too low number. Tell another")
        elif guess > number:
            print("⚡Too high number. Tell another")  
                    
        else:
            print(f"👍Congratulations! You have found the Correct Number in {5 - guesses_left +1} tries.")   
            return
        
        guesses_left -= 1
        # when faced defeated so!
    print(f"👎You have loss! 😔You are ran out this Game. The Number was {number}.")
    
guess_the_number()    
        
