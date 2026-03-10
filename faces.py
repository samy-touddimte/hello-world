def main():
    phrase = input("Say sum with an emoticon")
    return convert(phrase)

def convert(input):
    if ":)" in input :
        return input.replace(":)","🙂") 
    elif ":(" in input : 
        return input.replace(":(","🙁")
    else:
        return input
    
print(main())