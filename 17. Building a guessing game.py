secret_word = "panda"
guesses = ""
guess_counts = 0
guess_limits = 3
out_of_guesses = False

while guesses != secret_word and not(out_of_guesses):
    if guess_counts < guess_limits:
        guess = input("Enter your guess : ")
        guess_counts += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You lost the game")
else:
    print("You win")