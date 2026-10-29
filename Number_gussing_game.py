def check_guess(guess, secret):  
    if guess == secret:
        return "Correct!"
    elif guess < secret:
        return "Too low!"
    else:
        return "Too high!"

secret_number = 7  
attempts = 0  
player_name = input("Enter your name: ")
score = 0
player_record = {}

while attempts < 5:  
    guess = int(input("Guess the number: "))  
    attempts += 1
  
    result = check_guess(guess, secret_number)
    print(result)
    
    if result == "Correct!":
        score = 6 - attempts  # Higher score for fewer attempts
        print(f"You won in {attempts} attempts!")
        break
else:
    print(f"Game over! The secret number was {secret_number}.")


player_record[player_name] = score
print("\nPlayer Record:", player_record)