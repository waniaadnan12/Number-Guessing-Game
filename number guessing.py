from random import randint


def display_rules():
  print("/n=====Number Guessing Game=====")
  print("the computer has selected the number between 1 and 100.")
  print("You have a maximum of 7 valid attempts.")
  print("Invalid inputs and numbers outside 1 to 100 do not count.")
  print("Good Luck\n")

check_guess = lambda guess,number: guess == number

def play_game(number, attempts=0):
  if attempts >= 7:
    print(f"\n Game Over! the correct number was {number}.")
    return
  try:
    guess = int(input(f"attempt{attempts+1}\7 - Enter your guess:"))
    if guess < 1 and guess > 100:
      print("invalid input! please enter a number between 1 and 100.")
      play_game(number,attempts)
      return
  except ValueError:
    print("Invalid input! Please enter a valid number.")
    play_game(number, attempts)
    return
  attempts += 1
  if check_guess(guess, number):
    print(f"\nCongratulations! You guessed the number!")
    print(f"You won in {attempts} attempt(s).")
    return

  if guess < number:
       print("Too Low!")
  else:
       print("Too High!")
  play_game(number,attempts)

number = randint(1, 100)
display_rules()
play_game(number)