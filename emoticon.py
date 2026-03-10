emoticon = ":c"

def main():
    global emoticon
    say("Is anyone there ?")
    emoticon = ":D"
    say("OH ! Hi")
def say(phrase):
    print(phrase + " " + emoticon)

main()