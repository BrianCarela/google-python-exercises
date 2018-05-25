import sys

def main():
    u_gay = raw_input("Are you gay? (yes/no)")
    if(u_gay == "no"):
        trick = raw_input("Does your mom know you're gay? (yes/no)")
        if(trick == "no"):
            print("LOL ur gay bro")
        else:
            print("... Bet")
    elif(u_gay == "yes"):
        print("Facts, I respect it")
    else: main()

if __name__ == '__main__':
  main()
