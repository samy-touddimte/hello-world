def get_guess():
    guess = input("Enter a guess : ")
    return guess

def main(guess):
    if guess == "50" or guess == "fifty":
        return "You're right"
    else:
        return "Try again"

guess=get_guess()
answer=main(guess)
print("Damn, " + answer)