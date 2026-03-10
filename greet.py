def greet(input):
    if "hello" or "Hello" in input :
        return "hello there"
    else:
        return "I don't understand"

gretting = greet(input("Say something: "))
print("Hmm, " + gretting)